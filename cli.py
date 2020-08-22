import sys
import json

import click
import requests
from requests.exceptions import HTTPError



SHORTEN_URL_SERVICE_API = "http://127.0.0.1:8000/graphql/"
SHORTENED_URL = "http://127.0.0.1:8000/{}"

ALL_STATS_QUERY = """
query {
  urls {
    url
    hashedUrl
    createdAt
    urlClickedAt
    numUrlClicks
    urlClickClients
  }
}
"""

SHORTEN_QUERY = """
mutation {{
  createUrl(url:"{0}") {{
    url {{
      url
      hashedUrl
    }}
  }}
}}
"""

@click.group()
@click.version_option("1.0.0")
def main():
    """Cli Tool for Shortening URL"""
    pass

def get_shortened_url(url):
    return url


def get_query_response(query):
    try:
        r = requests.post(SHORTEN_URL_SERVICE_API, json={'query': query})
        response_code = r.status_code
        print("Response Code:", response_code)
        response_text = json.loads(r.text)
        return response_text

    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')

@main.command()
@click.argument('url', required=True)
def shorten(**kwargs):
    """Shorten URL"""
    click.echo(kwargs)
    url = kwargs.get("url")
    shorten_url_query = SHORTEN_QUERY.format(url)
    response_text = get_query_response(shorten_url_query)
    click.echo(f"\nLink has been shortened! You can open it here:")
    hashed_code = response_text['data']['createUrl']['url']['hashedUrl']
    hashed_url = SHORTENED_URL.format(hashed_code) 
    click.echo(f"{hashed_url}")

@main.command()
def get_all_stats(**kwargs):
    """Get all stats"""
    url = kwargs.get("url")
    response_text = get_query_response(all_stats_query)
    print(response_text)
    click.echo(f"All Stats\n: {response_text}")

@main.command()
@click.argument('name', required=True)
def stats(**kwargs):
    """Get stats for URL"""
    click.echo(url)

if __name__ == '__main__':
    args = sys.argv
    if "--help" in args or len(args) == 1:
        print("URL Shortener")
    main()