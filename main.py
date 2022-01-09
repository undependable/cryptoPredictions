import requests

url = "https://api.coinmarketcap.com/data-api/v3/map/all?listing_status=active,untracked&exchangeAux=is_active,status&cryptoAux=is_active,status&start=1&limit=10000"
resp = requests.get(url)

def coinID(resp):
    query = input("> ")
    res = resp.json()

    for data in res['data']['cryptoCurrencyMap']:
        if query.lower() == data['slug']:
            print("")
            print(
                f"Name: {data['name']}\nSymbol: {data['symbol']}\nRanking: {data['rank']}"
                )
            print("")

            id_ = data['id']

            def prediction(id_):
                url = f"https://api.coinmarketcap.com/data-api/v3/price-prediction/query/half-year?cryptoId={id_}"
                resp = requests.get(url)
                res = resp.json()

                print("Target year: 2022, showing price predictions from january to june.\n__________________________________________________________________")

                for data in res['data']['predictions']:
                    print("")
                    print(f"Month: {data['targetMonth']} | Votes: {data['voteCount']} | Median Price: {data['medianPrice']} | Average Price: {data['avgPrice']}")

            prediction(id_)
            return

    print("Couldn't find anything on,",query,", perhaps it is spelled wrong?")
coinID(resp)
