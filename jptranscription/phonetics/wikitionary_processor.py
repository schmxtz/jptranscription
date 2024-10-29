import json
import re
import urllib.request
import os
import spacy

# For German dictionary
file_name = 'de-extract.jsonl'
# Check if it hasn't been downloaded yet
if not os.path.isfile(file_name):
    german_dict_link = 'https://kaikki.org/dictionary/downloads/de/de-extract.jsonl'
    # https://kaikki.org/dictionary/downloads/de/de-extract.jsonl.gz compressed archive here
    file_name = german_dict_link.split('/')[-1]
    print('Downloading file')
    urllib.request.urlretrieve(german_dict_link, file_name)

IGNORE_TAGS = set(['Austrian German', 'outdated'])
IGNORE_RAW_TAGS = set(['umgangssprachlich,', 'umgangssprachlich'])

def get_ipa(x):
    sounds = x.get('sounds')
    if sounds:
        return sounds[0].get('ipa')

def get_word(x):
    return x.get('word')

def get_lang_code(x):
    return x.get('lang_code')

def get_example_sentences(x):
    senses = x.get('senses')
    if senses:
        examples = senses[0].get('examples')
        if examples:
            return [sentence.get('text') for sentence in examples]
        
def contains_tags_to_ignore(x):
    senses = x.get('senses')
    if senses:
        tags = set(senses[0].get('tags') or [])
        raw_tags = set(senses[0].get('raw_tags') or [])
        return len(tags & IGNORE_TAGS) > 0 or len(raw_tags & IGNORE_RAW_TAGS) > 0
        
def is_german(x):
    return get_lang_code(x) == 'de'

def contains_ipa_entry(x):
    ipa = get_ipa(x)
    return ipa and ipa != '…'

def might_be_foreign_word(x):
    translations = x.get('translations')
    word = x.get('word').lower()
    if translations:
        for translation in translations:
            if word == translation.get('word'):
                return True
    return False

def debug_print(i, total):
    percent = int(i / num_lines * 100)
    print('[' + 'X'* (percent//4) + '_'* ((100-percent)//4) + ']' + f' {i}/{total} entries analyzed')


file_name = 'de-extract.jsonl'
# Line count for 
with open(file_name, 'rb') as f:
    num_lines = sum(1 for _ in f)

output = {}
print('Starting analysis')
with open(file=file_name, encoding='UTF-8') as file:
    i = 0
    while line := file.readline():
        line = line.rstrip()
        json_obj = json.loads(line)

        word = get_word(json_obj)
        if word and is_german(json_obj) and contains_ipa_entry(json_obj):
            """
            This part is unsure, in the list, the most relevant entry comes first

            if output.get(word) and not contains_tags_to_ignore(json_obj):
                if output[word] != get_ipa(json_obj) and not might_be_foreign_word(json_obj):
                    print(f'word: {word}, old_ipa: {output[word]}, new_word: {get_ipa(json_obj)}')
                    output[word] = get_ipa(json_obj)
            """
            if output.get(word):
                pass
            else:
                output[word] = get_ipa(json_obj)
        i += 1
        if  i % (num_lines//25) == 0:
            debug_print(i, num_lines)

# Dump file
json.dump(output, open('lang-de.json', 'w', encoding='UTF-8'))
