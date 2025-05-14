import redis

# Try connecting to the Redis server
r = redis.Redis(host='127.0.0.1', port=6379, db=0)

# Try a simple command to test the connection
print(r.ping())  # This should return True
