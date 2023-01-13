Name: Aria Zhang

RavenRavenGo is a web crawler and a search engine, it will first crawl the website the you provide, crawling all the necessary data and then output the best 10 websites that are most related to your needs.


The project implements three modules in python: crawler.py, searchdata.py, and search.py, all the necessary data will be crawled in crawler module and it will be super fast to search data later on.


First, you should download the project codes and open it in python, and then provide the website address you want to crawl, besides, you need to tell us what kind of information you're searching for and whether you want your result of searching to be even more precise.


For example, the website you want to crawl is "http://people.scs.carleton.ca/~davidmckenney/fruits3/N-851.html" and the content you want to search is "I want to find what's the best for apple juice" and you put a "True" after the search sentence to state that you want the most precise result, then you should input:

seed =  "http://people.scs.carleton.ca/~davidmckenney/fruits4/N-851.html" 
phrase = "I want to find what's the best for apple juice" 
boost = "True"

And then you run this three module in python and you will get the result like:

[
{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-7.html', 'title': 'N-7', 'score': 0.9987742384869471}, 
{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-701.html', 'title': 'N-701', 'score': 0.9929174390182927}, 
{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-804.html', 'title': 'N-804', 'score': 0.9927182720503245}, 
{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-471.html', 'title': 'N-471', 'score': 0.9926890691297602}, 
{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-665.html', 'title': 'N-665', 'score': 0.992273451329603}, 
{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-400.html', 'title': 'N-400', 'score': 0.9922221546635857}, 
{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-896.html', 'title': 'N-896', 'score': 0.9899837610734362}, 
{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-755.html', 'title': 'N-755', 'score': 0.9894433428653931}, 
{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-590.html', 'title': 'N-590', 'score': 0.9890451220175763}, 
{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-448.html', 'title': 'N-448', 'score': 0.9887919006070602}
]
