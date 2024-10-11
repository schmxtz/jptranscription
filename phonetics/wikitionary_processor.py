import json, urllib.request

# For German dictionary
german_dict_link = 'https://kaikki.org/dictionary/downloads/de/de-extract.jsonl'
# https://kaikki.org/dictionary/downloads/de/de-extract.jsonl.gz compressed archive here
file_name = german_dict_link.split('/')[-1]
urllib.request.urlretrieve(german_dict_link, file_name)

# Write everything into python dictionary and dump it into json file at the end
output_file = open('lang-de.json', 'w')
output = {}

with (open(file=file_name, encoding=')UTF-8') as file):
    # It's jsonl file can be processed line by line (is too big to load into memory all at once anyway)
    while line := file.readline():
        json_obj = json.loads(line.rstrip())
        # Only need store German word with at least one IPA entry
        if json_obj.get('lang_code') == 'de' and \
                len(json_obj.get('sounds') or []) > 0 and \
                json_obj.get('sounds')[0].get('ipa'):
            # Since all words will be stored as lower case strings, some nouns and verbs might overlap
            # ("Fallen" vs. "fallen). To combat loss of information, ipa and word type are stored in arrays
            word = json_obj.get('word').lower()
            ipa = json_obj.get('sounds')[0].get('ipa')
            pos = json_obj.get('pos')
            if output.get(word):
                output[word]['ipa'].append(ipa)
                output[word]['pos'].append(pos)
            else:
                output[json_obj.get('word').lower()] = {'ipa': [ipa],
                                                        'pos': [pos]}

json.dump(output, output_file)

# Random example to check if it worked
output_file = open('phonetics/output.json')
output = json.load(output_file)
print(output['Weltschmerz'.lower()])
