# testrail/testrail_api.py
import requests
import time
from testrail import testrail_config as config

def add_result(case_id, status_id, comment=""):
    url = f"{config.BASE_URL}/index.php?/api/v2/add_result_for_case/{config.TEST_RUN_ID}/{case_id}"
    headers = {
        "Content-Type": "application/json"
    }
    auth = (config.USERNAME, config.API_KEY)

    data = {
        "status_id": status_id,
        "comment": comment
    }
    for attempt in range(3):
        try:
            response = requests.post(url, auth=auth, headers=headers, json=data)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"[TestRail ERROR] Could not send result: {e}")
            time.sleep(2)
    return None
