import datetime

# order
# order_fields = ["id", "user_id",  :type, :amount, :price, "time", "resolved"]

# initial state
buyLedger = []
sellLedger = []


# main

def main():
    order = { "id": 1, "user_id": 1,  "type": "sell", "amount": 10000, "price": 20000, "time": datetime.datetime.now() }
    matchLedgers(order)


# TODO: gestione errore esterna a questa funzione
def matchLedgers(order):
    if order["type"] == "buy":
        resolvedOrders, partialResolvedOrder, sellLedger, buyLedger = matchLedgerSell(order, sellLedger, buyLedger)
    else:
        matchLedgerBuy(order)

def matchLedgerSell(order, sellLedger, buyLedger): # order is buy
    lastMatchingOrderDepthPrice  = lastMatchingOrderDepthPriceSell(order["price"])
    lastMatchingOrderDepthAmount, amountMatched = lastMatchingOrderDepthAmountSell(order["amount"], sellLedger)


    if lastMatchingOrderDepthPrice < lastMatchingOrderDepthAmount:
        priceSell = findPriceSell(lastMatchingOrderDepthPrice)

        newOrder = order
        newOrder["amount"] = order["amount"] - amountMatched

        resolvedOrders = sellLedger[0:lastMatchingOrderDepthAmount]
        partialResolvedOrder = order
        partialResolvedOrder["price"]  = priceSell
        partialResolvedOrder["amount"] = amountMatched
        sellLedger = sellLedger[lastMatchingOrderDepthAmount:]
        buyLedger  = buyLedger.insert(0, newOrder)

        return resolvedOrders, partialResolvedOrder, sellLedger, buyLedger

    elif lastMatchingOrderDepthPrice == lastMatchingOrderDepthAmount:
        # return resolvedOrders, partialResolvedOrder, sellLedger, buyLedger
        return False, False, sellLedger, buyLedger

    else: # lastMatchingOrderDepthPrice > lastMatchingOrderDepthAmount:
        # return resolvedOrders, partialResolvedOrder, sellLedger, buyLedger
        return False, False, sellLedger, buyLedger
        # ... non ce ne po frega de meno

    # if order["amount"]


def findPriceSell(depth):
    amountTotal = 0
    priceTotal  = 0

    for index, order in enumerate(sellLedger):
        if index <= depth:
            priceTotal  += order["price"] * order["amount"]
            amountTotal += order["amount"]

    return priceTotal / amountTotal

def findPriceBuy(depth):
    # TODO ....
    return true

def lastMatchingOrderDepthPriceSell(price):
    for index, order in enumerate(sellLedger):
        if order["price"] > price:
            return index

def lastMatchingOrderDepthPriceBuy(price):
    for index, order in enumerate(sellLedger):
        if order["price"] < price:
            return index


# TODO: refactor these two, pass the ledger as a parameter then they're identical
def lastMatchingOrderDepthAmountSell(amount, sellLedger):
    amountMatched = 0
    for index, order in enumerate(sellLedger):
        amountMatched += order["amount"]
        if amountMatched > amount:
            return index, (amountMatched - order["amount"])

def lastMatchingOrderDepthAmountBuy(amount):
    amountMatched = 0
    for index, order in enumerate(buyLedger):
        amountMatched += order["amount"]
        if amountMatched > amount:
            return index, (amountMatched - order["amount"])
