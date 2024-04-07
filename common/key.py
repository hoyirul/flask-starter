import os
import string
import secrets
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Key:
    def generate_random_key(self, length=64):
        # Generate a random key with specified length
        alphabet = string.ascii_letters + string.digits + "!@$%^&*_+=-"
        return ''.join(secrets.choice(alphabet) for _ in range(length))

    def update_secret_key(self):
        # Generate a random key with length 64 (you can adjust the length as needed)
        random_key = self.generate_random_key(length=64)

        # Update SECRET_KEY with the new random key
        with open('.env', 'r') as f:
            lines = f.readlines()
        with open('.env', 'w') as f:
            for line in lines:
                if line.startswith('SECRET_KEY='):
                    f.write(f'SECRET_KEY={random_key}\n')
                else:
                    f.write(line)

        print(f'Secret key updated: {random_key}')