from line_bot_api import *
from urllib.parse import parse_qsl
import datetime

def appointment_event(event):
    carousel_template_message = TemplateSendMessage(
        alt_text='Carousel template',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='https://i.imgur.com/achPYfh.jpg',
                    title='Hair cut && Style',
                    text='請選擇服務',
                    actions=[
                        PostbackAction(
                            label='剪頭髮',
                            text='剪頭髮',
                            data='action=step2&service=剪頭髮'
                        ),
                        PostbackAction(
                            label='洗頭髮',
                            text='洗頭髮',
                            data='action=step2&service=洗頭髮'
                        ),
                        PostbackAction(
                            label='洗加剪',
                            text='洗加剪',
                            data='action=step2&service=洗加剪'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://i.imgur.com/SQnGl6n.jpg',
                    title='造型 && 按摩',
                    text='請選擇服務',
                    actions=[
                        PostbackAction(
                            label='臉部按摩',
                            text='臉部按摩',
                            data='action=step2&service=臉部按摩'
                        ),
                        PostbackAction(
                            label='燙髮',
                            text='燙髮',
                            data='action=step2&service=燙髮'
                        ),
                        PostbackAction(
                            label='染髮',
                            text='染髮',
                            data='action=step2&service=染髮'
                        )
                    ]
                )
            ]
        )
    )

    line_bot_api.reply_message(
        reply_token=event.reply_token,
        messages=[TextSendMessage(text='您想要預約什麼服務呢'),
                carousel_template_message]
    )


def appointment_datetime_event(event):
    data = dict(parse_qsl(event.postback.data))
    #設定日期選擇規則
    now = datetime.datetime.now()
    #最小預約時間為兩天後
    min_date = now + datetime.timedelta(days=2)
    #最大預約時間為九天後
    max_date = now + datetime.timedelta(days=9)
    image_carousel_template_message = TemplateSendMessage(
        alt_text='ImageCarousel template',
        template=ImageCarouselTemplate(
            columns=[
                ImageCarouselColumn(
                    image_url='https://i.imgur.com/6ZUpx8Q.jpg',
                    action=DatetimePickerAction(
                        label="請選擇想要預約的日期",
                        data="action=step3&service={}".format(data.get('service')),
                        mode="datetime",
                        initial=min_date.strftime('%Y-%m-%dT00:00'),
                        min=min_date.strftime('%Y-%m-%dT00:00'),
                        max=max_date.strftime('%Y-%m-%dT23:59')
                    )
                )
            ]
        )
    )

    line_bot_api.reply_message(
        reply_token = event.reply_token,
        messages=[image_carousel_template_message]
    )


def appointment_complete_event(event):
    appointment_service = dict(parse_qsl(event.postback.data)).get('service')
    appointment_datetime = datetime.datetime.strptime(event.postback.params.get('datetime'), '%Y-%m-%dT%H:%M')
    profile_name = line_bot_api.get_profile(event.source.user_id).display_name

    appointment_service_text = '親愛的 {} 您已完成{} 服務的預約'.format(profile_name, appointment_service)
    appointment_datetime_text = appointment_datetime.strftime('您預約的日為 %Y-%m-%d， 時間為%H:%M')

    line_bot_api.reply_message(
        reply_token = event.reply_token,
        messages=[TextSendMessage(text=appointment_service_text),
                TextSendMessage(text=appointment_datetime_text)]
    )
