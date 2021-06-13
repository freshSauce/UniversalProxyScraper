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
[![GPL 3.0 License][license-shield]][license-url]
[![Telegram][telegram-shield]][telegram-url]



<!-- PROJECT LOGO -->
<br />

  <h3 align="center">Universal Proxy Scraper BETA v 0.0.3</h3>

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

Distributed under the GPL-3.0 License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Telegram: - [@freshSauce](https://t.me/freshSauce)

Project Link: [https://github.com/freshSauce/UniversalProxyScraper](https://github.com/freshSauce/UniversalProxyScraper)






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
