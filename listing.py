



import time
import json
import phonenumbers
class Listing():
    
    #Not sure if picture data can belong to a object
    def __init__(self, seller_id, seller_username, location, userEmail, userPhoneNumber, listing_id, amtBananas):
        self.seller_id = seller_id
        self.seller_username = str(seller_username)
        self.userEmail = None
        if userEmail: self.userEmail = userEmail
        self.userPhoneNumber = None
        if userPhoneNumber: self.userPhoneNumber = self.set_phone(userPhoneNumber)
        self.listing_id = listing_id
        self.amtBananas = amtBananas
        self.location = location

    def set_phone(self, phone_number):
        self.phone_number = phonenumbers.format_number(
                            phonenumbers.parse(str(phone_number), 'US'),
                            phonenumbers.PhoneNumberFormat.NATIONAL)

    def __str__(self):
        return str(self.toJSON())

    def toJSON(self):
         return json.dumps(self, default=lambda o: o.__dict__,
            sort_keys=True)

def main():
    if __name__ == '__main__':
        main()
