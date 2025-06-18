class FlightData:
    # This class is responsible for structuring the flight data.

    def __init__(self):
        self.ORIGIN_IATA_CODE = "MNL"
        self.DESTINATION_CITY = ""
        self.PRICE = 0
        self.FLIGHT_DATE = None
        self.CURRENCY = "USD"
        self.CURRENCY_SYMBOL = "$"
        self.DESTINATION = ""
        self.NONSTOP = "true"
        self.MAX_PRICE = 0
        self.RETURN_DATE = None


    def find_cheapest_flight(self, flight_offers):
        # Call flight search's flight offers then
        # x.data[0].price.grandTotal

        # Loop through each offer
        # Get the price, compare against the current price
        cheapest_price = 0
        if not flight_offers == []:
            flight_prices = [offer["price"]["grandTotal"] for offer in flight_offers]
            cheapest_price = min(flight_prices)
            self.PRICE = cheapest_price

        return cheapest_price






