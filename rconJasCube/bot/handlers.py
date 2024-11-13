from aiogram import Router
from aiogram.filters import Command

from bot.utils import get_level, get_cmds, add_user, show_users, remove_user
from rcon_runner.command_executor import run_command

router = Router()


@router.message(Command('start'))
async def start(message):
    await message.answer("Привет! Это бот для управления JasCube.\n\n"
                         "Используйте /help для получения списка доступных комманд.")


@router.message(Command('help'))
async def start(message):
    level = get_level(message)
    cmds = get_cmds(level)
    await message.answer(
        f"\nВаш уровень: {level}\nВаш ID: {message.from_user.id}\nДоступные команды: {cmds}")


@router.message(Command('r'))
async def rcon(message):
    level = get_level(message)
    cmds = get_cmds(level)

    try:
        cmd = message.text.split()[1]
    except IndexError:
        await message.answer('Пожалуйста, введите команду!')
        return
    if '*' in cmds:
        resposne = str(await run_command(message.from_user.id, message.text[3:])).replace('§x§8§f§f§f§f§f', '').replace(
            '§x§5§0§C§6§F§F§l§n▌§r', '').replace('§f', '').replace('§9', '').replace('§f', '').replace('§8',
                                                                                                       '').replace('§7',
                                                                                                                   '').replace(
            '§b', '').replace('§l', '').replace('§x§5§0§C§6§F§F▌§r', '')
        if resposne:
            await message.answer('Ответ от сервера: \n' + str(resposne))
        await message.answer(f'Выполняю rcon-команду: /{message.text[3:]}')
    elif cmd == 'lp' and cmd in cmds.split(' | '):
        if message.text.startswith('/r lp user') and (
                message.text.endswith('yt') or message.text.endswith('yt+') or message.text.endswith('ofyt') \
                or message.text.endswith('helper') or message.text.endswith('moder') \
                or message.text.endswith('stmoder') or message.text.endswith('glmoder') \
                or message.text.endswith('cuber') or message.text.endswith('clear') \
                or message.text.endswith('hranitel') or message.text.endswith('burjui') or message.text.endswith(
            'prince') \
                or message.text.endswith('korol') or message.text.endswith('mefisto') or message.text.endswith('geroi') \
                or message.text.endswith('barin') or message.text.endswith('ricar') or message.text.endswith(
            'kupec') or message.text.endswith('bariga')):
            resposne = str(await run_command(message.from_user.id, message.text[3:])).replace('§x§8§f§f§f§f§f',
                                                                                              '').replace(
                '§x§5§0§C§6§F§F§l§n▌§r', '').replace('§f', '').replace('§9', '').replace('§f', '').replace('§8',
                                                                                                           '').replace(
                '§7', '').replace('§b', '').replace('§l', '').replace('§x§5§0§C§6§F§F▌§r', '')
            if resposne:
                await message.answer('Ответ от сервера: \n' + str(resposne))
            await message.answer(f'Выполняю rcon-команду: /{message.text[3:]}')

        else:
            await message.answer(f'Группа не найдена!')
    elif cmd in cmds.split(' | '):
        resposne = str(await run_command(message.from_user.id, message.text[3:])).replace('§x§8§f§f§f§f§f', '').replace(
            '§x§5§0§C§6§F§F§l§n▌§r', '').replace('§f', '').replace('§9', '').replace('§f', '').replace('§8',
                                                                                                       '').replace('§7',
                                                                                                                   '').replace(
            '§b', '').replace('§l', '').replace('§x§5§0§C§6§F§F▌§r', '')
        if resposne:
            await message.answer('Ответ от сервера: \n' + str(resposne))
        await message.answer(f'Выполняю rcon-команду: /{message.text[3:]}')
    else:
        await message.answer(f'Команда /{cmd} не найдена или у вас на неё нет прав!')


@router.message(Command('add_user'))
async def add_user_cmd(message):
    level = get_level(message)
    cmds = get_cmds(level)
    if '*' in cmds or 'add_user' in cmds:
        if len(message.text.split()) != 3:
            await message.answer('Использование: /add_user айди группа')
        else:
            try:
                user_id = int(message.text.split()[1])
                group = message.text.split()[2]
                await message.reply(add_user(user_id, group))
            except Exception as e:
                await message.reply(f'{e}')
    else:
        await message.answer('Команда /add_user не найдена или у вас на неё нет прав!')


@router.message(Command('remove_user'))
async def remove_user_cmd(message):
    level = get_level(message)
    cmds = get_cmds(level)
    if '*' in cmds or 'remove_user' in cmds:
        if len(message.text.split()) != 2:
            await message.answer('Использование: /remove_user айди')
        else:
            try:
                user_id = int(message.text.split()[1])
                await message.reply(remove_user(user_id))
            except Exception as e:
                await message.reply(f'{e}')
    else:
        await message.answer('Команда /remove_user не найдена или у вас на неё нет прав!')


@router.message(Command('show_users'))
async def show_users_cmd(message):
    level = get_level(message)
    cmds = get_cmds(level)
    if '*' in cmds or 'show_users' in cmds:
        await message.answer(str(show_users()))
    else:
        await message.answer('Команда /show_users не найдена или у вас на неё нет прав!')


@router.message()
async def rcon(message):
    level = get_level(message)
    cmds = get_cmds(level)
    await message.reply(f'Доступные команды для вас: {cmds}')
