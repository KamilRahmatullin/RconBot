from .users import groups, users


def get_cmds(level):
    cmds = ''
    for cmd in groups[level]:
        cmds = cmds + cmd + ' | '
    return cmds


def get_level(message):
    try:
        level = users[message.from_user.id]
    except Exception as e:
        level = '0'
        print(f'Error: {e}')
    return level


def add_user(user_id, group):
    if group not in groups:
        raise f'Данной группы не существует! {groups.keys()}'
    try:
        users[user_id] = group
        return f'Пользователь {user_id} добавлен в группу {group}'
    except Exception as e:
        return e


def remove_user(user_id):
    try:
        del users[user_id]
        return f'Пользователь {user_id} удален из групп'
    except Exception as e:
        return e


def show_users():
    return users
