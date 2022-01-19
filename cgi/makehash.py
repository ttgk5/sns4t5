import hashlib

def make_hash(data):
    hs = hashlib.md5(data.encode()).hexdigest()
    return hs