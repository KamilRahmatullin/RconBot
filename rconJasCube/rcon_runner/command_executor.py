from datetime import datetime
from pathlib import Path

from rcon import Client

from rconJasCube import config


async def run_command(user_id, cmd):
    BASE_DIR = Path(__file__).resolve().parent.parent

    command = cmd.split()
    arg1 = command[0]
    args = command[1:]

    with Client(host=config.rcon_ip, port=config.rcon_port,
                passwd=config.rcon_password) as client:
        response = client.run(arg1, *args)
    with open(f"{BASE_DIR}\logs\log.txt", 'a', encoding='utf-8') as f:
        f.write(f'\n{datetime.now()} | Пользователь {user_id} - /{cmd}')
    return str(response)
