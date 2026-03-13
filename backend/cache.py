import aioredis
import json
from functools import wraps

REDIS_URL = "redis://localhost:6379"

async def get_redis_client():
    return await aioredis.create_redis_pool(REDIS_URL)

async def set_cache_key(key, value, ttl):
    redis = await get_redis_client()
    await redis.set(key, json.dumps(value), expire=ttl)
    redis.close()
    await redis.wait_closed()

async def get_cache_key(key):
    redis = await get_redis_client()
    value = await redis.get(key)
    redis.close()
    await redis.wait_closed()
    return json.loads(value) if value else None

async def invalidate_cache_key(key):
    redis = await get_redis_client()
    await redis.delete(key)
    redis.close()
    await redis.wait_closed()

# Decorator for caching function results
def redis_cache(ttl=300):
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            cache_key = f"{func.__name__}:{args}:{kwargs}"
            cached_value = await get_cache_key(cache_key)
            if cached_value is not None:
                return cached_value
            result = await func(*args, **kwargs)
            await set_cache_key(cache_key, result, ttl)
            return result
        return wrapper
    return decorator