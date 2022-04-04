"""Constants for TaiPower Bimonthly Energy Cost Integration."""

CONFIG_FLOW_VERSION = 1

DOMAIN = "taipower_bimonthly_cost"
PLATFORMS = ["sensor"]

ATTR_BIMONTHLY_ENERGY = "bimonthly energy source"
ATTR_KWH_COST = "price per kwh"
ATTR_START_DAY = "start day"
ATTR_USED_DAYS = "used days"
UNIT_KWH_COST = "TWD/kWh"
UNIT_TWD = "TWD"
CONF_BIMONTHLY_ENERGY = "bimonthly_energy"
CONF_METER_START_DAY = "meter_start_day"
CONF_PRICE_TYPE = "price_type"

OPT_PRICE_TYPE = {
    "non_time_not_business": "Non Time and not business",
    "by_time_two_stages": "By Time with two stages",
    "by_time_three_stages": "By Time with three stages",
    "ladder_business": "Ladder and business",
    "ladder_not_business": "Ladder and not business"
}

