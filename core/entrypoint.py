import re
import json
import gc
from typing import Union
from .base_client import BaseClient
from logger.logger import get_logger
from urllib.parse import quote_plus
from utils.utils import save_to_json, get_state_id, normalize_text, get_random_timezone
from utils.config import STATIC_FILE_PATH, STATES, OUTPUT_FILE_PATH, PROVIDER_HEADERS, SEARCH_RADIUS 
from pathlib import Path


client = BaseClient(base_url="https://connect.werally.com")
logger = get_logger("BaseClient")

REQ_YEARS = ["2026"]

def process_json_file(file_path):
    """
    Process a single JSON file.
    Args:
        file_path (str): Path to the JSON file to process
    """
    try:
        with open(file_path, 'r') as f:
            content = json.load(f)
            
        # Extract needed data and clear the full content
        networks = content['networks']
        state = content['addresses'][0]['state'].strip().upper()
        zip = content['addresses'][0]['zip'].strip().upper()
        search_term = content['provider']['npi']
        
        # Clear large objects we don't need anymore
        content = None
        gc.collect()
    except (IOError, json.JSONDecodeError) as e:
        logger.error(f"Error reading or parsing {file_path}: {e}")
        raise
    except KeyError as e:
        logger.error(f"Missing required field in {file_path}: {e}")
        raise
    
    coords = get_coordinates(zip)
    
    available_plans = search_plan_for_state(state)
   
    provider_found = False
    search_radius = 20
    plan_code = ""
   
    search_result = {}
    for network in networks:
        network_name = (lambda m: m.group(1) if m else "")(re.search(r'\s*\-\s*(.*)', network['name'], re.IGNORECASE))
        normalized_network_name = normalize_text(network_name)
        for plan in available_plans:
            # plan  = json.loads(plan)
            year = plan['category']
            if year not in REQ_YEARS:
                continue
            
            plan_name = plan['planName']
            normalized_plan_name = normalize_text(plan_name)
            print(f"normalized network name: {normalized_network_name} | Normalized plan name: {normalized_plan_name}") 
            if normalized_network_name.strip() != normalized_plan_name.strip():
                continue
            
            plan_code = plan['planCode']
            search_result = search_provider(zip, state, coords, plan_code, search_term, search_radius)
            if search_result:
                provider_found = True
                break

        if provider_found:
            break
    
    if not provider_found:
        logger.critical(f"No Provider found for zip: {zip} | Search Term: {search_term}")
        return

    get_provider_info(search_result, search_radius, plan_code)


def get_provider_info(provider_info:dict, search_radius:str|int, plan_code:str|int) -> None:
    """
    Method to get provider full info and save the raw json to file.
    Args:
        provider_info (dict): Provider information dictionary
        search_radius (str|int): Search radius in miles
        plan_code (str|int): Plan code identifier
    """
    provider_id = provider_info['id']
    coverage_type = provider_info['providerCoverageType']
    lon = provider_info['locations'][0]['address']['geo'][0]
    lat = provider_info['locations'][0]['address']['geo'][1]
    zip = provider_info['locations'][0]['address']['zipCode']
    locationId = provider_info['locations'][0]['locationId']    
    random_timezone = quote_plus(get_random_timezone())
 
    provider_type = provider_info['type']

    url = f"/rest/provider/v3/partners/uhc.exchange/providerTypes/{provider_type}/providers/{provider_id}?coverageType={coverage_type}&limitLocations=50&lon={lon}&lat={lat}&searchRadius={search_radius}&planYear=2026&accountPolicyNumber=&planVariation=&planTierLevel=standard&timeZone={random_timezone}&userNetworkId={plan_code}&planCode={plan_code}"
    
    file_name = str(Path(OUTPUT_FILE_PATH) / f"{provider_id}.json") 
    
    PROVIDER_HEADERS['context-config-plancode'] = str(plan_code)
    PROVIDER_HEADERS['referer'] = f"https://connect.werally.com/provider/{provider_id}?locationId={locationId}&zipCode={zip}&lat={lat}&long={lon}&distanceMiles={SEARCH_RADIUS}&comparing=1&coverageType={coverage_type}&propFlow=true" 
   
    payload = [f"{plan_code}"]
    
    try:
        response = client._request("POST", url, headers=PROVIDER_HEADERS, json=payload)
        data = json.loads(response['body'])
        save_to_json(file_name, data)
    except Exception as e:
        logger.debug(f"An error occurred during the request: {e}")

   
def search_provider(zip:str|int, state:str ,coords:dict ,plan_code:str|int, search_term:str, search_radius:str|int) -> dict:
    """
    Search for a provider using the given parameters.
    Args:
        zip (str|int): Zip code to search in
        state (str): State abbreviation
        coords (dict): Coordinates dictionary with 'lat' and 'lon'
        plan_code (str|int): Plan code identifier
        search_term (str): Search term, typically NPI
        search_radius (str|int): Search radius in miles
    Returns:
        dict: The search result dictionary if found, else empty dict   
    """
    logger.info(f"Processing To Search For Zip: {zip} | Plan Code: {plan_code} | Search Term: {search_term}")
    joined_coords = ",".join(str(x) for x in coords)
    random_timezone = quote_plus(get_random_timezone())
    params = {
        "accountPolicyNumber": "",
        "autoIncreaseDistance": "true",
        "center": joined_coords,
        "configuration": "uhc.exchange",
        "distanceMiles": search_radius,
        "from": 0,
        "includeAggregations": "true",
        "includeBehavioralCarePaths": "true",
        "includeBillingCodeCarePaths": "true",
        "includeOutOfNetwork":"false",
        "isEapFilterSuppressed":"false",
        "isMedicalVirtualCareSuppressed": "false",
        "isTelementalHealthSuppressed": "false",
        "nptV21Enabled": "true",
        "planTierLevel": "standard",
        "planVariation": "",
        "planYear": "2026",
        "products.medical": f"{plan_code}:{plan_code}",
        "products.medical": f"{plan_code}:{plan_code}",
        "searchType": "areaOfExpertise,facilityServiceCode,person,place,specialtyCategory,hcbsService,hcbsWaiver,specialty,medicalGroup,commonCondition,providerWithoutLocationGroup,carePath,billingCode,dynamicNationalProvider",
        "selectedLang": "en",
        "sort": "score",
        "splitAnpReferralTypes": "true",
        "state": state,
        "suppressCostEfficiencySort": "false",
        "suppressType": "virtualVisit",
        "term": search_term,
        "timeZone": random_timezone,
        "zipCode": zip,
        "userNetworkId":plan_code,
    }
    url = "/rest/provider/v4/search/filtered"
    referer_url = f'https://connect.werally.com/searchResults/{zip}/page-1?term={search_term}&searchType=all&lat={coords[1]}&long={coords[0]}&propFlow=true'
    PROVIDER_HEADERS['referer'] = referer_url
    PROVIDER_HEADERS['context-config-plancode'] = str(plan_code)
    
    try:
        response = client._request("GET", url, headers=PROVIDER_HEADERS, params=params)
        data = json.loads(response['body'])
        return next((item for item in data.get("results", []) if item.get("nationalProviderId") == search_term), {})
    except Exception as e:
        logger.debug(f"An error occurred during the request: {e}")

    return {}


def search_plan_for_state(state:str) -> dict:
    """
    Search Plans for Given State and Returns the value
    Args:
        state (str): State abbreviation
    Returns:
        dict: The available plans for the state
    """

    logger.info(f"Searching Available Plans For State: {state}")

    full_state_name = STATES[state]
    state_id = get_state_id(full_state_name)
    url = f"/rest/guide/v1/guidedSearch/plan/{state_id}?language=en"
    try:
        response = client._request("GET", url)
        return json.loads(response['body'])['children']
    except Exception as e:
        logger.debug(f"An error occurred during the request: {e}")
    
    return {}

def get_coordinates(zip:Union[str, int]) -> dict:
    """
    This will return the coordinates details against the provided valid zip.
    This uses site's api
    """
    logger.info(f"Getting Coordinate For Zip: {zip}") 
    url= f"/rest/geolocation/v1/location/{zip}"
    
    try:
        response= client._request("GET", url)
        return json.loads(response['body'])['coords'] if response['body'] else {}
    except Exception as e:
        logger.debug(f"An error occurred during the request: {e}")

    return {}


def get_available_state_data() -> None:
    """
    Method to get available state data. Since this is a common file, we can import and save the content at the start of execution. 
    """
    
    url = '/rest/guide/v1/guidedSearch/plan/4?language=en'
    file_path =str(Path(STATIC_FILE_PATH) / "state_data.json")
    
    try:
        response = client._request("GET", url)
        data = json.loads(response['body'])
        save_to_json(file_path, data)

    except Exception as e:
        logger.debug(f"An error occurred during the request: {e}")



