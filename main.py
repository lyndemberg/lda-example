from tika import parser
from pre_process import *
import os
current_dir = os.path.dirname(os.path.realpath(__file__))
os.environ['TIKA_PATH'] = current_dir
os.environ['TIKA_LOG_PATH'] = os.path.join(current_dir, 'tika-logs')


def read_doc_file(path):
    parsed = parser.from_file(path)
    text = parsed['content']
    return text


content = read_doc_file('text-data.pdf')
processor = TextPreProcessor()
text_pre_processed = processor.execute_pre_process(content)


