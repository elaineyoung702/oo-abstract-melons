"""Classes for melon orders."""

class AbstractMelonOrder:
    """An abstract base class that other Melon Orders inherit from."""
    shipped = False

    def __init__(self,species, qty):
        self.species = species
        self.qty = qty

    def get_total(self):
        """Calculate price, including tax."""
        base_price = 5
        total = (1 + self.tax) * self.qty * base_price
        return total


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    def __init__(self,species,qty):
        """Initialize melon order attributes."""

        super().__init__(species,qty)
        self.order_type = "domestic"
        self.tax = 0.08

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""
    def __init__(self, species, qty, country_code):
    
        super().__init__(species,qty)
        self.country_code = country_code
        self.order_type = "international"
        self.tax = 0.17

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True

    def get_country_code(self):
        """Return the country code."""

        return self.country_code



