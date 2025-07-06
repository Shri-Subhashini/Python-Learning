# testrail_api.py
import requests
from testrail.testrail_config import BASE_URL, USERNAME, API_KEY, TEST_RUN_ID


def add_result(case_id, status_id, comment=""):
    url = f"{BASE_URL}/index.php?/api/v2/add_result_for_case/{TEST_RUN_ID}/{case_id}"
    response = requests.post(
        url,
        json={"status_id": status_id, "comment": comment},
        auth=(USERNAME, API_KEY)
    )

    try:
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        print(f"[ERROR] HTTP error occurred: {http_err}")
        print(f"[ERROR] Response body: {response.text}")
    except requests.exceptions.RequestException as req_err:
        print(f"[ERROR] Request error occurred: {req_err}")
    except ValueError as json_err:
        print(f"[ERROR] JSON decode failed: {json_err}")
        print(f"[ERROR] Response text was: '{response.text}'")
    
    return None  # fallback
