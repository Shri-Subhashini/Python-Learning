
def validate_login(username: str, password:str) -> dict:
    if not username:
        return {"success" : False, "error" : "Username is required"}
    if not password:
        return {"success": False, "error" : "Password is required"}
    if len(username) < 3:
        return {"success" : False, "error" : "Username too short"}
    if len(password) < 6:
        return {"success" : False, "error" : "Password too short"}
    return {"success" : True}