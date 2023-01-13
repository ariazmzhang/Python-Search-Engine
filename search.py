import os
import math
import json
from searchdata import get_idf
from searchdata import get_tf_idf
from searchdata import get_page_rank




def search(phrase, boost):
    
    vector = {}
    vector_word ={}
    
    phrase = phrase.split(" ")
    phrase = [element.lower() for element in phrase]

    file_path_mapping = os.path.join(os.path.dirname(__file__), "crawler_data","mapping.txt")
    if os.path.isfile(file_path_mapping):
        filein = open(file_path_mapping, "r")
        file_list = filein.read()
        file_list = json.loads(file_list)
       
        for url in file_list:
            for i in range(len(phrase)):
                word = phrase[i].lower()
                tf_idf = get_tf_idf(url, word)
                vector_word[word] = tf_idf
                vector[url] = {}
                if url not in vector:
                    vector[url] = vector_word
                else:
                    vector[url].update(vector_word)

   
    query_vector = {}
    for i in range(len(phrase)):
        query = phrase[i].lower()

        tf_phrase = math.log2((list.count(phrase, query) / len(phrase)) + 1)
        idf_phrase = get_idf(str(query))
        tf_idf_phrase = tf_phrase * idf_phrase
        query_vector[query] = (tf_idf_phrase)
        

    for word in query_vector:
        for url in vector:
            if word not in vector[url]:
                vector[url][word] = 0
    
    

    cosine_similarity = {}
    numerator = {}
    right_denom = {}
    for url in vector:
        numerator[url] = 0
        right_denom[url] = 0

    for url in vector:
        for word in query_vector:
            numerator[url] += vector[url][word] * query_vector[word]
            right_denom[url] += vector[url][word]**2
           

    
    left_denom = 0
    for word in query_vector:
        left_denom += query_vector[word]**2

    for url in right_denom:
        if numerator[url] == 0:
            cosine_similarity[url] = 0
        elif numerator[url] != 0 and (boost == False):
            cosine_similarity[url] = numerator[url] / (math.sqrt(left_denom) * math.sqrt(right_denom[url]))
        elif numerator[url] != 0 and (boost == True):
            cosine_similarity[url] = (numerator[url] / (math.sqrt(left_denom) * math.sqrt(right_denom[url]))) * get_page_rank(url)

    cosine_similarity_sorted = {k: v for k, v in sorted(cosine_similarity.items(), key=lambda item: item[1], reverse=True)}

    result = []
    # while len(result) < 10:
    for url in cosine_similarity_sorted:
        result.append({'url': url, 'title':url.split("/")[-1].split(".")[0], 'score': cosine_similarity[url]})
 
  

    return result[0:10]


