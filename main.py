import urllib3
import re
import urllib
import concurrent.futures
import base64
from specific.spys_one import Deofuscator
from random import choice
import argparse

logo = '''
██╗   ██╗   ██████╗ ███████╗    █████╗  ██████╗ 
██║   ██║   ██╔══██╗██╔════╝██╗██╔══██╗██╔═████╗
██║   ██║   ██████╔╝███████╗╚═╝╚█████╔╝██║██╔██║
██║   ██║   ██╔═══╝ ╚════██║██╗██╔══██╗████╔╝██║
╚██████╔╝██╗██║██╗  ███████║╚═╝╚█████╔╝╚██████╔╝
 ╚═════╝ ╚═╝╚═╝╚═╝  ╚══════╝    ╚════╝  ╚═════╝ 
                                                
            Proxy
Universal           Scraper | Your ideal proxy scraper ;)
       by: @freshSauce
           0.1.5
'''


def __ArgsBuilder():
    """
    This function works as the builder of the args that 
    """
    parser = argparse.ArgumentParser(description='Command-line option for the Universal Scraper')

    parser.add_argument('-f', '--file', type=str, action='store', required=True,
                    help='name of the file with the sites')
    parser.add_argument('-o', '--output', action='store_true',
                    help='if used, stores the scraped proxies')
    parser.add_argument('-q', '--quantity', type=int, action='store', default=10,
                    help='if used, stores the scraped proxies')
    parser.add_argument('-v', '--verify', action='store_true',
                    help='if used, verify every single proxy and returns the live ones')
    parser.add_argument('-p', '--print', action='store_true',
                    help='if used, prints out the obtained list of proxies')

    args = vars(parser.parse_args())

    return args

class ProxyScraper:
    HTML = str

    def __init__(
                self, 
                file: str, 
                output: bool = None,
                check: bool = None
                ) -> None:

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

        self.file = file
        self.output = output
        self.check = check
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
        if self.output:
            proxies = [proxy + '\n' for proxy in proxy_list]
            with open('output.txt', 'w') as output:
               output.writelines(proxies) 
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
            Contains the HTML code obtained.
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
            return {'html': result.data.decode('utf-8'), 'site': url.strip()}

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

    def __scrape(self, html: HTML, site: str) -> list[str]:
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
        if 'spys' in site:
            pattern = r'<table.*width=\"65%\"[\w\W]*?<\/table>'
            table_body = re.search(pattern, html.strip()).group()

            pattern = r'<tr.*?<\/tr>'

            table_rows = list(re.finditer(pattern, table_body))

            proxy_list = list()

            script = re.search(r'eval.*', html).group() 
            pattern = r'\(\'[\w].+?\}\)'

            variables_raw = re.search(pattern, script).group() 

            variables = variables_raw.lstrip('(').rstrip(')').replace('\\u005e', '^').split(',')

            p, r, o, x, y, s = variables[0].replace("'", ''), variables[1], variables[2], variables[3], variables[4], variables[5]

            for row in table_rows[2:]:
                elements_raw = re.findall(r'<td.*?<\/td>', row.group())
                elements = [re.sub(r'<.*?>', '', element).strip() for element in elements_raw]

                ip_port_cleaned = re.sub(r'(\'&nbsp;)|(\)\')|', '', elements[0])

                ip_port_splited = re.split(r'document\.write\(\":\"\+', ip_port_cleaned)

                ip, port = ip_port_splited[0].replace('&nbsp;', ''), ip_port_splited[1]

                port = Deofuscator(p, r, o, x, y, s).deofuscator(port)

                proxy_list.append(f'{ip}:{port}')

            return proxy_list

        pattern = r'<tbody>.*<\/tbody>'
        try:
            table_body = re.search(pattern, html).group()
        except AttributeError:
            table_body = re.search(pattern, html.replace('\n', '')).group()

        pattern = r'<tr.*?<\/tr>'

        table_rows = list(re.finditer(pattern, table_body))

        proxy_list = list()

        for row in table_rows:
            elements_raw = re.findall(r'<td.*?<\/td>', row.group())
            elements = [re.sub(r'<.*?>', '', element).strip() for element in elements_raw]

            try:
                ip, port = elements[0], elements[1]

            except IndexError:
                continue

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

            if 'write' in ip or 'write' in port:
                ip = re.sub(r'(.*\(\')|(\'\);)', '', ip)
                port = re.sub(r'(.*\(\')|(\'\);)', '', port)
            proxy_list.append(f'{ip}:{port}')
        
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
        request = urllib3.ProxyManager(f'http://{proxy}/')

        try:
            result = request.request('GET', 'https://httpbin.org/get', timeout=1.5)
            return True
        except (urllib3.exceptions.ProxyError, urllib3.exceptions.MaxRetryError):
             return False

           


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

        proxies = list()
        for html in html_content_list:
            proxy_list = self.__scrape(html['html'], html['site'])
            proxies += proxy_list
            
        if quantity > len(proxies):
            if self.output == True:
                self.__saveFile(proxies)

            if self.check == True:
                proxies = list()
                for proxy in proxy_list:
                    if self.__checker(proxy):
                        proxies.append(proxy)

        else:
            _proxies = list()
            for _ in range(quantity):
                proxy = choice(proxies)
                if proxy not in _proxies:
                    _proxies.append(proxy)
            if self.output == True:
                self.__saveFile(_proxies)
            
            if self.check == True:
                proxies = list()
                for proxy in _proxies:
                    if self.__checker(proxy):
                        proxies.append(proxy)

            proxies = _proxies

        
        return proxies

if __name__ == '__main__':

    print(logo)
    args = __ArgsBuilder()

    while True:
        result = ProxyScraper(args['file'], args['output'], args['verify']).Proxies(args['quantity'])
        print('Proxies obtained !!!')
        
        if args['print']:
            print(result)
        while True:
            option = input('Everything is done !!! Wanna get more proxies? (Y[es]/N[o]): ').lower()

            if option == 'y' or option == 'yes':
                break
                    
            elif option == 'n' or option == 'no':
                exit('Have a nice day !!!')

            else:
                print('Please, use Y[es]/N[o] only !!!')
            