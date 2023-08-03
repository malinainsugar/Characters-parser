from pydantic import BaseModel


class NoveltyBase(BaseModel):
    name: str
    author : str
    publisher : str 
    year : int
    page_count : int
    price : int
    description : str 
    link : str


class NoveltyCreate(NoveltyBase):
    product_id : int
    pass

class NoveltyUpdate(NoveltyBase):
    pass


class Novelty(NoveltyBase):
    id: int
    product_id : int
