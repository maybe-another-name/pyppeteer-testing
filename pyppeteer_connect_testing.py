import asyncio
from pyppeteer import connect


# this expects the browser be started with remote debugging enabled, for example:
#       chromium --remote-debugging-port=9222
# it will then report it's id, as follows:
#       DevTools listening on ws://127.0.0.1:9222/devtools/browser/e3b807df-40cb-4922-97bb-2e8ffc519d73
# this id is referened in the ws endpoint url

async def main():
    browser = await connect(browserWSEndpoint="ws://127.0.0.1:9222/devtools/browser/e935b210-04bd-41e4-9734-ecf448bf7583")
    page = await browser.newPage()
    await page.goto('http://...')

    # page.evaluate()

    # dimensions = await page.evaluate('''() => {
    #     return {
    #         width: document.documentElement.clientWidth,
    #         height: document.documentElement.clientHeight,
    #         deviceScaleFactor: window.devicePixelRatio,
    #     }
    # }''')

    # print(dimensions)
    # >>> {'width': 800, 'height': 600, 'deviceScaleFactor': 1}
    # await browser.close()


asyncio.get_event_loop().run_until_complete(main())
