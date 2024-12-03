import os
from dotenv import load_dotenv
from aocd import get_data

def get_puzzle(day: int) -> str:
    load_dotenv()
    session = os.getenv("AOC_SESSION")
    return get_data(day=day, year=2024, session=session)

