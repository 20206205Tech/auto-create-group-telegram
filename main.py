import asyncio
import env
from datetime import datetime
from telethon import TelegramClient
from telethon.sessions import StringSession
from telethon.tl.functions.messages import CreateChatRequest

# Sử dụng StringSession thay cho file session_name
client = TelegramClient(
    StringSession(env.TELEGRAM_SESSION), 
    env.TELEGRAM_API_ID, 
    env.TELEGRAM_API_HASH
)

async def cleanup_empty_groups():
    print("Đang quét các nhóm chat cũ...")
    count = 0
    async for dialog in client.iter_dialogs():
        if dialog.is_group:
            chat = dialog.entity
            messages = await client.get_messages(chat, limit=5)
            user_messages = [msg for msg in messages if msg.message and msg.message.strip() != ""]
            
            if len(user_messages) == 0:
                print(f"Đang xóa nhóm trống: {dialog.title} (ID: {chat.id})")
                await client.delete_dialog(dialog.input_entity)
                count += 1
                
    print(f"Đã dọn dẹp xong {count} nhóm không có tin nhắn.")

async def main():
    await cleanup_empty_groups()
    
    result = await client(CreateChatRequest(
        users=['me'], 
        title=datetime.now().strftime("%Y_%m_%d_%H_%M_%S_%f")
    ))
    
    print("Đã tạo nhóm chat mới thành công!")

with client:
    client.loop.run_until_complete(main())