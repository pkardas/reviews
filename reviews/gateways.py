import time
from typing import Optional

import requests


def get_website_html(url: str) -> Optional[bytes]:
    headers = {
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Methods": "GET",
        "Access-Control-All ow-Headers": "Content-Type",
        "Access-Control-Max-Age": "3600",
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0"
    }

    error = None

    for attempt in range(3):
        try:
            return requests.get(url, headers).content
        except Exception as e:
            print(f"Failed (attempt: {attempt + 1}): {e} -- waiting 30 seconds for a new retry")
            error = e
            time.sleep(30)
    else:
        print(f"Failed! {error}")

    return None
