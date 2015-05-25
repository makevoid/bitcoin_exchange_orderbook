import datetime
import unittest
import orderbook


buyLedger  = []
sellLedger = []

order1 = { "id": 1, "user_id": 1,  "type": "sell", "amount": 10000, "price": 20000, "time": datetime.datetime.now() }
sellLedger.append(order1)
order2 = { "id": 1, "user_id": 1,  "type": "sell", "amount": 10000, "price": 21000, "time": datetime.datetime.now() }
sellLedger.append(order2)
order3 = { "id": 1, "user_id": 1,  "type": "sell", "amount": 10000, "price": 22000, "time": datetime.datetime.now() }
sellLedger.append(order3)


class matchLedgers(unittest.TestCase):
    def generateValues(self):
        order          = { "id": 1, "user_id": 1,  "type": "buy", "amount": 25000, "price": 21000, "time": datetime.datetime.now() }
        resolvedOrders = [
            order1, order2
        ]
        partialResolvedOrder = { "id": 1, "user_id": 1,  "type": "buy", "amount": 5000, "price": 20500, "time": datetime.datetime.now() }
        sellLedgerResult  = [order3]
        buyOrderNew = order.copy()
        buyOrderNew["amount"] = 5000
        buyLedger   = [buyOrderNew]

        knownValues = {
            'inputs':  [
                [order, sellLedger, buyLedger]
            ],
            'results': [
                [resolvedOrders, partialResolvedOrder, sellLedgerResult, buyLedger]
            ]
        }
        return knownValues

    def testRightInput(self):
        knownValues = self.generateValues()
        for index, input_ in enumerate(knownValues["inputs"]):
            resolvedOrders, partialResolvedOrder, sellLedger, buyLedger = orderbook.matchLedgerSell(input_[0], input_[1], input_[2])
            self.assertEquals(knownValues["results"][index][0], resolvedOrders)
            self.assertEquals(knownValues["results"][index][1], partialResolvedOrder)
            self.assertEquals(knownValues["results"][index][2], sellLedger)
            self.assertEquals(knownValues["results"][index][3], buyLedger)

if __name__ == "__main__":
    unittest.main()
