import os
from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup
)
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes
)
from dotenv import load_dotenv

# Load file .env
load_dotenv()

# Ambil token dari file .env
BOT_TOKEN = os.getenv("BOT_TOKEN")

# 🔘 Tombol utama
def main_menu():
    keyboard = [
        [InlineKeyboardButton("🚀 JOIN 1", url="https://t.me/bokepviralindonesi4")],
        [InlineKeyboardButton("🚀 JOIN 2", url="https://t.me/MayorPajakBOT")],
        [InlineKeyboardButton("🚀 JOIN 3", url="https://t.me/ClaimEventPajaktoto")],
        [InlineKeyboardButton("🔁 START ULANG", callback_data="start_again")]
    ]
    return InlineKeyboardMarkup(keyboard)

# 🔘 Tombol mulai pertama
def start_button():
    keyboard = [[InlineKeyboardButton("▶️ MULAI", callback_data="mulai")]]
    return InlineKeyboardMarkup(keyboard)

# 📩 Command /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Halo! Selamat datang di *DI VIDEO BOKEP INDONESIA*\n\n"
        "Tekan tombol di bawah untuk memulai ✨",
        parse_mode="Markdown",
        reply_markup=start_button()
    )

# 📩 Callback tombol "mulai"
async def mulai_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    user = query.from_user
    await query.answer()

    text = (
        f"Hello {user.first_name or 'Sayang'} 💋\n\n"
        "🌸 Selamat datang di *DI VIDEO BOKEP INDONESIA*\n"
        "Tempat video viral & manja berbagi cerita dewasa ✨\n\n"
        "Sebelum lanjut, yuk gabung ke semua channel di bawah ini dulu 💋"
    )

    await query.message.edit_text(
        text=text,
        parse_mode="Markdown",
        reply_markup=main_menu()
    )

# 📩 Callback tombol "START ULANG"
async def start_again_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    await query.message.edit_text(
        "🔁 Kamu memilih untuk memulai ulang.\n\nTekan tombol di bawah untuk mulai lagi 💫",
        reply_markup=start_button()
    )

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(mulai_callback, pattern="^mulai$"))
    app.add_handler(CallbackQueryHandler(start_again_callback, pattern="^start_again$"))

    print("🤖 Bot sedang berjalan...")
    app.run_polling()

if __name__ == "__main__":
    main()
