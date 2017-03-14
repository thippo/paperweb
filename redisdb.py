import redis

r = redis.StrictRedis(host='localhost', port=6379, db=0)

def like_get(KEY):
    return r.get(KEY).decode() if r.exists(KEY) else '0'

def like_incr(KEY):
    return r.incr(KEY)

def like_decr(KEY):
    return r.decr(KEY)

def like_del(KEY):
    return r.delete(KEY) if r.exists(KEY) else True

