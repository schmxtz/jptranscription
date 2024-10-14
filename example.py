from transcription.katakanizer import Katakanizer
import pandas

kata = Katakanizer('lang-de')
kata.init_katakanizer()

# for entry in kata.phonetics_transcriber.lookup_table:
#     ipa = kata.phonetics_transcriber.lookup_word(entry)
#     # if ipa.startswith('\u0000' + 'ːən'):
#     if 'ːən' in ipa:
#         print(entry, ipa)

word_pairings = pandas.read_csv(filepath_or_buffer='words.csv')
for index, row in word_pairings.iterrows():
    converted_word, word_ipa = kata.transcribe_word(row['german'])
    print(converted_word, word_ipa, row['katakana'])
    if converted_word != row['katakana']:
        print('"""""""""""""""')
    # if row['german'] == 'gehen':
    #     converted_word, word_ipa = kata.transcribe_word(row['german'])
    #     print(converted_word, word_ipa, row['katakana'])
