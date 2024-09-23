from src.assistant import process_user_query

def main():
    user_query = input("User: ")
    response = process_user_query(user_query)
    print(response)

if __name__ == "__main__":
    main()
