from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

import app.keyboards as kb
from app.funcs import write_json, read_json

# from app.funcs import write_json, read_json

router = Router()


class Reg(StatesGroup):
    id = State()
    name = State()
    number = State()


'''Хэндлеры для Commands'''
@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(f'Hello, user with ID = {message.from_user.id}, named {message.from_user.username}!',
                        reply_markup=kb.main_inline)


@router.message(Command('help'))
async def get_help(message: Message):
    await message.answer('Can\'t help.... buuut))', reply_markup=await kb.inline_cars())


# @router.message(Command('get_photo'))
# async def get_photo(message: Message):
#     await message.answer_photo(photo='AgACAgIAAxkBAAIBJ2e-GwYi5AdjXkjnmK_tpRfreM09AAIb7jEbQ3zwSQz9C3y0sPuUAQADAgADeQADNgQ',
#                                caption='Black...')

@router.message(Command('get_user'))
async def reg_first(message: Message):
    data = await read_json(user_id=message.from_user.id)
    if data != {}:
        await message.answer(f'There is user. Name: {data["name"]}')
    else:
        await message.answer(f'There is no user...')



@router.message(Command('sign'))
async def reg_first(message: Message, state: FSMContext):
    await state.set_state(Reg.name)
    await message.answer('Write your name:')


@router.message(Reg.name)
async def reg_second(message: Message, state: FSMContext):
    await state.update_data(id=message.from_user.id, name=message.text)
    await state.set_state(Reg.number)
    await message.answer('Write your number (starts with "+"):')


@router.message(Reg.number)
async def reg_end(message: Message, state: FSMContext):
    await state.update_data(number=message.text)
    data = await state.get_data()
    await write_json(data)
    await message.answer(f'Thanks for registration!\n'
                         f'Your name is {data["name"]}\n'
                         f'Your number is {data["number"]}')
    await state.clear()


'''Хэндлеры с F фильтром'''
# @router.message(F.text == 'How are you?')
# async def howareu_cmd(message: Message):
#     await message.answer('All is good))')

@router.message(F.photo)
async def photo_handler(message: Message):
    await message.answer(f'ID photo: {message.photo[-1].file_id}')



'''Хэндлеры для поимки callback data'''
@router.callback_query(F.data.startswith('page'))
async def callback_home(callback: CallbackQuery):
    c_data = callback.data
    await callback.answer(f'You chose {c_data[5:]}')
    await callback.message.edit_text(f'Hello) You\'ve chosen {c_data[5:]}', reply_markup=await kb.inline_cars())



@router.callback_query(F.data.startswith('car'))
async def callback_cars(callback: CallbackQuery):
    c_data = callback.data
    await callback.answer(f'You chose {c_data[4:]}')
    await callback.message.edit_text(f'Hello) You\'ve chosen {c_data[4:]} car')


