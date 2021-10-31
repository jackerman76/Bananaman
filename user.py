import time
import json
import phonenumbers
class User():
    #Not sure if picture data can belong to a object
    def __init__(self, user_id, username, password, email,
                 phone_number, bananas_given):

        self.user_id = user_id
        self.username = str(username)
        self.password = str(password)
        self.email = None
        if email: self.email = email
        self.phone_number = None
        if phone_number: self.phone_number = self.set_phone(phone_number)
        self.bananas_given = bananas_given

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
