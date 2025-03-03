import json

async def write_json(data: str, path='debug/user_data.json'):
    with open(path, 'w+', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
        f.close()
