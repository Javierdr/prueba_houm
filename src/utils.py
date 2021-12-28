import requests
import re

def get_id_by_url(url):
  regex = r'pokemon/([0-9]+)/'
  match = re.search(regex, url)
  return int(match.group(1))

def make_request(url):
  try:
    response = requests.get(url)
  except requests.exceptions.HTTPError as e:
    return "Error: " + str(e)
  return response