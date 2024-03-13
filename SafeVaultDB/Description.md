# SafeVaultDB

## Description

SafeVaultDB is a library for managing a secure database stored as an encrypted JSON file. It provides a simple yet robust solution for storing and retrieving data with password protection.

### Features

- Encrypts and decrypts JSON data using the cryptography library.
- Password protection ensures secure access to the database.
- Easy integration with existing Python projects.
- Supports CRUD operations (Create, Read, Update, Delete) on JSON data.

## Installation

To install SafeVaultDB for python, you can use pip:

```bash
pip install safevaultdb
```

## Contributing
Contributions are welcome! If you'd like to contribute to SafeVaultDB, please submit a pull request to the [repository](https://github.com/RGB-CAT/SafeVaultDB-Python).

## License
SafeVaultDB for python is released under the GNU GPL 3 License.

## Example
```python
from SafeVaultDB import SafeVault

# Path to the database file
database_path = "D:/SafeVaultDB/Database.db"

# Password to access the database
password = "MyPassword123"

# Create an instance of SafeVault
vault = SafeVault(database_path, password)

# Add some data to the database
vault.add_data('name', 'Alice')
vault.add_data('age', 30)

# Get and print data from the database
print("Name:", vault.get_data('name'))
print("Age:", vault.get_data('age'))

# Update data in the database
vault.update_data('age', 31)

# Get and print updated data from the database
print("Updated Age:", vault.get_data('age'))

# Delete data from the database
vault.delete_data('name')

# Get remaining data from the database
print("Remaining data:", vault._read_database())
```