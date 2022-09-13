import argparse

import sys

from src.seed import add_random_users, add_user, delete_user, get_all_users, get_user, update_user

ACTIONS = {get_all_users: 'show', add_user: 'add', add_random_users: 'add_random',
           update_user: 'update', delete_user: 'remove', get_user: 'get'}


def main():
    parser = argparse.ArgumentParser(description='Address Book')
    parser.add_argument('--action', help='Command: add, update, get, remove, show, add_random')
    parser.add_argument('--id', help='User ID')
    parser.add_argument('--name', help='User name')
    parser.add_argument('--phone', help='User phone')
    parser.add_argument('--email', help='User email')
    parser.add_argument('--address', help='User address')

    args = parser.parse_args()
    my_args = vars(args)

    command = my_args.pop('action')

    for k, v in ACTIONS.items():
        if v == command:
            try:
                print(k(**my_args))
            except Exception as e:
                print(e)
                sys.exit(1)


if __name__ == '__main__':
    main()

