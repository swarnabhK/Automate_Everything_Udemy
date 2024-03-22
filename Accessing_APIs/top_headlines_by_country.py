import requests


# returns the top headlines for a country using the news API
def get_news(country,api_key="f5fadd7fda5c4a45ac4d1c793bdc0bfd"):
  url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={api_key}'
  r = requests.get(url)
  content = r.json()
  articles = content['articles']
  results = []
  for article in articles:
    results.append(f"TITLE\n{article['title']},'\nDESCRIPTION\n',{article['description']}")
    return results
  
print(get_news(country="us"))