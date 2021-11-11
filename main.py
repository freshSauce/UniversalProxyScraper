import urllib3
import re
import urllib
import concurrent.futures
import base64
from specific.spys_one import Deofuscator
from random import shuffle

class ProxyScraper:
    HTML = str

    def __init__(self, check: bool = None) -> None:

        """
        Parameters
        ----------
        file : str
            The name of the file with the sites
        output : bool, optional
            In case that the user needs the output he can store it
            on a file named 'output.txt'.
        check : bool, optional
            Used to check if the proxy is alive or not.
        """
        self.check = check
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.5 (KHTML, like Gecko) Chrome/4.0.249.0 Safari/532.5"
        }

    def __doRequest(self, url: str) -> str:
        """
        Parameters
        ----------
        url : str
            URL to be scraped

        Return
        -------
        str :
            Contains the HTML code obtained.
        """

        request = urllib3.PoolManager()

        try:
            result = request.request("GET", url, timeout=1.5, headers=self.headers)

        except urllib3.exceptions.MaxRetryError:
            print(f"Connection to {url.strip()} timed out ")
            return False

        if result.status == 200:
            return {"html": result.data.decode("utf-8"), "site": url.strip()}

        else:
            return False

    def __poolCreator(self, urls: list):
        # -> list[str]:
        """
        Params
        ------
        None :
            None

        Return
        ------
        list[str] :
            List with the full HTML code of each request.
        """
        html_list = list()

        with concurrent.futures.ThreadPoolExecutor() as executor:
            thread_list = [executor.submit(self.__doRequest, url) for url in urls]
            for result in concurrent.futures.as_completed(thread_list):
                if result.result():
                    html_list.append(result.result())

        return html_list

    def __scrape(self, html: HTML, site: str, quantity:int):
        # -> list[str]:
        """
        Parameters
        ----------
        html : HTML
            Requires HTML-like code, in string type.
        Return
        ------
        list[str] :
            List with every proxy obtained from the scraped data.
        """
        if "spys" in site:
            try:
                pattern = r"<table.*width=\"65%\"[\w\W]*?<\/table>"
                table_body = re.search(pattern, html.strip()).group()

                pattern = r"<tr.*?<\/tr>"

                table_rows = list(re.finditer(pattern, table_body))

                proxy_list = list()

                script = re.search(r"eval.*", html).group()
                pattern = r"\(\'[\w].+?\}\)"

                variables_raw = re.search(pattern, script).group()

                variables = (
                    variables_raw.lstrip("(")
                    .rstrip(")")
                    .replace("\\u005e", "^")
                    .split(",")
                )

                p, r, o, x, y, s = (
                    variables[0].replace("'", ""),
                    variables[1],
                    variables[2],
                    variables[3],
                    variables[4],
                    variables[5],
                )

                for row in table_rows[2:]:
                    if len(proxy_list) != quantity*1.5:
                        elements_raw = re.findall(r"<td.*?<\/td>", row.group())
                        elements = [
                            re.sub(r"<.*?>", "", element).strip()
                            for element in elements_raw
                        ]

                        ip_port_cleaned = re.sub(r"(\'&nbsp;)|(\)\')|", "", elements[0])

                        ip_port_splited = re.split(
                            r"document\.write\(\":\"\+", ip_port_cleaned
                        )

                        ip, port = (
                            ip_port_splited[0].replace("&nbsp;", ""),
                            ip_port_splited[1],
                        )

                        port = Deofuscator(p, r, o, x, y, s).deofuscator(port)

                        proxy_list.append(f"{ip}:{port}")
            except:
                proxy_list = list()

            return proxy_list

        pattern = r"<tbody>.*<\/tbody>"
        try:
            table_body = re.search(pattern, html).group()
        except AttributeError:
            table_body = re.search(pattern, html.replace("\n", "")).group()

        pattern = r"<tr.*?<\/tr>"

        table_rows = list(re.finditer(pattern, table_body))

        proxy_list = list()

        for row in table_rows:
            if len(proxy_list) != quantity*1.5:
                elements_raw = re.findall(r"<td.*?<\/td>", row.group())
                elements = [
                    re.sub(r"<.*?>", "", element).strip() for element in elements_raw
                ]

                try:
                    ip, port = elements[0], elements[1]

                except IndexError:
                    continue

                if "decode" in ip or "decode" in port:
                    ip = re.sub(r"(.*[^=\w\d]\")|(\"\).*)", "", ip)
                    port = re.sub(r"(.*[^=\w\d]\")|(\"\).*)", "", port)

                    if not bool(
                        re.search(r"[\d]{0,3}\.[\d]{0,3}\.[\d]{0,3}\.[\d]{0,3}", ip)
                    ):
                        try:
                            ip = base64.b64decode(ip).decode("utf-8")
                        except UnicodeDecodeError:

                            ip_raw = urllib.parse.unquote(ip)
                            ip = re.sub(r"<.*?>", ip_raw)

                    if not bool(re.search(r"[\d]{0,5}", port)):
                        try:
                            port = base64.b64decode(port).decode("utf-8")
                        except UnicodeDecodeError:

                            port_raw = urllib.parse.unquote(port)
                            port = re.sub(r"<.*?>", port_raw)

                if "write" in ip or "write" in port:
                    ip = re.sub(r"(.*\(\')|(\'\);)", "", ip)
                    port = re.sub(r"(.*\(\')|(\'\);)", "", port)
                proxy_list.append(f"{ip}:{port}")
        return proxy_list

    def __checker(self, proxy: str) -> bool:
        """
        Parameters
        ----------
        proxy : str
            Proxy that will be checked
        Return
        ------
        bool :
            It will return True/False whether the proxy is alive or not
        """
        request = urllib3.ProxyManager(f"http://{proxy}/")

        try:
            result = request.request("GET", "https://httpbin.org/get", timeout=1.5)
            return {"live": True, "proxy": proxy}
        except (urllib3.exceptions.ProxyError, urllib3.exceptions.MaxRetryError):
            return {"live": False, "proxy": proxy}

    def Proxies(self, quantity: int = 10):
        # -> list[str]:
        """
        Parameters
        ----------
        quantity : int, optional
            Determines the total of proxys to be returned.
            By default it returns 10.

        Return
        ------
        list[str] :
            List with every proxy scraped.
        """
        urls = [
            "https://hidemy.name/es/proxy-list/#list",
            # "https://www.proxynova.com/proxy-server-list",
            "https://spys.one/en/",
        ]

        html_content_list = self.__poolCreator(urls)

        proxies = list()
        for html in html_content_list:
            proxy_list = self.__scrape(html["html"], html["site"], quantity)
            proxies += proxy_list

        # Check proxies in parallel
        if self.check == True:
            liveProxies = list()
            with concurrent.futures.ThreadPoolExecutor() as executor:
                results = executor.map(self.__checker, proxies)
                for result in results:
                    if result["live"] == True:
                        liveProxies.append(result["proxy"])
                    print(result)
            proxies = liveProxies

        # Append the quantity of proxies that will be returned
        if quantity < len(proxies):
            shuffle(proxies)
            proxies = proxies[:quantity]
        return proxies
