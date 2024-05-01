import argparse
from pathlib import Path
import asyncio

import discord

from dotenv import dotenv_values


async def send_msg():

    parser = argparse.ArgumentParser()
    parser.add_argument("file", type=str)
    parser.add_argument("-e-", "--env", default=".env", type=str)
    args = parser.parse_args()

    env_path = Path(args.env)
    config = dotenv_values(env_path)
    
    file_path = Path(args.file)

    async with discord.Client(intents=discord.Intents.none()) as client:
        await client.login(config["api_token"])
        user = await client.fetch_user(config["user_id"])
        with open(file_path, "r") as file:
            await user.send(file=discord.File(file))
            
def send_msg_():

    asyncio.run(send_msg())
