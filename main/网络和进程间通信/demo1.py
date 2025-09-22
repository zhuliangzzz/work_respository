#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
   @file:demo1.py
   @author:zl
   @time: 2025/9/2 14:35
   @software:PyCharm
   @desc:
"""
import asyncio
import time

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)


async def main():
    print(f'started at {time.strftime("%X")}')
    await say_after(1, 'hello')
    await say_after(2, 'world')
    print(f'finished at {time.strftime("%X")}')


asyncio.run(main())