from collections import defaultdict

conversations_store = defaultdict(list)

def add_message(session_id: str, role: str, message: str):
    conversations_store[session_id].append({
        "role": role,
        "message": message
    })

def get_history(session_id: str, limit: int = 5):
    return conversations_store[session_id][-limit:]

def clear_history(session_id: str):
    conversations_store[session_id] = []

    