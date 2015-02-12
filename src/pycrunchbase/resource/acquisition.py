from .node import Node


class Acquisition(Node):
    """Represents a Acquisition on CrunchBase
    API Docs: https://developer.crunchbase.com/docs
    """

    KNOWN_PROPERTIES = [
        "disposition_of_acquired",
        "acquisition_type",
        "acquisition_status",
        "payment_type",
        "announced_on_year",
        "announced_on_day",
        "announced_on_month",
        "announced_on",
        "announced_on_trust_code",
        "price",
        "price_currency_code",
        "permalink",
        "name",
        "created_at",
        "updated_at",
    ]

    KNOWN_RELATIONSHIPS = [
        "acquirer",
        "acquiree",
        "news",
    ]

    def _coerce_values(self):
        for attr in ['announced_on']:
            if getattr(self, attr, None):
                setattr(self, attr, self._parse_date(getattr(self, attr)))
