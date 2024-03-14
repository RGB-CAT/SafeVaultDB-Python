import argparse
from .database import SafeVault  # Make sure to import the SafeVault class

def main():
    parser = argparse.ArgumentParser(description='SafeVaultDB Command Line Interface')
    parser.add_argument('database_path', type=str, help='Path to the database file')
    parser.add_argument('password', type=str, help='Password for encryption')
    parser.add_argument('--add', nargs=2, metavar=('key', 'value'), help='Add key-value pair to database')
    parser.add_argument('--update', nargs=2, metavar=('key', 'value'), help='Update value for existing key in database')
    parser.add_argument('--get', metavar='key', help='Get value for a key from database')
    parser.add_argument('--delete', metavar='key', help='Delete key-value pair from database')
    args = parser.parse_args()

    safe_vault = SafeVault(args.database_path, args.password)

    if args.add:
        key, value = args.add
        safe_vault.add_data(key, value)
        print(f'Added key-value pair: {key}: {value}')
    elif args.update:
        key, value = args.update
        if safe_vault.update_data(key, value):
            print(f'Updated value for key {key}')
        else:
            print(f'Key {key} not found in database')
    elif args.get:
        value = safe_vault.get_data(args.get)
        if value is not None:
            print(f'Value for key {args.get}: {value}')
        else:
            print(f'Key {args.get} not found in database')
    elif args.delete:
        if safe_vault.delete_data(args.delete):
            print(f'Deleted key {args.delete} from database')
        else:
            print(f'Key {args.delete} not found in database')

if __name__ == "__main__":
    main()
