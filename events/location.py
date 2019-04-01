from line_bot_api import *

line_bot_api = LineBotApi('hJTb3CUmLQcouVK7a9ieECQc1O+nv8Ky9uGKKyngF+14u9ESQpeAg6Y66wrnQ2iieP59FNOwgLD/xVEDz+T5kdSKj4QjWWm2fKz9+GOOtKMT1yMW7jF7QRVJrwuBuyqqtubOiWMfeA9EqdW4nBonPAdB04t89/1O/w1cDnyilFU=')


def location_event(event):
    title_text = 'Location'
    address_text = '110台北市信義區信義路五段7號台北101大樓'
    latitude = 51.5007841
    longitude = -0.1596448
    line_bot_api.reply_message(
    event.reply_token,
    LocationSendMessage(title = title_text,
                        address = address_text,
                        latitude = latitude,
                        longitude = longitude))
