import aiohttp
from src import app

if __name__ == "__main__":
    aiohttp.web.run_app(app)
