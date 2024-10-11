'''
Some notes to this mapping:
    - The character "t" is a little troublesome because it's pronunciation relies somewhat on the preceding characters
        -> If the preceding character is a short vowel, it is pronounced "ット" in "ベット" (Bett)
        -> If the preceding character is anything else, like a long vowel or consonant it is just "ト"
            like "ブロート" (Brot)
'''
GERMAN_IPA_TO_KATAKANA_MAP = {
    # Short vowels
    '\u0061': '\u30A2',  # a -> ア (Short "a" as in "alt")
    '\u0250\u032F': '\u30A2',  # ɐ̯ -> ア (Short non-syllabic "a" as in "Bier", it mimics the soft German "r" sound)
    '\u02C8\u0061': '\u30A2',  # ˈa -> ア (Short stressed "a" as in "Auto")
    '\u028A\u032F': '\u30A6',  # ʊ̯ -> ウ (Short non-syllabic "u" as in "Auto")

    # Long vowels
    '\u02C8\u0061\u02D0': '\u30A2\u30FC',  # ˈaː -> アー (Long stressed "a" as in "Abend")

    # B
    '\u0062': '\u30D6',  # ˈb -> ブ (Short "b" as in "Brief")
    '\u02C8\u0062': '\u30D6',  # ˈb -> ブ (Short stressed "b" as in "Blume")
    '\u0062\u0061': '\u30D0',  # ba -> バ (Short "ba" as in "Ballon")
    '\u0062\u025B': '\u30D9',  # bɛ -> ベ (Short "be" as in "Bett")
    '\u0062\u0069\u02D0': '\u30D3\u30FC',  # biː -> ビー (Long "bie" as in "Bier")
    '\u02C8\u0062\u0069\u02D0': '\u30D3\u30FC',  # ˈbiː -> ビー (Long stressed "bie" as in "Biene")
    '\u0062\u006E\u0329': '\u30D9\u30F3',  # bn̩ -> ベン (Silent "e" between "b" and "n" as in "Abend")

    # F
    '\u0066\u0000': '\u30D5',  # f -> フ (End of word "f" with long preceding vowel as in "Brief")

    # L
    '\u006C': '\u30EB',  # l -> ル (Short "l" as in "alt")
    '\u02C8\u006C\u0254': '\u30ED',  # ˈlɔ -> ロ (Short stressed "lo" as in "Ballon")
    '\u006C\u0075\u02D0': '\u30EB\u30FC',  # luː -> ルー (Long "lu" as in "Blume")

    # R
    '\u0281\u0069\u02D0': '\u30EA\u30FC',  # ʁiː -> リー (Long "rie" as in "Brief)
    '\u0281\u006F\u02D0': '\u30ED\u30FC',  # ʁoː -> ロー (Long "ro" as in "Brot")

    # T
    '\u0074': '\u30C8',  # t -> ト (Short "t" as in "alt")
    '\u0074\u006F': '\u30C8',  # to -> ト (Short "to" as in "Auto")

    # M
    '\u006D\u0259': '',  # mə -> メ (Short "me" as in "Blume")

    # N
    '\u006E\u0259': '\u30CD',  # nə -> ネ (Short "ne" as in "Biene")
    '\u014B': '\u30F3\u3050',  # ŋ -> ング (Short "ng" as in "lang")
    '\u014B\u006B': '\u30F3\u30AF',  # ŋk -> ンク (Short "nk" as in "Bank")

    # Edge cases for T with preceding short vowel
    '\u0062\u025B\u0074': '\u30D9\u30C3\u30C8',  # bɛt -> ベット (Short "t" with preceding short vowel as in "Bett")

    # Special characters
    '\u0000': '',  # Null character should not map to anything, if not used
}