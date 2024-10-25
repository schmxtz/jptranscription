import pandas
import re
import csv

from transcription.katakanizer import Katakanizer

kata = Katakanizer('lang-de')

# for entry in kata.phonetics_transcriber.lookup_table:
#     ipa, t = kata.phonetics_transcriber.lookup_word(entry)
#     # if ipa.startswith('\u0000' + 'xə'):
#     if 'ml̩' in ipa and 'mm' not in entry:
#         print(entry, ipa)   

# Making sure old words don't break
word_pairings = pandas.read_csv(filepath_or_buffer='words.csv')
pairings = []
for index, row in word_pairings.iterrows():
    word = row['german'].lower()
    katakana = row['katakana']
    pair = {'german': word, 'katakana': katakana}
    if pair not in pairings:
        pairings.append(pair)
    converted_word, word_ipa = kata.transcribe_word(word)
    if converted_word != katakana:
        print(word, katakana, converted_word, word_ipa)

# Replace duplicates
with open('test/words.csv', 'w', encoding='UTF-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=['german', 'katakana'], lineterminator='\n')
    writer.writeheader()
    writer.writerows(pairings)

# New sounds
text = open('text.txt', encoding='utf-8').readline()

words = text.split(' ')
for word in words:
    try:
        word =  re.sub('[^A-Za-z0-9üäöß ]+', '', word.lower())
        if word:
            converted_word, word_ipa = kata.transcribe_word(word)
            print('{},{}'.format(word, converted_word))
    except Exception as e:
        print(word, e)