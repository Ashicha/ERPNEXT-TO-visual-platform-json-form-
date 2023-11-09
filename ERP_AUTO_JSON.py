import os
import requests
import json
import schedule
import time


item_code_to_category = {
    'A01': 'Accessories',
    'A02': 'Accessories',
    'A03': 'Accessories',
    'A04': 'Accessories',
    'A05': 'Accessories',
    'C01': 'Clothes',
    'C02': 'Clothes',
    'C03': 'Clothes',
    'C04': 'Clothes',
    'C05': 'Clothes',
    'M01': 'Cosmetic',
    'M02': 'Cosmetic',
    'M03': 'Cosmetic',
    'M04': 'Cosmetic',
    'M05': 'Cosmetic',
}


class ERPDataExtractor_SI:
    def __init__(self, url, api_key, api_secret):
        self.url = url
        self.api_key = api_key
        self.api_secret = api_secret
        self.headers = {
            'Authorization': f'token {api_key}:{api_secret}',
            'Content-Type': 'application/json'
        }
        self.output_data_SI = []

    def extract_data(self):

        response = requests.get(self.url, headers=self.headers)


        if response.status_code == 200:
            data = response.json()


            for item in data["data"]:
                name = item["name"]
                base_url = f"https://erp04.tetraserver.com/api/resource/Sales%20Invoice/{name}/?limit=1000"
                print("Filled URL:", base_url)


                individual_response = requests.get(base_url, headers=self.headers)


                if individual_response.status_code == 200:
                    individual_data = individual_response.json()


                    name = individual_data['data']['name']
                    customer = individual_data['data']['customer']
                    status = individual_data['data']['status']
                    total_qty = individual_data['data']['total_qty']
                    total_amount = individual_data['data']['total']
                    company = individual_data['data']['company']
                    posting_date = individual_data['data']['posting_date']
                    due_date = individual_data['data']['due_date']
                    net_rate = individual_data['data'].get('net_rate')
                    discount_percentage = individual_data['data'].get('discount_percentage')
                    discount_amount = individual_data['data'].get('discount_amount')

                    items = individual_data['data']['items']
                    item_codes = []
                    item_names = []
                    item_categories = []

                    for item in items:
                        item_code = item['item_code']
                        item_name = item['item_name']
                        item_category = item_code_to_category.get(item_code, 'Old-product')

                        item_codes.append(item_code)
                        item_names.append(item_name)
                        item_categories.append(item_category)


                    print("Extracted Data:")
                    print(f"Name: {name}")
                    print(f"Customer: {customer}")
                    print(f"Status: {status}")
                    print(f"Total Quantity: {total_qty}")
                    print(f"Total Amount: {total_amount}")
                    print(f"Company: {company}")
                    print(f"Posting Date: {posting_date}")
                    print(f"Due Date: {due_date}")
                    print(f"Net Rate: {net_rate}")
                    print(f"Discount Percentage: {discount_percentage}")
                    print(f"Discount Amount: {discount_amount}")
                    print(f"Item Codes: {item_codes}")
                    print(f"Item Names: {item_names}")
                    print(f"Item Categories: {item_categories}")
                    print("-------------------------------------")


                    if company == "Graduation Company":
                        output_item_SI = {
                            'Company': company,
                            'Name': name,
                            'Customer': customer,
                            'Status': status,
                            'Total Quantity': total_qty,
                            'Total Amount': total_amount,
                            'Posting Date': posting_date,
                            'Due Date': due_date,
                            'Discount Percentage': discount_percentage,
                            'Discount Amount': discount_amount,
                            'Item Codes': item_codes,
                            'Item Names': item_names,
                            'Item Categories': item_categories
                        }


                        self.output_data_SI.append(output_item_SI)
                else:
                    print('Request failed with status code:', individual_response.status_code)
                    print('Error message:', individual_response.text)
        else:
            print('Request failed with status code:', response.status_code)
            print('Error message:', response.text)


class ERPDataExtractor_SO:
    def __init__(self, url, api_key, api_secret):
        self.url = url
        self.api_key = api_key
        self.api_secret = api_secret
        self.headers = {
            'Authorization': f'token {api_key}:{api_secret}',
            'Content-Type': 'application/json'
        }
        self.output_data_SO = []

    def extract_data(self):

        response = requests.get(self.url, headers=self.headers)


        if response.status_code == 200:
            data = response.json()


            for item in data["data"]:
                name = item["name"]
                base_url = f"https://erp04.tetraserver.com/api/resource/Sales%20Order/{name}/?limit=1000"
                print("Filled URL:", base_url)


                individual_response = requests.get(base_url, headers=self.headers)


                if individual_response.status_code == 200:
                    individual_data = individual_response.json()


                    name = individual_data['data']['name']
                    customer = individual_data['data']['customer']
                    status = individual_data['data']['status']
                    total_qty = individual_data['data']['total_qty']
                    total_amount = individual_data['data']['total']
                    company = individual_data['data']['company']
                    net_rate = individual_data['data'].get('net_rate')
                    discount_percentage = individual_data['data'].get('discount_percentage')
                    discount_amount = individual_data['data'].get('discount_amount')
                    delivery_date = individual_data['data']['delivery_date']

                    items = individual_data['data']['items']
                    item_codes = []
                    item_names = []
                    item_categories = []

                    for item in items:
                        item_code = item['item_code']
                        item_name = item['item_name']
                        item_category = item_code_to_category.get(item_code, 'Old-product')

                        item_codes.append(item_code)
                        item_names.append(item_name)
                        item_categories.append(item_category)


                    print("Extracted Data:")
                    print(f"Name: {name}")
                    print(f"Customer: {customer}")
                    print(f"Status: {status}")
                    print(f"Total Quantity: {total_qty}")
                    print(f"Total Amount: {total_amount}")
                    print(f"Company: {company}")
                    print(f"Net Rate: {net_rate}")
                    print(f"Discount Percentage: {discount_percentage}")
                    print(f"Discount Amount: {discount_amount}")
                    print(f"Item Codes: {item_codes}")
                    print(f"Item Names: {item_names}")
                    print(f"Item Categories: {item_categories}")
                    print("-------------------------------------")


                    if company == "Graduation Company":
                        output_item_SO = {
                            'Company': company,
                            'Name': name,
                            'Customer': customer,
                            'Status': status,
                            'Total Quantity': total_qty,
                            'Total Amount': total_amount,
                            'Discount Percentage': discount_percentage,
                            'Discount Amount': discount_amount,
                            'Item Codes': item_codes,
                            'Item Names': item_names,
                            'Item Categories': item_categories
                        }


                        self.output_data_SO.append(output_item_SO)
                else:
                    print('Request failed with status code:', individual_response.status_code)
                    print('Error message:', individual_response.text)
        else:
            print('Request failed with status code:', response.status_code)
            print('Error message:', response.text)


class DataExtractorHelper:
    @staticmethod
    def save_to_json(output_data, file_path):

        with open(file_path, 'w') as file:
            json.dump(output_data, file)

        print(f"Output JSON file saved to: {file_path}")


def extract_and_save_data():

    api_key = 'a0241e7861ae5c5'
    api_secret = '365f4b2f89e0d9a'


    url_SI = 'https://erp04.tetraserver.com/api/resource/Sales%20Invoice?limit=1000'
    url_SO = 'https://erp04.tetraserver.com/api/resource/Sales%20Order?limit=1000'


    sales_invoice_extractor = ERPDataExtractor_SI(url_SI, api_key, api_secret)
    sales_order_extractor = ERPDataExtractor_SO(url_SO, api_key, api_secret)


    sales_invoice_extractor.extract_data()
    sales_order_extractor.extract_data()


    desktop_path = os.path.expanduser("~/Desktop/ERP")  # Get the desktop path
    file_path_SI = os.path.join(desktop_path, "sales_invoices.json")  # Sales Invoices file path
    file_path_SO = os.path.join(desktop_path, "sales_orders.json")  # Sales Orders file path


    DataExtractorHelper.save_to_json(sales_invoice_extractor.output_data_SI, file_path_SI)
    DataExtractorHelper.save_to_json(sales_order_extractor.output_data_SO, file_path_SO)



schedule.every(1).minutes.do(extract_and_save_data)

while True:
    schedule.run_pending()
    time.sleep(1)
