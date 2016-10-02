import uuid

from mongoengine import *

class User(Document):

    user_id = StringField(max_length=200, required=True)
    full_name = StringField(max_length=200, required=True)
    country_code = StringField(max_length=5, required=True)
    mobile = IntField(required=True)

    def as_json(self):
        property_hash = {
            'user_id':self.user_id,
            'full_name': self.full_name,
            'country_code':self.country_code,
            'mobile': self.mobile
        }
        return property_hash

    @classmethod
    def create_user(cls, user_hash=None):
        user = User(user_id= uuid.uuid1().hex,
                    full_name=user_hash["full_name"],
                    country_code = user_hash["country_code"],
                    mobile=user_hash["mobile"])
        user.save()
        return user

    @staticmethod
    def is_valid_hash(user_hash):
        errors = []
        full_name = user_hash['full_name']
        errors.append({"full_name": "full_name cannot be blank"}) if not full_name else None

        country_code = user_hash['country_code']
        errors.append({"country_code": "country_code cannot be blank"}) if not country_code else None

        mobile = user_hash['mobile']
        errors.append({"mobile": "mobile cannot be blank"}) if not mobile else None

        if mobile.__len__()!=10:
            errors.append({"mobile": "invalid mobile number"})

        if not errors:
            return True
        else:
            raise ValueError(errors)

    def find_by_email(self, email):
        return [user.as_json() for user in User.objects(email=email)]

