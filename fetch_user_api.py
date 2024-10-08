import requests

def fetch_random_user():
    url = 'https://api.freeapi.app/api/v1/public/randomusers/user/random'
    response = requests.get(url)
    data = response.json()
    if data['success'] and 'data' in data:
        user_data = data['data']
        usermame = user_data['login']['username']
        country = user_data['location']['country']
        return usermame,country
    else:
        raise Exception('Failed to fetch the data')

def main():
    try:
        username,country = fetch_random_user()
        print(f'Username:{username} \n Country:{country}')
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()