#!/usr/bin/env python3
# Copyright (c) 2022-2024 José Manuel Barroso Galindo <theypsilon@gmail.com>

db = {
    "db_id": 'update_all_mister',
    "files": {
        'Scripts/.config/update_all/update_all_latest.zip': {
            'size': os.path.getsize('update_all_latest.zip'),
            'hash': hash_file('update_all_latest.zip'),
            'url': f'https://raw.githubusercontent.com/theypsilon/Update_All_MiSTer/{commit_id}/update_all_latest.zip',
            'tags': []
        }
    },
    "folders": {'Scripts': {}, 'Scripts/.config': {}, 'Scripts/.config/update_all': {}},
    "timestamp":  int(time.time())
}

with open('update_all_db.json', 'w') as json_file:
    json.dump(db, json_file, indent=4)

subprocess.run(['git', 'add', 'update_all_db.json'], check=True)
subprocess.run(['git', 'commit', '-m', '-'], check=True)
subprocess.run(['git', 'push', 'origin', 'master'], check=True)
subprocess.run(['git', 'push', '--force', 'origin', 'db'], check=True)
