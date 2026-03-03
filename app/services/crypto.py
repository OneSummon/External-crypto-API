import json
from redis.asyncio import Redis

from app.core.config import CACHE_TTL
from app.core.http_client import fetch_coin_all_info, fetch_crypto_price, fetch_crypto_symbols


async def get_crypto_price(symbol: str, redis: Redis) -> float:
    cache_key = f"crypto:price:{symbol}"
    
    cached_price = await redis.get(cache_key)
    if cached_price is not None:
        return float(cached_price)
    
    price = await fetch_crypto_price(symbol)
    
    await redis.set(cache_key, price, ex=CACHE_TTL)
    
    return price


async def get_crypto_symbols(redis: Redis):
    cache_key = "crypto:symbols"
    
    cached_symbols = await redis.get(cache_key)
    if cached_symbols is not None:
        return json.loads(cached_symbols)
    
    symbols = await fetch_crypto_symbols()
    
    await redis.set(cache_key, json.dumps(symbols), ex=CACHE_TTL)
    
    return symbols


async def get_coin_all_info(symbol: str, redis: Redis):
    cache_key = f"crypto:all_info_coin:{symbol}"
    
    cached_info = await redis.get(cache_key)
    if cached_info is not None:
        return json.loads(cached_info)
    
    info = await fetch_coin_all_info(symbol)
    
    await redis.set(cache_key, json.dumps(info), ex=CACHE_TTL)
    
    return info