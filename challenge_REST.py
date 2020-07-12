import requests

# get data in dictionary
response = requests.get('https://happyreturnsqatest.free.beeceptor.com/getProductVariants')
data = response.json()

# store product variants - API should always return an object
product_variants = data['variants']

# store individual variant object - Check object returned by API is not empty
if product_variants:
    product_variants_first_object = product_variants[0]

    # post first product variant object
    response = requests.post('https://happyreturnsqatest.free.beeceptor.com/order', data=product_variants_first_object)
    print(response)