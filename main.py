from telethon.sync import TelegramClient, events
from telethon.sessions import StringSession

api_id = 24806306
api_hash = 'fbd3ce3a8d462a357f3f4585d71d9f4a'
session_string = '1BJWap1wBu7x_hf4RWiBczyoR31NYJ9T8r7jImbSlyfDr3MRHk2MkFcr4-KM8MneeHFMhxtyELS4pbpvCu_xQuFCFxOyPuQIq_vS8uu6iGiSwtfHmKdOm45i-DVlI0qMmoHJwgJ8480ouzCKIJPMeC7peFj4rsv-4cjC8-gCG36uO0oVkvwVawLe6gT6PzTFOXA1uLQJD5V7BOSHIwUHeR8MYHMceHbpUW5-6NVf4FggBQWPogoK7MJbReHBNod1wLJUhmNXt7kuZiNqXqruaTktCiDl-5DtcALNEkU5vgvDAmLpK5G9YpFSV0-abXquZMY2KxySuU5Z4SC3SO0Kxgp_W_HRJU2g='

client = TelegramClient(StringSession(session_string), api_id, api_hash)

@client.on(events.NewMessage)
async def handler(event):
    await event.reply("البوت شغال 🔥")

client.start()
client.run_until_disconnected()
