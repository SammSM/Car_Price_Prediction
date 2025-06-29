from telebot import TeleBot
import prediction
import processing

TOKEN = 

bot = TeleBot(token = TOKEN)

@bot.message_handler(commands = ['start'])
def send_welcome(message):
    bot.reply_to(message, f"🤖 Hi {message.from_user.first_name}")
    bot.reply_to(message, f"""🚗 I am here to predict price for your car.
    Enter your car parameters by the following format:
                 
    model year, motor_type, running, wheel,	color, type, status, motor_volume

    Example:
    mercedes-benz, 2003, petrol, 230000 km,	left, black, Universal, normal,	1.8
                 
    Available parameters:
    - model: 'toyota', 'mercedes-benz', 'kia', 'nissan', 'hyundai
    - motor_type: 'petrol', 'gas', 'petrol and gas', 'diesel', 'hybrid'
    - color: 'skyblue', 'black', 'other', 'golden', 'blue', 'gray', 'silver',
       'white', 'clove', 'orange', 'red', 'green', 'cherry', 'brown',
       'beige', 'purple', 'pink'
    - type: 'sedan', 'suv', 'Universal', 'Coupe', 'pickup', 'hatchback',
       'minivan / minibus'
    - status: 'excellent', 'good', 'crashed', 'normal', 'new'
    """)

@bot.message_handler()
def price_prediction(message):
    try:
        car_params = message.text.split(',')
        car_params = [i[1:] if i[0]==' ' else i for i in car_params]
        params_list = processing.predict_price(car_params)
        bot.send_message(message.chat.id, f'{round(int(prediction.model.predict(params_list)), -2)} $')
    except ValueError as v:
        bot.send_message(message.chat.id, f"😢 Can't predict this car.")
        print(v.__class__.__name__)
        

bot.infinity_polling()