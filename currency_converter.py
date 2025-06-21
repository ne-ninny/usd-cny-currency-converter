class usd_to_cny():
    def __init__(self, usd_currency):
        self.conversion_to_cny = usd_currency * 7.1796463
        print(f"${usd_currency} = ¥{self.conversion_to_cny}")

class cny_to_usd():
    def __init__(self, cny_currency):
        self.conversion_to_usd = cny_currency * 0.13928263
        print(f"¥{cny_currency} = ${self.conversion_to_usd}")