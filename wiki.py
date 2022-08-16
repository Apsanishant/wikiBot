from ast import alias
from re import search
from unittest import result
import discord
import wikipedia
from discord.ext import commands

client = commands.Bot(command_prefix='/')



@client.command()
async def wiki(ctx, *, question):
    r = wikipedia.search(question)
    await ctx.send(r)    
    await ctx.send(wikipedia.page(r).summary)    
client.run("TOKEN")