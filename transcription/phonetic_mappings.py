'''
Some notes to this mapping:
    - The character "t" is a little troublesome because it's pronunciation relies somewhat on the preceding characters
        -> If the preceding character is a short vowel, it is pronounced "ット" in "ベット" (Bett)
        -> If the preceding character is anything else, like a long vowel or consonant it is just "ト"
            like "ブロート" (Brot)
'''
GERMAN_IPA_TO_KATAKANA_MAP = {
    # Short vowels
    '\u0061': '\u30A2',  # a -> ア (Short "a" as in "Alt")
    '\u026A': '\u30A4',  # ɪ -> イ (Short "i" as in "DEUtschland")
    '\u0259': '\u30A8',  # ə -> エ (Short "e" as in "familiE")
    '\u0250\u032F': '\u30A2',  # ɐ̯ -> ア (Short non-syllabic "a" as in "bieR", it mimics the soft German "r" sound)
    '\u02C8\u0061': '\u30A2',  # ˈa -> ア (Short stressed "a" as in "Auto")
    '\u028A\u032F': '\u30A6',  # ʊ̯ -> ウ (Short non-syllabic "u" as in "aUto")
    '\u0250\u032F\u02CC': '\u30A2',  # ɐ̯ˌ -> ア (Short non-syllabic secondary stressed "a" as in "FahRrad"

    # Long vowels
    '\u02C8\u0061\u02D0': '\u30A2\u30FC',  # ˈaː -> アー (Long stressed "a" as in "Abend")

    # B
    '\u0062': '\u30D6',  # ˈb -> ブ (Short "b" as in "Brief")
    '\u02C8\u0062': '\u30D6',  # ˈb -> ブ (Short stressed "b" as in "Blume")
    '\u0062\u0061': '\u30D0',  # ba -> バ (Short "ba" as in "BAllon")
    '\u0062\u025B': '\u30D9',  # bɛ -> ベ (Short "be" as in "BEtt")
    '\u0062\u0259': '\u30D9',  # bə -> ベ (Short "be" as in "farBE")
    '\u0062\u028A': '\u30D6',  # bʊ -> ブ (Short "bu" as in "BUs")
    '\u0062\u0069\u02D0': '\u30D3\u30FC',  # biː -> ビー (Long "bie" as in "BIEr")
    '\u02C8\u0062\u0069\u02D0': '\u30D3\u30FC',  # ˈbiː -> ビー (Long stressed "bie" as in "BIEne")
    '\u0062\u006E\u0329': '\u30D9\u30F3',  # bn̩ -> ベン (Silent "e" between "b" and "n" as in "abEnd")

    # D
    '\u0064\u0250': '\u30C0',  # dɐ -> ダ (Short "der" as in "bruDER")
    '\u02C8\u0064\u0254': '\u30C9', # ˈdɔ -> ド (Short stressed "do" as in "DEUtschland")

    # F
    '\u0066': '\u30D5',  # f -> フ (Short "f" as in "brieF")
    '\u02C8\u0066': '\u30D5',  # ˈf -> (Short stressed "f" as in "Flugzeug")
    '\u0066\u0061': '\u30D5\u30A1',  # fa -> ファ (Short "fa" as in "FAmilie")
    '\u0066\u026A': '\u30D5\u30A3',  # fɪ -> フィ (Short "fi" as in "FIlm")
    '\u02C8\u0066\u0061': '\u30D5\u30A1',  # ˈfa -> ファ (Short stressed "fa" as in "FAngen")
    '\u02C8\u0066\u026A': '\u30D5\u30A3',  # ˈfɪ -> フィ (Short stressed "fi" as in "FInger")
    '\u02C8\u0066\u0061\u02D0': '\u30D5\u30A1\u30FC',  # ˈfaː -> ファー (Long stressed "fah" as in "FAHrrad")

    # G
    '\u006B\u02CC': '\u30AF',  # kˌ -> ク (Short secondary stressed "g" as in "fluGzeug")
    '\u032F\u006B': '\u30AF',  # ̯k -> ク (Short "g" as in FlugzeuG")

    # L
    '\u006C': '\u30EB',  # l -> ル (Short "l" as in "aLt")
    '\u006C\u0061': '\u30E9',  # la -> ラ (Short "la" as in "deutschLAnd")
    '\u02C8\u006C\u0254': '\u30ED',  # ˈlɔ -> ロ (Short stressed "lo" as in "balLOn")
    '\u006C\u0075\u02D0': '\u30EB\u30FC',  # luː -> ルー (Long "lu" as in "bLUme")
    '\u006C\u0069\u032F': '\u30EA\u30FC',  # li̯ -> リー (Short "li" as in "famiLIe")

    # M
    '\u006D': '\u30E0',  # m -> ム (Short "m" as in "filM")
    '\u006D\u0259': '\u30E1',  # mə -> メ (Short "me" as in "bluME")
    '\u02C8\u006D\u0069\u02D0': '\u30DF',  # ˈmiː -> (Long stressed "mi" as in "faMIlie")

    # N
    '\u006E': '\u30F3',  # n -> ン (Short "n" as in "deutschlaNd")
    '\u014B': '\u30F3\u3050',  # ŋ -> ング (Short "ng" as in "laNG")
    '\u006E\u0259': '\u30CD',  # nə -> ネ (Short "ne" as in "bieNE")
    '\u014B\u006B': '\u30F3\u30AF',  # ŋk -> ンク (Short "nk" as in "baNK")
    '\u014B\u0259': '\u30F3\u30B2',  # ŋə -> ンゲ (Short "nge" as in "faNGEn")
    '\u014B\u0250': '\u30F3\u30AC',  # ŋɐ -> ンガ (Short "nger" as in "fiNGER")

    # R
    '\u0281': '\u30A2',  # ʁ -> ア (Soft German "r" as in "faRbe")
    '\u0281\u0069\u02D0': '\u30EA\u30FC',  # ʁiː -> リー (Long "rie" as in "bRIEf)
    '\u0281\u006F\u02D0': '\u30ED\u30FC',  # ʁoː -> ロー (Long "ro" as in "bROt")
    '\u0281\u0075\u02D0': '\u30EB\u30FC',  # ʁuː -> ルー (Long "ru" as in "bRUder")
    '\u0281\u0061\u02D0': '\u30E9\u30FC',  # ʁaː -> ラー (Long "ra" as in "fahrRAd")

    # S
    '\u0073': '\u30B9',  # s -> ス (Short "s" as in "buS")

    # T
    '\u0074': '\u30C8',  # t -> ト (Short "t" as in "alT")
    '\u0074\u006F': '\u30C8',  # to -> ト (Short "to" as in "auTO")
    '\u032F\u0074\u0361\u0283': '\u30C1\u30E5',  # ̯t͡ʃ -> チュ (Short "tsch" as in "deuTSCHland")

    # Z
    '\u0074\u0361\u0073\u0254': '\u30C4\u30A9',  # t͡sɔ -> ツォ (Short "zo" as in "flugZEUg")

    # Edge cases for T with preceding short vowel
    '\u0062\u025B\u0074': '\u30D9\u30C3\u30C8',  # bɛt -> ベット (Short "t" with preceding short vowel as in "BETT")

    # Edge cases for CH (Pronunciation of "ch" depends on the preceding vowel
    '\u0062\u0075\u02D0\u0078': '\u30D6\u30FC\u30D5',  # buːx -> ブーフ (Short "ch" with preceding "bu" as in "BUch")

    # Special characters
    '\u0000': '',  # Null character should not map to anything, if not used
}