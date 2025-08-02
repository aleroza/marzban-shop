from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.utils.i18n import gettext as _

from utils import goods

def get_buy_menu_keyboard() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    for good in goods.get():
        is_free = good['price'].get('free', False)
        price_text = _("FREE") if is_free else "{price_ru}₽".format(price_ru=good['price']['ru'])

        builder.row(
            InlineKeyboardButton(
                text=_("{title} - {price}").format(
                    title=good['title'],
                    price=price_text
                ),
                callback_data=good['callback']
            )
        )
    return builder.as_markup()
