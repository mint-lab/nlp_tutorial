import nltk
import torchtext # Install TorchText by 'conda install -c python torchtext' if necessary
                 # Install spaCy by 'conda install -c conda-forge spacy' and
                 #                  'python -m spacy download en_core_web_sm' if necessary

text = "This is Prof. Choi's lecture. His class doesn't start 9:00 A.M. but there are 1,000 examples,pratice,and homeworks."

tokenizers = [
    {'name': 'NLTK whitespace',  'tokenizer': nltk.tokenize.WhitespaceTokenizer().tokenize},
    {'name': 'NLTK recommended', 'tokenizer': nltk.tokenize.word_tokenize},
    {'name': 'TorchText-None',   'tokenizer': torchtext.data.utils.get_tokenizer(None)},
    {'name': 'TorchText-basic',  'tokenizer': torchtext.data.utils.get_tokenizer('basic_english')},
    {'name': 'TorchText-spacy',  'tokenizer': torchtext.data.utils.get_tokenizer('spacy')},
]

for ts in tokenizers:
    tokens = ts['tokenizer'](text)
    print('### ' + ts['name'])
    print(tokens)
