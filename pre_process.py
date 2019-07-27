import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.stem import SnowballStemmer

nltk.download('wordnet')
nltk.download('stopwords')


class TextPreProcessor:

    def __init__(self, language):
        self.language = language
        self.stop_words = stopwords.words(language)
        self.stemmer = SnowballStemmer(language)

    def __remove_stop_words(self, tokens):
        stopwords_removed = []
        for w in tokens:
            if w.lower() not in self.stop_words:
                stopwords_removed.append(w)
        return stopwords_removed

    def __tokenize_text_content(self, content):
        return nltk.word_tokenize(content, language=self.language)

    def __remove_pontuaction(self, tokens):
        tokens_without_pontuaction = []
        for w in tokens:
            if w.isalpha():
                tokens_without_pontuaction.append(w)
        return tokens_without_pontuaction

    def __lematize_text(self, tokens):
        lemmatized = []
        for w in tokens:
            stem = self.stemmer.stem(WordNetLemmatizer().lemmatize(w, pos='v'))
            lemmatized.append(stem)
        return lemmatized

    def execute_pre_process(self, content):
        tokenize = self.__tokenize_text_content(content)
        without_pontuation = self.__remove_pontuaction(tokenize)
        without_stop_words = self.__remove_stop_words(without_pontuation)
        lemmatized = self.__lematize_text(without_stop_words)
        return lemmatized
