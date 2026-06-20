from auth import AuthManager

def test_create_account():
    auth_manager = AuthManager()
    assert auth_manager.create_account("test@example.com", "Password123") == True
    assert auth_manager.create_account("test@example.com", "Password123") == False

def test_create_account_password_complexity():
    auth_manager = AuthManager()
    assert auth_manager.create_account("test@example.com", "password") == False
    assert auth_manager.create_account("test@example.com", "Password123") == True

def test_verify_email():
    auth_manager = AuthManager()
    auth_manager.create_account("test@example.com", "Password123")
    assert auth_manager.verify_email("test@example.com") == True
    assert auth_manager.verify_email("nonexistent@example.com") == False

def test_login():
    auth_manager = AuthManager()
    auth_manager.create_account("test@example.com", "Password123")
    auth_manager.verify_email("test@example.com")
    assert auth_manager.login("test@example.com", "Password123") == True
    assert auth_manager.login("test@example.com", "wrongpassword") == False
    assert auth_manager.login("nonexistent@example.com", "Password123") == False
