from .node import Node


class FundingRound(Node):
    """Represents a FundingRound on CrunchBase
    API Docs: https://developer.crunchbase.com/docs
    """

    KNOWN_PROPERTIES = [
       "funding_type",
       "money_raised_usd",
       "announced_on_year",
       "announced_on_day",
       "announced_on_month",
       "announced_on",
       "announced_on_trust_code",
       "canonical_currency_code",
       "money_raised",
       "money_raised_currency_code",
       "permalink",
       "name",
       "post_money_valuation_currency_code",
       "created_at",
       "updated_at",
    ]

    KNOWN_RELATIONSHIPS = [
       "investments",
       "funded_organization",
       "news",
    ]

    def _coerce_values(self):
        for attr in ['announced_on']:
            if getattr(self, attr, None):
                setattr(self, attr, self._parse_date(getattr(self, attr)))
