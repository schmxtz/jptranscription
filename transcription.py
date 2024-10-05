from gruut import sentences
import pandas

mappings = {
    # Diphtongs
    'aʊ̯': '\u30A2\u30AA',

    # Long Vowels
    'aː': '\u30A2',

    # B+Vowel (Long Vowel)
    'bə': '\u30D9',
    'ba': '\u30D0',
    'biː': '\u30D3',

    # D+Vowel
    'dɐ': '\u30C0\u30FC',

    # L+Vowel (Long Vowel)
    'luː': '\u30EB\u30FC',

    # M+Vowel (Long Vowel)
    'mə': '\u30E1',

    # R+Vowel (Long Vowel)
    'ʁiː': '\u30EA\u30FC',
    'ʁoː': '\u30ED\u30FC',
    'ʁuː': '\u30EB\u30FC',

    # T+Vowel
    'toː': '\u30C8',

    # Consonants
    'n': '\u30F3',
    'ŋ': '\u30F3',
    'k': '\u30AF',
    't': '\u30C8',
    'ʁ': '\u30A2',  # R-sound
    'b': '\u30D6',
    'f': '\u30D5',

    # Full syllables (Need seperation because 'x' sounds depends on previous one)
    'buːx': '\u30D6\u30FC\u30D5'

}


def convert_katakana(text):
    converted_words = []
    for sent in sentences(text, lang='de-de'):
        for word in sent:
            if word.phonemes:
                word_ipa = ''.join(word.phonemes)
                word_katakana = []
                start = 0
                while start < len(word_ipa):
                    modified = False
                    for i in range(min(len(word_ipa) - start, 4), 0, -1):
                        if word_ipa[start:start + i] in mappings:
                            word_katakana.append(mappings[word_ipa[start:start + i]])
                            start += i
                            modified = True
                            break
                    if not modified:
                        print('Error converting {}'.format(word_ipa))
                        break
                converted_words.append(''.join(word_katakana))
    return converted_words

word_pairings = pandas.read_csv('words.csv')