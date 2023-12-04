from datetime import datetime

from telegram import Update
from telegram.ext import CallbackContext

from app.bot.constants import PARSE_MODE
from app.bot.features.user import get_user, update_user
from app.bot.helpers import create_chat_with_first_message
from app.bot.keyboards import build_language_keyboard, build_mode_keyboard, build_settings_keyboard, \
    build_subscriptions_keyboard
from app.bot.locales.main import get_localization
from app.firebase import db, bucket
from app.models import SubscriptionType, Currency


async def start(update: Update, context: CallbackContext):
    user = await get_user(str(update.effective_user.id))
    if not user:
        transaction = db.transaction()
        await create_chat_with_first_message(transaction, update.effective_user, str(update.message.chat_id))
    elif update.message.chat_id not in user.telegram_chat_ids:
        user.telegram_chat_ids.append(str(update.message.chat_id))
        await update_user(user.id, {"telegram_chat_ids": user.telegram_chat_ids})

    greeting = get_localization(user.language_code if user else update.effective_user.language_code).START

    await update.message.reply_text(greeting, parse_mode=PARSE_MODE)


async def commands(update: Update, context: CallbackContext):
    user = await get_user(str(update.effective_user.id))

    await update.message.reply_text(get_localization(user.language_code).COMMANDS, parse_mode=PARSE_MODE)


async def language(update: Update, context: CallbackContext):
    language_code = (await get_user(str(update.effective_user.id))).language_code

    reply_markup = build_language_keyboard(language_code)

    await update.message.reply_text(get_localization(language_code).LANGUAGE,
                                    reply_markup=reply_markup,
                                    parse_mode=PARSE_MODE)


async def mode(update: Update, context: CallbackContext):
    user = await get_user(str(update.effective_user.id))

    reply_markup = build_mode_keyboard(user.language_code, user.current_model)

    await update.message.reply_text(get_localization(user.language_code).MODE,
                                    reply_markup=reply_markup,
                                    parse_mode=PARSE_MODE)


async def info(update: Update, context: CallbackContext):
    user = await get_user(str(update.effective_user.id))

    await update.message.reply_text(get_localization(user.language_code).INFO, parse_mode=PARSE_MODE)


async def profile(update: Update, context: CallbackContext):
    telegram_user = update.effective_user

    user_id = str(telegram_user.id)
    user = await get_user(user_id)

    await update_user(user_id, {
        "first_name": telegram_user.first_name,
        "last_name": telegram_user.last_name or "",
        "username": telegram_user.username,
        "is_premium": telegram_user.is_premium,
        "edited_at": datetime.now()
    })

    message = get_localization(user.language_code).profile(SubscriptionType.FREE.value,
                                                           user.gender,
                                                           user.current_model,
                                                           user.additional_usage_quota)

    await update.message.reply_text(message, parse_mode=PARSE_MODE)


async def settings(update: Update, context: CallbackContext):
    user = await get_user(str(update.effective_user.id))

    reply_markup = build_settings_keyboard(user.language_code, user.settings)

    await update.message.reply_text(get_localization(user.language_code).SETTINGS,
                                    reply_markup=reply_markup,
                                    parse_mode=PARSE_MODE)


async def subscribe(update: Update, context: CallbackContext):
    user = await get_user(str(update.effective_user.id))

    photo = bucket.blob(f'subscriptions/{user.language_code}.png')
    photo_data = photo.download_as_string()

    message = get_localization(user.language_code).subscribe(Currency.RUB)
    reply_markup = build_subscriptions_keyboard(user.language_code)

    await update.message.reply_photo(photo_data, message, parse_mode=PARSE_MODE, reply_markup=reply_markup)


async def buy(update: Update, context: CallbackContext):
    pass


async def catalog(update: Update, context: CallbackContext):
    pass


async def chats(update: Update, context: CallbackContext):
    pass