from nltk.probability import FreqDist


class Analyzer:
    @staticmethod
    def get_frequency(tokens_pre_process):
        fdist = FreqDist(tokens_pre_process)
        return fdist.items()
