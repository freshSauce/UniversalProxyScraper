<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![AGPL 3.0 License][license-shield]][license-url]
[![Telegram][telegram-shield]][telegram-url]



<!-- PROJECT LOGO -->
<br />

  <h3 align="center">Universal Proxy Scraper BETA v 0.1.5</h3>

  <p align="center">
    Need some proxys but don't want to scrap them manually?, just give this script the domain!
    <br />
    <a href="https://github.com/freshSauce/UniversalProxyScraper"><strong>Give the project a star!</strong></a>
    <br />
    <br />
    <a href="https://github.com/freshSauce/UniversalProxyScraper/issues">Report Bug</a>
    ·
    <a href="https://github.com/freshSauce/UniversalProxyScraper/issues">Request Feature</a>
  </p>


<!-- ABOUT THE PROJECT -->
## About The Project

### Example of the code imported as module
[![Module][example-script]](https://github.com/freshSauce/UniversalProxyScraper/)

### Output
[![Output][example-output]](https://github.com/freshSauce/UniversalProxyScraper/)

Hi there! The purpose of this script is to demonstrate the power and the functions that will be implemented in the future module of Universal Proxy Scraper, at first, this will be developed until the v 1.0.0 came out, that version will be the first version deployed as module :)

### Modules used

* [urllib3](https://urllib3.readthedocs.io/)
* [re](https://docs.python.org/3/library/re.html)

Just built-in modules! (Python >= 3.0)

<!-- GETTING STARTED -->
## Getting Started

Let's get to it! 

### Script usage

#### Setting up the list

To set-up the websites you wanna get the proxies from you have to place every single URL you wanna scrape into a list, just as:

```
http://free-proxy.cz/es/
https://free-proxy-list.net/
http://www.freeproxylists.net/
https://hidemy.name/es/proxy-list/#list
```

(For a better reference see the test_urls.txt that is in this same repository).

### Using via command-line

The usage of command line is pretty simple :D Ex.
```
path/to/the/script: python main.py -h


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

usage: main.py [-h] -f FILE [-o] [-q QUANTITY] [-v] [-p]

Command-line option for the Universal Scraper

optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  name of the file with the sites
  -o, --output          if used, stores the scraped proxies
  -q QUANTITY, --quantity QUANTITY
                        if used, stores the scraped proxies
  -v, --verify          if used, verify every single proxy and returns the live ones
  -p, --print           if used, prints out the obtained list of proxies


```

As you may see, there's a lot of options you can use :)

* file (required, value needed) : path or name of the file that contains all the webistes you want to scrape.
* output (optional, no value needed) : if used, writes a file named "output.txt" with every single scraped proxy. 
* quantity (optional, value needed, 10 by default) : it declares the quantity of proxies to be scraped.
* verify (optional, no value needed) : if used, verifys every single proxy scraped, and returns the list with those that are alive.
* print (optional, no value needed) : if used, prints out the list that contains all the proxies.

##### Example with every single argument

```
path/to/the/script: python main.py -f test_urls.txt -p -o -v -q 5

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

Connection to http://free-proxy.cz/es/ timed out
Proxies obtained !!!
['172.67.181.214:80', '172.67.80.190:80', '45.82.139.34:4443', '188.168.56.82:55443', '150.129.54.111:6667']
Everything is done !!! Wanna get more proxies? (Y[es]/N[o]): n
Have a nice day !!!
```

#### Setting up our code

In order to make it work with our own code we have to import it as module, just like:
```python

from main import ProxyScraper

```
There's no need to import it as 'main', you can change the script's name and import it with the name you gave to the script.
Now, once you done that you can use it as you please.

```python

# Storing it on a variable
proxy_scraper = ProxyScraper('test_urls.txt')

proxy_list = proxy_scraper.Proxies()

# Iterating through each proxy

for proxy in ProxyScraper('test_urls.txt').Proxies()
    ...

# Saving the proxies to a file

proxy_scraper = ProxyScraper('test_urls.txt', output=True)

proxy_list = proxy_scraper.Proxies() # This will give you the scraped proxies and save them into a file.

```



<!-- USAGE EXAMPLES -->
## Usage

It's pretty easy-to-use! just make sure to pass the URLs correctly and you're ready to go!
```python
from main import ProxyScraper

proxy_list = ProxyScraper('test_urls.txt').Proxies() # Will save the proxies list on a variable

ProxyScraper('test_urls.txt', output=True).Proxies() # Will save the output into an output file

proxy_list = ProxyScraper('test_urls.txt').Proxies(quantity=15) # Will save 15 of the scraped proxies into a variable (10 by default)

proxy_list = ProxyScraper('test_urls.txt', check=True).Proxies(quantity=15) # Will save 15 of the scraped proxies and will check each one of them
```

Hope it is useful for you!

<!-- CONTRIBUTING -->
## Contributing

Wanna contribute to the project? Great! Please follow the next steps in order to submit any feature or bug-fix :) You can also send me your ideas to my [Telegram](https://t.me/freshSauce), any submit is **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the AGPL-3.0 License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Telegram: - [@freshSauce](https://t.me/freshSauce)

Project Link: [https://github.com/freshSauce/UniversalProxyScraper](https://github.com/freshSauce/UniversalProxyScraper)

<!-- CHANGELOG -->

### Changelog

#### 0.1.5
* Added command-line support (yeah, no 0.1.3 nor 0.1.4, heh)

#### 0.1.2
* Added support to the first specific site: spys.one.

Now, I want to say that, if needed, I will create specific scripts for specific sites, this doesn't mean that I won't keep looking for an 'universal' solution, is just that sites like that one are pretty much different from the others.

[Module](https://github.com/freshSauce/UniversalProxyScraper/blob/d4e274b185e5710492439622e57041dd76d41b21/specific/spys_one.py) created for that site.

#### 0.1.1
* Added support to some sites with JS-based write, such as: 'document.write'.
* Added handlers for some exceptions.

#### 0.1.0
* Added proxy checker [function](https://github.com/freshSauce/UniversalProxyScraper/blob/637c16177f49128fde203a2a066453cb778a93b7/main.py#L192)
* Fixed some typos on the script documentation.






<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/freshSauce/UniversalProxyScraper.svg?style=for-the-badge
[contributors-url]: https://github.com/freshSauce/UniversalProxyScraper/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/freshSauce/UniversalProxyScraper.svg?style=for-the-badge
[forks-url]: https://github.com/freshSauce/UniversalProxyScraper/network/members
[stars-shield]: https://img.shields.io/github/stars/freshSauce/UniversalProxyScraper.svg?style=for-the-badge
[stars-url]: https://github.com/freshSauce/UniversalProxyScraper/stargazers
[issues-shield]: https://img.shields.io/github/issues/freshSauce/UniversalProxyScraper.svg?style=for-the-badge
[issues-url]: https://github.com/freshSauce/UniversalProxyScraper/issues
[license-shield]: https://img.shields.io/github/license/freshSauce/UniversalProxyScraper.svg?style=for-the-badge
[license-url]: https://github.com/freshSauce/UniversalProxyScraper/blob/master/LICENSE.txt
[telegram-shield]: https://img.shields.io/badge/-@freshSauce-black?style=for-the-badge&logo=telegram&colorB=0af
[telegram-url]: https://t.me/freshSauce
[example-script]: images/example_script.png
[example-output]: images/example_output.png
