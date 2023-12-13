from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher import FSMContext

from loader import dp, bot


from utils.misc.kursishi import rectangle, trapetsiya

from aiogram.dispatcher.filters.state import State, StatesGroup

class Misol(StatesGroup):
    a = State()
    b = State()
    n = State()
    tenglama = State()
    usul = State()


from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

tugmalar = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Trapetsiya", callback_data="trapetsiya"),
            InlineKeyboardButton(text="To'g'ri to'rtburchaklar", callback_data="rectangle"),
        ],
        [
            InlineKeyboardButton(text="Bekor qilish", callback_data="cancel"),
        ],
    ]
)




@dp.message_handler(commands=["misol"])
async def misol(message: Message):
    await message.answer("Integral tenglamaning quyi chegarasi a ni kiriting:")
    await Misol.a.set()

@dp.message_handler(state=Misol.a)
async def get_a(message: Message, state: FSMContext):
    a = message.text
    if a.isdigit():
        await state.update_data(a = a)
        await message.answer("Integral tenglamaning yuqori chegarasi b ni kiriting:")
        await Misol.next()
    else:
        await message.answer("Iltimos, raqam kiriting!")

@dp.message_handler(state=Misol.b)
async def get_b(message: Message, state: FSMContext):
    b = message.text
    if b.isdigit():
        await state.update_data(b = b)
        await message.answer("Integral tenglamaning qadamlar soni n ni kiriting")
        await Misol.next()
    else:
        await message.answer("Iltimos, raqam kiriting!")

@dp.message_handler(state=Misol.n)
async def get_n(message: Message, state: FSMContext):
    n = message.text
    if n.isdigit():
        await state.update_data(n=n)
        await message.answer("Integral tenglamani kiriting:\n\n\n<b>Misol:</b>\n1/x^2+8")
        await Misol.next()
    else:
        await message.answer("Iltimos, raqam kiriting!")

@dp.message_handler(state=Misol.tenglama)
async def get_tenglama(message: Message, state: FSMContext):
    await state.update_data(tenglama=message.text, message_id=message.message_id)
    await message.answer("Integral tenglamani yechish uchun quyidagi usullardan birini tanlang", reply_markup=tugmalar)
    await Misol.next()

@dp.callback_query_handler(state=Misol.usul)
async def usul(call: CallbackQuery, state: FSMContext):
    await call.message.edit_reply_markup()
    usul = call.data
    

    data = await state.get_data()
    a = data.get("a")
    b = data.get("b")
    n = data.get("n")
    tenlama = data.get("tenglama")
    message_id = data.get("message_id")
    
    await state.finish()
    
    print(usul)
    print(call.from_user.id)
    print(message_id, 'message_id')
    print(a, type(a))
    print(n, type(b))
    print(n, type(n))
    if usul == "trapetsiya":
        res = trapetsiya(a=int(a), b=int(b), n=int(n), integral=tenlama)
        await bot.send_message(chat_id=call.message.chat.id, text=res["data"], reply_to_message_id=message_id)
    elif usul == "rectangle":
        res = rectangle(a=int(a), b=int(b), n=int(n), integral=tenlama)
        await bot.send_message(chat_id=call.message.chat.id, text=res["data"], reply_to_message_id=message_id)
    else:
        await call.message.answer("Amal bekor qilindi!")