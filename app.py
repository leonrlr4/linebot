from urllib.parse import parse_qsl

from flask import Flask, abort, request

from events.about_us import about_us_event
from events.appointment import appointment_datetime_event
from events.appointment import appointment_event
from events.appointment import appointment_complete_event
from events.contact import contact_event
from events.location import location_event
from line_bot_api import *

app = Flask(__name__)

line_bot_api = LineBotApi('hJTb3CUmLQcouVK7a9ieECQc1O+nv8Ky9uGKKyngF+14u9ESQpeAg6Y66wrnQ2iieP59FNOwgLD/xVEDz+T5kdSKj4QjWWm2fKz9+GOOtKMT1yMW7jF7QRVJrwuBuyqqtubOiWMfeA9EqdW4nBonPAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('206b760a93bb7264601720c0772054de')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    # return 'OK'
    message_text = str(event.message.text).lower()
    if message_text == '@aboutus':
        #傳送關於我們的資訊
        about_us_event(event)

    elif message_text == '@location':
        #傳送我們的位置
        location_event(event)

    elif message_text == '@contact':
        #傳送聯絡方式（電話）
        contact_event(event)

    elif message_text == '@booknow':
        #接收使用者選擇的服務
        appointment_event(event)


@handler.add(PostbackEvent)
def handle_post_back(event):
    data = dict(parse_qsl(event.postback.data))
    if data.get('action') == 'step2':
        #預約步驟
        appointment_datetime_event(event)

    elif data.get('action') == 'step3':
        #完成預約步驟
        appointment_complete_event(event)



if __name__ == "__main__":
    app.run()