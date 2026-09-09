import asyncio
from datetime import datetime
import env
from telethon import TelegramClient
from telethon.sessions import StringSession
from telethon.tl.functions.messages import CreateChatRequest

client = TelegramClient(
    StringSession(env.TELEGRAM_SESSION), 
    env.TELEGRAM_API_ID, 
    env.TELEGRAM_API_HASH
)

DATE_FORMAT = "%Y_%m_%d_%H_%M_%S_%f"

def is_matching_date_format(title: str) -> bool:
    """Kiểm tra xem title có đúng định dạng ngày giờ hay không."""
    if not title:
        return False
    try:
        datetime.strptime(title.strip(), DATE_FORMAT)
        return True
    except ValueError:
        return False

async def cleanup_empty_groups():
    print("Đang quét các nhóm chat cũ...")
    count = 0
    async for dialog in client.iter_dialogs():
        # Kiểm tra nếu là group VÀ tên nhóm khớp đúng định dạng ngày tháng
        if dialog.is_group and is_matching_date_format(dialog.title):
            chat = dialog.entity
            messages = await client.get_messages(chat, limit=5)
            user_messages = [msg for msg in messages if msg.message and msg.message.strip() != ""]
            
            if len(user_messages) == 0:
                print(f"Đang xóa nhóm khớp định dạng & trống: {dialog.title} (ID: {chat.id})")
                await client.delete_dialog(dialog.input_entity)
                count += 1
                
    print(f"Đã dọn dẹp xong {count} nhóm thỏa điều kiện.")

async def main():
    await cleanup_empty_groups()
    
    result = await client(CreateChatRequest(
        users=['me'], 
        title=datetime.now().strftime(DATE_FORMAT)
    ))
    
    print("Đã tạo nhóm chat mới thành công!")

with client:
    client.loop.run_until_complete(main())