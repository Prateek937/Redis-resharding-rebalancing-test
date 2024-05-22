import redis

def test():
    # Connect to the Redis cluster
    redis_host = "nbbps01-w2ilxo.serverless.aps1.cache.amazonaws.com"
    rc = redis.Redis(host=redis_host, port = 6379, decode_responses=True)
    try:
        rc.ping()
        return 'connected to redis "{}"'.format(redis_host)
    except redis.exceptions.ResponseError as e:
        return e
    
test()