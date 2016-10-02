def get_user_json_attr_from_hash(user_hash):
    return {
        "full_name": user_hash.get("full_name"),
        "country_code":user_hash.get("country_code"),
        "mobile": user_hash.get("mobile"),

    }
