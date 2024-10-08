from gruut import sentences
import pandas

mappings = {
    # Diphtongs
    'aʊ̯': '\u30A2\u30A6',  # aʊ̯ -> アウ (sound "au" in "Auto")
    'ʁaʊ̯': '\u30E9\u30A6',  # ʁaʊ -> ラウ (sound "rau" in "Frau")

    # Vowels (Long Vowel)
    'ʏ': '\u30A4',  # イ
    'ə': '\u30A8',  # エ
    'a': '\u30A2',  # a -> ア (sound "a" in "alt")
    'ɐ': '\u30A2',  # ア
    'aː': '\u30A2\u30FC',  # aː -> アー (sound "a" in "Abend")
    'ʊ': '\u30A6',  # ウ
    'uː': '\u30A6',  # ウ
    'ʔuː': '\u30A6',  # ウ

    # B+Vowel (Long Vowel)
    'bə': '\u30D9',  # ベ
    'ba': '\u30D0',  # バ
    'biː': '\u30D3',  # ビ
    'biːə': '\u30D3\u30FC',  # biːə -> ビー (sound "bie" in "Biene")
    'bʊ': '\u30D6',  # ブ

    # D+Vowel (Long Vowel)
    'dɐ': '\u30C0',  # dɐ -> ダ (sound "der" in "Bruder")
    'dɔ': '\u30C9',  # ド
    'dɔɔ': '\u30C9',  # ド
    'dɛ': '\u30C7',  # デ
    'də': '\u30C7',  # デ

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
    'hoː': '\u30DB\u30FC',  # hoː -> ホー (sound "ho" in "Hotel")
    'hʊ': '\u30D5',  # フ

    # J+Vowel
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
    'mɛː': '\u30E1\u30FC',  # メー
    'miː': '\u30DF',  # ミ
    'ma': '\u30DE',  # マ
    'moː': '\u30E2',  # モ
    'mɔ': '\u30E2',  # モ
    'muː': '\u30E0',  # ム
    'mʊ': '\u30E0',  # ム

    # N+Vowel
    'na': '\u30CA',  # ナ
    'naː': '\u30CA\u30FC',  # ナー
    'nə': '\u30CD',  # ネ
    'nɛ': '\u30CD',  # ネ
    'nəə': '\u30CD\u30FC',  # ネー
    'nɛn': '\u30CD\u30F3',  # ネン
    'nɪ': '\u30CB',  # ニ
    'niː': '\u30CB',  # ニ

    # P+Vowel
    'pa': '\u30D1',  # パ
    'piː': '\u30D4',  # ピ

    # R+Vowel (Long Vowel)
    'ʁiː': '\u30EA\u30FC',  # リー
    'ʁuː': '\u30EB\u30FC',  # ルー
    'ʁa': '\u30E9\u30FC',  # ラー
    'ʁaː': '\u30E9\u30FC',  # ラー
    'ʁɔɔ': '\u30ED',  # ロ
    'ʁɔ': '\u30ED',  # ロ
    'ʁoː': '\u30ED\u30FC',  # ロー
    'ʁeː': '\u30EC\u30FC',  # レー

    # S+Vowel
    'sɐ': '\u30B5',  # サ
    'szə': '\u30BB',  # セ

    # T+Vowel
    'ta': '\u30BF',  # タ
    'tɐ': '\u30BF',  # タ
    'taː': '\u30BF\u30FC',  # ター
    'tak': '\u30BF\u30FC\u30AF',  # ターク
    'tat': '\u30BF\u30C3\u30C8',  # タット
    'toː': '\u30C8',  # ト
    'tɔx': '\u30C8\u30DB',  # トホ
    'tʏ': '\u30C8\u30A5',  # トゥ
    'tuː': '\u30C8\u30A5',  # トゥ
    'tʊ': '\u30C8\u30A5',  # トゥ
    'tyː': '\u30C8\u30A5\u30FC',  # トゥー
    'tɛ': '\u30C6',  # テ
    'tɛː': '\u30C6\u30FC',  # テー
    'tiː': '\u30C6\u30A3',  # ティ

    # V+Vowel
    'vɛ': '\u30F4\u30A7',  # ヴェ
    'va': '\u30F4\u30A1',  # ヴァ

    # Z+Vowel
    'zeː': '\u30BC\u30FC',  # ゼー
    'zoː': '\u30BE\u30FC',  # ゾー
    'zɔn': '\u30BE\u30F3',  # ゾン
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
    'buːx': '\u30D6\u30FC\u30D5',  # buːx -> ブーフ (Buch)
    'naχ': '\u30CA\u30CF',  # naχ -> ナハ (nach)
    'zɔnə': '\u30BE\u30F3\u30CD',  # zɔnə -> ゾンネ (Sonne)
    'bɛt': '\u30D9\u30C3\u30C8',  # bɛt -> ベット (Bett)
    'ziːk': '\u30B8\u30FC\u30AF',  # ziːk -> ジーク (Musik)

    # Uncategorized (unsure what to call these)
    '̯t͡ʃ': '\u30C1\u30E5',  # チュ
    'ʃ': '\u30B7\u30E5',  # シュ
    'ʃuː': '\u30B7\u30E5\u30FC',  # シュー
    'ʃə': '\u30B7\u30A7',  # シェ
    'ʃɛ': '\u30B7\u30A7',  # シェ
    'ŋɐ': '\u30F3\u30AC',  # ンガ
    'ŋə': '\u30F3\u30B2',  # ンゲ
    'tsɔ': '\u30C4\u30A9',  # ツォ
    'tsə': '\u30C3\u30C4\u30A7',  # ッツェ
    'ʁyː': '\u30EA\u30E5\u30FC',  # リュー
    'çə': '\u30D2\u30A7',  # ヒェ
    'ziː': '\u30B8',  # ジ
    'xə': '\u30C3\u30D8',  # ッヘ
}
MAX_IPA_SUBSTRING_LENGTH = len(max(mappings, key=len))


def convert_katakana(text):
    converted_words = []
    word_ipas = []
    for sent in sentences(text, lang='de-de'):
        for word in sent:
            if word.phonemes:
                word_ipas.append(''.join(word.phonemes))
                word_katakana = []
                start = 0
                while start < len(word_ipas[-1]):
                    modified = False
                    for i in range(min(len(word_ipas[-1]) - start, MAX_IPA_SUBSTRING_LENGTH), 0, -1):
                        if word_ipas[-1][start:start + i] in mappings:
                            word_katakana.append(mappings[word_ipas[-1][start:start + i]])
                            # print(word_ipas[-1][start:start + i])
                            start += i
                            modified = True
                            break
                    if not modified:
                        print('Error converting {}'.format(word_ipas[-1]))
                        break
                converted_words.append(''.join(word_katakana))
    return converted_words, word_ipas


word_pairings = pandas.read_csv(filepath_or_buffer='words.csv')
for index, row in word_pairings.iterrows():
    converted_word, word_ip = convert_katakana(row['german'])
    print(converted_word[-1], word_ip[-1])
    if not converted_word or converted_word[-1] != row['katakana']:
        print(word_ip[-1], converted_word[-1], row['katakana'])
        break
    # if row['german'] == 'Wasser':
    #     converted_word, word_ip = convert_katakana(row['german'])
    #     print(converted_word[-1], word_ip[-1])
    #     if not converted_word or converted_word[-1] != row['katakana']:
    #         print(word_ip, converted_word[-1], row['katakana'])
    #         break
