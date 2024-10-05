from gruut import sentences

text = ('Abend Auto')

mappings = {
    'aʊ̯': '\u30A2\u30AA',
    'toː': '\u30C8',
    'aː': '\u30A2',
    'bə': '\u30D9',
    't': '\u30C8',
    'n': '\u30F3',
    'ba': '\u30D0',
    'ŋ': '\u30F3',
    'k': '\u30AF',
    'biː': '\u30D3',
    'ʁ': '\u30A2',
    'bluː': '\u30D6\u30EB\u30FC',
    'mə': '\u30E1'
}

def convert_katakana(text):
    for sent in sentences(text, lang="de-de"):
        for word in sent:
            if word.phonemes:
                word_ipa = "".join(word.phonemes)
                word_katakana = []
                start = 0
                while start < len(word_ipa):
                    for i in range(min(len(word_ipa)-start, 4), 0, -1):
                        if word_ipa[start:start+i] in mappings:
                            word_katakana.append(mappings[word_ipa[start:start+i]])
                            start += i
                            break
                print("".join(word_katakana))


for sent in sentences("Blume", lang="de-de"):
    for word in sent:
        if word.phonemes:
            print(word.phonemes)

convert_katakana("Blume")

