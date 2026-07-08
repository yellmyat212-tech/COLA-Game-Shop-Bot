from telegram import Update
from telegram.ext import Application, MessageHandler, ContextTypes, filters

BOT_TOKEN = "YOUR_BOT_TOKEN"
ADMIN_ID = 123456789

PAYMENT_TEXT = """
🗒️ ✅ အချက်အလက်များ လက်ခံရပါပြီ။

⤵️ ငွေလွှဲရန်

💳 KBZ Pay
📱 09767766729
👤 Ye Myat Htut

💳 Wave Pay
📱 09764336243
👤 Myint Myint San

🛑 Note - Payment ဘဲရေးပေးပါ။

🚫 ငွေလွှဲပြီးလျှင် ပြေစာ (Screenshot) ကို ပြန်ပို့ပေးပါ။
"""

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    text = update.message.text

    await update.message.reply_text(PAYMENT_TEXT)

    admin_text = (
        f"🛒 New Order\n\n"
        f"👤 User: @{user.username}\n"
        f"🆔 User ID: {user.id}\n"
        f"📦 Order: {text}"
    )

    await context.bot.send_message(chat_id=ADMIN_ID, text=admin_text)

async def handle_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.forward_message(
        chat_id=ADMIN_ID,
        from_chat_id=update.effective_chat.id,
        message_id=update.message.message_id
    )

app = Application.builder().token(BOT_TOKEN).build()

app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
app.add_handler(MessageHandler(filters.PHOTO, handle_photo))

app.run_polling()
