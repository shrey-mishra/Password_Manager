Secure Password Manager

This is a secure password manager implemented in Python, utilizing the cryptography library for encryption. It allows users to add new passwords and view existing ones while keeping them encrypted.

Requirements

- Python 3.x
- cryptography library (install using `pip install cryptography`)

Features

- **Strong Encryption**: Passwords are encrypted using the Fernet symmetric encryption algorithm provided by the cryptography library.
- **Master Password**: The user needs to provide a master password to access the passwords. This master password is used along with the encryption key to enhance security.
- **Add and View Passwords**: Users can add new account credentials and view existing ones securely.

Encryption

Passwords are encrypted using Fernet symmetric encryption. The encryption key is derived from a combination of a key file (`key.key`) and the user's master password.

File Structure

- `password_manager.py`: The main Python script containing the password manager implementation.
- `passwords.txt`: The file where encrypted passwords are stored.
- `key.key`: The file containing the encryption key.

Usage

1. Clone the repository to your local machine.
2. Make sure you have Python and the cryptography library installed.
3. Run the `password_manager.py` script.
4. Enter the master password when prompted.
5. Choose whether to add a new password or view existing ones.

Contribution

Feel free to contribute to this project by forking the repository and submitting a pull request with your changes.

License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
