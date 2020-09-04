"""Main entry point for the script."""

import generalist

if __name__ == '__main__':
    token = generalist.login_user()
    print('GOT TOKEN:', token)
