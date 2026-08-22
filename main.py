
import asyncio
import env
from datetime import datetime
from telethon import TelegramClient
from telethon.tl.functions.messages import CreateChatRequest

# Thay thế bằng api_id và api_hash thực tế của bạn từ my.telegram.org

client = TelegramClient('session_name', env.TELEGRAM_API_ID, env.TELEGRAM_API_HASH)

async def main():
    # Tạo một nhóm chat thông thường với tên nhóm và danh sách thành viên (username hoặc ID)
    # Lưu ý: Các thành viên được thêm vào bắt buộc phải là người bạn đã từng nhắn tin hoặc có trong danh sách liên hệ.
    result = await client(CreateChatRequest(
        users=['me'],  # Có thể thay bằng username khác hoặc để 'me' để tạo nhóm trống với chính bạn
        title=datetime.now().strftime("%Y_%m_%d_%H_%M_%S_%f")
    ))
    
    print("Đã tạo nhóm chat thành công!")
    # print(result.stringify())

with client:
    client.loop.run_until_complete(main())