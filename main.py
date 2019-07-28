from tika import parser
from pre_process import *
import os
import glob
import gensim
current_dir = os.path.dirname(os.path.realpath(__file__))
os.environ['TIKA_PATH'] = current_dir
os.environ['TIKA_LOG_PATH'] = current_dir
DOCS_DIR = os.path.join(current_dir, 'docs')


def read_text_doc_file(path):
    parsed = parser.from_file(path)
    text = parsed['content']
    return text

docs_texts = []
files = [f for f in glob.glob(DOCS_DIR + "**/*.pdf")]
for f in files:
    docs_texts.append(read_text_doc_file(f))

processor = TextPreProcessor('portuguese')
docs_pre_processed = []
for text in docs_texts:
    text_pre_processed = processor.execute_pre_process(text)
    docs_pre_processed.append(text_pre_processed)

print(f'docs pre processed-> {len(docs_pre_processed)}')
dictionary = gensim.corpora.Dictionary(docs_pre_processed)
print(f'length words in dictionary=> {len(dictionary)}')
# -------OPTIONAL----------
dictionary.filter_extremes(no_below=3, no_above=0.8, keep_n=100000)
print(f'length words in dictionary after filter=> {len(dictionary)}')
bow_corpus = [dictionary.doc2bow(doc) for doc in docs_pre_processed]
bow_corpus_doc = bow_corpus[2]
for i in range(len(bow_corpus_doc)):
    print(f'Palavra {bow_corpus_doc[i][0]} '
          f'({dictionary[bow_corpus_doc[i][0]]}) '
          f' = {bow_corpus_doc[i][1]} ocorrências')

# LDA MODEL
lda_model = gensim.models.LdaMulticore(bow_corpus, num_topics=6, id2word=dictionary, passes=10, workers=2)
print(lda_model.get_topic_terms(0))
for idx, topic in lda_model.print_topics(-1):
    print(f'Tópico: {idx} \nPalavras: {topic}')
    print('\n')

lda_model.show_topic(0)