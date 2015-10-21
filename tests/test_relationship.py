from unittest import TestCase

from pycrunchbase import Relationship

PAST_TEAM_RELATIONSHIP = {
    "cardinality": "OneToMany",
    "paging": {
        "total_items": 3,
        "first_page_url": "https://api.crunchbase.com/v/3/"
        "organization/example/past_team",
        "sort_order": "created_at DESC"
    },
    "items": [
        {
            "type": "Job",
            "uuid": "558bac9a0e484b1478762b6e32b66aaa",
            "properties": {
                "title": "Co-Founder / President",
                "started_on": "2008-07-01",
                "started_on_trust_code": 6,
                "ended_on": None,
                "ended_on_trust_code": None,
                "created_at": 1401278974,
                "updated_at": 1437762874
                },
            "relationships": {
                "person": {
                    "type": "Person",
                    "uuid": "e37bfcba7c041eb29abf404725cf9fc9",
                    "properties": {
                        "permalink": "tom-preston-werner",
                        "api_path": "people/tom-preston-werner",
                        "web_path": "person/tom-preston-werner",
                        "first_name": "Tom",
                        "last_name": "Preston-Werner",
                        "also_known_as": None,
                        "bio": "Tom Preston-Werner is a software developer and entrepreneur who co-founded GitHub in 2008, along with Chris Wanstrath and PJ Hyett, to simplify sharing code and make it easy to collaborate on building software. Today, GitHub is the largest code host in the world, with a community of four million people building software together.\r\n\r\nBefore founding GitHub, Tom worked as a Ruby developer for Powerset, a Wikipedia search engine that was acquired by Microsoft. Additionally, Tom invented Gravatar, a service for providing unique avatars that follow you from site to site, which he sold to Automattic in 2007.\r\n\r\nTom grew up in Iowa and came to the west coast to study physics at Harvey Mudd College; he left after two years when he realized that he enjoyed programming far more than the math that was the core of his physics studies. He currently lives in San Francisco with his wife and son.",
                        "role_investor": True,
                        "born_on": None,
                        "born_on_trust_code": None,
                        "died_on": None,
                        "died_on_trust_code": 0,
                        "created_at": 1208251918,
                        "updated_at": 1443777328
                        }
                    }
                }
            }
        ]
}

HEADQUARTERS_RELATIONSHIP = {
    "cardinality": "OneToOne",
    "item": {
        "type": "Address",
        "uuid": "31adbab5e90fc45a47ae873e0656fadd",
        "properties": {
            "name": "Headquarters",
            "street_1": "1601 Willow Road",
            "street_2": None,
            "postal_code": "94025",
            "city": "Menlo Park",
            "city_web_path": "location/menlo-park/"
            "1f8abfef5379b26b702005a09908492f",
            "region": "California",
            "region_web_path": "location/california/"
            "eb879a83c91a121e0bb8829782dbcf04",
            "country": "United States",
            "country_web_path": "location/united-states/"
            "f110fca2105599f6996d011c198b3928",
            "latitude": 37.41605,
            "longitude": -122.151801,
            "created_at": 1205362453,
            "updated_at": 1398138077
        }
    }
}

T_R = {
    "cardinality": "OneToMany",
    "paging": {
        "total_items": 4,
        "first_page_url": "https://api.crunchbase.com/v/3/funding-rounds/49182d090879aebb464ac8ed65ccb936/investments",
        "sort_order": "created_at DESC"
    },
    "items": [
        {
            "type": "Investment",
            "uuid": "c04e0510e80ced0708d4a3490c60cd22",
            "properties": {
                "money_invested": None,
                "money_invested_currency_code": None,
                "money_invested_usd": None,
                "created_at": 1438215743,
                "updated_at": 1438273006
            },
            "relationships": {
                "investors": [
                    {
                        "type": "Organization",
                        "uuid": "a2281da98a3eda3d56b2b8e0725b1b51",
                        "properties": {
                            "permalink": "institutional-venture-partners",
                            "api_path": "organizations/institutional-venture-partners",
                            "name": "Investor"
                        }
                    }]
            }
        }]
}


class RelationshipTestCase(TestCase):
    def test_one_to_many_relationship(self):
        past_team = Relationship('past_team', PAST_TEAM_RELATIONSHIP)
        job = past_team.get(0)
        self.assertEqual(job.title, 'Co-Founder / President')
        self.assertEqual(job.person.first_name, 'Tom')
        self.assertEqual('past_team', past_team.name)

    def test_one_to_one_relationship(self):
        hq = Relationship('headquarters', HEADQUARTERS_RELATIONSHIP)
        self.assertEqual(hq.name, "Headquarters")

    def test_nested_relationships(self):
        r = Relationship('investments', T_R)
        self.assertEqual(r[0].investors[0].name, 'Investor')
