import datetime 
import telepot   
from telepot.loop import MessageLoop
import RPi.GPIO as GPIO 
from time import sleep  
from  picamera import PiCamera

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(7,GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(11, GPIO.IN)
GPIO.setup(13,GPIO.OUT)

now = datetime.datetime.now()

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']
    
    
    print ('Received:')
    print(command)

    if command == 'Take photo':
        bot.sendMessage (chat_id, str("Hi! User"))
        bot.sendMessage(chat_id, str("capturing....please wait !!!"))
        camera=PiCamera()
        camera.start_preview()
        sleep(2)
        camera.capture("sample.jpg")
        GPIO.output(13,GPIO.HIGH)
        sleep(1)
        GPIO.output(13,GPIO.LOW)
        camera.stop_preview()
        print("Sending photo to " + str(chat_id))
        bot.sendPhoto(chat_id, photo = open('./sample.jpg', 'rb'))
               
    elif (command == "Light on"):
        bot.sendMessage(chat_id, str("Light ON!!!"))
        GPIO.output(13,GPIO.HIGH)
        GPIO.output(5, 1)
        GPIO.output(13,GPIO.LOW)
    elif (command == "Light off"):
        bot.sendMessage(chat_id, str("Light OFF!!!"))
        GPIO.output(13,GPIO.HIGH)
        GPIO.output(5, 0)
        GPIO.output(13,GPIO.LOW)
    elif (command == "Fan on"):
        bot.sendMessage(chat_id, str("Fan ON!!!"))
        GPIO.output(7, 1)
    elif (command == "Fan off"):
        bot.sendMessage(chat_id, str("Fan OFF !!!"))
        GPIO.output(7, 0)
    elif (command == "Press"):
        button_state = GPIO.input(11)
        sleep(5)
        
        new_button_state = GPIO.input(11)
        bot.sendMessage(chat_id, "capturing....please wait !!")
        if button_state==new_button_state:
            camera=PiCamera()
            camera.start_preview()
            sleep(2)
            GPIO.output(13,GPIO.HIGH)
            camera.capture("sample.jpg")
            sleep(1)
            GPIO.output(13,GPIO.LOW)
            camera.stop_preview()
            print("Sending photo to " + str(chat_id))
            bot.sendPhoto(chat_id, photo = open('./sample.jpg', 'rb'))
    elif (command == "Take video"):
        bot.sendMessage(chat_id, str("capturing video....please wait !!!"))
        camera=PiCamera()
        GPIO.output(13,GPIO.HIGH)
        camera.start_recording("sample.h264")
        sleep(10)  
        camera.stop_recording()
        GPIO.output(13,GPIO.LOW)
        print("Sending video to " + str(chat_id))
        bot.sendVideo(chat_id, video=open('./sample.h264', 'rb'))
    
bot = telepot.Bot('7137927378:AAF5M6cnlPClBJdikt2rRbRGvL5hBXzY6fk')
print (bot.getMe())

print("Listening.....")
MessageLoop(bot, handle).run_as_thread()

while 1:
    sleep(10)
    
    
    
# 7137927378:AAF5M6cnlPClBJdikt2rRbRGvL5hBXzY6f









