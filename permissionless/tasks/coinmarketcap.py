# Filename: coinmarketcap.py
import luigi
import json
import datetime
import coinmarketcap

class ImportCryptoCurrencies(luigi.Task):
    """
    ImportCryptoCurrencies - Grab the coins from coinmarketcap and write to s3
    coins consist of market cap, price, volume, and other metrics
    This works for a single coin or all coins
    """

    task_namespace = 'permissionless.tasks'
#    coin = luigi.Parameter() or ""
#    limit = luigi.IntParameter or 0

    def requires(self):
        return []

    def run(self):
        market = coinmarketcap.Market()
        coins = market.ticker("", limit=0)
        with self.output().open("w") as target:
            json.dump(coins, target)

    def output(self):
        return luigi.LocalTarget("coinmarketcap_{}.txt".format(datetime.datetime.utcnow()))

if __name__ == '__main__':
    luigi.run()
