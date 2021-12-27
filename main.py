from utils import make_request, get_id_by_url
from constants import BASE_URL, TOTAL_POKEMONS, FIRST_GENERATION_MAX_ID

def pokemons_with_at_and_two_a():
  pokemons = make_request(f'{BASE_URL}/pokemon?limit={TOTAL_POKEMONS}').json()
  pokemons_names = map(lambda x: x['name'], pokemons['results'])
  return len([pokemon for pokemon in pokemons_names if pokemon.count('a') == 2 and 'at' in pokemon])


def raichu_procreate(pokemon_name):
  pokemon_species = make_request(f'{BASE_URL}/pokemon-species/{pokemon_name}')
  egg_groups_links = map(lambda x: x['url'], pokemon_species.json()['egg_groups'])
  procreative_species = set()
  for link in egg_groups_links:
    response = make_request(link).json()
    procreative_species.update(list(map(lambda x: x['name'], response['pokemon_species'])))
  return len(procreative_species)

def max_and_min_weight_by_type(type):
  pokemons = make_request(f'{BASE_URL}/type/{type}')
  max_weight, min_weight = 0, float('inf')
  for pokemon in pokemons.json()['pokemon']:
    if get_id_by_url(pokemon['pokemon']['url']) <= FIRST_GENERATION_MAX_ID:
      new_pokemon = make_request(pokemon['pokemon']['url']).json()
      max_weight = max(max_weight, new_pokemon['weight'])
      min_weight = min(min_weight, new_pokemon['weight'])    
  return ([max_weight, min_weight])

if __name__ == '__main__':
  print(pokemons_with_at_and_two_a())
  print(raichu_procreate('raichu'))
  print(max_and_min_weight_by_type('fighting'))




  


