import hashlib
import os
import re


def hash_password(password):
    """Hash a password with a random salt using PBKDF2."""
    salt = os.urandom(16)
    password_hash = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode("utf-8"),
        salt,
        100000
    )
    return salt.hex() + ":" + password_hash.hex()


def register_user(email, password):
    """Validate registration details and return a password hash."""
    if not re.match(r"^[^@\s]+@[^@\s]+\.[^@\s]+$", email):
        raise ValueError("Invalid email address")

    if len(password) < 8:
        raise ValueError("Password must be at least 8 characters long")

    return {
        "email": email,
        "password_hash": hash_password(password)
    }
