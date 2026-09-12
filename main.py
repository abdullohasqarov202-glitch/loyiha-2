"""python
"""
SmashBite Telegram Bot
Telegram orqali SmashBite veb-saytini ochish uchun bot.
"""

import os
import logging

from telegram import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    WebAppInfo,
    Update,
)
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
)


# =========================
# LOGGING
# =========================

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

logger = logging.getLogger(__name__)


# =========================
# SOZLAMALAR
# =========================

BOT_TOKEN = os.getenv("BOT_TOKEN")
WEBAPP_URL = os.getenv(
    "WEBAPP_URL",
    "https://loyiha-bir-production.up.railway.app"
)


# =========================
# /START
# =========================

async def start(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
) -> None:

    keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton(
                "🍔 Menyuni ochish",
                web_app=WebAppInfo(url=WEBAPP_URL)
            )
        ]
    ])

    await update.message.reply_text(
        "🔥 Xush kelibsiz, SmashBite botiga!\n\n"
        "🍔 Menyuni ko‘rish\n"
        "🛒 Buyurtma berish\n"
        "📅 Stol band qilish\n\n"
        "Quyidagi tugmani bosing 👇",
        reply_markup=keyboard,
    )


# =========================
# /MENU
# =========================

async def menu_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
) -> None:

    await start(update, context)


# =========================
# /HELP
# =========================

async def help_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
) -> None:

    await update.message.reply_text(
        "ℹ️ SmashBite yordam\n\n"
        "/start — Botni ishga tushirish\n"
        "/menu — Menyuni ochish\n"
        "/help — Yordam\n\n"
        "🍔 Menyuni ochish tugmasi orqali "
        "saytga kirishingiz mumkin."
    )


# =========================
# MAIN
# =========================

def main() -> None:

    if not BOT_TOKEN:
        logger.error(
            "BOT_TOKEN topilmadi! "
            "Railway Variables bo‘limiga BOT_TOKEN qo‘ying."
        )
        return

    if not WEBAPP_URL:
        logger.error(
            "WEBAPP_URL topilmadi!"
        )
        return

    logger.info("🚀 SmashBite bot ishga tushmoqda...")
    logger.info("🌐 WebApp: %s", WEBAPP_URL)

    application = (
        Application.builder()
        .token(BOT_TOKEN)
        .build()
    )

    application.add_handler(
        CommandHandler("start", start)
    )

    application.add_handler(
        CommandHandler("menu", menu_command)
    )

    application.add_handler(
        CommandHandler("help", help_command)
    )

    logger.info("✅ Bot ishga tushdi!")

    application.run_polling(
        allowed_updates=Update.ALL_TYPES
    )


# =========================
# START
# =========================

if __name__ == "__main__":
    main()
"""
