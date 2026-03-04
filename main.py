from dotenv import load_dotenv
import os

load_dotenv() # load environment variables from .env file

def main():
    print("Hello from hello-world!")
    print(os.getenv("GOOGLE_API_KEY"))


if __name__ == "__main__":
    main()
