TWITTER_STOP_WORDS =set(['replies','retweeted','retweets','quote', 'reply', 'account',
                         'more', 'retweet', 'likes', 'search', 'twitter', 'uct',
                        'university', 'cape', 'town', 'tweets', 'https', 'http', 'like']) 

def general_clean(text, lst_to_remove):
    # remove punctuation, numbers
    text = text.replace("[^a-zA-Z#]", " ")
    text = re.sub("[^a-zA-Z#]", " ", text)
    text = re.sub(r'(\s)(\w+)?(#|_|@)\w+', r'\1', text)
    text = text.lower()

    # remove short words
    text = ' '.join([w for w in text.split() if len(w)>3])

    # remove lst_to_remove from the analysed text
    for w in lst_to_remove:
        text = text.replace(w,'')
    
    return text
