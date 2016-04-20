from urllib.request import urlopen, urljoin
from bs4 import BeautifulSoup


class WebSpider(object):
    """ Spider to crawl through webs. """
    def __init__(self, seeds=[], log=True):
        self.seed = seeds  # Start point(s) for the crawler.
        self.visited = []  # Already visited URIs. We want to avoid cycles.
        self.unreachable = []  # Distinguish between processed and not.
        self.discovered = ()  # URIs discovered in this iteration.
        self.frontier = seeds  # Not yet visited URIs.
        self.depth = 1  # Recursion limit. As a default, 1 is a quite reasonable number.
        self.log = log

    def __getLinks(self, html, url):
        """ Extract Links from a Soup object. """
        soup = BeautifulSoup(html.read(), "html.parser")
        myset = set()
        for link in soup.find_all("a"):
            # Normalize the link
            myset.add(urljoin(url, link.get("href")).strip("/").split("#")[0])
        return myset

    def __sortDiscoveredLinks(self):
        """ Sort discovered tags between frontier and visited """
        new_links = [link for link in self.discovered if not link in self.visited]
        if self.log:
            with open("discovered.txt", "a+") as log_file:
                log_file.writelines("\n".join(new_links))
        self.frontier = new_links
        self.discovered = () # Flush

    def process(self, url, action):
        """
        Apply an action to the given url
        This acts as a handler.
        """
        try:
            action(url)
        except TypeError:
            pass

    def crawl(self, seeds=[], ttl=1, default_action=None):
        """ Recurse links """
        print("TTL: %s\n"%ttl)
        # If the spider is not seeded, seed it.
        # And update the value of frontier accordingly.
        self.seed.extend(seeds)
        self.frontier.extend(seeds)
        for url in self.frontier:
            print("Crawling ", url)
            try:
                html = urlopen(url)
                self.visited.append(url)
                self.process(url, default_action)
                self.discovered = self.__getLinks(html, url)
                self.__sortDiscoveredLinks()
            except ValueError:
                print("Malformed URL (", url, ")")
            except:
                print("Could not open ", url)
                self.unreachable.append(url)
        if ttl == 1:
            pass
        else:
            self.crawl(seeds=seeds, ttl=ttl-1, default_action=default_action)


if __name__ == "__main__":
    spider = WebSpider(["https://www.python.org"])
    spider.crawl(ttl=3)
