from transcription.katakanizer import Katakanizer
import pandas

kata = Katakanizer('lang-de')
kata.init_katakanizer()

word_pairings = pandas.read_csv(filepath_or_buffer='words.csv')
for index, row in word_pairings.iterrows():
    converted_word, word_ipa = kata.transcribe_word(row['german'])
    print(converted_word, word_ipa, row['katakana'])
