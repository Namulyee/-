import os
import discord
import asyncio
import datetime
from discord.ext import commands
import youtube_dl


from urllib import parse, request
import re

app = commands.Bot (command_prefix='곤드레야 ')

@app.event
async def on_ready():
    print('다음으로 로그인합니다: ')
    print('app.user.name')
    print('로딩성공')
    await app.change_presence (status=discord.Status.online)
    await app.change_presence(activity=discord.Game(name="곤드레야 도와줘로 여러 명령어를 확인하세요!"))

@app.command()
async def 안녕(ctx):
    await ctx.send('안녕하세요. 오늘 하루도 즐거우시길 바랄게요! :)')
    await ctx.send('https://tenor.com/view/shaq-shaquille-oneal-wiggle-evil-smile-gif-15358842')  
@app.command()
async def 섬정보(ctx):
    embed = discord.Embed(title="Pluto", description="섬 정보입니다.", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    embed.add_field(name="섬이 탄생한 날", value=f"{ctx.guild.created_at}")
    embed.add_field(name="섬장", value="필립, 네네치킨, 표범")
    embed.set_thumbnail(url="https://giphy.com/gifs/nasa-nasagif-pluto-nasa60th-25aA0HrWElytDpFNSu")

    await ctx.send(embed=embed)

@app.command()
async def 도와줘(ctx):
    embed = discord.Embed(title="플루토 안내데스크", desription="무슨 일로 오셨나요?", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    embed.add_field(name="접두사", value="곤드레야")
    embed.add_field(name="도와줘", value="안내데스크로 데려다드립니다.")
    embed.add_field(name="섬정보", value="섬 정보에 대해 알려드립니다.")
    embed.add_field(name="안녕", value="인사를 해드립니다.")
    embed.add_field(name="대여 (아이템이름)", value="대여 기능이 됩니다.")
    embed.add_field(name="반납", value="반납이 됩니다.")
    embed.set_thumbnail(url="https://bit.ly/2MmSAc1")
    
    await ctx.send(embed=embed)

@app.command()
async def 반납(ctx):
    await ctx.send(f"{ctx.author.name} 님의 섬 공용 도구를 성공적으로 반납했습니다!")

@app.command()
async def 대여(ctx, my_message):
    embed = discord.Embed(title="플루토 공용 도구 대여소", description="도구 대여 완료!", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    embed.add_field(name="닉네임", value=f"{ctx.author.mention}")
    embed.add_field(name="도구 이름", value=f"{my_message}")
    embed.set_thumbnail(url="https://bit.ly/36g5NKI")
    
    await ctx.send(embed=embed)

@app.command()
async def 닭머가리(ctx):
    await ctx.send("https://bit.ly/3aaHq26")
    

app.run('ODAxMjM0NDM2NzY3MDg4Njcy.YAdttw.XRIpMd3cSpNH5baWM7uE5qgr6B8')
 