import fetcher

if __name__ == '__main__':
    fetcher.get_all_binance('BTCUSDT','1h',True)
    fetcher.get_all_bitmex('XBTUSD','1h',True)
