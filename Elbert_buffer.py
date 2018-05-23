# More will be added

WHAT = 'what'
WHO = 'who'
HOW = 'how'
WHERE = 'where'
WHEN = 'when'
WHICH = 'which'
NAME = 'name'
WHY = 'why'
WHOM = 'whom'
BINARY = 'binary'
POLAR = 'polar'

HOW_SUBCLASS = {'many': [[], ['CD']], 
                'long': [['DURATION'], ['CD']], 
                'much': [['MONEY'], ['CD', 'FW', 'NN']], 
                'far': [[], ['CD']], 
                'tall': [[], ['CD']], 
                'rich': [['MONEY'], ['CD']], 
                'large': [[], ['CD']], 
                }

QUERY_CLASS = {WHAT: [[], ['NN']], 
               WHO: [['PERSON', 'ORGANIZATION'], ['NN']], 
               WHERE: [['LOCATION'], ['NN']],
               WHEN: [['DATE', 'TIME'], ['CD', 'NN']],
               WHICH: [['PERSON', 'LOCATION', 'DATE', 'TIME', 'ORGANIZATION'], ['NN']],
               NAME: [['PERSON', 'LOCATION', 'ORGANIZATION'], ['NN']],
               #'why': reason, find "reason word" 
               WHOM: [['PERSON', 'ORGANIZATION'], ['NN']], 
               
               # LOCATION, sometimes 'CD' also included as street number, unit number 
               # what if and not in query terms, then 
              
              }

def lemmatize_word(word):
    word = word.lower()
    lemma_n = lemmatizer.lemmatize(word,'n')
    lemma_v = lemmatizer.lemmatize(word,'v')
    
    # If both change, return the shorter one
    # If only one change, return the changed one
    # If neither change, return the original word
    
    if lemma_n != word and lemma_v != word:    
        if len(lemma_n) < len(lemma_v):
            return lemma_n
        else:
            return lemma_v
    elif lemma_n != word:
        return lemma_n
    elif lemma_v != word:
        return lemma_v
    else:
        return word

def extract_query(query):
    tokenized = nltk.word_tokenize(query)
    
    q_type = None
    
    if 'What' in tokenized or 'what' in tokenized:
        q_type = WHAT
                
    elif 'Who' in tokenized or 'who' in tokenized:
        q_type = WHO
        
    elif 'How' in tokenized or 'how' in tokenized:  
        # Since HOW queries have many answer types, furthrer analysis required
        how_index = 0
        
        if 'How' in tokenized:
            how_index = tokenized.index('How')
        else:
            how_index = tokenized.index('how')
            
        how_sub = tokenized[how_index + 1]
        
        if how_sub in HOW_SUBCLASS.values:
            tokenized.pop(how_index + 1)
            q_type = how_sub
        else:
            q_type = HOW

    elif 'Where' in tokenized or 'where' in tokenized:
        q_type = WHERE
     
    elif 'When' in tokenized or 'when' in tokenized:
        # Use SUTime
        q_type = WHEN
    
    elif 'Which' in tokenized or 'which' in tokenized:
        q_type = WHICH
        
    elif 'Why' in tokenized or 'why' in tokenized:
        q_type = WHY
    
    elif 'Whom' in tokenized or 'whom' in tokenized:
        q_type = WHOM
    
    elif 'Name' in tokenized:
        q_type = NAME
    else:
        if 'or' in tokenized:
            q_type = BINARY
        else:
            q_type = POLAR
        
    terms = []
    for token in tokenized:
        if token not in stopwords and token not in string.punctuation: 
            terms.append(lemmatize_word(token))
            
    return terms, q_type 