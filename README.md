# UrlShortener
A service to shorten urls

## TL;DR
The service spins up a docker containers running django GraphQL Api backed by Postgres DB engine. The cli app makes calls the api and returns response.

## Installation

### Step 1: Install Docker and Docker Compose

### Step 2: Build and Run Docker Containers
```
sudo make run
```
### Step 3: Run DB Migrations
```
sudo make migrate
```
### Step 4: Create Virtual Env to Run Cli App
```
python -m venv env
source ./env/bin/activate
pip install -r requirements.txt
```

## Running Cli Tool

### Activate Environment
```
source ./env/bin/activate
```

### Fetch All Stats
```
(env)$ python cli.py get-all-stats
```
It should return response as follows
```
Response Code: 200
All Stats
: {"data":{"urls":[{"url":"https://www.skillshare.com/browse/creative-writing","hashedUrl":"1e3a1b6a","createdAt":"2020-08-22T13:59:39.640917+00:00","urlClickedAt":["2020-08-22T14:00:26.982615+00:00","2020-08-22T14:00:32.479990+00:00"],"numUrlClicks":2,"urlClickClients":["127.0.0.1","127.0.0.1"]},{"url":"https://us.romwe.com/Butterfly-Print-Carrot-Jeans-Without-Belt-p-678060-cat-813.html","hashedUrl":"52830e8c","createdAt":"2020-08-22T14:03:18.380707+00:00","urlClickedAt":["2020-08-22T14:03:39.895598+00:00","2020-08-22T14:06:31.388944+00:00","2020-08-22T14:06:33.847274+00:00"],"numUrlClicks":3,"urlClickClients":["127.0.0.1","127.0.0.1","127.0.0.1"]}]}}
```

### Create Shortened Url
```
(env)$ python cli.py shorten "https://www.skillshare.com/browse/business-analytics"
``` 

It should return response as follows:
```
{'url': 'https://www.skillshare.com/browse/business-analytics'}
Response Code: 200

Link has been shortened! You can open it here:
http://127.0.0.1:8000/08098d43


```