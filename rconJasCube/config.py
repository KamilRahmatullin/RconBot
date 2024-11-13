from dotenv import dotenv_values
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
ENV_DIR = BASE_DIR / '.env'

env_cgf = dotenv_values(ENV_DIR)

config = {
    'TOKEN_API': env_cgf['TOKEN_API'],
    'rcon_ip': env_cgf['rcon_ip'],
    'rcon_port': env_cgf['rcon_port'],
    'rcon_password': env_cgf['rcon_password']
}
