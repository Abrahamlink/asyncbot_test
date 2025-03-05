import json
from urllib.parse import uses_query


async def write_json(data: dict, path='debug/user_data.json'):
    full_data = await read_json()
    full_data[str(data['id'])] = {'name': data['name'], 'number': data['number']}
    with open(path, 'w+', encoding='utf-8') as f:
        json.dump(full_data, f, ensure_ascii=False, indent=4)
        f.close()


async def read_json(user_id: int = -1, path='debug/user_data.json'):
    with open(path, 'r', encoding='utf-8') as f:
        try:
            user_data = json.load(f)
            if user_id == -1:
                return user_data
            return user_data[f'{user_id}']
        except Exception as e:
            return {}


# async def prettify(data: dict):
#     new_data = {'id': data['id'],
#                 'user_data:': {'name': data['name'], 'number': data['number']}}
#     return new_data

async def numerate(path='debug/numerater.json'):
    with open(path, 'r+', encoding='utf-8') as f:
        try:
            number = json.load(f)
            number['number'] = int(number['number']) + 1
        except Exception as e:
            number = {'number': 1}

        json.dump(number, f, ensure_ascii=False, indent=4)
        f.close()
        return number['number'] - 1

