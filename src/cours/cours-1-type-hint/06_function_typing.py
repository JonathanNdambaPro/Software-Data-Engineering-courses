def verify_password(submitted_password: str, stored_hash: str) -> bool:
    return submitted_password == stored_hash
