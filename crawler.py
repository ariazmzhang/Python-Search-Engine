import webdev
import os
import math
import json
from matmult import mult_matrix
from matmult import euclidean_dist
from binarycount import count


def delete_directory(dir_name):
    
    if os.path.isfile(dir_name):
        os.remove(dir_name)
    elif os.path.isdir(dir_name):
        for the_file in os.listdir(dir_name):
            delete_directory(os.path.join(dir_name, the_file))
        os.rmdir(dir_name)



def create_file(dir_name, file_name, contents):
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
    file_path = os.path.join(dir_name, file_name)

    if not os.path.exists(file_path):
        fileout = open(file_path, "w")  
        fileout.write(contents)
        fileout.close()
    else:
        fileout = open(file_path, "a")  
        fileout.write("\n" + contents)




def find_url(page_line):
    url_start = page_line.find('<a href="') + len('<a href="') + 2
    url_end = page_line.find('">')
    url = page_line[url_start:url_end]
    url_name = url.split('/')[-1]
    return url_name




def find_body(page_content):
    body_start = page_content.find('<p>') + len('<p>')
    body_end = page_content.find('</p>')
    body = page_content[body_start:body_end]
    return body



def get_num_from_url(url):
    if url in mapping_dic:
        number = mapping_dic[url]
        return number
    else:
        return -1



def get_url_from_num(num):
    if num < len(mapping_list):
        url = mapping_dic[mapping_list[num]]
        return url
    else:
        return -1



def get_mapping():
    dir_name = os.path.join(os.path.dirname(__file__), "crawler_data")
    create_file(dir_name, "mapping.txt", json.dumps(mapping_dic))




def get_page_rank():
    length = len(mapping_dic)
    adjacency_matrix = [[0 for j in range(length)] for i in range(length)]
    number = [0 for j in range(length)]
    
    # Initial transition probability matrix (dividing rows by # of 1s)
    for i in range(length):
        for j in range(length):
            dir_name = os.path.join(os.path.dirname(__file__), "crawler_data", str(j), "outgoing_links.txt")
            filein = open(dir_name, "r")
            outgoing_links = filein.read().split()
            filein.close()
            if (mapping_list[i]) in outgoing_links:
                adjacency_matrix[i][j] = 1
            else:
                adjacency_matrix[i][j] = 0
            number[i] += adjacency_matrix[i][j]
    
    for i in range(length):
        for j in range(length):
            if number[i] != 0:
                adjacency_matrix[i][j] /= (number[i]/0.9)
            adjacency_matrix[i][j] += 0.1/length

    t0 = [[1/length for j in range(length)] for i in range(1)]
    t1 = mult_matrix(t0, adjacency_matrix)

    euc = euclidean_dist(t0, t1)

    while euc > 0.0001:
        t0 = t1
        t1 = mult_matrix(t0, adjacency_matrix)
        euc = euclidean_dist(t0, t1)

    for i in range(len(t1[0])):
        pagerank = t1[0][i]
        dir_name = os.path.join(os.path.dirname(__file__), "crawler_data", str(i)) 
        create_file(dir_name, "pagerank.txt", str(pagerank))




def term_frequency():
    dir_name = os.path.join(os.path.dirname(__file__), "crawler_data")
    
    for url in mapping_list:
        
        num = get_num_from_url(url)
        dir_name_page = os.path.join(dir_name, str(num), "tf")
        file_path = os.path.join(dir_name, str(num), "body.txt")
        filein = open(file_path, "r")
        body_contents = filein.read().split()
        body_contents.sort()
        filein.close()
        
        for word in unique_word:
            tf_dic_word = count(body_contents, word)/len(body_contents)
            create_file(dir_name_page, word, str(tf_dic_word))
        
                
    

def calculate_idf():
    
    count_doc = len(mapping_list)
    dir_name = os.path.join(os.path.dirname(__file__), "crawler_data")
    dir_name_idf = os.path.join(os.path.dirname(__file__), "crawler_data", "idf")

    for i in range(len(unique_word)):
        freq_idf = 0
        for filename in os.listdir(dir_name):
            file_path = os.path.join(dir_name, filename, "body.txt") 
            if os.path.isfile(file_path):
                filein = open(file_path, "r")
                body_contents = filein.read()
                filein.close()
                if unique_word[i] in body_contents:
                    freq_idf += 1

        idf = math.log2(count_doc / (freq_idf + 1))

        create_file(dir_name_idf, unique_word[i], str(idf))

    


def calculate_tf_idf():
    dir_name = os.path.join(os.path.dirname(__file__), "crawler_data")

    for url in mapping_list:
        file_name = get_num_from_url(url)

        for word in unique_word:
            dir_name_page = os.path.join(dir_name, str(file_name), "tf_idf")

            file_path_tf = os.path.join(dir_name, str(file_name), "tf", word)
            if os.path.isfile(file_path_tf):
                filein_tf = open(file_path_tf, "r")
                tf = float(filein_tf.read())
                filein_tf.close()
            else:
                tf = 0

            file_path_idf = os.path.join(dir_name,"idf", word)
            if os.path.isfile(file_path_idf):
                filein_idf = open(file_path_idf, "r")
                idf = float(filein_idf.read())
                filein_idf.close()
            else:
                idf = 0
            
            tfidf =  (math.log2(1+tf))*idf

            create_file(dir_name_page, word, str(tfidf))


    




def crawl(seed):
    dir_name = os.path.join(os.path.dirname(__file__), "crawler_data") 
    
    delete_directory(dir_name)

    global mapping_dic
    global mapping_list
    global unique_word

    count = 0

    url_queue = []
    mapping_dic = {}
    mapping_list = []
    unique_word = []

    url_queue.append(seed) 
    mapping_dic[seed] = len(mapping_list)
    mapping_list.append(seed)

    
    
    while len(url_queue) > 0:
        count += 1
        page_content = webdev.read_url(url_queue[0])

        dir_name_title = os.path.join(dir_name, str(mapping_dic[url_queue[0]]))
        body = find_body(page_content)
        create_file(dir_name_title, "body.txt", body)
        body_contents = body.split()
        for i in range(len(body_contents)):
            if body_contents[i] not in unique_word:
                unique_word.append(body_contents[i])
                # create_file(dir_name, "uniquewords.txt", body_contents[i])
       
        seed_split = seed.split("/")
        page_list = page_content.split("\n")
        for i in range(len(page_list)):
            page_line = page_list[i]
            if 'a href=".' in page_line:
                url_name = find_url(page_line)
                url_link = seed[0: (-len(seed_split[len(seed_split)-1]))] + url_name
                
                create_file(dir_name_title, "outgoing_links.txt", url_link)
               
                if url_link not in mapping_dic:
                    mapping_dic[url_link] = len(mapping_list)
                    mapping_list.append(url_link)
                    url_queue.append(url_link)
                dir_name_incoming = os.path.join(dir_name, str(mapping_dic[url_link]))
                create_file(dir_name_incoming, "incoming_links.txt", url_queue[0])
        
        url_queue.pop(0)
    
    get_mapping()
    get_page_rank()
    term_frequency()
    calculate_idf()
    calculate_tf_idf()
    
    
        

    return count		       