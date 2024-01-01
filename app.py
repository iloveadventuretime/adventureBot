import songs
import random
import discord
import os
import dotenv
dotenv.load_dotenv()
token = str(os.getenv("TOKEN"))

bot = discord.Bot()
characters = ['finn', 'marceline', 'jake', 'bmo', 'ice king', 'princess bubblegum', 'lady rainicorn', 'lumpy space princess']

@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")

@bot.slash_command(name = "hello", description = "says hello to the user")
async def hello(ctx):
    await ctx.respond("Hey!")

@bot.slash_command(name = "songi", description = "testing the random song")
async def songi(ctx):
    song = random.randint(0, 9)
    songURL = "https://open.spotify.com/track/{}"
    await ctx.respond(songURL.format(songs.songs[song]))

@bot.slash_command(name = "characters", description = "input a character name or 'random' (must be in lowercase)")
async def character(ctx, char):
    if char.lower() in characters:
        charURL = "https://adventuretime.fandom.com/wiki/{}"
        await ctx.respond(charURL.format(char.lower()))
    else:
        await ctx.respond("couldn't find character or you didnt input a character")
        await ctx.respond(char)

bot.run(os.getenv('TOKEN')) #run the bot with the token
