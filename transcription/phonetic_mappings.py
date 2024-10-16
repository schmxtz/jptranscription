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
    '\u025B': '\u30A8',  # ɛ -> エ (Short "e" as in "Entscheiden")
    '\u006F': '\u30AA',  # o -> オ (Short "o" as in "viOlett")
    '\u0254': '\u30AA',  # ɔ -> オ (Short "o" as in "Oktober")
    '\u028A': '\u30A6',  # ʊ -> ウ (Short "u" as in "Und")
    '\u0250\u032F': '\u30A2',  # ɐ̯ -> ア (Short non-syllabic "a" as in "bieR", it mimics the soft German "r" sound)
    '\u026A\u032F': '\u30A4',  # ɪ̯  -> イ (Short "i" as in "fREUnd")
    '\u028A\u032F': '\u30A6',  # ʊ̯ -> ウ (Short non-syllabic "u" as in "aUto")
    '\u02C8\u0061': '\u30A2',  # ˈa -> ア (Short stressed "a" as in "Auto")
    '\u02C8\u026A': '\u30A4',  # ˈɪ -> イ (Short stressed "i" as in "Immer")
    '\u02C8\u025B': '\u30A8',  # ˈɛ -> エ (Short stressed "e" as in "Essen")
    '\u02C8\u028A': '\u30A6',  # ˈʊ -> ウ (Short stressed "u" as in "untergehenden")
    '\u02C8\u0153': '\u30AA\u30A7',  # ˈœ -> オェ (Short stressed "ö" as in "Öffnen")
    '\u02CC\u0075': '\u30A6',  # ˌu -> ウ (Short secondary stressed "u" as in "Universität")
    '\u02C8\u0075\u02D0': '\u30A6\u30FC',  # ˈuː -> ウー (Long stressed "u" as in "Ufer")

    # Long vowels
    '\u0065\u02D0': '\u30A8',  # eː -> エ (Long "e" as in "Er")
    '\u0075\u02D0': '\u30A6\u30FC',  # uː -> ウー (Long "u" as in "UHr")
    '\u02C8\u0061\u02D0': '\u30A2\u30FC',  # ˈaː -> アー (Long stressed "a" as in "Abend")
    '\u0061\u02D0\u0250\u032F': '\u30A2\u30FC',  # aːɐ̯  -> アー (Very long "ar" as in "januAR")

    # B
    '\u0062': '\u30D6',  # ˈb -> ブ (Short "b" as in "Brief")
    '\u02C8\u0062': '\u30D6',  # ˈb -> ブ (Short stressed "b" as in "Blume")
    '\u0062\u0061': '\u30D0',  # ba -> バ (Short "ba" as in "BAllon")
    '\u0062\u0250': '\u30D0',  # bɐ -> バ (Short "ber" as in "oktoBER")
    '\u0062\u025B': '\u30D9',  # bɛ -> ベ (Short "be" as in "BEtt")
    '\u0062\u0259': '\u30D9',  # bə -> ベ (Short "be" as in "farBE")
    '\u0062\u028A': '\u30D6',  # bʊ -> ブ (Short "bu" as in "BUs")
    '\u0062\u0069\u02D0': '\u30D3\u30FC',  # biː -> ビー (Long "bie" as in "BIEr")
    '\u02C8\u0062\u026A': '\u30D3',  # ˈbɪ -> ビ (Short stressed "bi" as in "BItte")
    '\u02C8\u0062\u0254': '\u30DC',  # ˈbɔ -> ボ -> (Short stressed "bo" as in "BÄUme")
    '\u0062\u006E\u0329': '\u30D9\u30F3',  # bn̩ -> ベン (Silent "e" between "b" and "n" as in "abEnd")
    '\u02C8\u0062\u0069\u02D0': '\u30D3\u30FC',  # ˈbiː -> ビー (Long stressed "bie" as in "BIEne")
    '\u02C8\u0062\u0075\u02D0': '\u30D6\u30FC',  # ˈbuː -> ブー (Long stressed "bu" as in "geBUrtstag")

    # C
    '\u00E7\u0259': '\u30D2\u30A7',  # çə -> ヒェ (Short "che" as in "mädCHEn")

    # D
    '\u0064': '\u30C9',  # d -> ド (Short "d" as in "Drei")
    '\u0064\u0061': '\u30C0',  # da -> ダ (Short "da" as in "DAs")
    '\u0064\u0250': '\u30C0',  # dɐ -> ダ (Short "der" as in "bruDER")
    '\u0064\u0259': '\u30C7',  # də -> デ (Short "de" as in "stunDE")
    '\u0064\u0065': '\u30C7',  # de -> デ (Short "de" as in "DEzember")
    '\u0064\u025B': '\u30C7',  # dɛ -> デ (Short "de" as in "DEs")
    '\u0064\u0254': '\u30C9',  # dɔ -> ド (Short "do" as in "DOrf")
    '\u0064\u0075\u02D0': '\u30C9\u30A5\u30FC',  # duː -> ドゥー (Long "du" as in "DU")
    '\u0064\u0065\u02D0': '\u30C7',  # deː -> デ (Long "de" as in "DEr")
    '\u0064\u0069\u02D0': '\u30C7\u30A3',  # diː -> ディ (Long "die" as in "DIE")
    '\u02C8\u0064\u0061': '\u30C0',  # ˈda -> ダ (Short stressed "da" as in "DAnke")
    '\u02C8\u0064\u025B': '\u30C7',  # ˈdɛ -> デ (Short "de" as in "stuDEnt")
    '\u02C8\u0064\u0254': '\u30C9',  # ˈdɔ -> ド (Short stressed "do" as in "DEUtschland")
    '\u0064\u006E\u0329': '\u30C7\u30F3',  # dn̩ -> デン (Short "den" as in "entscheiDEN")
    '\u02C8\u0064\u0069\u02D0': '\u30C7\u30A3\u30FC',  # ˈdiː -> ディー (Long stressed "die" as in "DIEnstag")
    '\u02C8\u0064\u025B\u02D0': '\u30C7\u30FC',  # ˈdɛː -> デー	(Long stressed "dä" as in "dÄmlich")

    # F
    '\u0066': '\u30D5',  # f -> フ (Short "f" as in "brieF")
    '\u02C8\u0066': '\u30D5',  # ˈf -> (Short stressed "f" as in "Flugzeug")
    '\u0066\u0061': '\u30D5\u30A1',  # fa -> ファ (Short "fa" as in "FAmilie")
    '\u0066\u0250': '\u30D5\u30A1',  # fɐ -> ファ (Short "fer" as in "uFER")
    '\u0066\u026A': '\u30D5\u30A3',  # fɪ -> フィ (Short "fi" as in "FIlm")
    '\u0066\u0065': '\u30D5\u30A7',  # fe -> フェ (Short "fe" as in "kafFEE")
    '\u0066\u028A': '\u30D5',  # fʊ -> フ (Short "fu" as in "FUchs")
    '\u0066\u028F': '\u30D5',  # fʏ -> フ (Short "fü" as in "FÜnf")
    '\u02C8\u0066\u0061': '\u30D5\u30A1',  # ˈfa -> ファ (Short stressed "fa" as in "FAngen")
    '\u02C8\u0066\u026A': '\u30D5\u30A3',  # ˈfɪ -> フィ (Short stressed "fi" as in "FInger")
    '\u02CC\u0066\u026A': '\u30D5\u30A3',  # ˌfɪ -> フィ (Short secondary stressed "fi" as in "sonnnenFInsternis")
    '\u0066\u006E\u0329': '\u30D5\u30A7\u30F3',  # fn̩ -> フェン (Short "fen" as in "helFEN")
    '\u02C8\u0066\u0061\u02D0': '\u30D5\u30A1\u30FC',  # ˈfaː -> ファー (Long stressed "fah" as in "FAHrrad")
    '\u02C8\u0066\u0065\u02D0': '\u30D5\u30A7\u30FC',  # ˈfeː -> フェー (Long stressed "fe" as in "

    # G
    '\u0261': '\u30B0',  # ɡ -> グ (Short "g" as in "Grün")
    '\u006B': '\u30AF',  # k -> ク (Short "g" as in flugzeuG")
    '\u02C8\u0261': '\u30B0',  # ˈɡ -> グ (Short stressed "g" as in "Glöckchen")
    '\u0261\u0259': '\u30B2',  # ɡə -> ゲ (Short "ge" as in "GEburtstag")
    '\u0261\u025B': '\u30B2',  # ɡɛ -> ゲ (Short "ge" as in "GEld")
    '\u02C8\u0261\u026A': '\u30AE',  # ˈɡɪ -> ギ (Short "gi" as in "beGInnen")
    '\u02C8\u0261\u025B': '\u30B2',  # ˈɡɛ -> ゲ (Short stressed "ge" as in "GEstern")
    '\u02C8\u0261\u028A': '\u30B0',  # ˈɡʊ -> グ (Short stressed "gu" as in "auGUst")
    '\u0261\u0075\u02D0': '\u30B0\u30FC',  # ɡuː -> グー (Long "gu" as in "GUt")
    '\u0261\u006E\u0329': '\u30B2\u30F3',  # ɡn̩ -> ゲン (Silent "e" between "g" and "n" as in "morGEN"
    '\u02C8\u0261\u0065\u02D0': '\u30B2\u30FC',  # ˈɡeː -> ゲー (Long stressed "ge" as in "GEben")
    '\u02CC\u0261\u0065\u02D0': '\u30B2\u30FC',  # ˌɡeː -> ゲー (Long secondary stressed "ge" as in "unterGEHenden")

    # H
    '\u0259\u006E': '\u30D8\u30F3',  # ən -> ヘン (Short "hen" as in "geHEN")
    '\u0068\u0061': '\u30CF',  # ha -> ハ (Short "ha" as in "HAnd")
    '\u0068\u006F': '\u30DB',  # ho -> ホ (Short "ho" as in "HOtel")
    '\u0068\u028A': '\u30D5',  # hʊ -> フ (Short "hu" as in "HUnd")
    '\u0068\u025B': '\u30D2\u30A7',  # hɛ -> ヒェ (Short "he" as in "HErbst")
    '\u02C8\u0068\u0061': '\u30CF',  # ˈha -> ハ (Short "ha" as in "HEIßen")
    '\u02C8\u0068\u025B': '\u30D8',  # ˈhɛ -> ヘ (Short stressed "he" as in "helfen")
    '\u02C8\u0068\u028A': '\u30D5',  # ˈhʊ -> フ (Short stressed "hu" as in "HUnger")
    '\u02C8\u0068\u0254': '\u30DB',  # ˈhɔ -> ホ (Short stressed "ho" as in "HEUte")
    '\u02C8\u0068\u0061\u02D0': '\u30CF\u30FC',  # ˈhaː -> ハー (Long stressed "ha" as in "HAben")
    '\u02C8\u0068\u006F\u02D0': '\u30DB\u30FC',  # ˈhoː -> ホー (Long stressed "ho" as in "HOlen")
    '\u02C8\u0068\u00F8\u02D0': '\u30DB\u30A7\u30FC',  # ˈhøː -> ホェー (Long stressed "ho" as in "HOlen")

    # J
    '\u02C8\u006A\u028A': '\u30E6',  # ˈjʊ -> ユ (Short stressed "ju" as in "JUnge")
    '\u006A\u0061\u02D0': '\u30E4\u30FC',  # jaː -> ヤー (Long "jah" as in "JAHr")
    '\u02C8\u006A\u0061': '\u30E4',  # ˈja -> ヤ
    '\u02C8\u006A\u0061\u02D0': '\u30E4\u30FC',  # ˈjaː -> ヤー (Long stressed "ja" as in "JApan")
    '\u02C8\u006A\u0075\u02D0': '\u30E6\u30FC',  # ˈjuː -> ユー (Long stressed "ju" as in "JUni")

    # K
    '\u006B\u0061': '\u30AB',  # ka -> カ (Short "ka" as in "KEIn")
    '\u006B\u026A': '\u30AD',  # kɪ -> キ (Short "ki" as in "KInd")
    '\u006B\u0254': '\u30B3',  # kɔ -> コ (Short "ko" as in "KOmmt")
    '\u02C8\u006B': '\u30AF',  # ˈk -> ク (Short stressed "k" as in "Klein")
    '\u006B\u0079\u02D0': '\u30AD\u30E5\u30FC',  # kyː -> キュー (Long "küh" as in KÜHl) 
    '\u02C8\u006B\u0061': '\u30AB',  # ˈka -> カ (Short "ka" as in "KAffee")
    '\u02C8\u006B\u0254': '\u30B3',  # ˈkɔ -> コ (Short stressed "ko" as in "KOmmen")

    # L
    '\u006C': '\u30EB',  # l -> ル (Short "l" as in "aLt")
    '\u006C\u0061': '\u30E9',  # la -> ラ (Short "la" as in "deutschLAnd")
    '\u006C\u0259': '\u30EC',  # lə -> レ (Short "le" as in "schuLE")
    '\u006C\u025B': '\u30EC',  # lɛ -> レ
    '\u006C\u0069': '\u30EA',  # li -> リ (Short "li" as in "juLI")
    '\u006C\u026A': '\u30EA',  # lɪ -> リ (Short "li" as in "frühLIng")
    '\u006C\u0153': '\u30ED',  # lœ -> ロ (Short "lö" as in "gLÖckchen")
    '\u006C\u028A': '\u30EB',  # lʊ -> ル (Short "lu" as in "fLUsses")
    '\u006C\u0329': '\u30EB',  # l̩ -> ル (Short "l" as in "spiegeLte")
    '\u02C8\u006C\u0254': '\u30ED',  # ˈlɔ -> ロ (Short stressed "lo" as in "balLOn")
    '\u02C8\u006C\u0061': '\u30E9',  # ˈla -> (Short stressed "la" as in "LAngsam")
    '\u006C\u0061\u02D0': '\u30E9\u30FC',  # laː -> ラー (Long "la" as in "schLAfen")
    '\u006C\u0075\u02D0': '\u30EB\u30FC',  # luː -> ルー (Long "lu" as in "bLUme")
    '\u006C\u0065\u02D0': '\u30EC',  # leː -> レ (Long "le" as in "probLEm")
    '\u006C\u0069\u032F': '\u30EA\u30FC',  # li̯ -> リー (Short "li" as in "famiLIe")
    '\u02C8\u006C\u0065\u02D0': '\u30EC\u30FC',  # ˈleː -> レー (Long stressed "le" as in "LEben") 

    # M
    '\u006D': '\u30E0',  # m -> ム (Short "m" as in "filM")
    '\u006D\u0061': '\u30DE',  # ma -> マ (Short "ma" as in "MAnn")
    '\u006D\u0250': '\u30DE',  # mɐ -> マ (Short "mer" as in "zimMER")
    '\u006D\u0259': '\u30E1',  # mə -> メ (Short "me" as in "bluME")
    '\u006D\u025B': '\u30E1',  # mɛ -> メ (Short "me" as in "mÄrz")
    '\u006D\u0075': '\u30E0',  # mu -> ム (Short "mu" as in "MUsik")
    '\u02C8\u006D\u0254': '\u30E2',  # ˈmɔ -> モ (Short "mo" as in "MOrgen")
    '\u02C8\u006D\u028A': '\u30E0',  # ˈmʊ -> ム (Short stressed "mu" as in "MUtter")
    '\u02C8\u006D\u0069\u02D0': '\u30DF',  # ˈmiː -> ミ (Long stressed "mi" as in "faMIlie")
    '\u02C8\u006D\u025B\u02D0': '\u30E1\u30FC',  # ˈmɛː -> メー (Long stressed "me" as in "MÄdchen")
    '\u02C8\u006D\u006F\u02D0': '\u30E2\u30FC',  # ˈmoː -> モー (Long stressed "mo" as in "MOnat")
    '\u02C8\u006D\u00F8\u02D0': '\u30E2\u30A7\u30FC',  # ˈmøː -> モェー (Long streesed "mö" as in "MÖwen")
    '\u02C8\u006D\u0079\u02D0': '\u30DF\u30E5\u30FC',  # ˈmyː -> ミュー (Long stressed "mü" as in "geMÜtlich")

    # N
    '\u006E': '\u30F3',  # n -> ン (Short "n" as in "deutschlaNd")
    '\u014B': '\u30F3\u30B0',  # ŋ -> ング (Short "ng" as in "laNG")
    '\u006E\u0061': '\u30CA',  # na -> ナ (Short "na" as in "moNAt")
    '\u006E\u0250': '\u30CA',  # nɐ -> ナ (Short "ner" as in "donNERstag")
    '\u006E\u0259': '\u30CD',  # nə -> ネ (Short "ne" as in "bieNE")
    '\u006E\u025B': '\u30CD',  # nɛ -> ネ (Short "ne" as in "schNEll")
    '\u006E\u026A': '\u30CB',  # nɪ -> ニ (Short "ni" as in "sonnenfinsterNIs")
    '\u006E\u0069': '\u30CB',  # ni -> ニ (Short "ni" as in "uNIversität")
    '\u006E\u0254': '\u30CE',  # nɔ -> ノ (Short "neu" as in "NEUn")
    '\u006E\u006F': '\u30CE',  # no -> ノ (Short "no" as in "NOvember")
    '\u006E\u0075': '\u30CC',  # nu -> ヌ (Short "nu" as in "jaNUar")
    '\u014B\u006B': '\u30F3\u30AF',  # ŋk -> ンク (Short "nk" as in "baNK")
    '\u014B\u0259': '\u30F3\u30B2',  # ŋə -> ンゲ (Short "nge" as in "faNGEn")
    '\u014B\u0250': '\u30F3\u30AC',  # ŋɐ -> ンガ (Short "nger" as in "fiNGER")
    '\u006E\u0065\u02D0': '\u30CD\u30FC',  # neː -> ネー (Long "nee" as in "schNEE")
    '\u014B\u006B\u0259': '\u30F3\u30B1',  # ŋkə -> ンケ (Short "nke" as in "daNKE")
    '\u02C8\u006E\u0061\u02D0': '\u30CA\u30FC',  # ˈnaː -> ナー (Long stressed "na" as in "NAme")
    '\u02C8\u006E\u0065\u02D0': '\u30CD\u30FC',  # ˈneː -> ネー (Long stressed "neh" as in "NEHmen")
    '\u014B\u006B\u006E\u0329': '\u30F3\u30B1\u30F3',  # ŋkn̩ -> ンケン (Short "nken" as in "deNKEN")

    # P
    '\u0070': '\u30D7',  # p -> プ (Short "p" as in "Problem")
    '\u02C8\u0070': '\u30D7',  # ˈp -> プ (Short stressed "p" as in "aPril")
    '\u0070\u0061': '\u30D1',  # pa -> パ (Short "pa" as in "jaPAn")
    '\u0070\u0069\u02D0': '\u30D4\u30FC',  # piː -> ピー (Long "pie" as in "sPIElen")
    '\u02C8\u0070\u0069\u02D0': '\u30D4',  # ˈpiː -> ピ (Long stressed "pie" as in "paPIEr")

    # Q
    '\u006B\u0076\u0065\u02D0': '\u30AF\u30A7',  # kveː -> クェ (Long "que" as in "QUEr")

    # R
    '\u0281': '\u30A2',  # ʁ -> ア (Soft German "r" as in "faRbe")
    '\u0281\u0061': '\u30E9',  # ʁa -> ラ (Short "ra" as in "fRAu")
    '\u0281\u0259': '\u30EC',  # ʁə -> レ (Short "re" as in "fahREn")
    '\u0281\u025B': '\u30EC',  # ʁɛ -> レ (Short "re" as in "spREchen")
    '\u0281\u0254': '\u30ED',  # ʁɔ -> ロ (Short "ro" as in "fREUnd")
    '\u0281\u006F': '\u30ED',  # ʁo -> ロ (Short "ro" as in "pROblem")
    '\u0281\u0075': '\u30EB',  # ʁu -> ル (Short "ru" as in "febRUar")
    '\u0281\u026A': '\u30EA',  # ʁɪ -> リ (Short "ri" as in "apRIl")
    '\u0281\u0069\u02D0': '\u30EA\u30FC',  # ʁiː -> リー (Long "rie" as in "bRIEf)
    '\u0281\u006F\u02D0': '\u30ED\u30FC',  # ʁoː -> ロー (Long "ro" as in "bROt")
    '\u0281\u0075\u02D0': '\u30EB\u30FC',  # ʁuː -> ルー (Long "ru" as in "bRUder")
    '\u0281\u0061\u02D0': '\u30E9\u30FC',  # ʁaː -> ラー (Long "ra" as in "fahrRAd")
    '\u0281\u0079\u02D0': '\u30EA\u30E5\u30FC',  # ʁyː -> リュー (Long "rüh" as in "fRÜHstück")
    '\u02C8\u0281\u025B': '\u30EC',  # ˈʁɛ -> レ (Short stressed "re" as in "REchen")
    '\u02C8\u0281\u0065\u02D0': '\u30EC\u30FC',  # ˈʁeː -> レー (Long stressed "re" as in "REgen")
    '\u02C8\u0281\u0075\u02D0': '\u30EB\u30FC',  # ˈʁuː -> ルー (Long stressed "")
    '\u02CC\u0281\u0061\u02D0': '\u30E9\u30FC',  # ˌʁaː -> ラー (Long secondary stressed "ra" as in "fahrRAd")

    # S
    '\u0073': '\u30B9',  # s -> ス (Short "s" as in "buS")
    '\u0283': '\u30B7\u30E5',  # ʃ -> シュ (Short "sch" as in "SCHnee")
    '\u0073\u0259': '\u30BB',  # sə -> セ (Short "ße" as in "straSSE")
    '\u007A\u025B': '\u30BC',  # zɛ -> ゼ (Short "se" as in "SEchs")
    '\u0073\u0250': '\u30B5',  # sɐ -> サ (Short "ser" as in "wasSER")
    '\u007A\u026A': '\u30BA\u30A3',  # zɪ -> ズィ (Short "si" as in "SIch")
    '\u032F\u0073': '\u30B9',  # ̯s -> ス (Short "ß" as in "weiSS")
    '\u007A\u0069': '\u30BA\u30A3',  # zi -> ズィ (Short "si" as in "univerSItät")
    '\u007A\u0061': '\u30B6',  # za -> ザ (Short "sa" as in "sein")
    '\u0283\u0259': '\u30B7\u30A7',  # ʃə -> シェ (Short "sche" as in "taSCHE")
    '\u02C8\u0283': '\u30B7\u30E5',  # ˈʃ -> シュ (Short stressed "sch" as in "SCHwester")
    '\u02CC\u0283': '\u30B7\u30E5',  # ˌʃ -> シュ (Short secondary stressed "st" as in "frühSTück")
    '\u007A\u0061\u02D0': '\u30B6\u30FC',  # zaː -> ザー (Long "sa" as in "langSAm")
    '\u007A\u0069\u02D0': '\u30BA\u30A3\u30FC',  # ziː -> ズィー (Long "sie" as in "SIE")
    '\u007A\u0065\u02D0': '\u30BC\u30FC',  # zeː -> ゼー (Long "see" as in "SEE")
    '\u007A\u006F\u02D0': '\u30BE\u30FC',  # zoː -> ゾー (Long "soh" as in "SOHn")
    '\u02C8\u007A\u0061': '\u30B6',  # ˈza -> ザ (Short stressed "sa" as in "SAmstag")
    '\u02C8\u007A\u0254': '\u30BE',  #  ˈzɔ -> ゾ (Short stressed "so" as in "SOmmer")
    '\u02C8\u007A\u026A': '\u30BA\u30A3',  # ˈzɪ -> ズィ (Short "si" as in "SIngen")
    '\u0283\u00F8\u02D0': '\u30B7\u30E5\u30FC',  # ʃøː -> シュー (Long "schö" as in "SCHÖn")
    '\u02C8\u0283\u025B': '\u30B7\u30A7',  # ˈʃɛ -> シェ (Short "sche" as in "geSCHEnk")
    '\u02C8\u0283\u0061': '\u30B7\u30E3',  # ˈʃa -> シャ (Short stressed "scha" as in "entSCHEIden")
    '\u007A\u006E\u0329': '\u30BC\u30F3',  # zn̩ -> ゼン (Short "sen" as in "tauSENd")
    '\u02C8\u0283\u0075\u02D0': '\u30B7\u30E5\u30FC',  # ˈʃuː -> シュー (Long stressed "schu" as in "SCHUle")
    '\u02C8\u007A\u0069\u02D0': '\u30BA\u30A3\u30FC',  # ˈziː -> ズィー (Long stressed "si" as in "muSIk")
    '\u02C8\u007A\u0061\u02D0': '\u30B6\u30FC',  # ˈzaː -> ザー (Long stressed "sa" as in "SAgen")
    '\u02C8\u007A\u0065\u02D0': '\u30BC\u30FC',  # ˈzeː -> ゼー (Long stressed "se" as in "sehen")

    # T
    '\u0074': '\u30C8',  # t -> ト (Short "t" as in "alT")
    '\u0074\u0250': '\u30BF',  # tɐ -> タ (Short "ter" as in "mutTER")
    '\u0074\u006F': '\u30C8',  # to -> ト (Short "to" as in "auTO")
    '\u0074\u0259': '\u30C6',  # tə -> テ (Short "te" as in "heuTE")
    '\u0074\u0075': '\u30C8\u30A5',  # tu -> トゥ (Short "tu" as in "sTUdent")
    '\u0074\u028A': '\u30C8\u30A5',  # tʊ -> トゥ (Short "tu" as in "sTUdent")
    '\u0074\u028F': '\u30C8\u30A5',  # tʏ -> トゥ (Short "tü" as in "frühsTÜck)
    '\u0074\u0061\u02D0': '\u30BF\u30FC',  # taː -> ター (Long "ta" as in "TAg")
    '\u0074\u0069\u02D0': '\u30C6\u30A3\u30FC',  # tiː -> ティー (Long "tie" as in "TIEr")
    '\u0074\u0079\u02D0': '\u30C8\u30A5\u30FC',  # tyː -> トゥー (Long "tü" as in "TÜr")
    '\u02C8\u0074\u0061': '\u30BF',  # ˈta -> タ (Short stressed "ta" as in "TAsche")
    '\u02C8\u0074\u025B': '\u30C6',  # ˈtɛ -> テ (Short stressed "te" as in "hoTEl")
    '\u0074\u0361\u0283': '\u30C1\u30E5',  # t͡ʃ -> チュ (Short "tsch" as in "deuTSCHland")
    '\u0074\u0361\u0073': '\u30C4',  # t͡s -> ツ (Short "ts" as in "geburTStag")
    '\u0074\u006E\u0329': '\u30C6\u30F3',  # tn̩ -> テン (Short "ten" as in "antworTEN")
    '\u02C8\u0074\u025B\u02D0': '\u30C6\u30FC',  # ˈtɛː -> テー (Long stressed "tä" as in "universiTÄt")
    '\u02C8\u0074\u006F\u02D0': '\u30C8\u30FC',  # ˈtoː -> トー (Long stressed "to" as in "okTOber")
    '\u02CC\u0074\u0061\u02D0': '\u30BF\u30FC',  # ˌtaː -> ター (Long secondary stressed "ta" as in "geburtsTAg")
    '\u0074\u0361\u0073\u0259': '\u30C3\u30C4\u30A7',  # t͡sə -> ッツェ (Short "tze" as in "kaTZE")

    # V
    '\u0076\u0069': '\u30F4\u30A3',  # vi -> ヴィ (Short "vi" as in "VIolett")
    '\u0066\u0069': '\u30D5\u30A3',  # fi -> フィ (Short "vie" as in "VIElleicht")
    '\u0066\u0069\u02D0': '\u30D5\u30A3',  # fiː -> フィ (Long "vie" as in "VIEr")
    '\u02C8\u0076\u025B': '\u30F4\u30A7',  # ˈvɛ -> ヴェ (Short stressed "ve" as in "noVEmber")

    # W
    '\u0076\u0061': '\u30F4\u30A1',  # va -> ヴァ (Short "wa" as in "schWArz")
    '\u0076\u025B': '\u30F4\u30A7',  # vɛ -> ヴェ (Short "we" as in "schWEster")
    '\u0076\u0254': '\u30F4\u30A9',  # vɔ -> ヴォ (Short "wo" as in "WOrt")
    '\u02C8\u0076\u0061': '\u30F4\u30A1',  # ˈva -> ヴァ (Short stressed "wa" as in "WAsser")
    '\u02C8\u0076\u026A': '\u30F4\u30A3',  # ˈvɪ -> ヴィ (Short stressed "wi" as in "WInter")
    '\u02CC\u0076\u0254': '\u30F4\u30A9',  # ˌvɔ -> ヴォ (Short secondary stressed "wo" as in "antWOrten")
    '\u0076\u006E\u0329': '\u30F4\u30A7\u30F3',  # vn̩ -> ヴェン (Short "wen" as in "möWEN")
    '\u02C8\u0076\u006F\u02D0': '\u30F4\u30A9\u30FC',  # ˈvoː -> ヴォー (Long stressed "woh" as in "WOHnen")
    '\u02C8\u0076\u0069\u02D0': '\u30F4\u30A3\u30FC',  # ˈviː -> ヴィー (Long stressed "wie" as in "WIEsen")
    '\u02C8\u0076\u025B\u02D0': '\u30F4\u30A7\u30FC',  # ˈvɛː -> ヴェー (Long stressed "wäh" as in "WÄHrend")

    # Z
    '\u0074\u0361\u0073\u0061': '\u30C4\u30A1',  # t͡sa -> ツァ (Short "za" as in "ZEIt")
    '\u0074\u0361\u0073\u0061\u02D0': '\u30C4\u30A1\u30FC',  # t͡saː -> ツァー (Long "zah" as in "ZAHl")
    '\u0074\u0361\u0073\u0075\u02D0': '\u30C4\u30FC',  # t͡suː -> ツー (Long "zu" as in "ZUg")
    '\u0074\u0361\u0073\u0065\u02D0': '\u30C4\u30A7\u30FC',  # t͡seː -> ツェー (Long "zeh" as in "ZEHn")
    '\u02C8\u0074\u0361\u0073\u026A': '\u30C4\u30A3',  # ˈt͡sɪ -> ツィ (Short stressed "zi" as in "ZImmer")
    '\u02C8\u0074\u0361\u0073\u025B': '\u30C4\u30A7',  # ˈt͡sɛ -> ツェ (Short stressed "ze" as in "deZEmber")
    '\u0074\u0361\u0073\u006E\u0329': '\u30C4\u30A7\u30F3',  # t͡sn̩ -> ツェン (Short "zen" as in "ächZEN")
    '\u02CC\u0074\u0361\u0073\u0254': '\u30C4\u30A9',  # ˌt͡sɔ -> ツォ (Short secondary stressed "zo" as in "flugZEUg")

    # Ü
    '\u02C8\u0079\u02D0': '\u30E6',  # ˈyː -> ユ (Long stressed "ü" as in "Über")

    # Edge cases for T with preceding short vowel
    '\u0062\u025B\u0074': '\u30D9\u30C3\u30C8',  # bɛt -> ベット (Short "t" with preceding short vowel as in "BETT")
    '\u0074\u0061\u0074': '\u30BF\u30C3\u30C8',  # tat -> タット (Short "t" with preceding short vowel as in "sTADT")
    '\u02C8\u006C\u025B\u0074': '\u30EC\u30C3\u30C8',  # lɛt -> レット (Short "t" with preceding short vowel as in "vioLETT")
    '\u02C8\u006D\u026A\u0074': '\u30DF\u30C3\u30C8',  # ˈmɪt -> ミット (Short "t" with preceding short vowel as in "miTTwoch")

    # Edge cases for CH "x" (Pronunciation of "ch" depends on the preceding vowel
    '\u0061\u0078\u0074': '\u30A2\u30CF\u30C8',  # axt -> アハト (Short "cht" with preceding "a" as in "ACHT")
    '\u0062\u0075\u02D0\u0078': '\u30D6\u30FC\u30D5',  # buːx -> ブーフ (Short "ch" with preceding "bu" as in "BUCH")
    '\u006E\u0061\u0078\u0074': '\u30CA\u30CF\u30C8',  # naxt -> ナハト (Short "ch" with preceding "na" as in "NACHT")
    '\u02C8\u0074\u0254\u0078': '\u30C8\u30DB',  # ˈtɔx -> トホ (Short "ch" with preceding "to" as in "toCHter")
    '\u02CC\u0076\u0254\u0078': '\u30F4\u30A9\u30C3\u30DB',  # ˌvɔx -> ヴォッホ (Short "ch" with preceding "wo" as in "mittWOCH")
    '\u0281\u0061\u02D0\u0078\u0259': '\u30E9\u30FC\u30C3\u30D8',  # ʁaːxə -> ラーッヘ ("spraCHE")
    '\u02C8\u0076\u0254\u0078\u0259': '\u30F4\u30A9\u30C3\u30D8',  # ˈvɔxə -> ヴォッヘ ("woCHE")
    
    # Edge cases for CH "ç" 
    '\u00E7': '\u30C3\u30D2',  # ç -> ッヒ (Short "ch" anywhere not previously covered as in "niCHt")
    '\u00E7\u0000': '\u30C3\u30D2',  # çNULL -> ッヒ (Short "ch" at the end of a word as in "iCH")
    '\u00E7\u0259': '\u30C3\u30D2\u30A7',  # çə -> ッヒェ (Short "che" in the middle of the word as in "glöckCHEn")
    '\u0000\u00E7\u0065': '\u30B7\u30A7',  # NULLçe -> シェ (Short "che" at the start of a word as in "CHEmie")
    '\u00E7\u006E\u0329': '\u30C3\u30D2\u30A7\u30F3',  # çn̩ -> ッヒェン (Short "chen" as in "reCHEN")

    # Edge cases for N in the middle of word as "nn", e.g. "soNNe"
    '\u02C8\u007A\u0254\u006E\u0259': '\u30BE\u30F3\u30CD',  # ˈzɔnə -> ゾンネ (Short "ne" as in "soNNE")

    # Edge cases for M pronunciation, sometimes the Katakana "ン" is pronuounced "m" which is closer than "ム"
    '\u006D\u0062\u0250': '\u30F3\u30D0',  # mbɐ -> ンバ (Short "mber" as in "September")

    # Edge cases in general
    '\u0073\u006E\u0329': '\u30C3\u30BB\u30F3',  # sn̩ -> ッセン (Short "ssen" as in "eSSEN")
    '\u0073\u006E\u0329\u0074': '\u30B6\u30F3\u30AF\u30C8',  # sn̩t -> ザンクト	("St." pronounced as "Sankt")
    '\u02C8\u006E\u025B\u02D0\u0259': '\u30CD\u30FC\u30D8',  # ˈnɛːə -> ネーヘ ("nähe")

    # Special characters
    '\u0000': '',  # NULL character should not map to anything, if not used
    '\u0020': '\u0020',  # Space character just maps to space again
    '\u0000\u002C': '\u3001',  # , -> 、
    '\u002C\u0000': '\u3001',  # , -> 、
    '\u002E\u0000': '\u3002',  # . -> 。
    '\u0000\u002E': '\u3002',  # . -> 。
    '\u0000\u0022': '\u300C',  # "_ -> 「
    '\u0022\u0000': '\u300D',  # _" -> 」
}
