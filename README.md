# WebSpider

 Simple - yet extensible - python module that can recursively crawl through
 websites.

## Contents:
1. Requirements
2. Installation
3. Using WebSpider


## 1. Requirements

This module is written in python3.5.1. It makes use of the module BeautifulSoup
for parsing HTML.
For the moment only the standard HTML parser bundled with BS is used.

## 2. Installation

I'm your daily python module. Just add me to your module folder, or extend the
environment variable PYTHONPATH with the folder containing the module.
Afterwards, just import me  whole or each class separately.

## 3. Using WebSpider

Make an instance of the object. It can be initialized just empty, or it can be
seeded with a list of websites.

```python
my_spider = WebSpider()
my_seeded_spider = WebSpider(["https://www.python.org"])
```

For the moment only two actions are available: "crawl" and "process"


**WebSpider.crawl(seeds=[], ttl=1, default_action=None)**

It starts crawling through the list of seeds the spider was initialized with (if
given). The list of seeds can be expanded passing a list to this function.
* `seeds`  -  Expands the list of seeds with this list.
* `ttl`  -  Time To Live, which is the number of steps the spider gives.
* `default_action`  -  What to do with the found elements. It must be a single
  string representing a callable (see WebSpider.process()) which only accepts
  a URL as parameter.
By default, it does nothing (eventually write some logs, but nothing else).
  
**WebSpider.process(url, action)**

Applies the action named `action` to the given URL. This is just intended as an
  action handler.
