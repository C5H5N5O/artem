import discord
from discord.ext import commands
import serial

ser = serial.Serial("COM4", 9600)


token = "ODA4Mzg2MjIzMjEwMjMzODY2.YCFyVg.QzlmRUuSANMzKLcCybLu8wa9RlE"


class Bot(discord.Client):
    async def on_ready(self):
        print('bot ready')


    async def on_message(self, message):
        print(message.content)
        ser.write(message.content.encode('utf-8'))

bot = Bot()
bot.run(token)