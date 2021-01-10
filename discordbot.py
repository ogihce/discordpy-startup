from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.commands()
async def ping(ctx):
    await ctx.send('pong')

@bot.commands()
async def ping(ctx):
    await ctx.send('pong')

@bot.commands()
async def bath(ctx):
    bath = f'{message.author.mention} 呼んだ？ねえ今呼んだ？呼んだよねぇｗｗ'
    await ctx.send(bath)
    
@client.event
async def on_message(message):
    if client.user in message.mentions: # 話しかけられたかの判定
        await reply(message) # 返信する非同期関数を実行

bot.run(token)
