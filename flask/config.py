from app import app
import redis

class Config(object):
    DEBUG = False
    TESTING = False

class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True

# Connect to Redis instance
r = redis.Redis(host="redis.default.svc.cluster.local", port=6379)

# Insert first entries into Redis Database. Put Some JSON into Redis. These represent common/ cached API calls
r.set('Bob', '{"Age": "31", "Occupation": "Data Engineer", "Favourite Food": "Spagetti"}')
r.set('Alice', '{"Age": "24", "Occupation": "Software Engineer", "Favourite Food": "Tuna"}')
