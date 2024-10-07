from gruut import sentences
import pandas

mappings = {
    # Diphtongs
    'aʊ̯': '\u30A2\u30A6',  # aʊ̯ -> アウ (sound "au" in "Auto")
    'ʁaʊ̯': '\u30E9\u30A6',  # ラウ

    # Vowels (Long Vowel)
    'ʏ': '\u30A4',  # イ
    'ə': '\u30A8',  # エ
    'aː': '\u30A2\u30FC',  # aː -> アー (sound "a" in "Abend")
    'ɐ': '\u30A2',  # ア
    'ʊ': '\u30A6',  # ウ

    # B+Vowel (Long Vowel)
    'bə': '\u30D9',  # ベ
    'ba': '\u30D0',  # バ
    'biː': '\u30D3',  # ビ
    'biːə': '\u30D3\u30FC',  # biːə -> ビー (sound "bie" in "Biene")
    'bʊ': '\u30D6',  # ブ

    # D+Vowel (Long Vowel)
    'dɐ': '\u30C0',  # dɐ -> ダ (sound "der" in "Bruder")
    'dɔɔ': '\u30C9',  # ド

    # F+Vowel
    'fa': '\u30D5\u30A1',  # ファ
    'fɪ': '\u30D5\u30A3',  # フィ
    'feː': '\u30D5\u30A7',  # フェ
    'faːɐ': '\u30D5\u30A1\u30FC',  # ファー
    'faʁ': '\u30D5\u30A1\u30FC',  # ファー

    # G+Vowel
    'gə': '\u30B2',  # ゲ
    'gɛ': '\u30B2',  # ゲ

    # H+Vowel
    'ha': '\u30CF',  # ハ
    'hoː': '\u30DB',  # ホ
    'hʊ': '\u30D5',  # フ

    # J+Vowel
    'jaːɐ': '\u30E4\u30FC',  # ヤー
    'jaː': '\u30E4\u30FC',  # ヤー
    'jʊ': '\u30E6',  # ユ

    # K+Vowel
    'ka': '\u30AB',  # カ
    'kɪ': '\u30AD',  # キ

    # L+Vowel (Long Vowel)
    'la': '\u30E9',  # ラ
    'luː': '\u30EB\u30FC',  # ルー
    'liː': '\u30EA\u30FC',  # リー
    'lə': '\u30EC',  # レ
    'lloː': '\u30C3\u30ED\u30FC',  # ッロー

    # M+Vowel (Long Vowel)
    'mə': '\u30E1',  # メ
    'mɛː': '\u30E1',  # メ
    'miː': '\u30DF',  # ミ
    'ma': '\u30DE',  # マ
    'moː': '\u30E2',  # モ
    'mɔ': '\u30E2',  # モ
    'muː': '\u30E0',  # ム
    'mʊ': '\u30E0',  # ム

    # N+Vowel
    'na': '\u30CA',  # ナ
    'naː': '\u30CA',  # ナ
    'nə': '\u30CD',  # ネ
    'nəə': '\u30CD\u30FC',  # ネー

    # P+Vowel
    'pa': '\u30D1',  # パ
    'piː': '\u30D4',  # ピ

    # R+Vowel (Long Vowel)
    'ʁiː': '\u30EA\u30FC',  # リー
    'ʁuː': '\u30EB\u30FC',  # ルー
    'ʁaː': '\u30E9\u30FC',  # ラー
    'ʁɔɔ': '\u30ED',  # ロ
    'ʁɔ': '\u30ED',  # ロ
    'ʁoː': '\u30ED\u30FC',  # ロー
    'ʁeː': '\u30EC\u30FC',  # レー

    # T+Vowel
    'tak': '\u30BF\u30FC\u30AF',  # ターク
    'tɐ': '\u30BF',  # タ
    'tat': '\u30BF\u30C3\u30C8',  # タット
    'toː': '\u30C8',  # ト
    'tʏ': '\u30C8\u30A5',  # ト
    'tɛ': '\u30C6',  # テ

    # V+Vowel
    'vɛ': '\u30F4\u30A7',  # ヴェ

    # Z+Vowel
    'zeː': '\u30BC\u30FC',  # ゼー
    'szə': '\u30C3\u30BC',  # ッゼ
    'zoː': '\u30BE\u30FC',  # ゾー
    'zɔ': '\u30BE',  # ゾ

    # Consonants
    'n': '\u30F3',  # ン
    '̯n': '\u30F3',  # ン
    'ŋ': '\u30F3',  # ン
    'nn': '\u30F3',  # ン
    'k': '\u30AF',  # ク
    'ŋk': '\u30F3\u30AF',  # ンク
    '̯k': '\u30AF',  # ク
    't': '\u30C8',  # ト
    'ʁ': '\u30A2',  # ア
    'b': '\u30D6',  # ブ
    'f': '\u30D5',  # フ
    's': '\u30B9',  # ス
    '̯s': '\u30B9',  # ス
    'l': '\u30EB',  # ル
    'm': '\u30E0',  # ム
    'ts': '\u30C4',  # ツ
    'p': '\u30D7',  # プ

    # Full syllables (Need seperation because 'x' sounds depends on previous one)
    'buːx': '\u30D6\u30FC\u30D5',  # ブーフ
    'naχ': '\u30CA\u30CF',  # ナハ
    'zɔnə': '\u30BE\u30F3\u30CD',  # ゾンネ

    # Uncategorized (unsure what to call these)
    '̯t͡ʃ': '\u30C1\u30E5',  # チュ
    'ʃ': '\u30B7\u30E5',  # シュ
    'ʃuː': '\u30B7\u30E5\u30FC',  # シュー
    'ŋɐ': '\u30F3\u30AC',  # ンガ
    'ŋə': '\u30F3\u30B2',  # ンゲ
    'tsɔ': '\u30C4\u30A9',  # ツォ
    'tsə': '\u30C3\u30C4\u30A7',  # ッツェ
    'ʁyː': '\u30EA\u30E5\u30FC',  # リュー
    'ʃɛ': '\u30B7\u30A7',  # シェ
    'çə': '\u30D2\u30A7',  # ヒェ
    'ziː': '\u30B8\u30FC'  # ジー
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
    converted_word, word_ip = convert_katakana(row['german'])
    print(converted_word[0], word_ip)
    if not converted_word or converted_word[0] != row['katakana']:
        print(word_ip, converted_word[0], row['katakana'])
        break
