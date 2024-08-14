import re
import math
import numpy as np
from scipy.spatial import distance
from pyvi import ViTokenizer

docs = [
    'data mining is awesome. data mining helps to find frequent itemsets in database.',
    'information retrieval is cool. information retrieval helps to search data quickly.',
    'natural language processing is interesting. it helps computer to better understand text.'
]

query = 'information retrieval'

docs.append(query)

docs = [re.sub('\\W',' ', doc) for doc in docs]

doc_len = len(docs)

id_token_dict = {}
token_id_dict = {}
doc_id_token_ids_dict = {}
token_id_doc_id_term_freq_dict = {}
doc_id_token_id_term_freq_dict = {}
token_id_doc_ids_dict = {}
token_id = 0
for doc_idx, doc in enumerate(docs):
    tokens = doc.split(' ')
    doc_token_ids = []
    for token in tokens:
        if len(token) > 0:
            if token not in token_id_dict.keys():
                token_id_dict[token] = token_id
                id_token_dict[token_id] = token
                token_id+=1
            target_token_id = token_id_dict[token]
            if target_token_id not in token_id_doc_id_term_freq_dict.keys():
                token_id_doc_id_term_freq_dict[target_token_id] = {}
                token_id_doc_id_term_freq_dict[target_token_id][doc_idx] = 1
            else:
                if doc_idx not in token_id_doc_id_term_freq_dict[target_token_id].keys():
                    token_id_doc_id_term_freq_dict[target_token_id][doc_idx] = 1
                else:
                    token_id_doc_id_term_freq_dict[target_token_id][doc_idx] += 1
                    
            if doc_idx not in doc_id_token_id_term_freq_dict.keys():
                doc_id_token_id_term_freq_dict[doc_idx] ={}
                doc_id_token_id_term_freq_dict[doc_idx][target_token_id] = 1
            else:
                if target_token_id not in doc_id_token_id_term_freq_dict[doc_idx].keys():
                    doc_id_token_id_term_freq_dict[doc_idx][target_token_id] = 1
                else:
                    doc_id_token_id_term_freq_dict[doc_idx][target_token_id] += 1
            if target_token_id not in token_id_doc_ids_dict.keys():
                token_id_doc_ids_dict[target_token_id] = [doc_idx]
            else:
                if doc_idx not in token_id_doc_ids_dict[target_token_id]:
                    token_id_doc_ids_dict[target_token_id].append(doc_idx)
                    
            doc_token_ids.append(token_id_dict[token])
    doc_id_token_ids_dict[doc_idx] = doc_token_ids
vocab_size = len(id_token_dict.keys())
print('Kích thước tập từ vựng: [{}]'.format(vocab_size))
