import urllib3
import re

class ProxyScraper:

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
            on a file
        """

        self.file = file
        self.output = output

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
                f'An error ocurred while trying to open file {self.file},',
                'please, make sure you typed correctly your file\'s name'
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

        result = request.request('GET', url)

        if result.status == 200:
            return result.data

        else:
            return False



    def Scrape(
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

        
    
