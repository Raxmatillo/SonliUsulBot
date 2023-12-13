from aiogram.types import Message


from loader import dp, bot




@dp.message_handler(command=["misol"])
async def misol(message: Message):
    await message.answer("hey")