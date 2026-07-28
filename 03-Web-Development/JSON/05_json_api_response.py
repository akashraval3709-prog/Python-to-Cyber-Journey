import json
def get_product_api(request_payload):
    product_database = {
        101: {
            "title": "Wireless Gaming Mouse",
            "price": 1499.50,
            "in_stock": True,
            "discount": 10.0,
            "tags": ("electronics", "accessories") # Tuple -> JSON Array
        },
        102: {
            "title": "Mechanical Keyboard",
            "price": 3499.00,
            "in_stock": False,
            "discount": None,                     # None -> JSON null
            "tags": ["gaming", "keyboard"]
        },
        103: {
            "title": "USB-C Fast Charger",
            "price": 699.00,
            "in_stock": True,
            "discount": 5.5,
            "tags": ("mobile", "charger")
        }
    }

    request_id = request_payload.get('product_id')
   

    if request_id in product_database:
        responcePayload={ "status_code" : 200 ,
                         "message": "product record fetched successfully", 
                         "data" :product_database[request_id]
                         }
    else:
         responcePayload={ "status_code" : 404 ,
                                 "message": "product ID does not exist in database", 
                                 "data" :None
                                 }
    json_data = json.dumps(responcePayload,indent=2)

    return json_data


request1 = {"product_id": 101}
http_response = get_product_api(request1)
print(f"---- First API Response ----\n{http_response}")

request2 = {"product_id": 102}
http_response = get_product_api(request2)
print(f"\n---- Second API Response ----\n{http_response}")

request3 = {"product_id": 105}
http_response = get_product_api(request3)
print(f"\n---- Third API Response ----\n{http_response}")
