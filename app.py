import discord
import os
import dotenv
dotenv.load_dotenv()
token = str(os.getenv("TOKEN"))

bot = discord.Bot()

@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")

@bot.slash_command(name = "hello", description = "says hello to the user")
async def hello(ctx):
    await ctx.respond("Hey!")

bot.run(os.getenv('TOKEN')) #run the bot with the token
