import asyncio
import os
from playwright.async_api import async_playwright

async def validate():
    errors = []
    media_404 = []

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        # Capture console errors
        page.on("console", lambda msg: errors.append(f"[{msg.type}] {msg.text}") if msg.type == "error" else None)

        # Capture 404 errors for media
        page.on("response", lambda response: media_404.append(f"404: {response.url}") if response.status == 404 else None)

        # Load the local HTML file
        file_path = "file:///workspace/congreso-electronico-2026/index.html"

        try:
            await page.goto(file_path, wait_until="networkidle", timeout=30000)
            await asyncio.sleep(2)  # Wait for animations to load
        except Exception as e:
            print(f"Page load error: {e}")

        await browser.close()

    print("=== VALIDATION RESULTS ===\n")

    if errors:
        print("CONSOLE ERRORS:")
        for err in errors:
            print(f"  - {err}")
    else:
        print("No console errors found.")

    print()

    if media_404:
        print("MEDIA 404 ERRORS:")
        for err in media_404:
            print(f"  - {err}")
    else:
        print("No 404 errors found for media files.")

    print("\n=== VALIDATION COMPLETE ===")

if __name__ == "__main__":
    asyncio.run(validate())