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
    '\u006F': '\u30AA',  # o -> オ (Short "o" as in "viOlett")
    '\u0250\u032F': '\u30A2',  # ɐ̯ -> ア (Short non-syllabic "a" as in "bieR", it mimics the soft German "r" sound)
    '\u026A\u032F': '\u30A4',  # ɪ̯  -> イ (Short "i" as in "fREUnd")
    '\u028A\u032F': '\u30A6',  # ʊ̯ -> ウ (Short non-syllabic "u" as in "aUto")
    '\u02C8\u0061': '\u30A2',  # ˈa -> ア (Short stressed "a" as in "Auto")
    '\u02CC\u0075': '\u30A6',  # ˌu -> ウ (Short secondary stressed "u" as in "Universität")

    # Long vowels
    '\u0075\u02D0': '\u30A6\u30FC',  # uː -> ウー (Long "u" as in "UHr")
    '\u02C8\u0061\u02D0': '\u30A2\u30FC',  # ˈaː -> アー (Long stressed "a" as in "Abend")

    # B
    '\u0062': '\u30D6',  # ˈb -> ブ (Short "b" as in "Brief")
    '\u02C8\u0062': '\u30D6',  # ˈb -> ブ (Short stressed "b" as in "Blume")
    '\u0062\u0061': '\u30D0',  # ba -> バ (Short "ba" as in "BAllon")
    '\u0062\u025B': '\u30D9',  # bɛ -> ベ (Short "be" as in "BEtt")
    '\u0062\u0259': '\u30D9',  # bə -> ベ (Short "be" as in "farBE")
    '\u0062\u028A': '\u30D6',  # bʊ -> ブ (Short "bu" as in "BUs")
    '\u0062\u0069\u02D0': '\u30D3\u30FC',  # biː -> ビー (Long "bie" as in "BIEr")
    '\u0062\u006E\u0329': '\u30D9\u30F3',  # bn̩ -> ベン (Silent "e" between "b" and "n" as in "abEnd")
    '\u02C8\u0062\u0069\u02D0': '\u30D3\u30FC',  # ˈbiː -> ビー (Long stressed "bie" as in "BIEne")
    '\u02C8\u0062\u0075\u02D0': '\u30D6\u30FC',  # ˈbuː -> ブー (Long stressed "bu" as in "geBUrtstag")

    # C
    '\u00E7\u0259': '\u30D2\u30A7',  # çə -> ヒェ (Short "che" as in "mädCHEn")

    # D
    '\u0064': '\u30C9',  # d -> ド (Short "d" as in "Drei")
    '\u0064\u0250': '\u30C0',  # dɐ -> ダ (Short "der" as in "bruDER")
    '\u0064\u0259': '\u30C7',  # də -> デ (Short "de" as in "stunDE")
    '\u02C8\u0064\u025B': '\u30C7',  # ˈdɛ -> デ (Short "de" as in "stuDEnt")
    '\u02C8\u0064\u0254': '\u30C9',  # ˈdɔ -> ド (Short stressed "do" as in "DEUtschland")

    # F
    '\u0066': '\u30D5',  # f -> フ (Short "f" as in "brieF")
    '\u02C8\u0066': '\u30D5',  # ˈf -> (Short stressed "f" as in "Flugzeug")
    '\u0066\u0061': '\u30D5\u30A1',  # fa -> ファ (Short "fa" as in "FAmilie")
    '\u0066\u026A': '\u30D5\u30A3',  # fɪ -> フィ (Short "fi" as in "FIlm")
    '\u0066\u0065': '\u30D5\u30A7',  # fe -> フェ (Short "fe" as in "kafFEE")
    '\u02C8\u0066\u0061': '\u30D5\u30A1',  # ˈfa -> ファ (Short stressed "fa" as in "FAngen")
    '\u02C8\u0066\u026A': '\u30D5\u30A3',  # ˈfɪ -> フィ (Short stressed "fi" as in "FInger")
    '\u02CC\u0066\u026A': '\u30D5\u30A3',  # ˌfɪ -> フィ (Short secondary stressed "fi" as in "sonnnenFInsternis")
    '\u02C8\u0066\u0061\u02D0': '\u30D5\u30A1\u30FC',  # ˈfaː -> ファー (Long stressed "fah" as in "FAHrrad")

    # G
    '\u0261': '\u30B0',  # ɡ -> グ (Short "g" as in "Grün")
    '\u006B': '\u30AF',  # k -> ク (Short "g" as in flugzeuG")
    '\u0261\u0259': '\u30B2',  # ɡə -> ゲ (Short "ge" as in "GEburtstag")
    '\u0261\u025B': '\u30B2',  # ɡɛ -> ゲ (Short "ge" as in "GEld")
    '\u0261\u006E\u0329': '\u30B2\u30F3',  # ɡn̩ -> ゲン (Silent "e" between "g" and "n" as in "morGEN"

    # H
    '\u0068\u0061': '\u30CF',  # ha -> ハ (Short "ha" as in "HAnd")
    '\u0068\u006F': '\u30DB',  # ho -> ホ (Short "ho" as in "HOtel")
    '\u0068\u028A': '\u30D5',  # hʊ -> フ (Short "hu" as in "HUnd")
    '\u02C8\u0068\u028A': '\u30D5',  # ˈhʊ -> フ (Short stressed "hu" as in "HUnger")

    # J
    '\u02C8\u006A\u028A': '\u30E6',  # ˈjʊ -> ユ (Short stressed "ju" as in "JUnge")
    '\u006A\u0061\u02D0': '\u30E4\u30FC',  # jaː -> ヤー (Long "jah" as in "JAHr")
    '\u02C8\u006A\u0061\u02D0': '\u30E4\u30FC',  # ˈjaː -> ヤー (Long stressed "ja" as in "JApan")

    # K
    '\u006B\u026A': '\u30AD',  # kɪ -> キ (Short "ki" as in "KInd")キ
    '\u02C8\u006B\u0061': '\u30AB',  # ˈka -> カ (Short "ka" as in "KAffee")

    # L
    '\u006C': '\u30EB',  # l -> ル (Short "l" as in "aLt")
    '\u006C\u0061': '\u30E9',  # la -> ラ (Short "la" as in "deutschLAnd")
    '\u006C\u0259': '\u30EC',  # lə -> レ (Short "le" as in "schuLE")
    '\u02C8\u006C\u0254': '\u30ED',  # ˈlɔ -> ロ (Short stressed "lo" as in "balLOn")
    '\u006C\u0075\u02D0': '\u30EB\u30FC',  # luː -> ルー (Long "lu" as in "bLUme")
    '\u006C\u0065\u02D0': '\u30EC',  # leː -> レ
    '\u006C\u0069\u032F': '\u30EA\u30FC',  # li̯ -> リー (Short "li" as in "famiLIe")

    # M
    '\u006D': '\u30E0',  # m -> ム (Short "m" as in "filM")
    '\u006D\u0061': '\u30DE',  # ma -> マ (Short "ma" as in "MAnn")
    '\u006D\u0250': '\u30DE',  # mɐ -> マ (Short "mer" as in "zimMER")
    '\u006D\u0259': '\u30E1',  # mə -> メ (Short "me" as in "bluME")
    '\u006D\u0075': '\u30E0',  # mu -> ム (Short "mu" as in "MUsik")
    '\u02C8\u006D\u0254': '\u30E2',  # ˈmɔ -> モ (Short "mo" as in "MOrgen")
    '\u02C8\u006D\u028A': '\u30E0',  # ˈmʊ -> ム (Short stressed "mu" as in "MUtter")
    '\u02C8\u006D\u0069\u02D0': '\u30DF',  # ˈmiː -> (Long stressed "mi" as in "faMIlie")
    '\u02C8\u006D\u025B\u02D0': '\u30E1\u30FC',  # ˈmɛː -> メー (Long stressed "me" as in "MÄdchen")
    '\u02C8\u006D\u006F\u02D0': '\u30E2\u30FC',  # ˈmoː -> モー (Long stressed "mo" as in "MOnat")


    # N
    '\u006E': '\u30F3',  # n -> ン (Short "n" as in "deutschlaNd")
    '\u014B': '\u30F3\u3050',  # ŋ -> ング (Short "ng" as in "laNG")
    '\u006E\u0061': '\u30CA',  # na -> ナ (Short "na" as in "moNAt")
    '\u006E\u0259': '\u30CD',  # nə -> ネ (Short "ne" as in "bieNE")
    '\u006E\u026A': '\u30CB',  # nɪ -> ニ (Short "ni" as in "sonnenfinsterNIs")
    '\u006E\u0069': '\u30CB',  # ni -> ニ (Short "ni" as in "uNIversität")
    '\u014B\u006B': '\u30F3\u30AF',  # ŋk -> ンク (Short "nk" as in "baNK")
    '\u014B\u0259': '\u30F3\u30B2',  # ŋə -> ンゲ (Short "nge" as in "faNGEn")
    '\u014B\u0250': '\u30F3\u30AC',  # ŋɐ -> ンガ (Short "nger" as in "fiNGER")
    '\u006E\u0065\u02D0': '\u30CD\u30FC',  # neː -> ネー (Long "nee" as in "schNEE")
    '\u02C8\u006E\u0061\u02D0': '\u30CA\u30FC',  # ˈnaː -> ナー (Long stressed "na" as in "NAme")

    # P
    '\u0070': '\u30D7',  # p -> プ (Short "p" as in "Problem")
    '\u0070\u0061': '\u30D1',  # pa -> パ (Short "pa" as in "jaPAn")
    '\u02C8\u0070\u0069\u02D0': '\u30D4',  # ˈpiː -> ピ (Long stressed "pie" as in "paPIEr")

    # R
    '\u0281': '\u30A2',  # ʁ -> ア (Soft German "r" as in "faRbe")
    '\u0281\u0061': '\u30E9',  # ʁa -> ラ (Short "ra" as in "fRAu")
    '\u0281\u0254': '\u30ED',  # ʁɔ -> ロ (Short "ro" as in "fREUnd")
    '\u0281\u006F': '\u30ED',  # ʁo -> ロ (Short "ro" as in "pROblem")
    '\u0281\u0069\u02D0': '\u30EA\u30FC',  # ʁiː -> リー (Long "rie" as in "bRIEf)
    '\u0281\u006F\u02D0': '\u30ED\u30FC',  # ʁoː -> ロー (Long "ro" as in "bROt")
    '\u0281\u0075\u02D0': '\u30EB\u30FC',  # ʁuː -> ルー (Long "ru" as in "bRUder")
    '\u0281\u0061\u02D0': '\u30E9\u30FC',  # ʁaː -> ラー (Long "ra" as in "fahrRAd")
    '\u0281\u0079\u02D0': '\u30EA\u30E5\u30FC',  # ʁyː -> リュー (Long "rüh" as in "fRÜHstück")
    '\u02C8\u0281\u0065\u02D0': '\u30EC\u30FC',  # ˈʁeː -> レー (Long stressed "re" as in "REgen")
    '\u02CC\u0281\u0061\u02D0': '\u30E9\u30FC',  # ˌʁaː -> ラー (Long secondary stressed "ra" as in "fahrRAd")

    # S
    '\u0073': '\u30B9',  # s -> ス (Short "s" as in "buS")
    '\u0283': '\u30B7\u30E5',  # ʃ -> シュ (Short "sch" as in "SCHnee")
    '\u0073\u0259': '\u30BB',  # sə -> セ (Short "ße" as in "straSSE")
    '\u0073\u0250': '\u30B5',  # sɐ -> サ (Short "ser" as in "wasSER")
    '\u032F\u0073': '\u30B9',  # ̯s -> ス (Short "ß" as in "weiSS")
    '\u007A\u0069': '\u30BA\u30A3',  # zi -> ズィ (Short "si" as in "univerSItät")
    '\u0283\u0259': '\u30B7\u30A7',  # ʃə -> シェ (Short "sche" as in "taSCHE")
    '\u02C8\u0283': '\u30B7\u30E5',  # ˈʃ -> シュ (Short stressed "sch" as in "SCHwester")
    '\u02CC\u0283': '\u30B7\u30E5',  # ˌʃ -> シュ (Short secondary stressed "st" as in "frühSTück")
    '\u007A\u0065\u02D0': '\u30BC\u30FC',  # zeː -> ゼー (Long "see" as in "SEE")
    '\u007A\u006F\u02D0': '\u30BE\u30FC',  # zoː -> ゾー (Long "soh" as in "SOHn")
    '\u02C8\u0283\u025B': '\u30B7\u30A7',  # ˈʃɛ -> シェ (Short "sche" as in "geSCHEnk")
    '\u02C8\u0283\u0075\u02D0': '\u30B7\u30E5\u30FC',  # ˈʃuː -> シュー (Long stressed "schu" as in "SCHUle")
    '\u02C8\u007A\u0069\u02D0': '\u30BA\u30A3\u30FC',  # ˈziː -> ズィー (Long stressed "si" as in "muSIk")

    # T
    '\u0074': '\u30C8',  # t -> ト (Short "t" as in "alT")
    '\u0074\u0250': '\u30BF',  # tɐ -> タ (Short "ter" as in "mutTER")
    '\u0074\u006F': '\u30C8',  # to -> ト (Short "to" as in "auTO")
    '\u0074\u0075': '\u30C8\u30A5',  # tu -> トゥ (Short "tu" as in "sTUdent")
    '\u0074\u028A': '\u30C8\u30A5',  # tʊ -> トゥ (Short "tu" as in "sTUdent")
    '\u0074\u028F': '\u30C8\u30A5',  # tʏ -> トゥ (Short "tü" as in "frühsTÜck)
    '\u0074\u0061\u02D0': '\u30BF\u30FC',  # taː -> ター (Long "ta" as in "TAg")
    '\u0074\u0069\u02D0': '\u30C6\u30A3\u30FC',  # tiː -> ティー (Long "tie" as in "TIEr")
    '\u0074\u0079\u02D0': '\u30C8\u30A5\u30FC',  # tyː -> トゥー (Long "tü" as in "TÜr")
    '\u02C8\u0074\u0061': '\u30BF',  # ˈta -> タ (Short stressed "ta" as in "TAsche")
    '\u02C8\u0074\u025B': '\u30C6\u30FC',  # ˈtɛ -> テー (Short stressed "te" as in "hoTEl")
    '\u0074\u0361\u0283': '\u30C1\u30E5',  # t͡ʃ -> チュ (Short "tsch" as in "deuTSCHland")
    '\u0074\u0361\u0073': '\u30C4',  # t͡s -> ツ (Short "ts" as in "geburTStag")
    '\u02C8\u0074\u025B\u02D0': '\u30C6\u30FC',  # ˈtɛː -> テー (Long stressed "tä" as in "universiTÄt")
    '\u02CC\u0074\u0061\u02D0': '\u30BF\u30FC',  # ˌtaː -> ター (Long secondary stressed "ta" as in "geburtsTAg")
    '\u0074\u0361\u0073\u0259': '\u30C3\u30C4\u30A7',  # t͡sə -> ッツェ (Short "tze" as in "kaTZE")

    # V
    '\u0076\u0069': '\u30F4\u30A3',  # vi -> ヴィ (Short "vi" as in "VIolett")
    '\u0066\u0069\u02D0': '\u30D5\u30A3',  # fiː -> フィ (Long "vie" as in "VIEr")

    # W
    '\u0076\u0061': '\u30F4\u30A1',  # va -> ヴァ
    '\u0076\u025B': '\u30F4\u30A7',  # vɛ -> ヴェ (Short "we" as in "schWEster")
    '\u0076\u0254': '\u30F4\u30A9',  # vɔ -> ヴォ (Short "wo" as in "WOrt")
    '\u02C8\u0076\u0061': '\u30F4\u30A1',  # ˈva -> ヴァ (Short "wa" as in "WAsser")

    # Z
    '\u0074\u0361\u0073\u0061': '\u30C4\u30A1',  # t͡sa -> ツァ (Short "za" as in "ZEIt")
    '\u0074\u0361\u0073\u0061\u02D0': '\u30C4\u30A1\u30FC',  # t͡saː -> ツァー (Long "zah" as in "ZAHl")
    '\u0074\u0361\u0073\u0075\u02D0': '\u30C4\u30FC',  # t͡suː -> ツー (Long "zu" as in "ZUg")
    '\u02C8\u0074\u0361\u0073\u026A': '\u30C4\u30A3',  # ˈt͡sɪ -> ツィ (Short stressed "zi" as in "ZImmer")
    '\u02CC\u0074\u0361\u0073\u0254': '\u30C4\u30A9',  # ˌt͡sɔ -> ツォ (Short secondary stressed "zo" as in "flugZEUg")

    # Edge cases for T with preceding short vowel
    '\u0062\u025B\u0074': '\u30D9\u30C3\u30C8',  # bɛt -> ベット (Short "t" with preceding short vowel as in "BETT")
    '\u006C\u025B\u0074': '\u30EC\u30C3\u30C8',  # lɛt -> レット (Short "t" with preceding short vowel as in "vioLETT")
    '\u0074\u0061\u0074': '\u30BF\u30C3\u30C8',  # tat -> タット (Short "t" with preceding short vowel as in "sTADT")

    # Edge cases for CH (Pronunciation of "ch" depends on the preceding vowel
    '\u0062\u0075\u02D0\u0078': '\u30D6\u30FC\u30D5',  # buːx -> ブーフ (Short "ch" with preceding "bu" as in "BUCH")
    '\u006E\u0061\u0078\u0074': '\u30CA\u30CF\u30C8',  # naxt -> ナハト (Short "ch" with preceding "na" as in "NACHT")
    '\u02C8\u0074\u0254\u0078': '\u30C8\u30DB',  # ˈtɔx -> トホ (Short "ch" with preceding "to" as in "toCHter")
    '\u0281\u0061\u02D0\u0078\u0259': '\u30E9\u30FC\u30C3\u30D8',  # ʁaːxə -> ラーッヘ ("spraCHE")
    '\u02C8\u0076\u0254\u0078\u0259': '\u30F4\u30A9\u30C3\u30D8',  # ˈvɔxə -> ヴォッヘ ("woCHE")

    # Edge cases for N in the middle of word as "nn", e.g. "soNNe"
    '\u02C8\u007A\u0254\u006E\u0259': '\u30BE\u30F3\u30CD',  # ˈzɔnə -> ゾンネ (Short "ne" as in "soNNE")

    # Special characters
    '\u0000': '',  # Null character should not map to anything, if not used
}