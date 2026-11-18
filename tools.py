import forty7_sdk
from forty7_sdk import tool

_RATES = "https://api.frankfurter.dev/v1/latest"


@tool(egress=["api.frankfurter.dev"])
async def exchange_rate(base: str, to: str) -> dict:
    """Return today's published exchange rate between two currencies.

    `base` and `to` are three-letter currency codes such as EUR, USD or GBP. The returned
    rate is how many `to` one `base` buys, so the number comes from the live feed rather
    than the model, which is what proves the tool actually ran.
    """
    response = await forty7_sdk.http.get(_RATES, params={"base": base, "symbols": to})
    response.raise_for_status()
    rate = response.json()["rates"][to]
    return {"base": base, "to": to, "rate": rate}

