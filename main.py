from Mahsan import info as Mahsan

from Hossein import info as Hossein

from Hossein import Resistance as Resistance

from Methods import run

result = run(Hossein, Resistance)    # dict_keys(['ke', 'element', 'kg', 'u', 'WS', 'Lager'])

print(result['Lager'])
