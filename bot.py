import logging
import os
import sys
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
    handlers=[logging.StreamHandler(sys.stdout)]
)
logger = logging.getLogger(__name__)

# Get bot token from environment variable (SECURE!)
BOT_TOKEN = os.environ.get('BOT_TOKEN', '8956959036:AAG4hEZLDRshbfsGW2z_BuWsA3vvFvEQbvU')

# Website URL (your game)
WEBSITE_URL = "https://www.joy-game-center.web.app"

# Account details
ACCOUNTS = {
    'cbe': {
        'name': 'CBE Bank',
        'account_number': '1000670806627',
        'account_name': 'Ermiyas Abeje Mihrte'
    },
    'telebirr': {
        'name': 'Telebirr',
        'phone': '0931126693',
        'account_name': 'Ermiyas Abeje Mihirte'
    },
    'dashen': {
        'name': 'Dashen Bank',
        'account_number': '5293745544011',
        'account_name': 'Ermiyas Abeje Mihirte'
    }
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send welcome message with WebApp button."""
    keyboard = [
        [InlineKeyboardButton("🎮 PLAY YAS GAME", web_app=WebAppInfo(url=WEBSITE_URL))],
        [InlineKeyboardButton("💰 Balance", callback_data='balance'),
         InlineKeyboardButton("💳 Deposit", callback_data='deposit')],
        [InlineKeyboardButton("🏧 Withdraw", callback_data='withdraw'),
         InlineKeyboardButton("🏆 Leaderboard", callback_data='leaderboard')],
        [InlineKeyboardButton("📜 My History", callback_data='history'),
         InlineKeyboardButton("❓ Help", callback_data='help')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    welcome_text = (
        f"🎮 **WELCOME TO YAS GAME!** 🎮\n\n"
        f"🏆 *Ethiopia's #1 Real-Time Bingo Platform*\n\n"
        f"👋 Hello! Welcome to Yas Game!\n\n"
        f"🏠 **Features:**\n"
        f"• 400 Cards (20×20 Grid)\n"
        f"• Win 80% of Prize Pool\n"
        f"• Telebirr, CBE, Bank Transfer\n\n"
        f"💰 **Get 10 ETB FREE on registration!**\n"
        f"📈 **Min Deposit/Withdrawal:** 100 ETB\n\n"
        f"🎮 **Click PLAY YAS GAME to start playing inside Telegram!**"
    )
    
    await update.message.reply_text(welcome_text, reply_markup=reply_markup, parse_mode='Markdown')

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle button presses."""
    query = update.callback_query
    await query.answer()
    
    if query.data == 'balance':
        keyboard = [[InlineKeyboardButton("🎮 Check Balance", web_app=WebAppInfo(url=WEBSITE_URL))]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            "💰 **CHECK BALANCE**\n\nClick below to open Yas Game and see your balance.",
            reply_markup=reply_markup,
            parse_mode='Markdown'
        )
    
    elif query.data == 'deposit':
        keyboard = [
            [InlineKeyboardButton("🏦 CBE Bank", callback_data='deposit_cbe')],
            [InlineKeyboardButton("📱 Telebirr", callback_data='deposit_telebirr')],
            [InlineKeyboardButton("🏛️ Dashen Bank", callback_data='deposit_dashen')],
            [InlineKeyboardButton("🎮 Make Deposit", web_app=WebAppInfo(url=WEBSITE_URL))]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            "💳 **DEPOSIT METHODS**\n\nSelect your payment method:",
            reply_markup=reply_markup,
            parse_mode='Markdown'
        )
    
    elif query.data == 'deposit_cbe':
        keyboard = [[InlineKeyboardButton("🎮 Complete Deposit", web_app=WebAppInfo(url=WEBSITE_URL))]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            f"🏦 **CBE BANK DEPOSIT**\n\n"
            f"Send to:\nAccount: `{ACCOUNTS['cbe']['account_number']}`\n"
            f"Name: `{ACCOUNTS['cbe']['account_name']}`\n\n"
            f"After payment, upload screenshot in web app.\n\n"
            f"⬇️ Click to complete deposit",
            reply_markup=reply_markup,
            parse_mode='Markdown'
        )
    
    elif query.data == 'deposit_telebirr':
        keyboard = [[InlineKeyboardButton("🎮 Complete Deposit", web_app=WebAppInfo(url=WEBSITE_URL))]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            f"📱 **TELEBIRR DEPOSIT**\n\n"
            f"Send to:\nPhone: `{ACCOUNTS['telebirr']['phone']}`\n"
            f"Name: `{ACCOUNTS['telebirr']['account_name']}`\n\n"
            f"After payment, upload screenshot in web app.\n\n"
            f"⬇️ Click to complete deposit",
            reply_markup=reply_markup,
            parse_mode='Markdown'
        )
    
    elif query.data == 'deposit_dashen':
        keyboard = [[InlineKeyboardButton("🎮 Complete Deposit", web_app=WebAppInfo(url=WEBSITE_URL))]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            f"🏛️ **DASHEN BANK DEPOSIT**\n\n"
            f"Send to:\nAccount: `{ACCOUNTS['dashen']['account_number']}`\n"
            f"Name: `{ACCOUNTS['dashen']['account_name']}`\n\n"
            f"After payment, upload screenshot in web app.\n\n"
            f"⬇️ Click to complete deposit",
            reply_markup=reply_markup,
            parse_mode='Markdown'
        )
    
    elif query.data == 'withdraw':
        keyboard = [
            [InlineKeyboardButton("🏦 CBE Bank", callback_data='withdraw_cbe')],
            [InlineKeyboardButton("📱 Telebirr", callback_data='withdraw_telebirr')],
            [InlineKeyboardButton("🏛️ Dashen Bank", callback_data='withdraw_dashen')],
            [InlineKeyboardButton("🎮 Request Withdrawal", web_app=WebAppInfo(url=WEBSITE_URL))]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            "🏧 **WITHDRAWAL**\n\nSelect your withdrawal method:",
            reply_markup=reply_markup,
            parse_mode='Markdown'
        )
    
    elif query.data == 'withdraw_cbe':
        keyboard = [[InlineKeyboardButton("🎮 Withdraw to CBE", web_app=WebAppInfo(url=WEBSITE_URL))]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            "🏦 **CBE WITHDRAWAL**\n\nClick below to withdraw to CBE.",
            reply_markup=reply_markup,
            parse_mode='Markdown'
        )
    
    elif query.data == 'withdraw_telebirr':
        keyboard = [[InlineKeyboardButton("🎮 Withdraw to Telebirr", web_app=WebAppInfo(url=WEBSITE_URL))]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            "📱 **TELEBIRR WITHDRAWAL**\n\nClick below to withdraw to Telebirr.",
            reply_markup=reply_markup,
            parse_mode='Markdown'
        )
    
    elif query.data == 'withdraw_dashen':
        keyboard = [[InlineKeyboardButton("🎮 Withdraw to Dashen", web_app=WebAppInfo(url=WEBSITE_URL))]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            "🏛️ **DASHEN WITHDRAWAL**\n\nClick below to withdraw to Dashen.",
            reply_markup=reply_markup,
            parse_mode='Markdown'
        )
    
    elif query.data == 'leaderboard':
        keyboard = [[InlineKeyboardButton("🎮 View Leaderboard", web_app=WebAppInfo(url=WEBSITE_URL))]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            "🏆 **LEADERBOARD**\n\nClick below to view live leaderboard.",
            reply_markup=reply_markup,
            parse_mode='Markdown'
        )
    
    elif query.data == 'history':
        keyboard = [[InlineKeyboardButton("🎮 View History", web_app=WebAppInfo(url=WEBSITE_URL))]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            "📜 **YOUR HISTORY**\n\nClick below to view your complete history.",
            reply_markup=reply_markup,
            parse_mode='Markdown'
        )
    
    elif query.data == 'help':
        keyboard = [
            [InlineKeyboardButton("📖 How to Play", callback_data='howtoplay')],
            [InlineKeyboardButton("💬 Support", callback_data='support')],
            [InlineKeyboardButton("🎮 Open Game", web_app=WebAppInfo(url=WEBSITE_URL))]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            "❓ **HELP & SUPPORT**\n\nSelect an option:",
            reply_markup=reply_markup,
            parse_mode='Markdown'
        )
    
    elif query.data == 'howtoplay':
        keyboard = [[InlineKeyboardButton("🎮 Play Now", web_app=WebAppInfo(url=WEBSITE_URL))]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            "📖 **HOW TO PLAY**\n\n"
            "1. Click PLAY YAS GAME\n"
            "2. Register/Login\n"
            "3. Deposit min 100 ETB\n"
            "4. Buy bingo cards (10 ETB)\n"
            "5. Win 80% of prize pool!\n\n"
            "⬇️ Start playing now!",
            reply_markup=reply_markup,
            parse_mode='Markdown'
        )
    
    elif query.data == 'support':
        keyboard = [[InlineKeyboardButton("📞 Contact", url="https://t.me/YasGameSupport")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            "💬 **SUPPORT**\n\n📱 Telegram: @YasGameSupport\n⏱️ 24/7 Support\n\nClick below to message.",
            reply_markup=reply_markup,
            parse_mode='Markdown'
        )

async def webapp_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Direct command to open web app."""
    keyboard = [[InlineKeyboardButton("🎮 Open Yas Game", web_app=WebAppInfo(url=WEBSITE_URL))]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "🎮 **Click to open Yas Game inside Telegram!**",
        reply_markup=reply_markup,
        parse_mode='Markdown'
    )

def main():
    """Start the bot."""
    print("🤖 Yas Game Bot is starting...")
    print(f"🌐 WebApp URL: {WEBSITE_URL}")
    
    if not BOT_TOKEN or BOT_TOKEN == 'YOUR_BOT_TOKEN_HERE':
        print("❌ ERROR: BOT_TOKEN environment variable not set!")
        print("Please set BOT_TOKEN in Render environment variables.")
        return
    
    application = Application.builder().token(BOT_TOKEN).build()
    
    # Add handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("webapp", webapp_command))
    application.add_handler(CommandHandler("play", webapp_command))
    application.add_handler(CallbackQueryHandler(button_handler))
    
    print("✅ Bot is running with WebApp support!")
    print("🎮 Game will open INSIDE Telegram")
    
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()
