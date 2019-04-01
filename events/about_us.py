from line_bot_api import *


def about_us_event(event):
    about_us_text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec pretium ante erat, vitae sodales mi varius quis. Etiam vestibulum lorem vel urna tempor, eu fermentum odio aliquam. Aliquam consequat urna vitae ipsum pulvinar, in blandit purus eleifend.'
    about_us_image = 'https://i.imgur.com/Kgnhtqf.jpg'
    line_bot_api.reply_message(
        event.reply_token,
    [
        TextSendMessage(text=about_us_text),
        ImageSendMessage(original_content_url = about_us_image,                              preview_image_url = about_us_image),
        StickerSendMessage(package_id = '2', sticker_id = '28')
    ]
    )
