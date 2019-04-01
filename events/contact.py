from line_bot_api import TemplateSendMessage
from line_bot_api import line_bot_api
from line_bot_api import ButtonsTemplate
from line_bot_api import URIAction

def contact_event(event):
    buttons_template_message = TemplateSendMessage(
        alt_text='Buttons template',
        template=ButtonsTemplate(
            thumbnail_image_url='https://i.imgur.com/PVL8X0B.jpg',
            title='Contact',
            text='Please select',
            actions=[
                URIAction(
                    label='聯繫我們',
                    uri='TEL:+886123456789'
                )
            ]
        )
    )

    line_bot_api.reply_message(
        reply_token=event.reply_token, messages=[buttons_template_message]
    )
