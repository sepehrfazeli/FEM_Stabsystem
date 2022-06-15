from Database import database

from Methods import run, save

# databases Hossein, Mahsan

result = run(database, 'Hossein')  # dict_keys(['ke', 'element', 'kg', 'u', 'WS', 'Lager'])

# print(result['kg'])
save(result)
