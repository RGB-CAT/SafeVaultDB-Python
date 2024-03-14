# Usage
```python
from SafeVaultDB import SafeVault

# Initialize SafeVault with database path and password
vault = SafeVault(database_path="path/to/database.db", password="your_password")
```

## Installation

You can install SafeVaultDB for python using pip:
```bash
pip install SafeVaultDB
```

# Functions
## Initialization
### __init__(database_path:str, password:str)
### Initialize SafeVault object.

#### database_path (str): The path to the database file.
#### password (str): The password used to generate the encryption key.
## Adding Data
### add_data(key:str, value:str)
### Adds key-value pair to the encrypted database.

#### key (str): The key to add.
#### value (str): The value corresponding to the key.
## Updating Data
### update_data(key:str, value:str)
### Updates the value corresponding to the given key in the encrypted database.

#### key (str): The key to update.
#### value (str): The new value corresponding to the key.
## Retrieving Data
### get_data(key:str)
### retrieves data corresponding to the given key from the encrypted database.

#### key (str): The key to retrieve data for.
## Deleting Data
### delete_data(key:str)
#### Key (str): The key to delete
### Deletes data corresponding to the given key from the encrypted database.
