from aiogram_i18n import L
from aiogram_i18n.types import InlineKeyboardButton, InlineKeyboardMarkup

from data.repository.PostRepository import PostRepository


class ChannelPostMessage:

    @staticmethod
    async def make_post_channel(data, bot, channel_id, i18n, identify):

        try:
            post = PostRepository().post(identify)
            my_post = i18n.ADMIN.POST.TEMPLATE(
                name=data['name'],
                code=post['code'],
                year=data['year'],
                temp=data['temp'],
                desc=data['desc']
            )

            if len(data.get('buttons', [])) > 0:
                kb_buttons = []
                for btn in data.get('buttons'):
                    kb_buttons.append([InlineKeyboardButton(text=btn['btn_text'], url=btn['btn_url'])])
                kb_buttons = InlineKeyboardMarkup(inline_keyboard=kb_buttons)
            else:
                kb_buttons = None

            if data.get('photo', None):
                await bot.send_photo(
                    chat_id=channel_id,
                    photo=data.get('photo'),
                    caption=my_post,
                    reply_markup=kb_buttons
                )
            elif data.get('video', None):
                await bot.send_video(
                    chat_id=channel_id,
                    video=data.get('video'),
                    caption=my_post,
                    reply_markup=kb_buttons
                )
            else:
                await bot.send_message(
                    chat_id=channel_id,
                    text=my_post,
                    reply_markup=kb_buttons
                )

            return True
        except Exception as e:
            print(f"make_post_channel: {e}")
            return False
