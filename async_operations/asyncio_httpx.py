import asyncio
import httpx


async def process_url(client: httpx.AsyncClient, url: str):
    print(f"Processing {url}")

    response = await client.get(url)
    response.raise_for_status()

    print(f"Finished {url}: {response.status_code}")
    return response.text


async def main():
    async with httpx.AsyncClient(timeout=10) as client:
        results = await asyncio.gather(
            process_url(client, "https://www.google.com"),
            process_url(client, "https://www.instagram.com"),
            return_exceptions=True,
        )

    for result in results:
        if isinstance(result, Exception):
            print("Request failed:", result)
        else:
            print("Request succeeded")


asyncio.run(main(), debug=True)
