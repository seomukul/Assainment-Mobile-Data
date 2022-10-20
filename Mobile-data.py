mobile_data = {
   'status': True,
   'data': [
       {'name': 'Xiaomi Note 5', 'price': '300 USD', 'made': 'China'},
       {'name': 'Samsung Note 6', 'price': '200 USD', 'made': 'USA'},
       {'name': 'Iphone 5', 'price': '180.5 USD', 'made': 'Japan'},
       {'name': 'Pixel 5', 'price': '89.60 USD', 'made': 'Rusia'},
       {'name': 'Techno 5', 'price': '110 USD', 'made': 'Uk'},
       {'name': 'Huawei 5', 'price': '350 USD', 'made': 'Malaysia'},
       {'name': 'Huawei 5', 'price': '350 USD', 'made': 'Malaysia'},
   ],
   'exchnage_rate': 103.25
}

#  Your Code Starts from here
import random

mobile_dict = mobile_data['data'][1]
name = mobile_dict['name']
made = mobile_dict['made']
usd_price = mobile_dict.get('price')
exchange = mobile_data.get('exchnage_rate')
price_draft = usd_price.split()
price_str = price_draft[0]
final_price = float(price_str)
bdt_price = round(final_price * exchange)

first_sentence_list = [f'The name of the mobile is {name}. ',
       f'This is the 2022 first model is {name}. ',
       f'hurrah ! you are getting {name}. '
       ]
second_sentence_list = [
       f'made in {made}. ',
       f'the beast from {made}. ',
       f'its origin from {made}. ',]
third_sentence_list = [
       f'you can buy it {usd_price} USD which is almost equal to {bdt_price}',
       f'early grab it only {usd_price} USD that is nealy equal to {bdt_price}',
       f'this week price is only {usd_price} USD which is nearly to {bdt_price}',]

first_sentence = random.choice(first_sentence_list)
second_sentence = random.choice(second_sentence_list)
third_sentence = random.choice(third_sentence_list)

print(first_sentence, second_sentence, third_sentence)

