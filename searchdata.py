import os
from crawler import get_num_from_url



def get_outgoing_links(URL):
    URL_name = str(get_num_from_url(URL))
    dir_name = os.path.join(os.path.dirname(__file__), "crawler_data", URL_name, "outgoing_links.txt")

    if os.path.isfile(dir_name):
        filein = open(dir_name, "r")
        outgoing_links = filein.read().split()
        filein.close()
    else:
        return None

    return outgoing_links


def get_incoming_links(URL):
    URL_name = str(get_num_from_url(URL))
    dir_name = os.path.join(os.path.dirname(__file__), "crawler_data", URL_name, "incoming_links.txt")

    if os.path.isfile(dir_name):
        filein = open(dir_name, "r")
        incoming_links = filein.read().split()
        filein.close()
    else:
        return None

    return incoming_links





def get_page_rank(URL):
    URL_name = get_num_from_url(URL)
    dir_name = os.path.join(os.path.dirname(__file__), "crawler_data", str(URL_name), "pagerank.txt") 
    if os.path.isfile(dir_name):
        filein = open(dir_name, "r")
        pagerank = float(filein.read())
        filein.close()
        return pagerank
    else:
        return -1

        


def get_idf(word):
    dir_name = os.path.join(os.path.dirname(__file__), "crawler_data","idf", word)
    
    if os.path.isfile(dir_name):
        filein = open(dir_name, "r")
        idf = float(filein.read())
        filein.close()
        return idf
    else:
        return 0



def get_tf(URL, word):
    URL_name = get_num_from_url(URL)
    dir_name = os.path.join(os.path.dirname(__file__), "crawler_data", str(URL_name), "tf", word)
    if os.path.isfile(dir_name):
        filein = open(dir_name, "r")
        tf = float(filein.read())
        filein.close()
        return tf
    else:
        return 0





def get_tf_idf(URL, word):
    URL_name = get_num_from_url(URL)
    dir_name = os.path.join(os.path.dirname(__file__), "crawler_data", str(URL_name), "tf_idf", word)
    if os.path.isfile(dir_name):
        filein = open(dir_name, "r")
        tf_idf = float(filein.read())
        filein.close()
        return tf_idf
    else:
        return 0



    
    
