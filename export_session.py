import env
from telethon import TelegramClient
from telethon.sessions import StringSession

# Đăng nhập thủ công một lần cuối để sinh ra chuỗi string session
client = TelegramClient(StringSession(), env.TELEGRAM_API_ID, env.TELEGRAM_API_HASH)
with client:
    print("CHUỖI SESSION CỦA BẠN (Hãy copy chuỗi dài bên dưới để lưu vào Doppler):")
    print(client.session.save())