from typing import Dict

STATIC_FILE_PATH="output/static"
OUTPUT_FILE_PATH="output/providers"

SEARCH_RADIUS = 20

STATES = {
    "AL": "Alabama",
    "AK": "Alaska",
    "AZ": "Arizona",
    "AR": "Arkansas",
    "CA": "California",
    "CO": "Colorado",
    "CT": "Connecticut",
    "DE": "Delaware",
    "FL": "Florida",
    "GA": "Georgia",
    "HI": "Hawaii",
    "ID": "Idaho",
    "IL": "Illinois",
    "IN": "Indiana",
    "IA": "Iowa",
    "KS": "Kansas",
    "KY": "Kentucky",
    "LA": "Louisiana",
    "ME": "Maine",
    "MD": "Maryland",
    "MA": "Massachusetts",
    "MI": "Michigan",
    "MN": "Minnesota",
    "MS": "Mississippi",
    "MO": "Missouri",
    "MT": "Montana",
    "NE": "Nebraska",
    "NV": "Nevada",
    "NH": "New Hampshire",
    "NJ": "New Jersey",
    "NM": "New Mexico",
    "NY": "New York",
    "NC": "North Carolina",
    "ND": "North Dakota",
    "OH": "Ohio",
    "OK": "Oklahoma",
    "OR": "Oregon",
    "PA": "Pennsylvania",
    "RI": "Rhode Island",
    "SC": "South Carolina",
    "SD": "South Dakota",
    "TN": "Tennessee",
    "TX": "Texas",
    "UT": "Utah",
    "VT": "Vermont",
    "VA": "Virginia",
    "WA": "Washington",
    "WV": "West Virginia",
    "WI": "Wisconsin",
    "WY": "Wyoming"
}


US_TIMEZONES = [
    "America/New_York",       # Eastern Time (EST/EDT)
    "America/Chicago",        # Central Time (CST/CDT)
    "America/Denver",         # Mountain Time (MST/MDT)
    "America/Phoenix",        # Mountain Time (no DST, Arizona)
    "America/Los_Angeles",    # Pacific Time (PST/PDT)
    "America/Anchorage",      # Alaska Time (AKST/AKDT)
    "America/Juneau",         # Alaska Time
    "America/Adak",           # Hawaii-Aleutian Time (HAST/HADT)
    "Pacific/Honolulu",       # Hawaii Time (HST, no DST)
    "America/Puerto_Rico"     # Atlantic Time (AST/ADT, US territories)
]

PROVIDER_HEADERS: Dict[str, str] = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en',
    'context-config-consumersource': 'connect-web',
    'context-config-partnergroup': 'uhc',
    'context-config-partnerid': 'uhc.exchange',
    'current-connect-session-type': 'guest',
    'origin': 'https://connect.werally.com',
    'priority': 'u=1, i',
    'sec-ch-ua': '"Brave";v="141", "Not?A_Brand";v="8", "Chromium";v="141"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'sec-gpc': '1',
    # 'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36',
    'x-rally-locale': 'en-US',
}
