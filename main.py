# Import FastAPI
from fastapi import FastAPI
from mangum import Mangum



# Initialize the app
app = FastAPI()
handler = Mangum(app)

# Define a route
@app.get("/")
async def read_root():
    return "Salut, on dirait que j'arrive bientôt"
