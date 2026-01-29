def verify_password_2(submitted_password: str, stored_hash: str = "123456") -> bool:
    return submitted_password == stored_hash
