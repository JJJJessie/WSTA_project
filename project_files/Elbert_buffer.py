# coding: utf-8
from nltk.tag import StanfordNERTagger
from nltk.tag.stanford import StanfordPOSTagger

# def get_ans(sent, tag):
#     for item in sent:
#         print item
#         if item[1] == tag:
#             ans = item[0]
#             return ans
#     return ''

# NERTagger

ner_dir = '/Users/yifan/Desktop/stanford-ner-2018-02-27/'
ner_jarfile = ner_dir + 'stanford-ner.jar'
ner_modelfile = ner_dir + 'classifiers/english.all.3class.distsim.crf.ser.gz'
ner_tagger = StanfordNERTagger(model_filename=ner_modelfile, path_to_jar=ner_jarfile)

pos_dir = '/Users/yifan/Desktop/stanford-postagger-2018-02-27/'
pos_modelfile = pos_dir + 'models/english-bidirectional-distsim.tagger'
pos_jarfile = pos_dir + 'stanford-postagger.jar'
pos_tagger = StanfordPOSTagger(model_filename=pos_modelfile, path_to_jar=pos_jarfile)

sents = []
# sents.append("Rami Eid is studying at Stony Brook University in NY")
# sents.append("Elbert lives in Melbourne.")
# sents.append("Banana is $6 per kilo this Monday in Sydney.")
# sents.append("Elbert lives 100 kilometers away from Melbourne.")
# sents.append("Elbert is enrolled in University of Melbourne .")
# sents.append("Elbert in Melbourne.")
# sents.append("Elbert's address is Unit 1004 50 Albert Road South Melbourne 3205.")
# sents.append("The price of a bottle of water is $1")
# sents.append("The event will be on Sunday.")
# sents.append("The event will be on 1pm.")
# sents.append("Elbert will submit the assignment by email.")
# sents.append("Elbert will submit the assignment by email tomorrow.")
# sents.append("Elbert will submit the assignment tomorrow.")
# sents.append("The dog is amazing.")
# sents.append("The price is $244 billion")
sents.append("The envent is cancelled due to raining.")
# sents.append("Albert is studying in University of Melbourne.") 
# sents.append("Is it true or false that an apple is red?") 
# sents.append("Jackson is taken care of by Jessie.") 



for sent in sents:
    
    print sent
    
    print ner_tagger.tag(sent.split())
    
    print pos_tagger.tag(sent.split())
    
    print('\n\n')

# q1 = 'Who lives in Melbourne?'
# q2 = 'Where does Albert lives?'
# 
# for q in [q1, q2]:
#     if q.split()[0] == 'Who':
#         print 'PERSON'
#         print get_ans(tagged_sent, 'PERSON')
#     elif q.split()[0] == 'Where':
#         print 'LOCATION'
#         print get_ans(tagged_sent, 'LOCATION')