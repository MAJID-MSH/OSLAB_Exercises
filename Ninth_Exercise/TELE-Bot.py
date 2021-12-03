import telebot
import random
import qrcode
import jdatetime
from gtts import gTTS


bot = telebot.TeleBot("5071909239:AAE-kLbsN5Rllk1Rjodru8T2hTlJ-GQomZc")

@bot.message_handler(commands=['start'])
def starter(message):
    bot.send_message(message.chat.id ,"Hi "+message.from_user.first_name+" ,Welcome to My Bot!"+"\nسلام "+message.from_user.first_name+" به ربات من خوش آمدید")
    # bot.reply_to(message , "Hi Welcome to My Bot!\nسلام به بات من خوش آمدید!")
    bot.send_message(message.chat.id ,"/help\n to show menu\nنمایش راهنمای ربات")

@bot.message_handler(commands=['help'])
def help(message):
    bot.reply_to(message , """
	/help ---> Bot Guide(راهنمای ربات)
	/game ---> Number guessing(بازی حدس عدد)
	/age ---> Calculating age(محاسبه سن)
	/voice ---> text to voice(تبدیل متن انگلیسی به ویس)
	/max ---> find biggest number(نمایش بزرگترین عدد از میان اعداد ورودی)
	/argmax ---> index of biggest number(اندیس بزرگترین عدد)
	/qrcode ---> Makes QR-Code(نمایش کد qr)
 	""")

#****************===========================************************
@bot.message_handler(commands=['game'])
def RandNum(message):
    global Computer_Number
    Computer_Number = str(random.randint(0,100))
    User_Number = bot.send_message(message.chat.id , "Guess number between 0-100\nعددی بین 0=-100 حدس بزنید")
    bot.register_next_step_handler(User_Number , RandGame)


def RandGame(User_Number):
    if Computer_Number > User_Number.text :
        User_Number =bot.send_message(User_Number.chat.id,"GO UP !\n برو بالا ! ")
        bot.register_next_step_handler(User_Number , RandGame)
    elif Computer_Number < User_Number.text:
        User_Number = bot.send_message(User_Number.chat.id,"GO DOWN !\n برو پایین ! ")
        bot.register_next_step_handler(User_Number , RandGame)
    elif Computer_Number == User_Number.text :
        bot.send_message(User_Number.chat.id,"GOOD JOB! ♥ \n باریکلا♥")
        bot.send_message(User_Number.chat.id,"Try again click on /game")
        bot.send_message(User_Number.chat.id , "    MADE BY MAJID-MSH :)    \n\t\t<----GOODLUCK---->")

#****************===========================************************
@bot.message_handler(commands=['age'])
def ReciveAge(message):
    user_age = bot.send_message(message.chat.id , "Enter The Date Of Birth In This Form(Hijri Shamsi) 1400/8/12 \n تاریخ تولد هجری شمسی را وارد کنید :")
    bot.register_next_step_handler(user_age , FindAge)

def FindAge(user_age):
    tempdate = jdatetime.date.today()
    user_date = user_age.text.split('/')
    year = tempdate.year - int(user_date[0])
    bot.send_message(user_age.chat.id , "Your Age Is: \n سن شما :"+ str(year))
    bot.send_message(user_age.chat.id , "    MADE BY MAJID-MSH :)    ")

#****************===========================************************
@bot.message_handler(commands=['voice'])
def ReciveVoice(message):
	user_text = bot.send_message(message.chat.id , "Enter Your Text:\nمتن خود را به انگلیسی وارد کنید :")
	bot.register_next_step_handler(user_text,CreateVoice)

def CreateVoice(user_text):
    mytext= user_text.text
    language = 'en'
    vtemp = gTTS(text=mytext, lang=language, slow=False)
    vtemp.save('Voice.mp3') 
    voice = open('Voice.mp3' , 'rb')
    bot.send_voice(user_text.chat.id ,voice)
    bot.send_message(user_text.chat.id , "    MADE BY MAJID-MSH :)    \n\t\t<----GOODLUCK---->")

#****************===========================************************
@bot.message_handler(commands=['max'])
def ReciveMax(message):
	user_num = bot.send_message(message.chat.id, "Enter Numbers in this form \nیک رشته از اعداد به این صورت وارد نمایید:  1,2,3,4,5,6")
	bot.register_next_step_handler(user_num , FindMax)

def FindMax(user_num):
    numbers = list(map(int, user_num.text.split(',')))
    bot.send_message(user_num.chat.id, "The Biggest Number is(بزرگترین عدد): \n" + str(max(numbers)))
    bot.send_message(user_num.chat.id , "    MADE BY MAJID-MSH :)    ")

#****************===========================************************
@bot.message_handler(commands=['argmax'])
def Reciveindex(message):
	user_index= bot.send_message(message.chat.id, "Enter Numbers in this form \nیک رشته از اعداد به این صورت وارد نمایید:  1,2,3,4,5,6")
	bot.register_next_step_handler(user_index, FindIndex)

def FindIndex(user_index):
    numbers = list(map(int, user_index.text.split(',')))
    bot.send_message(user_index.chat.id, "Maximum Number Index is(اندیس بزرگترین عدد): \n" + str(numbers.index(max(numbers))))
    bot.send_message(user_index.chat.id , "    MADE BY MAJID-MSH :)    ")

#****************===========================************************
@bot.message_handler(commands=['qrcode'])
def MakeQrcode(message):
	user_qr= bot.send_message(message.chat.id , "Write somthing to convert into QrCode\n متنی بنویسید تا به کد qr تبدیل شود")
	bot.register_next_step_handler(user_qr,CreateQrcode)

def CreateQrcode(user_qr):
    img= qrcode.make(user_qr.text)
    img.save('QrCode.png')
    photo = open('QrCode.png', 'rb')
    bot.send_photo(user_qr.chat.id , photo)
    bot.send_message(user_qr.chat.id , "    MADE BY MAJID-MSH :)    \n\t\t<----GOODLUCK---->")

#****************===========================************************
@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, "You entered the wrong message, please try again! \n پیام اشتباه وارد کردید , دوباره تلاش کنید!")

bot.infinity_polling()
