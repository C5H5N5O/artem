from logging import ERROR
import discord
from discord.ext import tasks
from discord import Client




token = "ODA4Mzg2MjIzMjEwMjMzODY2.YCFyVg.5MNH25ocQnYs7GOkC9RRCyGuqK0"
CHENNEL_ID = 910925137942052897

bot = Client()   


def read_data(delete_after_read=False):
    with open("buffer.txt", "r") as f:
        data = f.read()
        f.close()
    if delete_after_read:
        open("buffer.txt", "w").close()
    return data




async def on_ready():
    channel = Client.get_channel(910925137942052898) # Voice channel
    bot_connection = member.guild.voice_client # Bot connection



@tasks.loop(seconds=0.05)
async def write():
    await bot.wait_until_ready() 

    message = read_data(delete_after_read=True)

    if message == None: return
    try:
        if len(message) > 0: 
            channel = Client.get_channel(bot, CHENNEL_ID)
            print(message)
            await channel.send(message)
    except: pass


write.start()
bot.run(token)