import pandas
import re

from transcription.katakanizer import Katakanizer

kata = Katakanizer('lang-de')
kata.init_katakanizer()

# for entry in kata.phonetics_transcriber.lookup_table:
#     ipa, t = kata.phonetics_transcriber.lookup_word(entry)
#     if ipa.startswith('\u0000' + 'xə'):
#     # if 'hʏ' in ipa:
#         print(entry, ipa)   

# Making sure old words don't break
word_pairings = pandas.read_csv(filepath_or_buffer='words.csv')
for index, row in word_pairings.iterrows():
    converted_word, word_ipa = kata.transcribe_word(row['german'])
    if converted_word != row['katakana']:
        print(row['german'], row['katakana'], converted_word, word_ipa)

# New sounds
# text = open('text.txt', encoding='utf-8').readline()

# words = text.split(' ')
# for word in words:
#     try:
#         converted_word, word_ipa = kata.transcribe_word(word)
#         print('{},{} {}'.format(word, converted_word, word_ipa))
#     except Exception as e:
#         print(word, e)
