import discord
import asyncio
import time
import logging

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if "woof" in message.content.upper().lower() or "dog" in message.content.upper().lower():
        msg = await client.send_message(message.channel,"stupid dog, you make me look bad")
        msg1 = await client.send_file(message.channel, "Mr._Eustace_Bagge.jpg")
        time.sleep(2)
        await client.delete_message(msg)
        await client.delete_message(msg1)

    if "unacceptable" in message.content.upper().lower():
        msg1 = await client.send_file(message.channel, "lemon.gif")

client.run('NDE4MDc4MDgwMjU1NjU1OTM2.DXcVSA.X1_R1WrieRixZLRgM7N_q_O2Ny8')