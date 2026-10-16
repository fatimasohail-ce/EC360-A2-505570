import unittest

from auth_service import register_user


class TestRegistration(unittest.TestCase):

    def test_valid_registration(self):
        user = register_user("student@example.com", "StrongPass123")
        self.assertEqual(user["email"], "student@example.com")
        self.assertIn("password_hash", user)
        self.assertNotEqual(user["password_hash"], "StrongPass123")

    def test_invalid_email(self):
        with self.assertRaises(ValueError):
            register_user("invalid-email", "StrongPass123")

    def test_short_password(self):
        with self.assertRaises(ValueError):
            register_user("student@example.com", "short")

    def test_passwords_use_different_salts(self):
        user1 = register_user("student@example.com", "StrongPass123")
        user2 = register_user("student@example.com", "StrongPass123")
        self.assertNotEqual(
            user1["password_hash"],
            user2["password_hash"]
        )


if __name__ == "__main__":
    unittest.main()
