import redis

r = redis.StrictRedis(host='localhost', port=6379, db=0)

def like_get(KEY):
    return r.get(KEY)

def like_incr(KEY):
    return r.incr(KEY)

def like_decr(KEY):
    return r.decr(KEY)
