import sys
import os
import asyncio
from playwright.async_api import async_playwright

async def capture_diagram(html_path, png_path):
    if not os.path.exists(html_path):
        print(f"Error: HTML file '{html_path}' not found.")
        sys.exit(1)

    abs_html_path = os.path.abspath(html_path)
    file_url = f"file://{abs_html_path}"

    async with async_playwright() as p:
        # Launch Chromium headlessly
        browser = await p.chromium.launch(headless=True)
        
        # device_scale_factor=2 ensures a high-resolution (retina) capture
        context = await browser.new_context(device_scale_factor=2)
        page = await context.new_page()

        print(f"Loading HTML: {file_url}")
        # Wait until network is fully idle so Mermaid.js can load and execute
        await page.goto(file_url, wait_until="networkidle")

        try:
            # Target the SVG element directly to crop out body margins/padding
            svg_locator = page.locator(".mermaid svg")
            
            # Wait for Mermaid to finish rendering and attaching the SVG
            await svg_locator.wait_for(state="attached", timeout=15000)
            
            # Give a brief moment for internal SVG browser paint to finalize
            await page.wait_for_timeout(500)
            
            # Screenshot only the bounding box of the SVG
            await svg_locator.screenshot(path=png_path, omit_background=True)
            print(f"Successfully captured and cropped diagram to: {png_path}")
            
        except Exception as e:
            print(f"Failed to capture SVG specifically: {e}")
            print("Falling back to capturing the .mermaid container div...")
            try:
                div_locator = page.locator(".mermaid")
                # Fallback to div screenshot
                await div_locator.screenshot(path=png_path, omit_background=True)
                print(f"Successfully captured diagram (fallback) to: {png_path}")
            except Exception as inner_e:
                print(f"Error during fallback capture: {inner_e}")
                sys.exit(1)
        finally:
            await browser.close()

def main():
    if len(sys.argv) != 3:
        print("Usage: python capture_diagram.py <html-path> <png-path>")
        sys.exit(1)

    html_path = sys.argv[1]
    png_path = sys.argv[2]
    
    asyncio.run(capture_diagram(html_path, png_path))

if __name__ == "__main__":
    main()
