# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model


class GoogleCloudRegion(Enum):
    US_CENTRAL_1 = "US_CENTRAL_1"
    US_EAST_1 = "US_EAST_1"
    ASIA_EAST_1 = "ASIA_EAST_1"
    EUROPE_WEST_1 = "EUROPE_WEST_1"
    US_WEST_1 = "US_WEST_1"
    ASIA_EAST_2 = "ASIA_EAST_2"
    ASIA_NORTHEAST_1 = "ASIA_NORTHEAST_1"
    ASIA_SOUTH_1 = "ASIA_SOUTH_1"
    ASIA_SOUTHEAST_1 = "ASIA_SOUTHEAST_1"
    AUSTRALIA_SOUTHEAST_1 = "AUSTRALIA_SOUTHEAST_1"
    EUROPE_NORTH_1 = "EUROPE_NORTH_1"
    EUROPE_WEST_2 = "EUROPE_WEST_2"
    EUROPE_WEST_4 = "EUROPE_WEST_4"
    NORTHAMERICA_NORTHEAST_1 = "NORTHAMERICA_NORTHEAST_1"
    SOUTHAMERICA_EAST_1 = "SOUTHAMERICA_EAST_1"
    US_EAST_4 = "US_EAST_4"
    US_WEST_2 = "US_WEST_2"