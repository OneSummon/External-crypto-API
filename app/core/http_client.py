import httpx
from app.core.config import EXT_API_COIN_ALL_INFO_URL, EXT_API_PRICE_URL
from app.core.config import EXT_API_SYMBOLS_URL

async def fetch_crypto_price(symbol: str) -> float:
    url = EXT_API_PRICE_URL
    params = {
        "ids": symbol,
        "vs_currencies": "usd",
    }
    
    async with httpx.AsyncClient() as client:
        response = await client.get(url, params=params)
        response.raise_for_status()
        
        data = response.json()
        
        return data[symbol]["usd"]


async def fetch_crypto_symbols():
    url = EXT_API_SYMBOLS_URL
    
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        response.raise_for_status()
        
        data = response.json()
        
        return data
    

async def fetch_coin_all_info(symbol: str):
    url = EXT_API_COIN_ALL_INFO_URL
    params = {
        "ids": symbol,
        "vs_currency": "usd",
    }
    
    async with httpx.AsyncClient() as client:
        response = await client.get(url, params=params)
        response.raise_for_status()
        
        data = response.json()
        
        return data[0] if data else None