from phonetics.transcribe import IPATranscription
import pandas, re

mappings = {
    # Diphtongs
    'aʊ̯': '\u30A2\u30A6',  # aʊ̯ -> アウ (sound "au" in "Auto")
    'ʁaʊ̯': '\u30E9\u30A6',  # ʁaʊ -> ラウ (sound "rau" in "Frau")

    # Vowels (Long Vowel)
    'ʏ': '\u30A4',  # イ
    'ə': '\u30A8',  # エ
    'eː': '\u30A8',  # エ
    'a': '\u30A2',  # a -> ア (sound "a" in "alt")
    'ɐ': '\u30A2',  # ア
    'aː': '\u30A2\u30FC',  # aː -> アー (sound "a" in "Abend")
    'ʊ': '\u30A6',  # ウ
    'uː': '\u30A6',  # ウ
    'ʔuː': '\u30A6',  # ウ
    'oː': '\u30AA',  # オ

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
    'faː': '\u30D5\u30A1\u30FC',  # ファー
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
    'mɐ': '\u30DE',  # マ
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
    'vɔ': '\u30F4\u30A9',  # ヴォ
    'viː': '\u30F4\u30A3\u30FC',  # ヴィー

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
    'g': '\u30B0',  # グ
    'ŋk': '\u30F3\u30AF',  # ンク
    '̯k': '\u30AF',  # ク
    't': '\u30C8',  # ト
    'ʁ': '\u30A2',  # ア
    'b': '\u30D6',  # ブ
    'f': '\u30D5',  # フ
    's': '\u30B9',  # ス
    'ss': '\u30B9',  # ス
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
    'tsa': '\u30C4\u30A1',  # ツァ
    'tsaː': '\u30C4\u30A1\u30FC',  # ツァー
    'tsə': '\u30C3\u30C4\u30A7',  # ッツェ
    't͡sɪ': '\u30C4\u30A3',  # ツィ
    't͡suː': '\u30C4\u30FC',  # ツー
    'ʁyː': '\u30EA\u30E5\u30FC',  # リュー
    'çə': '\u30D2\u30A7',  # ヒェ
    'ziː': '\u30B8',  # ジ
    'xə': '\u30C3\u30D8',  # ッヘ
}

updated_mappings = {
    # Short vowels
    '\u0061': '\u30A2',  # a -> ア (Short "a" as in "alt")
    '\u0250\u032F': '\u30A2',  # ɐ̯ -> ア (Short non-syllabic "a" as in "Bier", it mimics the soft German "r" sound)
    '\u02C8\u0061': '\u30A2',  # ˈa -> ア (Short stressed "a" as in "Auto")
    '\u028A\u032F': '\u30A6',  # ʊ̯ -> ウ (Short non-syllabic "u" as in "Auto")
    
    # Long vowels
    '\u02C8\u0061\u02D0': '\u30A2\u30FC',  # ˈaː -> アー (Long stressed "a" as in "Abend")

    # B
    '\u0062\u0061': '\u30D0',  # ba -> バ (Short "ba" as in "Ballon")
    '\u0062\u025B': '\u30D9',  # bɛ -> ベ (Short "be" as in "Bett")
    '\u0062\u0069\u02D0': '\u30D3\u30FC',  # biː -> ビー (Long "bie" as in "Bier")
    '\u02C8\u0062\u0069\u02D0': '\u30D3\u30FC',  # ˈbiː -> ビー (Long stressed "bie" as in "Biene")
    '\u0062\u006E\u0329': '\u30D9\u30F3',  # bn̩ -> ベン (Silent "e" between "b" and "n" as in "Abend")

    # L
    '\u006C': '\u30EB',  # l -> ル (Short "l" as in "alt")
    '\u02C8\u006C\u0254': '\u30ED',  # ˈlɔ -> ロ (Short stressed "lo" as in "Ballon")

    # T
    '\u0074': '\u30C8',  # t -> ト (Short "t" as in "alt")
    '\u0074\u0000': '\u30C3\u30C8',  # t -> ット (End of word "t" with short preceding vowel as in "Bett")
    '\u0074\u006F': '\u30C8',  # to -> ト (Short "to" as in "Auto")

    # N
    '\u006E\u0259': '\u30CD',  # nə -> ネ (Short "ne" as in "Biene")
    '\u014B': '\u30F3\u3050',  # ŋ -> ング (Short "ng" sound as in "lang")
    '\u014B\u006B': '\u30F3\u30AF',  # ŋk -> ンク (Short "nk" sound as in "Bank")

    # Special characters
    '\u0000': '',  # Null character should not map to anything, if not used


}
MAX_IPA_SUBSTRING_LENGTH = len(max(updated_mappings, key=len))
# The characters: ˈ̩ˌ̯͡ are not relevant to phonetics into Katakana
IRRELEVANT_IPA_CHAR = '\u02C8\u0329\u02CC\u032F\u0361'


trans = IPATranscription('lang-de')
trans.init_lookup_table()


def convert_katakana(text):
    word_ipa = trans.lookup_word(text)
    # word_ipa = re.sub(r'[{}]'.format(IRRELEVANT_IPA_CHAR), '', word_ipa)
    word_katakana = ''
    start = 0
    while start < len(word_ipa):
        modified = False
        for i in range(min(len(word_ipa) - start, MAX_IPA_SUBSTRING_LENGTH), 0, -1):
            if word_ipa[start:start + i] in updated_mappings:
                word_katakana += updated_mappings[word_ipa[start:start + i]]
                start += i
                modified = True
                break
        if not modified:
            print('Error converting {}'.format(word_ipa))
            break
    return word_katakana, word_ipa


word_pairings = pandas.read_csv(filepath_or_buffer='words.csv')
for index, row in word_pairings.iterrows():
    converted_word, word_ip = convert_katakana(row['german'])
    print(converted_word, word_ip, row['katakana'])

