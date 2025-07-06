# import requests
# from testrail.testrail_config import BASE_URL, USERNAME, API_KEY, TEST_RUN_ID

# def add_result(case_id, status_id, comment=""):
#     url = f"{BASE_URL}/index.php?/api/v2/add_result_for_case/{TEST_RUN_ID}/{case_id}"
#     response = requests.post(
#         url,
#         json={"status_id": status_id, "comment": comment},
#         auth=(USERNAME, API_KEY)
#     )

#     print(f"Using TEST_RUN_ID = {TEST_RUN_ID}")


#     try:
#         response.raise_for_status()
#         return response.json()
#     except requests.exceptions.RequestException as err:
#         print(f"[ERROR] {err}\n[RESPONSE] {response.text}")
#     return None



import requests
from testrail.testrail_config import BASE_URL, USERNAME, API_KEY

# Mapping of case IDs to their Test Run IDs
CASE_ID_TO_RUN_ID = {
    7: 6,  # project1 valid login
    9: 6,  # project1 invalid login
    8: 7,  # project2 checkout success
    10: 7  # project2 checkout failure
}

def add_result(case_id, status_id, comment=""):
    test_run_id = CASE_ID_TO_RUN_ID.get(case_id)
    if not test_run_id:
        print(f"[ERROR] No test run mapped for case ID {case_id}")
        return None

    url = f"{BASE_URL}/index.php?/api/v2/add_result_for_case/{test_run_id}/{case_id}"
    response = requests.post(
        url,
        json={"status_id": status_id, "comment": comment},
        auth=(USERNAME, API_KEY)
    )

    print(f"[INFO] Reporting result to run {test_run_id} for case {case_id}")
    try:
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as err:
        print(f"[ERROR] {err}\n[RESPONSE] {response.text}")
        return None
