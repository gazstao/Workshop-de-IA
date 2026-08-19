from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Meu Servidor Personalizado")

@mcp.tool()
def somar_valores(a: int, b: int) -> int:
    """Soma dois números inteiros."""
    return a + b

if __name__ == "__main__":
    mcp.run()
