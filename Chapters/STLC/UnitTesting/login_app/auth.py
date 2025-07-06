User_Db = {
    "admin": "admin123",
    "user1": "welcome"
}

def login(username: str, password: str) -> str:
    if not username or not password:
        return "Username or password cannot be empty"
    
    if username not in User_Db:
        return "User not found"
    
    if User_Db[username] != password:
        return "Incorrect password"
    
    return "Login successful"
