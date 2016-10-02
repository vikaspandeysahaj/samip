class Config(object):
    DEBUG = False

    MONGO_DB_NAME="samipdevdb"
    MONGO_DB_USERNAME="samipdev"
    MONGO_DB_PASSWORD="passw0rd1234d"
    MONGO_DB_HOST="localhost"
    MONGO_DB_PORT="27017"
    MONGO_CONNECTION_URL = "mongodb://"+ MONGO_DB_HOST + "/"+ MONGO_DB_NAME

class Development(Config):
    DEBUG = True

class Test(Config):
    DEBUG = True
    MONGO_DB_NAME="samiptestdb"
    MONGO_DB_USERNAME="samiptest"
    MONGO_DB_PASSWORD="passw0rd1234"
    MONGO_DB_HOST="localhost"
    MONGO_DB_PORT="27017"
    MONGO_CONNECTION_URL = "mongodb://"+ MONGO_DB_HOST + "/"+ MONGO_DB_NAME


# use samipdevdb
# db.createUser(
#    {
#      user: "samipdev",
#      pwd: "passw0rd1234",
#      roles: [ "readWrite", "dbAdmin" ]
#    }
# )