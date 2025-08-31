import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = "8099679587:AAFjLjlUNC-ar3oHhdrKWZVpshBU8MQ097g"
bot = telebot.TeleBot(TOKEN)

# Allowed users list
ALLOWED_USERS = [7843340099]  # Apna ID yahan daalein

# Admin ID jo approve karega
ADMIN_ID = 7843340099  # Aapka Telegram ID

# /start command
@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_id = message.from_user.id
    if user_id in ALLOWED_USERS:
        bot.reply_to(message, "Hello! Aapko access hai. Kaise ho?")
    else:
        # Inline button create karte hain
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("Request Access", callback_data=f"request_{user_id}"))
        bot.reply_to(message, "Aapko access nahi hai. Access ke liye request bheje:", reply_markup=markup)

# Callback handle karna
@bot.callback_query_handler(func=lambda call: call.data.startswith("request_"))
def handle_request(call):
    user_id = int(call.data.split("_")[1])
    # Admin ko notify karna
    bot.send_message(ADMIN_ID, f"User {user_id} ne access request ki hai!")
    # User ko reply
    bot.answer_callback_query(call.id, "Request bhej di gayi hai. Wait karein admin approval ka.")

# Bot start
print("Bot started...")
bot.polling()
