from mcp.server.fastmcp import FastMCP

mcp = FastMCP("FWQMCPServer")

@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

@mcp.tool()
def multiply(a: int, b: int) -> int:
    """Multiply two numbers"""
    return a * b

@mcp.tool()
def get_quote(city_name: str) -> str:
    """Fetch the quote for a flight from ZRH to a destination (city_name)"""
    destinations = [
        ("London", "LHR", 180),
        ("New York", "JFK", 620),
        ("Dubai", "DXB", 450),
        ("Amsterdam", "AMS", 160),
        ("Frankfurt", "FRA", 140)
    ]

    code_to_price = {code: price for _, code, price in destinations}
    city_to_code = {city.lower(): code for city, code, _ in destinations}

    code = city_to_code.get(city_name.lower())

    if not code:
        raise Exception(f"Could not find destination: {city_name}, please choose from {city_to_code}")

    else:
        return f"A flight from Zurich to {city_name} ({code}) costs {code_to_price[code]} CHF."

if __name__ == "__main__":
    mcp.run(transport="stdio")