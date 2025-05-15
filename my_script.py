from playwright.async_api import Playwright, async_playwright, expect
import asyncio

async def run(playwright: Playwright) -> None:
    browser_args = [
        '--window-size=1300,570',
        '--window-position=000,000',
        '--disable-dev-shm-usage',
        '--no-sandbox',
        '--disable-web-security',
        '--disable-features=site-per-process',
        '--disable-setuid-sandbox',
        '--disable-accelerated-2d-canvas',
        '--no-first-run',
        '--no-zygote',
        '--use-gl=egl',
        '--disable-blink-features=AutomationControlled',
        '--disable-background-networking',
        '--enable-features=NetworkService,NetworkServiceInProcess',
        '--disable-background-timer-throttling',
        '--disable-backgrounding-occluded-windows',
        '--disable-breakpad',
        '--disable-client-side-phishing-detection',
        '--disable-component-extensions-with-background-pages',
        '--disable-default-apps',
        '--disable-extensions',
        '--disable-features=Translate',
        '--disable-hang-monitor',
        '--disable-ipc-flooding-protection',
        '--disable-popup-blocking',
        '--disable-prompt-on-repost',
        '--disable-renderer-backgrounding',
        '--disable-sync',
        '--force-color-profile=srgb',
        '--metrics-recording-only',
        '--enable-automation',
        '--password-store=basic',
        '--use-mock-keychain',
        '--hide-scrollbars',
        '--mute-audio'
    ]         
    chromium = playwright.chromium
    browser = await chromium.launch(
        headless=False,
        args=browser_args,
    )

    context = await browser.new_context(
        ignore_https_errors=True,
        locale='en-US',
        permissions=['notifications'],
    )

    page = await context.new_page()

    await page.goto('https://freecloud.ltd/login', wait_until='networkidle')
    print(page.url)

    await context.close()
    await browser.close()
async def main():
    async with async_playwright() as playwright:
        await run(playwright)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
loop.close()
