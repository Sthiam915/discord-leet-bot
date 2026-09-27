from datetime import datetime, timedelta
import discord
from discord.ext import tasks

reminder_channel_id = YOUR_CHANNEL_ID  # Replace with your channel ID
reminder_time = "09:00"  # Time to send reminders

@tasks.loop(hours=24)
async def set_reminders():
    now = datetime.now()
    if now.strftime("%H:%M") == reminder_time:
        channel = discord.utils.get(discord.Client.get_all_channels(), id=reminder_channel_id)
        if channel:
            await channel.send("Don't forget to mark your LeetCode daily challenge as done!")

@set_reminders.before_loop
async def before_set_reminders():
    await discord.Client.wait_until_ready()