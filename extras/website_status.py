from requests import Response, Request, get


class RequestStatus:
    def __init__(self, url: str) -> None:
        # normalising url
        self._url = url if url.startswith(("http://", "https://")) else f"https://{url}"

    def get_url_status(self, timeout: int):
        try:
            response: Response = get(url=self._url, timeout=timeout)
        except Exception as e:
            print(f"ERROR: {e}")
            return

        print(f"{"=" * 10} STATUS for URL: {self._url} {"=" * 10}")
        print(f"Status Code:  {response.status_code} ({response.reason})")
        print(f"Elapsed Time: {response.elapsed}")
        print(f"Headers:")
        for k, v in response.headers.items():
            print(f"===> {k}: {v}")


if __name__ == "__main__":
    url = "https://www.google.com"
    # url = "https://amanbhargava.onrender.com/"
    request_status: RequestStatus = RequestStatus(url=url)
    request_status.get_url_status(timeout=10)
