import requests

def fetch_random_product():
    url = 'https://api.freeapi.app/api/v1/public/randomproducts/product/random'
    response = requests.get(url)
    data = response.json()

    if data['success'] and 'data' in data:
        product_data = data['data']
        brand = product_data['brand']
        category = product_data['category']
        discount = product_data['discountPercentage']
        return brand,category,discount
    else:
        raise Exception('Failed to fetch data/Api Error')
def main():
    try:
        brand,category,discount = fetch_random_product()
        print(f'Product brand is {brand}, it belongs to {category} and it has the discount of {discount} %')
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()
fetch_random_product()