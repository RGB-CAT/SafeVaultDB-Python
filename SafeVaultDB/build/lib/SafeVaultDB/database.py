import os
from cryptography.fernet import Fernet
import base64
import hashlib
import json

class SafeVault:
    def __init__(self, database_path, password):
        self.database_path = database_path
        self.key = self.generate_key_from_password(password)
        self.valid_key = self.check_key()
        self.create_database_file()

    def generate_key_from_password(self, password):
        hashed_text = hashlib.sha256(password.encode()).digest()
        key = hashed_text[:32]
        return base64.urlsafe_b64encode(key)

    def check_key(self):
        if not os.path.exists(self.database_path):
                    # Create the database file if it doesn't exist
                    self.create_database_file()

        try:
            with open(self.database_path, 'rb') as file:
                encrypted_data = file.read()
            cipher = Fernet(self.key)
            decrypted_data = cipher.decrypt(encrypted_data)
            return True
        except Exception as e:
            return False

    def create_database_file(self):
        if not os.path.exists(self.database_path):
            try:
                # Encrypt a placeholder string
                cipher = Fernet(self.key)
                encrypted_data = cipher.encrypt(b"{}")
                # Write the encrypted data to the database file
                with open(self.database_path, 'wb') as file:
                    file.write(encrypted_data)
            except Exception as e:
                print("An error occurred while creating the database file:", e)

    def _read_database(self):
        if not os.path.exists(self.database_path):
            # Create the database file if it doesn't exist
            self.create_database_file()
        
        if self.valid_key:
            try:
                with open(self.database_path, 'rb') as file:
                    encrypted_data = file.read()
                cipher = Fernet(self.key)
                decrypted_data = cipher.decrypt(encrypted_data)
                return decrypted_data.decode()
            except Exception as e:
                print("Error reading database file:", e)
                return ''

    def _write_database(self, data):
        try:
            cipher = Fernet(self.key)
            encrypted_data = cipher.encrypt(data.encode())
            with open(self.database_path, 'wb') as file:
                file.write(encrypted_data)
        except Exception as e:
            print("Error writing to database file:", e)


    def add_data(self, key, value):
        if self.valid_key:
            data = self._read_database()
            data_dict = {} if not data else json.loads(data)
            data_dict[key] = value
            self._write_database(json.dumps(data_dict))

    def update_data(self, key, value):
        if self.valid_key:
            data = self._read_database()
            data_dict = {} if not data else json.loads(data)
            if key in data_dict:
                data_dict[key] = value
                self._write_database(json.dumps(data_dict))
                return True
        return False

    def get_data(self, key):
        if self.valid_key:
            data = self._read_database()
            if data:
                data_dict = json.loads(data)
                return data_dict.get(key)
        return None

    def delete_data(self, key):
        if self.valid_key:
            data = self._read_database()
            if data:
                data_dict = json.loads(data)
                if key in data_dict:
                    del data_dict[key]
                    self._write_database(json.dumps(data_dict))
                    return True
        return False