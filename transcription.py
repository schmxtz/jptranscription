from gruut import sentences
import pandas

mappings = {
    # Diphtongs
    'aʊ̯': '\u30A2\u30AA',

    # Vowels (Long Vowel)
    'ʏ': '\u30A4',
    'ə': '\u30A8',
    'aː': '\u30A2\u30FC',
    'ʊ': '\u30A6',

    # B+Vowel (Long Vowel)
    'bə': '\u30D9',
    'ba': '\u30D0',
    'biː': '\u30D3',
    'bʊ': '\u30D6',

    # D+Vowel (Long Vowel)
    'dɐ': '\u30C0\u30FC',
    'dɔɔ': '\u30C9',

    # F+Vowel
    'fa': '\u30D5\u30A1',
    'fɪ': '\u30D5\u30A3',
    'fe': '\u30D5\u30A7',
    'faːɐ': '\u30D5\u30A1\u30FC',
    'faʁ': '\u30D5\u30A1\u30FC',

    # G+Vowel
    'gə': '\u30B2',
    'gɛ': '\u30B2',

    # H+Vowel
    'ha': '\u30CF',
    'hoː': '\u30DB',
    'hʊ': '\u30D5',

    # J+Vowel
    'jaːɐ': '\u30E4\u30FC',
    'jaː': '\u30E4\u30FC',
    'jʊ': '\u30E6',

    # K+Vowel
    'ka': '\u30AB',
    'kɪ': '\u30AD',

    # L+Vowel (Long Vowel)
    'la': '\u30E9',
    'luː': '\u30EB\u30FC',
    'liː': '\u30EA\u30FC',

    # M+Vowel (Long Vowel)
    'mə': '\u30E1',
    'miː': '\u30DF',

    # P+Vowel
    'pa': '\u30D1',

    # R+Vowel (Long Vowel)
    'ʁiː': '\u30EA\u30FC',
    'ʁoː': '\u30ED\u30FC',
    'ʁuː': '\u30EB\u30FC',
    'ʁaː': '\u30E9\u30FC',
    'ʁaː': '\u30E9\u30FC',
    'ʁɔɔ': '\u30ED',

    # T+Vowel
    'tak': '\u30BF\u30FC\u30AF',
    'toː': '\u30C8',
    'tʏ': '\u30C8\u30A5',
    'tɛ': '\u30C6',

    # Consonants
    'n': '\u30F3',
    '̯n': '\u30F3',
    'ŋ': '\u30F3',
    'k': '\u30AF',
    'ŋk': '\u30F3\u30AF',
    '̯k': '\u30AF',
    't': '\u30C8',
    'ʁ': '\u30A2',  # R-sound
    'b': '\u30D6',
    'f': '\u30D5',
    's': '\u30B9',
    '̯s': '\u30B9',
    'l': '\u30EB',
    'm': '\u30E0',
    'ts': '\u30C4',

    # Full syllables (Need seperation because 'x' sounds depends on previous one)
    'buːx': '\u30D6\u30FC\u30D5',
    'fʁaʊ̯': '\u30D5\u30E9\u30AA',

    # Uncategorized (unsure what to call these)
    '̯t͡ʃ': '\u30C1\u30E5',
    'ŋɐ': '\u30F3\u30AC',
    'ŋə': '\u30F3\u30B2',
    'tsɔ': '\u30C4\u30A9',
    'tsə': '\u30C3\u30C4\u30A7',
    'ʁyː': '\u30EA\u30E5\u30FC',
    'ʃɛ': '\u30B7\u30A7',
}
MAX_IPA_SUBSTRING_LENGTH = len(max(mappings, key=len))



def convert_katakana(text):
    converted_words = []
    word_ipa = ''
    for sent in sentences(text, lang='de-de'):
        for word in sent:
            if word.phonemes:
                word_ipa = ''.join(word.phonemes)
                word_katakana = []
                start = 0
                while start < len(word_ipa):
                    modified = False
                    for i in range(min(len(word_ipa) - start, MAX_IPA_SUBSTRING_LENGTH), 0, -1):
                        if word_ipa[start:start + i] in mappings:
                            word_katakana.append(mappings[word_ipa[start:start + i]])
                            start += i
                            modified = True
                            break
                    if not modified:
                        print('Error converting {}'.format(word_ipa))
                        break
                converted_words.append(''.join(word_katakana))
    return converted_words, word_ipa


word_pairings = pandas.read_csv(filepath_or_buffer='words.csv')
for index, row in word_pairings.iterrows():
    converted_word, word_ipa = convert_katakana(row['german'])
    print(converted_word[0], word_ipa)
    if not converted_word or converted_word[0] != row['katakana']:
        print(word_ipa, converted_word[0], row['katakana'])
        break