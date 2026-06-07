import logging
import os
import sys
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
    handlers=[logging.StreamHandler(sys.stdout)]
)
logger = logging.getLogger(__name__)

# Get bot token from environment variable
BOT_TOKEN = os.environ.get('BOT_TOKEN', 'YOUR_BOT_TOKEN_HERE')

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

# Website/Game URL (for instructions only)
GAME_URL = "https://www.joy-game-center.web.app"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send welcome message with main menu."""
    keyboard = [
        [InlineKeyboardButton("🎮 PLAY BINGO", callback_data='play_bingo')],
        [InlineKeyboardButton("💰 BALANCE", callback_data='balance'),
         InlineKeyboardButton("💳 DEPOSIT", callback_data='deposit')],
        [InlineKeyboardButton("🏧 WITHDRAW", callback_data='withdraw'),
         InlineKeyboardButton("🏆 LEADERBOARD", callback_data='leaderboard')],
        [InlineKeyboardButton("📜 MY HISTORY", callback_data='history'),
         InlineKeyboardButton("❓ HELP", callback_data='help')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    welcome_text = (
        f"🏆 YAS GAME | Ethiopia's #1 Real-Time Bingo Platform\n\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
        f"👋 Welcome {update.effective_user.first_name}!\n\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
        f"📊 Platform Features:\n"
        f"• 400 Cards (20x20 Grid)\n"
        f"• Win 80% of Prize Pool\n"
        f"• Real-Time Drawing Every 2 Minutes\n\n"
        f"💳 Payment Methods:\n"
        f"• Telebirr\n"
        f"• CBE Bank\n"
        f"• Dashen Bank\n\n"
        f"🎁 Welcome Bonus:\n"
        f"• Get 10 ETB FREE on Registration\n"
        f"• Minimum Deposit: 100 ETB\n"
        f"• Minimum Withdrawal: 100 ETB\n\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
        f"🎮 Click PLAY BINGO to start your winning journey!"
    )
    
    await update.message.reply_text(welcome_text, reply_markup=reply_markup, parse_mode=None)

async def play_bingo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Show how to play bingo."""
    keyboard = [[InlineKeyboardButton("⬅️ BACK", callback_data='back_to_main')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    play_text = (
        f"🎮 HOW TO PLAY YAS BINGO\n\n"
        f"━━━━━━━━━━━━━━━━━━━━━━\n\n"
        f"📱 To start playing:\n\n"
        f"1️⃣ Open your web browser\n"
        f"2️⃣ Go to: {GAME_URL}\n"
        f"3️⃣ Register/Login to your account\n"
        f"4️⃣ Deposit minimum 100 ETB\n"
        f"5️⃣ Buy bingo cards (10 ETB each)\n"
        f"6️⃣ Numbers drawn every 2 minutes\n"
        f"7️⃣ Match patterns to win!\n\n"
        f"━━━━━━━━━━━━━━━━━━━━━━\n\n"
        f"🏆 Winning Patterns:\n"
        f"⭐ Complete horizontal line\n"
        f"⭐ Complete vertical line\n"
        f"⭐ Four corners\n"
        f"⭐ X pattern\n"
        f"⭐ Full house\n\n"
        f"━━━━━━━━━━━━━━━━━━━━━━\n\n"
        f"💰 Win 80% of prize pool!\n\n"
        f"📞 Need help? @YasGameSupport"
    )
    
    await update.callback_query.edit_message_text(play_text, reply_markup=reply_markup, parse_mode=None)

async def balance(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Show balance information."""
    keyboard = [[InlineKeyboardButton("⬅️ BACK", callback_data='back_to_main')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    balance_text = (
        f"💰 YOUR BALANCE\n\n"
        f"━━━━━━━━━━━━━━━━━━━━━━\n\n"
        f"To check your balance:\n\n"
        f"1️⃣ Open your web browser\n"
        f"2️⃣ Go to: {GAME_URL}\n"
        f"3️⃣ Log in to your account\n"
        f"4️⃣ Your balance is on the dashboard\n\n"
        f"━━━━━━━━━━━━━━━━━━━━━━\n\n"
        f"📊 Balance Info:\n"
        f"• Welcome Bonus: 10 ETB\n"
        f"• Minimum Deposit: 100 ETB\n"
        f"• Minimum Withdrawal: 100 ETB\n\n"
        f"🎮 Click PLAY BINGO to start playing!"
    )
    
    await update.callback_query.edit_message_text(balance_text, reply_markup=reply_markup, parse_mode=None)

async def deposit(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Show deposit options."""
    keyboard = [
        [InlineKeyboardButton("🏦 CBE BANK", callback_data='deposit_cbe')],
        [InlineKeyboardButton("📱 TELEBIRR", callback_data='deposit_telebirr')],
        [InlineKeyboardButton("🏛️ DASHEN BANK", callback_data='deposit_dashen')],
        [InlineKeyboardButton("⬅️ BACK", callback_data='back_to_main')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    deposit_text = (
        f"💳 DEPOSIT METHODS\n\n"
        f"━━━━━━━━━━━━━━━━━━━━━━\n\n"
        f"💰 Minimum Deposit: 100 ETB\n"
        f"💰 Maximum Deposit: No Limit\n\n"
        f"Select your payment method below:\n\n"
        f"━━━━━━━━━━━━━━━━━━━━━━\n\n"
        f"📌 After payment:\n"
        f"1️⃣ Take a screenshot\n"
        f"2️⃣ Open {GAME_URL}\n"
        f"3️⃣ Go to Deposit section\n"
        f"4️⃣ Upload screenshot\n"
        f"5️⃣ Funds credited within 5 minutes"
    )
    
    await update.callback_query.edit_message_text(deposit_text, reply_markup=reply_markup, parse_mode=None)

async def deposit_cbe(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Show CBE deposit details."""
    keyboard = [[InlineKeyboardButton("⬅️ BACK", callback_data='deposit')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    deposit_cbe_text = (
        f"🏦 CBE BANK DEPOSIT\n\n"
        f"━━━━━━━━━━━━━━━━━━━━━━\n\n"
        f"📌 Send payment to:\n\n"
        f"Bank: Commercial Bank of Ethiopia\n"
        f"Account: {ACCOUNTS['cbe']['account_number']}\n"
        f"Name: {ACCOUNTS['cbe']['account_name']}\n\n"
        f"Reference: Your Phone Number\n"
        f"Amount: Minimum 100 ETB\n\n"
        f"━━━━━━━━━━━━━━━━━━━━━━\n\n"
        f"✅ After sending payment:\n"
        f"1️⃣ Take a screenshot\n"
        f"2️⃣ Open {GAME_URL}\n"
        f"3️⃣ Upload in Deposit section\n"
        f"4️⃣ Funds credited within 5 minutes"
    )
    
    await update.callback_query.edit_message_text(deposit_cbe_text, reply_markup=reply_markup, parse_mode=None)

async def deposit_telebirr(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Show Telebirr deposit details."""
    keyboard = [[InlineKeyboardButton("⬅️ BACK", callback_data='deposit')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    deposit_telebirr_text = (
        f"📱 TELEBIRR DEPOSIT\n\n"
        f"━━━━━━━━━━━━━━━━━━━━━━\n\n"
        f"📌 Send payment to:\n\n"
        f"Phone: {ACCOUNTS['telebirr']['phone']}\n"
        f"Name: {ACCOUNTS['telebirr']['account_name']}\n\n"
        f"Reference: Your Name\n"
        f"Amount: Minimum 100 ETB\n\n"
        f"━━━━━━━━━━━━━━━━━━━━━━\n\n"
        f"✅ After sending payment:\n"
        f"1️⃣ Take a screenshot\n"
        f"2️⃣ Open {GAME_URL}\n"
        f"3️⃣ Upload in Deposit section\n"
        f"4️⃣ Funds credited within 2 minutes"
    )
    
    await update.callback_query.edit_message_text(deposit_telebirr_text, reply_markup=reply_markup, parse_mode=None)

async def deposit_dashen(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Show Dashen Bank deposit details."""
    keyboard = [[InlineKeyboardButton("⬅️ BACK", callback_data='deposit')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    deposit_dashen_text = (
        f"🏛️ DASHEN BANK DEPOSIT\n\n"
        f"━━━━━━━━━━━━━━━━━━━━━━\n\n"
        f"📌 Send payment to:\n\n"
        f"Bank: Dashen Bank\n"
        f"Account: {ACCOUNTS['dashen']['account_number']}\n"
        f"Name: {ACCOUNTS['dashen']['account_name']}\n\n"
        f"Reference: Your Phone Number\n"
        f"Amount: Minimum 100 ETB\n\n"
        f"━━━━━━━━━━━━━━━━━━━━━━\n\n"
        f"✅ After sending payment:\n"
        f"1️⃣ Take a screenshot\n"
        f"2️⃣ Open {GAME_URL}\n"
        f"3️⃣ Upload in Deposit section\n"
        f"4️⃣ Funds credited within 5 minutes"
    )
    
    await update.callback_query.edit_message_text(deposit_dashen_text, reply_markup=reply_markup, parse_mode=None)

async def withdraw(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Show withdrawal options."""
    keyboard = [
        [InlineKeyboardButton("🏦 CBE BANK", callback_data='withdraw_cbe')],
        [InlineKeyboardButton("📱 TELEBIRR", callback_data='withdraw_telebirr')],
        [InlineKeyboardButton("🏛️ DASHEN BANK", callback_data='withdraw_dashen')],
        [InlineKeyboardButton("⬅️ BACK", callback_data='back_to_main')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    withdraw_text = (
        f"🏧 WITHDRAWAL METHODS\n\n"
        f"━━━━━━━━━━━━━━━━━━━━━━\n\n"
        f"💰 Minimum Withdrawal: 100 ETB\n"
        f"💰 Maximum Withdrawal: 50,000 ETB/day\n"
        f"⏱️ Processing Time: 24 Hours\n"
        f"✅ Fee: Free\n\n"
        f"Select your withdrawal method below:\n\n"
        f"━━━━━━━━━━━━━━━━━━━━━━\n\n"
        f"📌 Process:\n"
        f"1️⃣ Open {GAME_URL}\n"
        f"2️⃣ Go to Withdrawal section\n"
        f"3️⃣ Select your method\n"
        f"4️⃣ Enter your account details\n"
        f"5️⃣ Enter amount\n"
        f"6️⃣ Submit request"
    )
    
    await update.callback_query.edit_message_text(withdraw_text, reply_markup=reply_markup, parse_mode=None)

async def withdraw_cbe(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Show CBE withdrawal details."""
    keyboard = [[InlineKeyboardButton("⬅️ BACK", callback_data='withdraw')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    withdraw_cbe_text = (
        f"🏦 CBE BANK WITHDRAWAL\n\n"
        f"━━━━━━━━━━━━━━━━━━━━━━\n\n"
        f"📌 To receive payment, provide:\n\n"
        f"• Your CBE Account Number\n"
        f"• Your Account Name\n\n"
        f"━━━━━━━━━━━━━━━━━━━━━━\n\n"
        f"✅ Process:\n"
        f"1️⃣ Open {GAME_URL}\n"
        f"2️⃣ Go to Withdrawal → CBE Bank\n"
        f"3️⃣ Enter your CBE account details\n"
        f"4️⃣ Enter amount (min 100 ETB)\n"
        f"5️⃣ Submit request\n\n"
        f"⏱️ Processing: 24 hours\n"
        f"✅ Fee: Free"
    )
    
    await update.callback_query.edit_message_text(withdraw_cbe_text, reply_markup=reply_markup, parse_mode=None)

async def withdraw_telebirr(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Show Telebirr withdrawal details."""
    keyboard = [[InlineKeyboardButton("⬅️ BACK", callback_data='withdraw')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    withdraw_telebirr_text = (
        f"📱 TELEBIRR WITHDRAWAL\n\n"
        f"━━━━━━━━━━━━━━━━━━━━━━\n\n"
        f"📌 To receive payment, provide:\n\n"
        f"• Your Telebirr Phone Number\n"
        f"• Your Full Name\n\n"
        f"━━━━━━━━━━━━━━━━━━━━━━\n\n"
        f"✅ Process:\n"
        f"1️⃣ Open {GAME_URL}\n"
        f"2️⃣ Go to Withdrawal → Telebirr\n"
        f"3️⃣ Enter your phone number\n"
        f"4️⃣ Enter amount (min 100 ETB)\n"
        f"5️⃣ Submit request\n\n"
        f"⏱️ Processing: 24 hours\n"
        f"✅ Fee: Free"
    )
    
    await update.callback_query.edit_message_text(withdraw_telebirr_text, reply_markup=reply_markup, parse_mode=None)

async def withdraw_dashen(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Show Dashen Bank withdrawal details."""
    keyboard = [[InlineKeyboardButton("⬅️ BACK", callback_data='withdraw')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    withdraw_dashen_text = (
        f"🏛️ DASHEN BANK WITHDRAWAL\n\n"
        f"━━━━━━━━━━━━━━━━━━━━━━\n\n"
        f"📌 To receive payment, provide:\n\n"
        f"• Your Dashen Account Number\n"
        f"• Your Account Name\n\n"
        f"━━━━━━━━━━━━━━━━━━━━━━\n\n"
        f"✅ Process:\n"
        f"1️⃣ Open {GAME_URL}\n"
        f"2️⃣ Go to Withdrawal → Dashen Bank\n"
        f"3️⃣ Enter your account details\n"
        f"4️⃣ Enter amount (min 100 ETB)\n"
        f"5️⃣ Submit request\n\n"
        f"⏱️ Processing: 24 hours\n"
        f"✅ Fee: Free"
    )
    
    await update.callback_query.edit_message_text(withdraw_dashen_text, reply_markup=reply_markup, parse_mode=None)

async def leaderboard(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Show leaderboard."""
    keyboard = [[InlineKeyboardButton("⬅️ BACK", callback_data='back_to_main')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    leaderboard_text = (
        f"🏆 LEADERBOARD - TOP PLAYERS\n\n"
        f"━━━━━━━━━━━━━━━━━━━━━━\n\n"
        f"📊 Weekly Rankings:\n\n"
        f"1️⃣ Player 1 - 52,420 ETB\n"
        f"2️⃣ Player 2 - 48,690 ETB\n"
        f"3️⃣ Player 3 - 36,150 ETB\n"
        f"4️⃣ Player 4 - 28,430 ETB\n"
        f"5️⃣ Player 5 - 21,870 ETB\n\n"
        f"━━━━━━━━━━━━━━━━━━━━━━\n\n"
        f"📈 Global Stats:\n"
        f"• Total Players: 1,247\n"
        f"• Prize Pool: 156,430 ETB\n"
        f"• Games Today: 2,345\n\n"
        f"━━━━━━━━━━━━━━━━━━━━━━\n\n"
        f"🏅 To see your rank:\n"
        f"1️⃣ Open {GAME_URL}\n"
        f"2️⃣ Log in to your account\n"
        f"3️⃣ Check Leaderboard section\n\n"
        f"⏰ Next Reset: Sunday 00:00 EAT"
    )
    
    await update.callback_query.edit_message_text(leaderboard_text, reply_markup=reply_markup, parse_mode=None)

async def history(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Show transaction history."""
    keyboard = [[InlineKeyboardButton("⬅️ BACK", callback_data='back_to_main')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    history_text = (
        f"📜 YOUR TRANSACTION HISTORY\n\n"
        f"━━━━━━━━━━━━━━━━━━━━━━\n\n"
        f"To view your complete history:\n\n"
        f"1️⃣ Open {GAME_URL}\n"
        f"2️⃣ Log in to your account\n"
        f"3️⃣ Go to History section\n\n"
        f"━━━━━━━━━━━━━━━━━━━━━━\n\n"
        f"📊 You can view:\n"
        f"• Deposit history\n"
        f"• Withdrawal history\n"
        f"• Game results\n"
        f"• Bingo card purchases\n"
        f"• Transaction status\n\n"
        f"━━━━━━━━━━━━━━━━━━━━━━\n\n"
        f"📞 For detailed history, contact:\n"
        f"@YasGameSupport"
    )
    
    await update.callback_query.edit_message_text(history_text, reply_markup=reply_markup, parse_mode=None)

async def help_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Show help menu."""
    keyboard = [
        [InlineKeyboardButton("📖 HOW TO PLAY", callback_data='how_to_play')],
        [InlineKeyboardButton("💬 CONTACT SUPPORT", callback_data='support')],
        [InlineKeyboardButton("⬅️ BACK", callback_data='back_to_main')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    help_text = (
        f"❓ HELP & SUPPORT\n\n"
        f"━━━━━━━━━━━━━━━━━━━━━━\n\n"
        f"Select an option below:\n\n"
        f"📖 HOW TO PLAY - Game rules & instructions\n"
        f"💬 CONTACT SUPPORT - Get help from our team\n\n"
        f"━━━━━━━━━━━━━━━━━━━━━━\n\n"
        f"📌 Quick Info:\n"
        f"• Min Deposit: 100 ETB\n"
        f"• Min Withdrawal: 100 ETB\n"
        f"• Processing Time: 24 hours\n"
        f"• Support: 24/7"
    )
    
    await update.callback_query.edit_message_text(help_text, reply_markup=reply_markup, parse_mode=None)

async def how_to_play(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Show detailed how to play."""
    keyboard = [[InlineKeyboardButton("⬅️ BACK", callback_data='help')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    how_to_play_text = (
        f"📖 HOW TO PLAY YAS BINGO\n\n"
        f"━━━━━━━━━━━━━━━━━━━━━━\n\n"
        f"🎯 STEP BY STEP GUIDE:\n\n"
        f"1️⃣ Click PLAY BINGO button\n"
        f"2️⃣ Open your web browser\n"
        f"3️⃣ Go to {GAME_URL}\n"
        f"4️⃣ Register/Login to your account\n"
        f"5️⃣ Deposit minimum 100 ETB\n"
        f"6️⃣ Buy bingo cards (10 ETB each)\n"
        f"7️⃣ Numbers drawn every 2 minutes\n"
        f"8️⃣ Match patterns to WIN!\n\n"
        f"━━━━━━━━━━━━━━━━━━━━━━\n\n"
        f"🏆 WINNING PATTERNS:\n\n"
        f"⭐ Complete horizontal line\n"
        f"⭐ Complete vertical line\n"
        f"⭐ Four corners\n"
        f"⭐ X pattern (both diagonals)\n"
        f"⭐ Full house (all numbers)\n"
        f"⭐ Frame (outer border)\n\n"
        f"━━━━━━━━━━━━━━━━━━━━━━\n\n"
        f"💰 PRIZE STRUCTURE:\n\n"
        f"• Winner gets 80% of prize pool\n"
        f"• Multiple winners share the prize\n"
        f"• Prizes credited instantly\n\n"
        f"━━━━━━━━━━━━━━━━━━━━━━\n\n"
        f"🎮 Click PLAY BINGO to start winning!"
    )
    
    await update.callback_query.edit_message_text(how_to_play_text, reply_markup=reply_markup, parse_mode=None)

async def support(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Show support information."""
    keyboard = [
        [InlineKeyboardButton("📞 CONTACT ON TELEGRAM", url="https://t.me/YasGameSupport")],
        [InlineKeyboardButton("⬅️ BACK", callback_data='help')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    support_text = (
        f"💬 CUSTOMER SUPPORT\n\n"
        f"━━━━━━━━━━━━━━━━━━━━━━\n\n"
        f"📱 Telegram: @YasGameSupport\n"
        f"⏱️ Response Time: 5-30 minutes\n"
        f"🕒 Hours: 24/7\n\n"
        f"━━━━━━━━━━━━━━━━━━━━━━\n\n"
        f"📌 Before contacting support:\n\n"
        f"✓ Have your User ID ready\n"
        f"✓ Transaction reference (if payment issue)\n"
        f"✓ Screenshot of the issue\n\n"
        f"━━━━━━━━━━━━━━━━━━━━━━\n\n"
        f"📋 Common Issues:\n"
        f"• Deposit not credited\n"
        f"• Withdrawal delay\n"
        f"• Game not loading\n"
        f"• Account problems\n\n"
        f"━━━━━━━━━━━━━━━━━━━━━━\n\n"
        f"📞 Click below to message support!"
    )
    
    await update.callback_query.edit_message_text(support_text, reply_markup=reply_markup, parse_mode=None)

async def back_to_main(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Return to main menu."""
    query = update.callback_query
    await query.answer()
    
    keyboard = [
        [InlineKeyboardButton("🎮 PLAY BINGO", callback_data='play_bingo')],
        [InlineKeyboardButton("💰 BALANCE", callback_data='balance'),
         InlineKeyboardButton("💳 DEPOSIT", callback_data='deposit')],
        [InlineKeyboardButton("🏧 WITHDRAW", callback_data='withdraw'),
         InlineKeyboardButton("🏆 LEADERBOARD", callback_data='leaderboard')],
        [InlineKeyboardButton("📜 MY HISTORY", callback_data='history'),
         InlineKeyboardButton("❓ HELP", callback_data='help')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    welcome_text = (
        f"🏆 YAS GAME | Ethiopia's #1 Real-Time Bingo Platform\n\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
        f"👋 Welcome back!\n\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
        f"📊 Platform Features:\n"
        f"• 400 Cards (20x20 Grid)\n"
        f"• Win 80% of Prize Pool\n"
        f"• Real-Time Drawing Every 2 Minutes\n\n"
        f"💳 Payment Methods:\n"
        f"• Telebirr | CBE Bank | Dashen Bank\n\n"
        f"🎁 Get 10 ETB FREE on Registration!\n\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
        f"🎮 Click PLAY BINGO to start winning!"
    )
    
    await query.edit_message_text(welcome_text, reply_markup=reply_markup, parse_mode=None)

def main():
    """Start the bot."""
    print("🤖 Yas Game Bot is starting...")
    
    if not BOT_TOKEN or BOT_TOKEN == 'YOUR_BOT_TOKEN_HERE':
        print("❌ ERROR: BOT_TOKEN environment variable not set!")
        return
    
    application = Application.builder().token(BOT_TOKEN).build()
    
    # Command handlers
    application.add_handler(CommandHandler("start", start))
    
    # Callback handlers
    application.add_handler(CallbackQueryHandler(play_bingo, pattern='play_bingo'))
    application.add_handler(CallbackQueryHandler(balance, pattern='balance'))
    application.add_handler(CallbackQueryHandler(deposit, pattern='deposit'))
    application.add_handler(CallbackQueryHandler(deposit_cbe, pattern='deposit_cbe'))
    application.add_handler(CallbackQueryHandler(deposit_telebirr, pattern='deposit_telebirr'))
    application.add_handler(CallbackQueryHandler(deposit_dashen, pattern='deposit_dashen'))
    application.add_handler(CallbackQueryHandler(withdraw, pattern='withdraw'))
    application.add_handler(CallbackQueryHandler(withdraw_cbe, pattern='withdraw_cbe'))
    application.add_handler(CallbackQueryHandler(withdraw_telebirr, pattern='withdraw_telebirr'))
    application.add_handler(CallbackQueryHandler(withdraw_dashen, pattern='withdraw_dashen'))
    application.add_handler(CallbackQueryHandler(leaderboard, pattern='leaderboard'))
    application.add_handler(CallbackQueryHandler(history, pattern='history'))
    application.add_handler(CallbackQueryHandler(help_menu, pattern='help'))
    application.add_handler(CallbackQueryHandler(how_to_play, pattern='how_to_play'))
    application.add_handler(CallbackQueryHandler(support, pattern='support'))
    application.add_handler(CallbackQueryHandler(back_to_main, pattern='back_to_main'))
    
    print("✅ Bot is running!")
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()
