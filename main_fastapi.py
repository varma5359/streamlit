from fastapi import FastAPI,HTTPException

app = FastAPI()

@app.get("/")
def display():
    return {"message": "Hello, World!"}

@app.post("/items/")
def create_item(name: str, price: float):
    if price < 0:
        raise HTTPException(status_code=400, detail="Price must be non-negative")
    return {"name": name, "price": price}
 

