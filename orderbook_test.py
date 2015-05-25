import datetime
import unittest
import orderbook


buyLedger  = []
sellLedger = []

order1 = { "id": 1, "user_id": 1,  "type": "sell", "amount": 10000, "price": 20000}
sellLedger.append(order1)
order2 = { "id": 1, "user_id": 1,  "type": "sell", "amount": 10000, "price": 21000}
sellLedger.append(order2)
order3 = { "id": 1, "user_id": 1,  "type": "sell", "amount": 10000, "price": 22000}
sellLedger.append(order3)


class matchLedgers(unittest.TestCase):
    def generateValues(self):
        order          = { "id": 1, "user_id": 1,  "type": "buy", "amount": 25000, "price": 21000}
        resolvedOrders = [
            order1, order2
        ]
        partialResolvedOrder = { "id": 1, "user_id": 1,  "type": "buy", "amount": 20000, "price": 20500}
        sellLedgerResult  = [order3]
        buyOrderNew = order.copy()
        buyOrderNew["amount"] = 5000
        buyLedgerResult   = [buyOrderNew]

        knownValues = {
            'inputs':  [
                [order, sellLedger, buyLedger]
            ],
            'results': [
                [resolvedOrders, partialResolvedOrder, sellLedgerResult, buyLedgerResult]
            ]
        }
        return knownValues

    def assertEqualsPretty(expectedResult, result):
        return self.assertEquals( expectedResult, result, msg='\n{0}\n-----\n{1}'.format(expectedResult, result) )

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
