import os
from cryptography.fernet import Fernet
import base64
import hashlib
import json

class SafeVault:
    def __init__(self, database_path, password):
        """
        Function Usage: __init__(database_path:str, password:str)
        
        Function Description:
            Initializes the SafeVault object with the given database path and password.
        
        Args:
            database_path (str): The path to the database file.
            password (str): The password used to generate the encryption key.
        """
        self.database_path = database_path
        self.key = self.generate_key_from_password(password)
        self.valid_key = self.check_key()
        self.create_database_file()

    def generate_key_from_password(self, password):
        """
        Function Usage: generate_key_from_password(password:str)
        
        Function Description:
            Generates an encryption key using the provided password.
        
        Args:
            password (str): The password used to generate the encryption key.
        
        Returns:
            bytes: The generated encryption key.
        """
        hashed_text = hashlib.sha256(password.encode()).digest()
        key = hashed_text[:32]
        return base64.urlsafe_b64encode(key)

    def check_key(self):
        """
        Function Usage: check_key()
        
        Function Description:
            Checks if the encryption key is valid by attempting to decrypt data.
        
        Returns:
            bool: True if the key is valid, False otherwise.
        """
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
        """
        Function Usage: create_database_file()
        
        Function Description:
            Creates the database file if it doesn't exist and encrypts an empty dictionary.
        """
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
        """
        Function Usage: _read_database()
        
        Function Description:
            Reads data from the encrypted database file.
        
        Returns:
            str: Decrypted data from the database.
        """
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
        """
        Function Usage: _write_database(data:str)
        
        Function Description:
            Writes data to the encrypted database file.
        
        Args:
            data (str): Data to be written to the database.
        """
        try:
            cipher = Fernet(self.key)
            encrypted_data = cipher.encrypt(data.encode())
            with open(self.database_path, 'wb') as file:
                file.write(encrypted_data)
        except Exception as e:
            print("Error writing to database file:", e)


    def add_data(self, key, value):
        """
        Function Usage: add_data(key:str, value:str)
        
        Function Description:
            Adds key-value pair to the encrypted database.
        
        Args:
            key (str): The key to add.
            value (str): The value corresponding to the key.
        """
        if self.valid_key:
            data = self._read_database()
            data_dict = {} if not data else json.loads(data)
            data_dict[key] = value
            self._write_database(json.dumps(data_dict))

    def update_data(self, key, value):
        """
        Function Usage: update_data(key:str, value:str)
        
        Function Description:
            Updates the value corresponding to the given key in the encrypted database.
        
        Args:
            key (str): The key to update.
            value (str): The new value corresponding to the key.
        
        Returns:
            bool: True if the update was successful, False otherwise.
        """
        if self.valid_key:
            data = self._read_database()
            data_dict = {} if not data else json.loads(data)
            if key in data_dict:
                data_dict[key] = value
                self._write_database(json.dumps(data_dict))
                return True
        return False

    def get_data(self, key):
        """
        Function Usage: get_data(key:str)
        
        Function Description:
            Retrieves data corresponding to the given key from the encrypted database.
        
        Args:
            key (str): The key to retrieve data for.
        
        Returns:
            str: The value corresponding to the key, or None if key not found.
        """
        if self.valid_key:
            data = self._read_database()
            if data:
                data_dict = json.loads(data)
                return data_dict.get(key)
        return None

    def delete_data(self, key):
        """
        Function Usage: delete_data(key:str)
        
        Function Description:
            Deletes data corresponding to the given key from the encrypted database.
        
        Args:
            key (str): The key to delete data for.
        
        Returns:
            bool: True if the data was successfully deleted, False otherwise.
        """
        if self.valid_key:
            data = self._read_database()
            if data:
                data_dict = json.loads(data)
                if key in data_dict:
                    del data_dict[key]
                    self._write_database(json.dumps(data_dict))
                    return True
        return False
