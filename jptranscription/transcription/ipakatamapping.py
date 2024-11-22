'''
Some notes to this mapping:
    - The character "t" is a little troublesome because it's pronunciation relies somewhat on the preceding characters
        -> If the preceding character is a short vowel, it is pronounced "ット" "ベット" (Bett)
        -> If the preceding character is anything else, like a long vowel or consonant it is just "ト"
            like "ブロート" (Brot)
'''
GERMAN_IPA_TO_KATAKANA_MAP = {
    # Short vowels
    '\u0061': '\u30A2',                                 # a -> ア (word: "alt", ipa: "alt")
    '\u0250': '\u30A2',                                 # ɐ -> ア (word: "Schleier", ipa: "ˈʃlaɪ̯ɐ")
    '\u0259': '\u30A8',                                 # ə -> エ (word: "Familie", ipa: "faˈmiːli̯ə")
    '\u025B': '\u30A8',                                 # ɛ -> エ (word: "Entscheiden", ipa: "ɛntˈʃaɪ̯dn̩")
    '\u0065': '\u30A8',                                 # e -> エ (word: "er", ipa: "eːɐ̯")
    '\u026A': '\u30A4',                                 # ɪ -> イ (word: "Deutschland", ipa: "ˈdɔɪ̯t͡ʃlant")
    '\u0069': '\u30A4',                                 # i -> イ (word: "ihr", ipa: "iːɐ̯")
    '\u006F': '\u30AA',                                 # o -> オ (word: "violett", ipa: "vioˈlɛt")
    '\u0254': '\u30AA',                                 # ɔ -> オ (word: "Oktober", ipa: "ɔkˈtoːbɐ")
    '\u0075': '\u30A6',                                 # u -> ウ (word: "Uhr", ipa: "uːɐ̯")
    '\u028A': '\u30A6',                                 # ʊ -> ウ (word: "und", ipa: "ʊnt")
    '\u0153': '\u30AA\u30A7',                           # œ -> オェ (word: "öffnen", ipa: "ˈœfnən")
    '\u00F8': '\u30AA\u30A7',                           # ø -> オェ (word: "Ökologie", ipa: "ˌøkoloˈɡiː")
    '\u0061\u02D0\u0250\u032F': '\u30A2\u30FC',         # aːɐ̯  -> アー (word: "Januar", ipa: "ˈjanuaːɐ̯")

    # B
    '\u0062': '\u30D6',                                 # b -> ブ (word: "Brief", ipa: "bʁiːf")
    '\u0062\u0061': '\u30D0',                           # ba -> バ (word: "Ballon", ipa: "baˈlɔŋ")
    '\u0062\u0250': '\u30D0',                           # bɐ -> バ (word: "Oktober", ipa: "ɔkˈtoːbɐ")
    '\u0062\u025B': '\u30D9',                           # bɛ -> ベ (word: "Bett", ipa: "ɔkˈtoːbɐ")
    '\u0062\u0259': '\u30D9',                           # bə -> ベ (word: "Brieftaube", ipa: "ˈbʁiːfˌtaʊ̯bə")
    '\u0062\u026A': '\u30D3',                           # bɪ -> ビ (word: "Bitte", ipa: "ˈbɪtə")
    '\u0062\u0069': '\u30D3',                           # bi -> ビ (word: "Bier", ipa: "biːɐ̯")
    '\u0062\u006F': '\u30DC',                           # bo -> ボ (word: "Boot", ipa: "boːt")
    '\u0062\u0254': '\u30DC',                           # bɔ -> ボ (word: "Bäume", ipa: "ˈbɔɪ̯mə")
    '\u0062\u028A': '\u30D6',                           # bʊ -> ブ (word: "Tribus", ipa: "ˈtʁiːbʊs")
    '\u0062\u0075': '\u30D6',                           # bu -> ブ (word: "schnabulieren", ipa: "ʃnabuˈliːʁən")
    '\u0062\u028F': '\u30D3\u30E5',                     # bʏ -> ビュ (word: "büffeln", ipa: "ˈbʏfl̩n")
    '\u0062\u006E\u0329': '\u30D9\u30F3',               # bn̩ -> ベン (word: "lieben", ipa: "ˈliːbn̩")

    # C
    '\u00E7\u0065': '\u30B1',                           # çe -> ケ (word: "Elektrochemie", ipa: "eˌlɛktʁoçeˈmiː")

    # D
    '\u0064': '\u30C9',                                 # d -> ド (word: "Drei", ipa: "dʁaɪ̯")
    '\u0064\u0061': '\u30C0',                           # da -> ダ (word: "das", ipa: "das")
    '\u0064\u0250': '\u30C0',                           # dɐ -> ダ (word: "Bruder", ipa: "ˈbʁuːdɐ")
    '\u0064\u0259': '\u30C7',                           # də -> デ (word: "Stunde", ipa: "ˈʃtʊndə")
    '\u0064\u0065': '\u30C7',                           # de -> デ (word: "Dezember", ipa: "deˈt͡sɛmbɐ")
    '\u0064\u025B': '\u30C7',                           # dɛ -> デ (word: "des", ipa: "dɛs")
    '\u0064\u0069': '\u30C7\u30A3',                     # di -> ディ (word: "die", ipa: "diː")
    '\u0064\u026A': '\u30C7\u30A3',                     # dɪ -> ディ (word: "Dichter", ipa: "ˈdɪçtɐ")
    '\u0064\u0254': '\u30C9',  # dɔ -> ド (Short "do" as "DOrf")
    '\u0064\u006F': '\u30C9',  # do -> ド (Short "do" as "suborDO")
    '\u0064\u0075': '\u30C9\u30A5',  # du -> ドゥ (Long "du" as "DU")
    '\u0064\u028A': '\u30C9\u30A5',  # dʊ -> ドゥ (Short stressed "du" as "DUnkelheit")
    '\u0064\u006C\u0329': '\u30C7\u30EB',  # dl̩ -> デル (Short "del" as "verwanDELt")
    '\u0064\u006E\u0329': '\u30C7\u30F3',  # dn̩ -> デン (Short "den" as "entscheiDEN")

    # F
    '\u0066': '\u30D5',  # f -> フ (Short "f" as "brieF")
    '\u0066\u0061': '\u30D5\u30A1',  # fa -> ファ (Short "fa" as "FAmilie")
    '\u0066\u0250': '\u30D5\u30A1',  # fɐ -> ファ (Short "fer" as "uFER")
    '\u0066\u0065': '\u30D5\u30A7',  # fe -> フェ (Short "fe" as "kafFEE")
    '\u0066\u0259': '\u30D5\u30A7',  # fə -> フェ (Short "fe" as "kafFEE")
    '\u0066\u026A': '\u30D5\u30A3',  # fɪ -> フィ (Short "fi" as "FIlm")
    '\u0066\u0254': '\u30D5\u30A9',  # fɔ -> フォ (Short "fo" as "FOrt")
    '\u0066\u028A': '\u30D5',  # fʊ -> フ (Short "fu" as "FUchs")
    '\u0066\u028F': '\u30D5\u30E5',  # fʏ -> フュ (Short "fü" as "FÜnf")
    '\u0066\u0079': '\u30D5\u30E5',  # fy -> フュ (Long "fü" as "FÜr")
    '\u0066\u006C': '\u30D5\u30A7\u30EB',  # fl -> フェル (Short "fel" as "büFFELn")
    '\u0066\u006C\u0075': '\u30D5\u30EB',  # flu -> フル (Long "flu" as "FLUghafen")
    '\u0066\u006E\u0329': '\u30D5\u30A7\u30F3',  # fn̩ -> フェン (Short "fen" as "helFEN")

    # G
    '\u0261': '\u30B0',  # ɡ -> グ (Short "g" as "Grün")
    '\u0261\u0061': '\u30AC',  # ɡa -> ガ (SHort stressed "ga" as "verGAngenheit")
    '\u0261\u0259': '\u30B2',  # ɡə -> ゲ (Short "ge" as "GEburtstag")
    '\u0261\u025B': '\u30B2',  # ɡɛ -> ゲ (Short "ge" as "GEld")
    '\u0261\u0065': '\u30B2',  # ɡe -> ゲ (Short "ge" as "GEld")
    '\u0261\u026A': '\u30AE',  # ɡɪ -> ギ (Short "gi" as "beGInnen")
    '\u0261\u0069': '\u30AE',  # ɡi -> ギ (Long "gie" as "ÖkologIE")
    '\u0261\u028A': '\u30B0',  # ɡʊ -> グ (Short stressed "gu" as "auGUst")
    '\u0261\u0075': '\u30B0',  # ɡu -> グ (Long "gu" as "GUt")
    '\u0261\u006E\u0329': '\u30B2\u30F3',  # ɡn̩ -> ゲン (Silent "e" between "g" and "n" as "morGEN")
    '\u0261\u014B\u030D': '\u30B2\u30F3',  # ɡŋ̍ -> ゲン (Silent "e" between "g" and "n" as "morGEN")
    '\u0261\u006C\u0329': '\u30B2\u30EB',  # ɡl̩ -> ゲル (Short "gel" as "vöGEL")

    # H
    '\u0068\u0061': '\u30CF',  # ha -> ハ (Short "ha" as "HAnd")
    '\u0068\u025B': '\u30D8',  # hɛ -> ヘ (Short "he" as "HErbst")
    '\u0068\u026A': '\u30D2',  # hɪ -> ヒ (Short "hi" as "HIn")
    '\u0068\u0069': '\u30D2',  # hi -> ヒー (Long "hie" as "HIEr")
    '\u0068\u006F': '\u30DB',  # ho -> ホ (Short "ho" as "HOtel")
    '\u0068\u0254': '\u30DB',  # hɔ -> ホ (Short stressed "ho" as "HEUte")
    '\u0068\u028A': '\u30D5',  # hʊ -> フ (Short "hu" as "HUnd")
    '\u0068\u0075': '\u30D5',  # hu -> フ (Long "hu" as "HUt")
    '\u0068\u028F': '\u30D2\u30E5',  # hʏ -> ヒュ (Short stressed "hü" as "umHÜllen")
    '\u0068\u0153': '\u30DB\u30A7',  # hœ -> ホェ (Short stressed "hö  as "HÖlzerne")
    '\u0068\u00F8': '\u30DB\u30A7',  # hø -> ホェ (Long stressed "ho" as "HOlen")
    '\u0259\u006E': '\u30D8\u30F3',  # ən -> ヘン (Short "hen" as "geHEN")

    # J
    '\u006A\u0061': '\u30E4',  # ja -> ヤ (Long "jah" as "JAHr")
    '\u006A\u0065': '\u30A4\u30A7',  # je -> イェ (Long stressed "je" as "JEden")
    '\u006A\u0069': '\u30B8',  # ji -> ジ (Long "ji" as "oktroYIeren")
    '\u006A\u028A': '\u30E6',  # jʊ -> ユ (Short stressed "ju" as "JUnge")
    '\u006A\u0075': '\u30E6',  # ju -> ユ (Long stressed "ju" as "JUni")

    # K
    '\u006B': '\u30AF',  # k -> ク (Short stressed "k" as "Klein")
    '\u006B\u0061': '\u30AB',  # ka -> カ (Short "ka" as "KEIn")
    '\u006B\u0259': '\u30B1',  # kə -> ケ (Short "ke" as "rabauKE")
    '\u006B\u026A': '\u30AD',  # kɪ -> キ (Short "ki" as "KInd")
    '\u006B\u0069': '\u30AD',  # ki -> キ (Short "ki" as "KInd")
    '\u006B\u0254': '\u30B3',  # kɔ -> コ (Short "ko" as "KOmmt")
    '\u006B\u006F': '\u30B3',  # ko -> コ (Short "cho" as "melanCHOlie") 
    '\u006B\u028A': '\u30AF',  # kʊ -> ク (Short secondary stressed "ku" as "zuKUnft")
    '\u006B\u0075': '\u30AF',  # ku -> ク (Short secondary stressed "ku" as "KUh")
    '\u006B\u0079': '\u30AD\u30E5',  # ky -> キュ (Long "küh" as KÜHl)
    '\u006B\u028F': '\u30AD\u30E5',  # kʏ -> キュ (Short stressed "kü" as KÜche)
    '\u006B\u006E\u0329': '\u30B1\u30F3',  # kn̩ -> ケン (Short "ken" as "wolKEN")

    # L
    '\u006C': '\u30EB',  # l -> ル (Short "l" as "aLt")
    '\u006C\u0061': '\u30E9',  # la -> ラ (Short "la" as "deutschLAnd")
    '\u006C\u0259': '\u30EC',  # lə -> レ (Short "le" as "schuLE")
    '\u006C\u025B': '\u30EC',  # lɛ -> レ 
    '\u006C\u0065': '\u30EC',  # le -> レ (Long "le" as "probLEm")
    '\u006C\u0069': '\u30EA',  # li -> リ (Short "li" as "juLI")
    '\u006C\u026A': '\u30EA',  # lɪ -> リ (Short "li" as "frühLIng")
    '\u006C\u0254': '\u30ED',  # lɔ -> ロ (Short stressed "lo" as "balLOn")
    '\u006C\u006F': '\u30ED',  # lo -> ロ (Long "lo" as "fLOgen")
    '\u006C\u028A': '\u30EB',  # lʊ -> ル (Short "lu" as "fLUsses")
    '\u006C\u0075': '\u30EB',  # lu -> ル (Long "lu" as "bLUme")
    '\u006C\u0153': '\u30ED',  # lœ -> ロ (Short "lö" as "gLÖckchen")
    '\u006C\u0329': '\u30EB',  # l̩ -> ル (Short "l" as "spiegeLte")

    # M
    '\u006D': '\u30E0',  # m -> ム (Short "m" as "filM")
    '\u006D\u0061': '\u30DE',  # ma -> マ (Short "ma" as "MAnn")
    '\u006D\u0250': '\u30DE',  # mɐ -> マ (Short "mer" as "zimMER")
    '\u006D\u0259': '\u30E1',  # mə -> メ (Short "me" as "bluME")
    '\u006D\u025B': '\u30E1',  # mɛ -> メ (Short "me" as "mÄrz")
    '\u006D\u0065': '\u30E1',  # me -> メ (Short "me" as "MElancholie")
    '\u006D\u0069': '\u30DF',  # mi -> ミ (Long stressed "mi" as "faMIlie")
    '\u006D\u026A': '\u30DF',  # mɪ -> ミ (Short "mi" as "MIttag")
    '\u006D\u006F': '\u30E2',  # mo -> モ (Short "mo" as "MOment")
    '\u006D\u0254': '\u30E2',  # mɔ -> モ (Short "mo" as "MOrgen")
    '\u006D\u0075': '\u30E0',  # mu -> ム (Short "mu" as "MUsik")
    '\u006D\u028A': '\u30E0',  # mʊ -> ム (Short stressed "mu" as "MUtter")
    '\u006D\u00F8': '\u30E2\u30A7',  # mø -> モェ (Long streesed "mö" as "MÖwen")
    '\u006D\u028F': '\u30DF\u30E5',  # mʏ -> ミュ (Short stressed "mü" as "Müller")
    '\u006D\u0079': '\u30DF\u30E5',  # my -> ミュ (Long stressed "mü" as "geMÜtlich")
    '\u006D\u006C\u0329': '\u30E1\u30EB',  # ml̩ -> メル (Short "mel" as "himMEL")
    '\u006D\u02C8\u0070\u006A\u0075': '\u30F3\u30D4\u30E5',  # mˈpju -> ンピュ

    # N
    '\u006E': '\u30F3',  # n -> ン (Short "n" as "deutschlaNd")
    '\u014B': '\u30F3\u30B0',  # ŋ -> ング (Short "ng" as "laNG")
    '\u006E\u0061': '\u30CA',  # na -> ナ (Short "na" as "moNAt")
    '\u006E\u0250': '\u30CA',  # nɐ -> ナ (Short "ner" as "donNERstag")
    '\u006E\u0259': '\u30CD',  # nə -> ネ (Short "ne" as "bieNE")
    '\u006E\u0065': '\u30CD',  # ne -> ネ (Long "nee" as "schNEE")
    '\u006E\u025B': '\u30CD',  # nɛ -> ネ (Short "ne" as "schNEll")
    '\u006E\u026A': '\u30CB',  # nɪ -> ニ (Short "ni" as "sonnenfinsterNIs")
    '\u006E\u0069': '\u30CB',  # ni -> ニ (Short "ni" as "uNIversität")
    '\u006E\u0254': '\u30CE',  # nɔ -> ノ (Short "neu" as "NEUn")
    '\u006E\u006F': '\u30CE',  # no -> ノ (Short "no" as "NOvember")
    '\u006E\u0075': '\u30CC',  # nu -> ヌ (Short "nu" as "jaNUar")
    '\u006E\u028A': '\u30CC',  # nʊ -> ヌ (Short "nu" as "subregNUm")
    '\u014B\u006B': '\u30F3\u30AF',  # ŋk -> ンク (Short "nk" as "baNK")
    '\u014B\u0259': '\u30F3\u30B2',  # ŋə -> ンゲ (Short "nge" as "faNGEn")
    '\u014B\u0250': '\u30F3\u30AC',  # ŋɐ -> ンガ (Short "nger" as "fiNGER")
    '\u014B\u006B\u0259': '\u30F3\u30B1',  # ŋkə -> ンケ (Short "nke" as "daNKE")
    '\u014B\u006B\u006E\u0329': '\u30F3\u30B1\u30F3',  # ŋkn̩ -> ンケン (Short "nken" as "deNKEN")
    '\u014B\u006B\u006C\u0329': '\u30F3\u30B1\u30EB',  # ŋkl̩ -> ンケル (Short "nkel" as "duNKELheit")

    # P
    '\u0070': '\u30D7',  # p -> プ (Short "p" as "Problem")
    '\u0070\u0061': '\u30D1',  # pa -> パ (Short "pa" as "jaPAn")
    '\u0070\u0250': '\u30D1',  # pɐ -> パ (Short "pa" as "jaPAn")
    '\u0070\u0069': '\u30D4',  # pi -> ピ (Long "pie" as "sPIElen")
    '\u0070\u026A': '\u30D4',  # pɪ -> ピ (Short "pi" as "PIttoresk")
    '\u0070\u0065': '\u30DA',  # pe -> ペ (Long "pe" as "PEter")
    '\u0070\u0259': '\u30DA',  # pə -> ペ 
    '\u0070\u0079': '\u30D4\u30E5',  # py -> ピュ (Long "pü" as "sPÜrte")
    '\u0070\u0361\u0066': '\u30D7\u30D5',  # p͡f -> プフ (Short "pf" as "baumstumPF")
    '\u0070\u0361\u0066\u0061': '\u30D5\u30A1',  # p͡fa -> ファ ("P" has to be silent here)
    '\u0070\u0361\u0066\u006E\u0329': '\u30D7\u30D5\u30A7\u30F3',  # p͡fn̩ -> プフェン (Short "pfen" as "troPFEN")

    # Q
    '\u006B\u0076\u0061': '\u30AF\u30A1',  # kva -> クァ (Short "qua" as "QUArk")
    '\u006B\u0076\u0061': '\u30AF\u30A1',  # kva -> クァ (Short "qua" as "QUArk")
    '\u006B\u0076\u0250': '\u30AF\u30A1',  # kvɐ -> クァ (Short "qua" as "QUArk")
    '\u006B\u0076\u0065': '\u30AF\u30A7',  # kve -> クェ (Long "que" as "QUEr")
    '\u006B\u0076\u025B': '\u30AF\u30A7',  # kvɛ -> クェ (Short stressed "que" as "QUElle")
    '\u006B\u0076\u0259': '\u30AF\u30A7',  # kvə -> クェ (Short stressed "que" as "QUElle")
    '\u006B\u0076\u026A': '\u30AF\u30A3',  # kvɪ -> クィ (Short "qui" as "QUIz")
    '\u006B\u0076\u0069': '\u30AF\u30A3',  # kvi -> クィ (Short "qui" as "quiekt")
    '\u006B\u0076\u006F': '\u30AF\u30A9',  # kvo -> クォ (Short "quo" as "QUOte")
    '\u006B\u0076\u0254': '\u30AF\u30A9',  # kvɔ -> クォ (Short "quo" as "QUOte")

    # R
    '\u0281': '\u30A2',  # ʁ -> ア (Soft German "r" as "faRbe")
    '\u0281\u0061': '\u30E9',  # ʁa -> ラ (Short "ra" as "fRAu")
    '\u0281\u0250': '\u30E9',  # ʁɐ -> ラ (Short "re" as "ihREr") 
    '\u0281\u0251': '\u30E9',  # ʁɑ -> ラ (Short "ra" as "oRAnge")
    '\u0281\u0259': '\u30EC',  # ʁə -> レ (Short "re" as "fahREn")
    '\u0281\u025B': '\u30EC',  # ʁɛ -> レ (Short "re" as "spREchen")
    '\u0281\u0065': '\u30EC',  # ʁe -> レ (Long "reh" as "dREHte")
    '\u0281\u026A': '\u30EA',  # ʁɪ -> リ (Short "ri" as "apRIl")
    '\u0281\u0069': '\u30EA',  # ʁi -> リ (Short "ri" as "hoRIzont")
    '\u0281\u0254': '\u30ED',  # ʁɔ -> ロ (Short "ro" as "fREUnd")
    '\u0281\u006F': '\u30ED',  # ʁo -> ロ (Short "ro" as "pROblem")
    '\u0281\u0075': '\u30EB',  # ʁu -> ル (Short "ru" as "febRUar")
    '\u0281\u028A': '\u30EB',  # ʁʊ -> ル (Short "ru" as "dämmeRUng")
    '\u0281\u0079': '\u30EA\u30E5',  # ʁy -> リュ (Long "rüh" as "fRÜHstück")
    '\u0281\u028F': '\u30EA\u30E5',  # ʁʏ -> リュ (Short "rü" as "zuRÜck")

    # S
    '\u0073': '\u30B9',  # s -> ス (Short "s" as "buS")
    '\u0283': '\u30B7\u30E5',  # ʃ -> シュ (Short "sch" as "SCHnee")
    '\u007A\u0250': '\u30B6',  # zɐ -> ザ (Short "sa" as "häuSERn")
    '\u0073\u0250': '\u30B5',  # sɐ -> サ (Short "ser" as "wasSER")
    '\u0073\u0061': '\u30B5',  # sa -> サ (Short "sa" as "XAnten")
    '\u007A\u0061': '\u30B6',  # za -> ザ (Short "sa" as "sein")
    '\u0073\u0259': '\u30BB',  # sə -> セ (Short "ße" as "straSSE")
    '\u007A\u0259': '\u30BC',  # zə -> ゼ (Short "se" as "tauSEnd")
    '\u007A\u0065': '\u30BC',  # ze -> ゼ (Long "see" as "SEE")
    '\u007A\u025B': '\u30BC',  # zɛ -> ゼ (Short "se" as "SEchs")
    '\u007A\u026A': '\u30BA\u30A3',  # zɪ -> ズィ (Short "si" as "SIch")
    '\u007A\u0069': '\u30BA\u30A3',  # zi -> ズィ (Short "si" as "univerSItät")
    '\u007A\u006F': '\u30BE',  # zo -> ゾ (Long "soh" as "SOHn")
    '\u007A\u0254': '\u30BE',  # zɔ -> ゾ (Short stressed "so" as "SOmmer")
    '\u0073\u0254': '\u30BE',  # sɔ -> ゾ (Short stressed "so" as "SOmmer")
    '\u007A\u0075': '\u30BA',  # zu -> ズ (Long stressed "su" as "SUche")
    '\u007A\u028A': '\u30BA',  # zʊ -> ズ (Short "su" as "SUbordo")
    '\u0283\u0061': '\u30B7\u30E3',  # ʃa -> シャ (Short stressed "scha" as "entSCHEIden")
    '\u0283\u0259': '\u30B7\u30A7',  # ʃə -> シェ (Short "sche" as "taSCHE")    
    '\u0283\u025B': '\u30B7\u30A7',  # ʃɛ -> シェ (Short "sche" as "geSCHEnk")
    '\u0283\u026A': '\u30B7',  # ʃɪ -> シ (Short "schi" as "muSCHI")
    '\u0283\u0069': '\u30B7',  # ʃi -> シ (Short "schi" as "muSCHI")
    '\u0283\u0254': '\u30B7\u30E7',  # ʃɔ -> ショ (Short stressed "scho" as "SCHOrnstein")
    '\u0283\u006F': '\u30B7\u30E7',  # ʃo -> ショ (Short "scho" as "SCHOn")
    '\u0283\u0075': '\u30B7\u30E5',  # ʃu -> シュ (Long stressed "schu" as "SCHUle")
    '\u0283\u00F8': '\u30B7\u30E5',  # ʃø -> シュ (Long "schö" as "SCHÖn")
    '\u0283\u006C\u0329': '\u30B7\u30A7\u30EB',  # ʃl̩ -> シェル (Short "schel" as "raSCHELn")
    '\u007A\u006E\u0329': '\u30BC\u30F3',  # zn̩ -> ゼン (Short "sen" as "tauSENd")
    '\u007A\u006C\u0329': '\u30BC\u30EB',  # zl̩ -> ゼル (Short "sel" as "inSEL")
    '\u0283\u006E\u0329': '\u30B7\u30A7\u30F3',  # ʃn̩ -> シェン (Short "schen" as "rauSCHENden")

    # T
    '\u0074': '\u30C8',  # t -> ト (Short "t" as "alT")
    '\u0074\u0061': '\u30BF',  # ta -> タ (Short "ta" as "sTAnd")
    '\u0074\u0250': '\u30BF',  # tɐ -> タ (Short "ter" as "mutTER")
    '\u0074\u0259': '\u30C6',  # tə -> テ (Short "te" as "heuTE")
    '\u0074\u025B': '\u30C6',  # tɛ -> テ (Short stressed "te" as "hoTEl")
    '\u0074\u0065': '\u30C6',  # te -> テ (Long "te" as "sTEhen") 
    '\u0074\u0069': '\u30C6\u30A3',  # ti -> ティ (Long "tie" as "TIEr")
    '\u0074\u026A': '\u30C6\u30A3',  # tɪ -> ティ (Short "ti" as "aalarTIg")
    '\u0074\u006F': '\u30C8',  # to -> ト (Short "to" as "auTO")
    '\u0074\u0254': '\u30C8',  # tɔ -> ト (Short "to" as "auTO")
    '\u0074\u0075': '\u30C8\u30A5',  # tu -> トゥ (Short "tu" as "sTUdent")
    '\u0074\u028A': '\u30C8\u30A5',  # tʊ -> トゥ (Short "tu" as "sTUdent")
    '\u0074\u028F': '\u30C8\u30A5',  # tʏ -> トゥ (Short "tü" as "frühsTÜck)
    '\u0074\u0079': '\u30C8\u30A5',  # ty -> トゥ (Long "tü" as "TÜr")
    '\u0074\u0361\u0283': '\u30C1\u30E5',  # t͡ʃ -> チュ (Short "tsch" as "deuTSCHland")
    '\u0074\u0361\u0073': '\u30C4',  # t͡s -> ツ (Short "ts" as "geburTStag")
    '\u0074\u006E\u0329': '\u30C6\u30F3',  # tn̩ -> テン (Short "ten" as "antworTEN")
    '\u0074\u0361\u0283\u025B': '\u30C1\u30A7',  # t͡ʃɛ -> チェ (Short "che" as "CHAtten")
    '\u0074\u0361\u0283\u0069': '\u30C1',  # t͡ʃi -> チ (Short "tschi" as "liTSCHI")
    '\u0074\u0361\u0073\u0259': '\u30C3\u30C4\u30A7',  # t͡sə -> ッツェ (Short "tze" as "kaTZE")
    '\u0074\u0361\u0283\u0250': '\u30C1\u30E3',  # -> チャ (Short "tsche" as "zwiTSCHErn")

    # V
    '\u0066\u0061': '\u30D5\u30A1',  # fa -> ファ (Long secondary stressed "va" as "großVAter")
    '\u0066\u025B': '\u30D5\u30A7',  # fɛ -> フェ (Short "ve" as "VErsank")
    '\u0076\u025B': '\u30F4\u30A7',  # vɛ -> ヴェ (Short stressed "ve" as "noVEmber")
    '\u0076\u0069': '\u30F4\u30A3',  # vi -> ヴィ (Short "vi" as "VIolett")
    '\u0066\u0069': '\u30D5\u30A3',  # fi -> フィ (Short "vie" as "VIElleicht")
    '\u0066\u0069': '\u30D5\u30A3',  # fi -> フィ (Long "vie" as "VIEr")
    '\u0066\u006F': '\u30D5\u30A9',  # fo -> フォ (Long "vo" as "VOr")
    '\u0066\u00F8': '\u30D5\u30A9\u30A8',  # fø -> フォエ (Long stressed "vö" as "VÖgeln")

    # W
    '\u0076\u0061': '\u30F4\u30A1',  # va -> ヴァ (Short "wa" as "schWArz")
    '\u0076\u0251': '\u30F4\u30A1',  # vɑ -> ヴァ 
    '\u0076\u0250': '\u30F4\u30A1',  # vɐ -> ヴァ 
    '\u0076\u025B': '\u30F4\u30A7',  # vɛ -> ヴェ (Short "we" as "schWEster")
    '\u0076\u0065': '\u30F4\u30A7',  # ve -> ヴェ (Long "weh" as "WEHt")
    '\u0076\u026A': '\u30F4\u30A3',  # vɪ -> ヴィ (Short "wi" as "WInd")
    '\u0076\u0254': '\u30F4\u30A9',  # vɔ -> ヴォ (Short "wo" as "WOrt")
    '\u0076\u006F': '\u30F4\u30A9',  # vo -> ヴォ (Long stressed "woh" as "WOHnen")
    '\u0076\u028A': '\u30F4',  # vʊ -> ヴ (Short stressed "wu" as "WUrde")
    '\u0076\u00F8': '\u30F4\u30A9\u30A8',  # vø -> ヴォエ (Long stressed "wöh" as "geWÖHnlich")
    '\u0076\u0153': '\u30F4\u30A9\u30A8',  # vœ -> ヴォエ ()
    '\u0076\u006E\u0329': '\u30F4\u30A7\u30F3',  # vn̩ -> ヴェン (Short "wen" as "möWEN")

    # Z
    '\u0074\u0361\u0073\u0061': '\u30C4\u30A1',  # t͡sa -> ツァ (Short "za" as "ZEIt")
    '\u0074\u0361\u0073\u0065': '\u30C4\u30A7',  # t͡se -> ツェ (Long "zeh" as "ZEHn")
    '\u0074\u0361\u0073\u025B': '\u30C4\u30A7',  # t͡sɛ -> ツェ (Short stressed "ze" as "deZEmber")
    '\u0074\u0361\u0073\u026A': '\u30C4\u30A3',  # t͡sɪ -> ツィ (Short stressed "zi" as "ZImmer")
    '\u0074\u0361\u0073\u0069': '\u30C4\u30A3',  # t͡si -> ツィ (Long stressed "zieh" as "ZIEHen")
    '\u0074\u0361\u0073\u006F': '\u30C4\u30A9',  # t͡so -> ツォ (Long "zo" as "ZOg")
    '\u0074\u0361\u0073\u0254': '\u30C4\u30A9',  # t͡sɔ -> ツォ (Short stressed "zo" as "horiZOnt")
    '\u0074\u0361\u0073\u0075': '\u30C4',  # t͡su -> ツ (Short "zu" as "ZUrück")
    '\u0074\u0361\u0073\u028F': '\u30C4',  # t͡sʏ -> ツ (Short secondary stressed "zü" as "angeZÜndet"W)
    '\u0074\u0361\u0073\u006E\u0329': '\u30C4\u30A7\u30F3',  # t͡sn̩ -> ツェン (Short "zen" as "ächZEN")
    '\u0361\u0073\u0074\u006E\u0329': '\u30C4\u30C6\u30F3',  # ͡stn -> ツテン (Short "zten" as "letZTEN")

    # Ü
    '\u0079': '\u30E6',  # y -> ユ (Long stressed "ü" as "Über")

    # Edge cases for T with preceding short vowel
    '\u0062\u025B\u0074': '\u30D9\u30C3\u30C8',  # bɛt -> ベット (Short "t" with preceding short vowel as "BETT")
    '\u0074\u0061\u0074': '\u30BF\u30C3\u30C8',  # tat -> タット (Short "t" with preceding short vowel as "sTADT")
    '\u02C8\u006C\u025B\u0074': '\u30EC\u30C3\u30C8',  # ˈlɛt -> レット (Short "t" with preceding short vowel as "vioLETT")
    '\u02C8\u006D\u026A\u0074': '\u30DF\u30C3\u30C8',  # ˈmɪt -> ミット (Short "t" with preceding short vowel as "miTTwoch")

    # Edge cases for CH "x" (Pronunciation of "ch" depends on the preceding vowel
    '\u0078\u0259': '\u30C3\u30D8',  # xə -> ッヘ (Short "che" as "spraCHE")
    '\u0078\u0074\u0259': '\u30C3\u30D8\u30C6',  # xtə -> ッヘテ (Short "chte" as "daCHTE")
    '\u0061\u0078\u0074': '\u30A2\u30C3\u30CF\u30C8',  # axt -> アッハト (Short "cht" with preceding "a" as "ACHT")
    '\u006D\u0061\u0078\u0074': '\u30DE\u30C3\u30CF\u30C8',  # -> マッハト (Short "cht" with preceding "ma" as "MACHT")
    '\u006E\u0061\u0078': '\u30CA\u30C3\u30CF',  # nax -> ナッハ (Short "ch" with preceding "na" as "NACH")
    '\u006E\u0254\u0078': '\u30CE\u30C3\u30DB',  # nɔx -> ノッホ (Short "ch" with preceding "no" as "NOCH")
    '\u0064\u0254\u0078': '\u30C9\u30C3\u30DB',  # dɔx -> ドッホ (Short "ch" with preceding "do" as "DOCH")
    '\u0064\u0061\u0078': '\u30C0\u30C3\u30CF',  # dax -> ダッハ (Short "ch" with preceding "da" as "daCH")
    '\u0078\u006E': '\u30C3\u30D8\u30F3',  # xn -> ッヘン (Short "chen" as "spraCHEN")
    '\u028A\u032F\u0078': '\u30A6\u30C3\u30D5',  # ʊ̯x -> ウッフ (Short "uch" as "raUCH")
    '\u0062\u0061\u0078': '\u30D0\u30C3\u30CF',  # bax -> バッハ (Short "ch" with preceding "ba" as "BACH")
    '\u0074\u0254\u0078': '\u30C8\u30C3\u30DB',  # tɔx -> トッホ (Short "ch" with preceding "to" as "toCHter")
    '\u006B\u0254\u0078': '\u30B3\u30C3\u30DB',  # kɔx -> コッホ (Short "ch" with preceding "ko" as "koCHt")
    '\u0281\u0061\u0078': '\u30E9\u30C3\u30CF',  # ʁax -> ラッハ (Short "ch" with preceding "ra" as "herunterbraCHst")
    '\u0283\u0061\u0078': '\u30B7\u30E3\u30C3\u30CF',  # ʃax -> シャッハ (Short "ch" with preceding "scha" as "schaCH")
    '\u0066\u006C\u0075\u0078\u028A': '',  # fluxʊ -> フルッフ
    '\u0076\u0254\u0078': '\u30F4\u30A9\u30C3\u30DB',  # vɔx -> ヴォッホ (Short "ch" with preceding "wo" as "mittWOCH")
    '\u0076\u0254\u0078\u0259': '\u30F4\u30A9\u30C3\u30D8',  # vɔxə -> ヴォッヘ (Short "ch" with preceding "wo" as "mittWOCH")
    '\u006E\u0061\u02D0\u0078': '\u30CA\u30C3\u30CF',  # naːx -> ナッハ
    '\u0062\u0075\u02D0\u0078': '\u30D6\u30FC\u30C3\u30D5',  # buːx -> ブーッフ (Long "ch" with preceding "bu" as "BUCH")
    '\u0074\u0075\u02D0\u0078': '\u30C8\u30A5\u30FC\u30C3\u30D5',  # tuːx -> トゥーッフ (Long "ch" with predecing "tu" as "TUCH")
    
    # Edge cases for CH "ç" 
    '\u00E7': '\u30C3\u30D2',  # ç -> ッヒ (Short "ch" anywhere not previously covered as "niCHt")
    '\u00E7\u0000': '\u30C3\u30D2',  # çNULL -> ッヒ (Short "ch" at the end of a word as "iCH")
    '\u00E7\u0259': '\u30C3\u30D2\u30A7',  # çə -> ッヒェ (Short "che" the middle of the word as "glöckCHEn")
    '\u0000\u00E7\u0065': '\u30B1',  # NULLçe -> ケ (Short "che" at the start of a word as "CHEmie")
    '\u00E7\u006E\u0329': '\u30C3\u30D2\u30A7\u30F3',  # çn̩ -> ッヒェン (Short "chen" as "reCHEN")

    # Edge cases for N the middle of word as "nn", e.g. "soNNe"
    '\u02C8\u007A\u0254\u006E\u0259': '\u30BE\u30F3\u30CD',  # ˈzɔnə -> ゾンネ (Short "ne" as "soNNE")

    # Edge cases for M pronunciation, sometimes the Katakana "ン" is pronuounced "m" which is closer than "ム"
    '\u006D\u0062\u0250': '\u30F3\u30D0',  # mbɐ -> ンバ (Short "mber" as "September")

    # Edge cases general
    '\u0281\u00E7\u0000': '\u30A2\u30B7\u30E5',  # ʁç -> アシュ (Short "rch" at the end of the word as "stoRCH")
    '\u0073\u006E\u0329': '\u30C3\u30BB\u30F3',  # sn̩ -> ッセン (Short "ssen" as "eSSEN")
    '\u0073\u006E\u0329\u0074': '\u30B6\u30F3\u30AF\u30C8',  # sn̩t -> ザンクト	("St." pronounced as "Sankt")
    '\u0076\u026A\u0073\u0259': '\u30F4\u30A3\u30C3\u30BB',  # vɪsə -> ヴィッセ (Short "wisse" as "geWISSE")
    '\u02C8\u006E\u025B\u02D0\u0259': '\u30CD\u30FC\u30D8',  # ˈnɛːə -> ネーヘ ("nähe")

    # Special characters
    '\u0000': '',  # NULL character should not map to anything, if not used
    '\u0020': '\u0020',  # Space character just maps to space again
    '\u002D': '',  # - -> 
    '\u0294': '',  # ʔ ->
    '\u02C8': '',  # ˈ -> 
    '\u02D0': '\u30FC',  # ː -> ー
    '\u02CC': '',  # ˌ ->
    '\u0329': '',  # ˌ ->
    '\u032F': '',  # ̯  ->
    '\u0303': '',  # ̃  -> 
    '\u0361': '',  # ͡  ->
}
