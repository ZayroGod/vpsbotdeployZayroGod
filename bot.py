# Final Complete bot.py - Rebranded for VantixHost
import discord
from discord import app_commands
from discord.ext import commands, tasks
import asyncio
import subprocess
import json
import os
import random
import logging
from datetime import datetime, timedelta

# ---------------- CONFIG ----------------
TOKEN = "" 
GUILD_ID = 1432390408184529084
MAIN_ADMIN_IDS = {1397506807089598474}
SERVER_IP = "207.244.240.48"
QR_IMAGE = ""
IMAGE = "jrei/systemd-ubuntu:22.04"
DEFAULT_RAM_GB = 32
DEFAULT_CPU = 6
DEFAULT_DISK_GB = 100
DATA_DIR = "data"
USERS_FILE = os.path.join(DATA_DIR, "users.json")
VPS_FILE = os.path.join(DATA_DIR, "vps_db.json")
INV_CACHE_FILE = os.path.join(DATA_DIR, "inv_cache.json")
GIVEAWAY_FILE = os.path.join(DATA_DIR, "giveaways.json")
POINTS_PER_DEPLOY = 6
POINTS_RENEW_15 = 4
POINTS_RENEW_30 = 8
VPS_LIFETIME_DAYS = 15
RENEW_MODE_FILE = os.path.join(DATA_DIR, "renew_mode.json")
LOG_CHANNEL_ID = None
OWNER_ID = 1397506807089598474

# Global admin sets
ADMIN_IDS = set(MAIN_ADMIN_IDS)

# Logging - Updated to VantixHost
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("VantixHostBot")

# ... [Keep your JSON helpers and Docker helper functions here] ...

async def send_log(action: str, user, details: str = "", vps_id: str = ""):
    """Send professional VantixHost log embed to log channel"""
    if not LOG_CHANNEL_ID:
        return
    
    try:
        channel = bot.get_channel(LOG_CHANNEL_ID)
        if not channel: return
        
        # ... [Keep your color_map logic] ...

        embed = discord.Embed(
            title=f"🛡️ VantixHost | {action}",
            color=color,
            timestamp=datetime.utcnow()
        )
        
        # ... [Keep your field additions] ...
        
        embed.set_footer(text="VantixHost VPS Management System")
        await channel.send(embed=embed)
        
        # ... [Keep your log saving logic] ...
    except Exception as e:
        print(f"Failed to send log: {e}")

# ---------------- Bot Events ----------------
@bot.event
async def on_ready():
    # Set custom status for VantixHost
    await bot.change_presence(activity=discord.Game(name="Managing VantixHost VPS"))
    logger.info(f"VantixHost Bot ready: {bot.user}")
    expire_check_loop.start()
    giveaway_check_loop.start()

@bot.event
async def on_message(message):
    if message.author.bot:
        return
    
    content = message.content.lower()
    # Pterodactyl Help rebranded for VantixHost
    if any(keyword in content for keyword in ['how to install pterodactyl', 'pterodactyl install', 'pterodactyl setup']):
        embed = discord.Embed(
            title="🦕 Pterodactyl Panel on VantixHost", 
            description="Our VPS environments are optimized for panel hosting.",
            color=discord.Color.from_rgb(0, 255, 255)
        )
        embed.add_field(name="Official Guide", value="https://pterodactyl.io/panel/1.0/getting_started.html", inline=False)
        embed.add_field(name="VantixHost Edge", value="Use `/deploy` to get started with a fresh Linux environment immediately.", inline=False)
        embed.set_footer(text="VantixHost - Premium Infrastructure")
        await message.channel.send(embed=embed)
    
    await bot.process_commands(message)

# ---------------- Changes to create_vps DM ----------------
# Update the giveaway DM section in giveaway_check_loop to match:
# embed = discord.Embed(title="🎉 You Won a VantixHost VPS!", color=discord.Color.gold())
# embed.set_footer(text="VantixHost Giveaway - No renewal for free tier.")
