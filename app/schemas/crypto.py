from pydantic import BaseModel

class PriceResponse(BaseModel):
    symbol: str
    price: float
    
class SymbolsResponse(BaseModel):
    symbols: list[str]