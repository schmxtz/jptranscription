import json
import re
import urllib.request
import os

# For German dictionary
file_name = 'de-extract.jsonl'
# Check if it hasn't been downloaded yet
if not os.path.isfile(file_name):
    german_dict_link = 'https://kaikki.org/dictionary/downloads/de/de-extract.jsonl'
    # https://kaikki.org/dictionary/downloads/de/de-extract.jsonl.gz compressed archive here
    file_name = german_dict_link.split('/')[-1]
    urllib.request.urlretrieve(german_dict_link, file_name)

# Write everything into python dictionary and dump it into json file at the end
output_file_name = 'lang-de.json'
output_file = open(output_file_name, 'w', encoding='UTF-8')
output = {}

# Exceptions (Dictionary contains words that break stuff e.g. "seine" is a normal posessive pronoun,
# But written as the start of a sentence it is "Seine", however the dictionary holds an entry as the 
# river "Seine" which is pronounced in French and that breaks everything.
word_types_to_ignore = ['phrase', 'abbrev', 'prefix', 'noun']
word_types_to_keep = ['adj', 'verb', 'pron', 'adv', 'num', 'unknown', 'noun']
word_types = {}
with (open(file=file_name, encoding='UTF-8') as file):
    # It's jsonl file can be processed line by line (is too big to load into memory all at once anyway)
    while line := file.readline():
        line = line.rstrip()
        json_obj = json.loads(line)

        # Only need store German word with at least one IPA entry
        if json_obj.get('lang_code') == 'de' and \
                len(json_obj.get('sounds') or []) > 0 and \
                json_obj.get('sounds')[0].get('ipa'):
            
            word = re.sub('[^A-Za-z0-9üäöß ]+', '', json_obj.get('word').lower())
            ipa = json_obj.get('sounds')[0].get('ipa')
            pos = json_obj.get('pos')

            word_types[pos] = word

            if not output.get(word) and ipa != '…' and ipa:
                output[word] = {'ipa': ipa,
                                'pos': pos,
                                'alternate_reading': [],
                                'original_word': json_obj.get('word'),
                                'size': len(line)}
            else:
                if ipa and ipa != '…' and 'name' not in (json_obj.get('pos')) and \
                    'outdated' not in (json_obj.get('senses')[0].get('tags') or []) and \
                    'name' not in (json_obj.get('other_pos') or []) and \
                    pos in word_types_to_keep and output[word]['pos'] in word_types_to_ignore:
                    output[word]['ipa'] = ipa
                    output[word]['pos'] = pos
                    output[word]['original_word'] = json_obj.get('word')
                    output[word]['size'] = len(line)                

print(output['bus'])
print(output['auto'])
print(output['alt'])
print(output['am'])
print(output['kaffee'])
print(output['sechs'])
print(output['seine'])

print(word_types)

json.dump(output, output_file)


