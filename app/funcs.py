import json

async def write_json(data: str, path='debug/user_data.json'):
    with open(path, 'w+', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
        f.close()


async def read_json(path='debug/user_data.json'):
    with open(path, 'r', encoding='utf-8') as f:
        try:
            user_data = json.load(f)
            return user_data
        except Exception as e:
            return {}