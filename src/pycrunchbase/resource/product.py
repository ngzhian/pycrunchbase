from .node import Node
from .utils import parse_date


class Product(Node):
    """Represents a Product on CrunchBase
    API Docs: https://developer.crunchbase.com/docs
    """

    KNOWN_PROPERTIES = [
        "lifecycle_stage",
        "short_description",
        "permalink",
        "homepage_url",
        "name",
        "description",
        "launched_on_year",
        "launched_on_day",
        "launched_on_month",
        "launched_on",
        "launched_on_trust_code",
        "created_at",
        "updated_at",
        "owner_name",
        "owner_path",
    ]

    KNOWN_RELATIONSHIPS = [
        "primary_image",
        "images",
        "websites",
        "news",
    ]

    def _coerce_values(self):
        for attr in ['launched_on']:
            if getattr(self, attr, None):
                setattr(self, attr, parse_date(getattr(self, attr)))
