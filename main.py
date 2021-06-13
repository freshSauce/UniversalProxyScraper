import urllib3
import re
import urllib
import concurrent.futures
import base64

class ProxyScraper:
    HTML = str

    def __init__(
                self, 
                file: str, 
                output: str = None
                ) -> None:

        """
        Parameters
        ----------
        file : str
            The name of the file with the sites
        output : str, optional
            In case that the user needs the output he can store it
            on a filem, in format: <file_name>.txt
        """

        self.file = file
        self.output = output
        self.headers = {
                        'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.5 (KHTML, like Gecko) Chrome/4.0.249.0 Safari/532.5'
                        }

    def __openFile(self) -> list[str]:
        """
        Return
        ------
        list[str] : 
            List with every site on the file.
            In case the file doesn't exists, an exception is raised.
        """
        try:
            with open(self.file, 'r') as sites:
                return sites.readlines()

        except FileNotFoundError:
            exit(
                f'An error ocurred while trying to open file {self.file}, please, make sure you typed correctly your file\'s name'
                )
            


    def __saveFile(
                    self, 
                    proxy_list: list
                    ) -> None:
        """
        Parameters
        -----------
        proxy_list : list
            List with every proxy scraped

        Return
        ------
        None
        """
        if self.output != None:
            with open('output.txt', 'w') as output:
               output.writelines(proxy_list) 
        else:
            pass
    
    def __doRequest(
                    self, 
                    url: str
                    )-> str: 
        """
        Parameters
        ----------
        url : str
            URL to be scraped
        
        Return
        -------
        str :
            Constains all the data collected by the scrape.
        """

        request = urllib3.PoolManager()
        
        try:
            result = request.request(
                                        'GET', 
                                        url, 
                                        timeout=1.5,
                                        headers=self.headers
                                    )

        except urllib3.exceptions.MaxRetryError:
            print(f'Connection to {url.strip()} timed out ')
            return False

        if result.status == 200:
            return result.data.decode('utf-8')

        else:
            return False

    def __poolCreator(
                        self, 
                        urls: list[str]
                    ) -> list[str]:
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

    def __scrape(self, html: HTML) -> list[str]:
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

        pattern = r'<tbody>.*<\/tbody>'

        table_body = re.search(pattern, html).group()
        

        pattern = r'<tr>.*?<\/tr>'

        table_rows = list(re.finditer(pattern, table_body))

        proxy_list = list()

        for row in table_rows:
            elements_raw = re.findall(r'<td.*?<\/td>', row.group())
            elements = [re.sub(r'<.*?>', '', element) for element in elements_raw]

            ip, port = elements[0], elements[1]

            if 'decode' in ip or 'decode' in port:
                ip = re.sub(r'(.*[^=\w\d]\")|(\"\).*)', '', ip)
                port = re.sub(r'(.*[^=\w\d]\")|(\"\).*)', '', port)

                if not bool(re.search(r'[\d]{0,3}\.[\d]{0,3}\.[\d]{0,3}\.[\d]{0,3}', ip)):
                    try:
                        ip = base64.b64decode(ip).decode('utf-8')
                    except UnicodeDecodeError:

                        ip_raw = urllib.parse.unquote(ip)
                        ip = re.sub(r'<.*?>', ip_raw)

                if not bool(re.search(r'[\d]{0,5}', port)):
                    try:
                     port = base64.b64decode(port).decode('utf-8')
                    except UnicodeDecodeError:

                        port_raw = urllib.parse.unquote(port)
                        port = re.sub(r'<.*?>', port_raw)
                
            proxy_list.append(f'{ip}:{port}')
        
        return proxy_list


    def Proxies(
                self, 
                quantity: int = 10
                ) -> list[str]:
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
        urls = self.__openFile()

        if not urls:
            exit(f'File {self.file} is empty.')

        html_content_list = self.__poolCreator(urls)

        proxy_list = list()
        for html in html_content_list:
            proxies = self.__scrape(html)
            proxy_list += proxies
        
        if quantity > len(proxy_list):
            return proxy_list
        else:
            return proxy_list[0:quantity]


if __name__ == '__main__':
    ProxyScraper('test_urls.txt').Proxies()