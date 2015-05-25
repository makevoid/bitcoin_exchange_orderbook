import datetime
import unittest
import orderbook

class matchLedgers(unittest.TestCase):
    def generateValues(self):
        order = { "id": 1, "user_id": 1,  "type": "buy", "amount": 10000, "price": 20000, "time": datetime.datetime.now() }
        knowValues = {
            'inputs':  [order]
            'results': [resolvedOrders, partialResolvedOrder, sellLedger, buyLedger]
        }
