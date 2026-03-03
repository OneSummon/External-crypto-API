from fastapi import APIRouter
from app.deps.rate_limit import RateLimitDep
from app.deps.redis import RedisDep
from app.schemas.crypto import PriceResponse, SymbolsResponse
from app.services.crypto import get_coin_all_info, get_crypto_price, get_crypto_symbols


router = APIRouter(prefix="/crypto", tags=["Crypto"])


@router.get("/price/{symbol}", response_model=PriceResponse)
async def crypto_price(symbol: str, redis: RedisDep, _: RateLimitDep):
    price = await get_crypto_price(symbol, redis)
    
    return {"symbol": symbol, "price": price}


@router.get("/all_info/{symbol}")
async def crypto_all_info(symbol: str, redis: RedisDep, _: RateLimitDep):
    all_info = await get_coin_all_info(symbol, redis)
    
    return {"symbol": symbol, "all_info": all_info}


@router.get("/symbols", response_model=SymbolsResponse)
async def crypto_symbols(redis: RedisDep, _: RateLimitDep):
    symbols = await get_crypto_symbols(redis)
    
    return {"symbols": symbols}