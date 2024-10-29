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
    '\u0250': '\u30A2',  # ɐ -> ア (Short "er" as in "schleiER")
    '\u0259': '\u30A8',  # ə -> エ (Short "e" as in "familiE")
    '\u025B': '\u30A8',  # ɛ -> エ (Short "e" as in "Entscheiden")
    '\u026A': '\u30A4',  # ɪ -> イ (Short "i" as in "DEUtschland")
    '\u028A': '\u30A6',  # ʊ -> ウ (Short "u" as in "Und")
    '\u006F': '\u30AA',  # o -> オ (Short "o" as in "viOlett")
    '\u0254': '\u30AA',  # ɔ -> オ (Short "o" as in "Oktober")
    '\u0153': '\u30AA\u30A7',  # œ -> オェ (Short stressed "ö" as in "Öffnen")

    # Long vowels
    '\u0065': '\u30A8',  # e -> エ (Long "e" as in "Er")
    '\u0069': '\u30A4',  # i -> イ (Long "i" as in "IHr")
    '\u0075': '\u30A6',  # u -> ウ (Long "u" as in "UHr")
    '\u0061\u02D0\u0250\u032F': '\u30A2\u30FC',  # aːɐ̯  -> アー (Very long "ar" as in "januAR")

    # B
    '\u0062': '\u30D6',  # b -> ブ (Short "b" as in "Brief")
    '\u0062\u0061': '\u30D0',  # ba -> バ (Short "ba" as in "BAllon")
    '\u0062\u0250': '\u30D0',  # bɐ -> バ (Short "ber" as in "oktoBER")
    '\u0062\u025B': '\u30D9',  # bɛ -> ベ (Short "be" as in "BEtt")
    '\u0062\u0259': '\u30D9',  # bə -> ベ (Short "be" as in "farBE")
    '\u0062\u026A': '\u30D3',  # bɪ -> ビ (Short stressed "bi" as in "BItte")
    '\u0062\u0069': '\u30D3',  # bi -> ビ (Long "bie" as in "BIEr")
    '\u0062\u006F': '\u30DC',  # bo -> ボ (Long "bo" as in "BOOt")
    '\u0062\u0254': '\u30DC',  # bɔ -> ボ -> (Short stressed "bo" as in "BÄUme")
    '\u0062\u028A': '\u30D6',  # bʊ -> ブ (Short "bu" as in "BUs")
    '\u0062\u0075': '\u30D6',  # bu -> ブ (Long stressed "bu" as in "geBUrtstag")
    '\u0062\u006E\u0329': '\u30D9\u30F3',  # bn̩ -> ベン (Silent "e" between "b" and "n" as in "abEnd")

    # C

    # D
    '\u0064': '\u30C9',  # d -> ド (Short "d" as in "Drei")
    '\u0064\u0061': '\u30C0',  # da -> ダ (Short "da" as in "DAs")
    '\u0064\u0250': '\u30C0',  # dɐ -> ダ (Short "der" as in "bruDER")
    '\u0064\u0259': '\u30C7',  # də -> デ (Short "de" as in "stunDE")
    '\u0064\u0065': '\u30C7',  # de -> デ (Short "de" as in "DEzember")
    '\u0064\u025B': '\u30C7',  # dɛ -> デ (Short "de" as in "DEs")
    '\u0064\u0069': '\u30C7\u30A3',  # di -> ディ (Long "die" as in "DIE")
    '\u0064\u026A': '\u30C7\u30A3',  # dɪ -> ディ (Short "di" as in "DIchter") 
    '\u0064\u0254': '\u30C9',  # dɔ -> ド (Short "do" as in "DOrf")
    '\u0064\u0075': '\u30C9\u30A5',  # du -> ドゥ (Long "du" as in "DU")
    '\u0064\u028A': '\u30C9\u30A5',  # dʊ -> ドゥ (Short stressed "du" as in "DUnkelheit")
    '\u0064\u006C\u0329': '\u30C7\u30EB',  # dl̩ -> デル (Short "del" as in in "verwanDELt")
    '\u0064\u006E\u0329': '\u30C7\u30F3',  # dn̩ -> デン (Short "den" as in "entscheiDEN")

    # F
    '\u0066': '\u30D5',  # f -> フ (Short "f" as in "brieF")
    '\u0066\u0061': '\u30D5\u30A1',  # fa -> ファ (Short "fa" as in "FAmilie")
    '\u0066\u0250': '\u30D5\u30A1',  # fɐ -> ファ (Short "fer" as in "uFER")
    '\u0066\u0065': '\u30D5\u30A7',  # fe -> フェ (Short "fe" as in "kafFEE")
    '\u0066\u026A': '\u30D5\u30A3',  # fɪ -> フィ (Short "fi" as in "FIlm")
    '\u0066\u0254': '\u30D5\u30A9',  # fɔ -> フォ (Short "fo" as in "FOrt")
    '\u0066\u028A': '\u30D5',  # fʊ -> フ (Short "fu" as in "FUchs")
    '\u0066\u028F': '\u30D5\u30E5',  # fʏ -> フュ (Short "fü" as in "FÜnf")
    '\u0066\u0079': '\u30D5\u30E5',  # fy -> フュ (Long "fü" as in "FÜr")
    '\u0066\u006E\u0329': '\u30D5\u30A7\u30F3',  # fn̩ -> フェン (Short "fen" as in "helFEN")

    # G
    '\u0261': '\u30B0',  # ɡ -> グ (Short "g" as in "Grün")
    '\u0261\u0061': '\u30AC',  # ɡa -> ガ (SHort stressed "ga" as in "verGAngenheit")
    '\u0261\u0259': '\u30B2',  # ɡə -> ゲ (Short "ge" as in "GEburtstag")
    '\u0261\u025B': '\u30B2',  # ɡɛ -> ゲ (Short "ge" as in "GEld")
    '\u0261\u0065': '\u30B2',  # ɡe -> ゲ (Short "ge" as in "GEld")
    '\u0261\u026A': '\u30AE',  # ɡɪ -> ギ (Short "gi" as in "beGInnen")
    '\u0261\u028A': '\u30B0',  # ɡʊ -> グ (Short stressed "gu" as in "auGUst")
    '\u0261\u0075': '\u30B0',  # ɡu -> グ (Long "gu" as in "GUt")
    '\u0261\u006E\u0329': '\u30B2\u30F3',  # ɡn̩ -> ゲン (Silent "e" between "g" and "n" as in "morGEN")
    '\u0261\u014B\u030D': '\u30B2\u30F3',  # ɡŋ̍ -> ゲン (Silent "e" between "g" and "n" as in "morGEN")
    '\u0261\u006C\u0329': '\u30B2\u30EB',  # ɡl̩ -> ゲル (Short "gel" as in "vöGEL")

    # H
    '\u0068\u0061': '\u30CF',  # ha -> ハ (Short "ha" as in "HAnd")
    '\u0068\u025B': '\u30D8',  # hɛ -> ヘ (Short "he" as in "HErbst")
    '\u0068\u026A': '\u30D2',  # hɪ -> ヒ (Short "hi" as in "HIn")
    '\u0068\u0069': '\u30D2',  # hi -> ヒー (Long "hie" as in "HIEr")
    '\u0068\u006F': '\u30DB',  # ho -> ホ (Short "ho" as in "HOtel")
    '\u0068\u0254': '\u30DB',  # hɔ -> ホ (Short stressed "ho" as in "HEUte")
    '\u0068\u028A': '\u30D5',  # hʊ -> フ (Short "hu" as in "HUnd")
    '\u0068\u0075': '\u30D5',  # hu -> フ (Long "hu" as in "HUt")
    '\u0068\u028F': '\u30D2\u30E5',  # hʏ -> ヒュ (Short stressed "hü" as in "umHÜllen")
    '\u0068\u0153': '\u30DB\u30A7',  # hœ -> ホェ (Short stressed "hö  as in "HÖlzerne")
    '\u0068\u00F8': '\u30DB\u30A7',  # hø -> ホェ (Long stressed "ho" as in "HOlen")
    '\u0259\u006E': '\u30D8\u30F3',  # ən -> ヘン (Short "hen" as in "geHEN")

    # J
    '\u006A\u0061': '\u30E4',  # ja -> ヤ (Long "jah" as in "JAHr")
    '\u006A\u0065': '\u30A4\u30A7',  # je -> イェ (Long stressed "je" as in "JEden")
    '\u006A\u028A': '\u30E6',  # jʊ -> ユ (Short stressed "ju" as in "JUnge")
    '\u006A\u0075': '\u30E6',  # ju -> ユ (Long stressed "ju" as in "JUni")

    # K
    '\u006B': '\u30AF',  # k -> ク (Short stressed "k" as in "Klein")
    '\u006B\u0061': '\u30AB',  # ka -> カ (Short "ka" as in "KEIn")
    '\u006B\u026A': '\u30AD',  # kɪ -> キ (Short "ki" as in "KInd")
    '\u006B\u0254': '\u30B3',  # kɔ -> コ (Short "ko" as in "KOmmt")
    '\u006B\u006F': '\u30B3',  # ko -> コ (Short "cho" as in "melanCHOlie") 
    '\u006B\u028A': '\u30AF',  # kʊ -> ク (Short secondary stressed "ku" as in "zuKUnft")
    '\u006B\u0079': '\u30AD\u30E5',  # ky -> キュ (Long "küh" as in KÜHl)
    '\u006B\u028F': '\u30AD\u30E5',  # kʏ -> キュ (Short stressed "kü" as in KÜche)
    '\u006B\u006E\u0329': '\u30B1\u30F3',  # kn̩ -> ケン (Short "ken" as in "wolKEN")

    # L
    '\u006C': '\u30EB',  # l -> ル (Short "l" as in "aLt")
    '\u006C\u0061': '\u30E9',  # la -> ラ (Short "la" as in "deutschLAnd")
    '\u006C\u0259': '\u30EC',  # lə -> レ (Short "le" as in "schuLE")
    '\u006C\u025B': '\u30EC',  # lɛ -> レ 
    '\u006C\u0065': '\u30EC',  # le -> レ (Long "le" as in "probLEm")
    '\u006C\u0069': '\u30EA',  # li -> リ (Short "li" as in "juLI")
    '\u006C\u026A': '\u30EA',  # lɪ -> リ (Short "li" as in "frühLIng")
    '\u006C\u0254': '\u30ED',  # lɔ -> ロ (Short stressed "lo" as in "balLOn")
    '\u006C\u006F': '\u30ED',  # lo -> ロ (Long "lo" as in "fLOgen")
    '\u006C\u028A': '\u30EB',  # lʊ -> ル (Short "lu" as in "fLUsses")
    '\u006C\u0075': '\u30EB',  # lu -> ル (Long "lu" as in "bLUme")
    '\u006C\u0153': '\u30ED',  # lœ -> ロ (Short "lö" as in "gLÖckchen")
    '\u006C\u0329': '\u30EB',  # l̩ -> ル (Short "l" as in "spiegeLte")

    # M
    '\u006D': '\u30E0',  # m -> ム (Short "m" as in "filM")
    '\u006D\u0061': '\u30DE',  # ma -> マ (Short "ma" as in "MAnn")
    '\u006D\u0250': '\u30DE',  # mɐ -> マ (Short "mer" as in "zimMER")
    '\u006D\u0259': '\u30E1',  # mə -> メ (Short "me" as in "bluME")
    '\u006D\u025B': '\u30E1',  # mɛ -> メ (Short "me" as in "mÄrz")
    '\u006D\u0065': '\u30E1',  # me -> メ (Short "me" as in "MElancholie")
    '\u006D\u0069': '\u30DF',  # mi -> ミ (Long stressed "mi" as in "faMIlie")
    '\u006D\u026A': '\u30DF',  # mɪ -> ミ (Short "mi" as in "MIttag")
    '\u006D\u006F': '\u30E2',  # mo -> モ (Short "mo" as in "MOment")
    '\u006D\u0254': '\u30E2',  # mɔ -> モ (Short "mo" as in "MOrgen")
    '\u006D\u0075': '\u30E0',  # mu -> ム (Short "mu" as in "MUsik")
    '\u006D\u028A': '\u30E0',  # mʊ -> ム (Short stressed "mu" as in "MUtter")
    '\u006D\u00F8': '\u30E2\u30A7',  # mø -> モェ (Long streesed "mö" as in "MÖwen")
    '\u006D\u028F': '\u30DF\u30E5',  # mʏ -> ミュ (Short stressed "mü" as in "Müller")
    '\u006D\u0079': '\u30DF\u30E5',  # my -> ミュ (Long stressed "mü" as in "geMÜtlich")
    '\u006D\u006C\u0329': '\u30E1\u30EB',  # ml̩ -> メル (Short "mel" as in "himMEL")

    # N
    '\u006E': '\u30F3',  # n -> ン (Short "n" as in "deutschlaNd")
    '\u014B': '\u30F3\u30B0',  # ŋ -> ング (Short "ng" as in "laNG")
    '\u006E\u0061': '\u30CA',  # na -> ナ (Short "na" as in "moNAt")
    '\u006E\u0250': '\u30CA',  # nɐ -> ナ (Short "ner" as in "donNERstag")
    '\u006E\u0259': '\u30CD',  # nə -> ネ (Short "ne" as in "bieNE")
    '\u006E\u0065': '\u30CD',  # ne -> ネ (Long "nee" as in "schNEE")
    '\u006E\u025B': '\u30CD',  # nɛ -> ネ (Short "ne" as in "schNEll")
    '\u006E\u026A': '\u30CB',  # nɪ -> ニ (Short "ni" as in "sonnenfinsterNIs")
    '\u006E\u0069': '\u30CB',  # ni -> ニ (Short "ni" as in "uNIversität")
    '\u006E\u0254': '\u30CE',  # nɔ -> ノ (Short "neu" as in "NEUn")
    '\u006E\u006F': '\u30CE',  # no -> ノ (Short "no" as in "NOvember")
    '\u006E\u0075': '\u30CC',  # nu -> ヌ (Short "nu" as in "jaNUar")
    '\u014B\u006B': '\u30F3\u30AF',  # ŋk -> ンク (Short "nk" as in "baNK")
    '\u014B\u0259': '\u30F3\u30B2',  # ŋə -> ンゲ (Short "nge" as in "faNGEn")
    '\u014B\u0250': '\u30F3\u30AC',  # ŋɐ -> ンガ (Short "nger" as in "fiNGER")
    '\u014B\u006B\u0259': '\u30F3\u30B1',  # ŋkə -> ンケ (Short "nke" as in "daNKE")
    '\u014B\u006B\u006E\u0329': '\u30F3\u30B1\u30F3',  # ŋkn̩ -> ンケン (Short "nken" as in "deNKEN")
    '\u014B\u006B\u006C\u0329': '\u30F3\u30B1\u30EB',  # ŋkl̩ -> ンケル (Short "nkel" as in "duNKELheit")

    # P
    '\u0070': '\u30D7',  # p -> プ (Short "p" as in "Problem")
    '\u0070\u0061': '\u30D1',  # pa -> パ (Short "pa" as in "jaPAn")
    '\u0070\u0069': '\u30D4',  # pi -> ピ (Long "pie" as in "sPIElen")
    '\u0070\u0065': '\u30DA',  # pe -> ペ (Long "pe" as in "PEter")
    '\u0070\u0079': '\u30D4\u30E5',  # py -> ピュ (Long "pü" as in "sPÜrte")
    '\u0070\u0361\u0066': '\u30D7\u30D5',  # p͡f -> プフ (Short "pf" as in "baumstumPF")
    '\u0070\u0361\u0066\u0061': '\u30D5\u30A1',  # p͡fa -> ファ ("P" has to be silent here)
    '\u0070\u0361\u0066\u006E\u0329': '\u30D7\u30D5\u30A7\u30F3',  # p͡fn̩ -> プフェン (Short "pfen" as in "troPFEN")

    # Q
    '\u006B\u0076\u0065': '\u30AF\u30A7',  # kve -> クェ (Long "que" as in "QUEr")

    # R
    '\u0281': '\u30A2',  # ʁ -> ア (Soft German "r" as in "faRbe")
    '\u0281\u0061': '\u30E9',  # ʁa -> ラ (Short "ra" as in "fRAu")
    '\u0281\u0250': '\u30E9',  # ʁɐ -> ラ (Short "re" as in "ihREr") 
    '\u0281\u0251': '\u30E9',  # ʁɑ -> ラ (Short "ra" as in "oRAnge")
    '\u0281\u0259': '\u30EC',  # ʁə -> レ (Short "re" as in "fahREn")
    '\u0281\u025B': '\u30EC',  # ʁɛ -> レ (Short "re" as in "spREchen")
    '\u0281\u0065': '\u30EC',  # ʁe -> レ (Long "reh" as in "dREHte")
    '\u0281\u026A': '\u30EA',  # ʁɪ -> リ (Short "ri" as in "apRIl")
    '\u0281\u0069': '\u30EA',  # ʁi -> リ (Short "ri" as in "hoRIzont")
    '\u0281\u0254': '\u30ED',  # ʁɔ -> ロ (Short "ro" as in "fREUnd")
    '\u0281\u006F': '\u30ED',  # ʁo -> ロ (Short "ro" as in "pROblem")
    '\u0281\u0075': '\u30EB',  # ʁu -> ル (Short "ru" as in "febRUar")
    '\u0281\u028A': '\u30EB',  # ʁʊ -> ル (Short "ru" as in "dämmeRUng")
    '\u0281\u0079': '\u30EA\u30E5',  # ʁy -> リュ (Long "rüh" as in "fRÜHstück")
    '\u0281\u028F': '\u30EA\u30E5',  # ʁʏ -> リュ (Short "rü" as in "zuRÜck")

    # S
    '\u0073': '\u30B9',  # s -> ス (Short "s" as in "buS")
    '\u0283': '\u30B7\u30E5',  # ʃ -> シュ (Short "sch" as in "SCHnee")
    '\u007A\u0250': '\u30B6',  # zɐ -> ザ (Short "sa" as in "häuSERn")
    '\u0073\u0250': '\u30B5',  # sɐ -> サ (Short "ser" as in "wasSER")
    '\u007A\u0061': '\u30B6',  # za -> ザ (Short "sa" as in "sein")
    '\u0073\u0259': '\u30BB',  # sə -> セ (Short "ße" as in "straSSE")
    '\u007A\u0259': '\u30BC',  # zə -> ゼ (Short "se" as in "tauSEnd")
    '\u007A\u0065': '\u30BC',  # ze -> ゼ (Long "see" as in "SEE")
    '\u007A\u025B': '\u30BC',  # zɛ -> ゼ (Short "se" as in "SEchs")
    '\u007A\u026A': '\u30BA\u30A3',  # zɪ -> ズィ (Short "si" as in "SIch")
    '\u007A\u0069': '\u30BA\u30A3',  # zi -> ズィ (Short "si" as in "univerSItät")
    '\u007A\u006F': '\u30BE',  # zo -> ゾ (Long "soh" as in "SOHn")
    '\u007A\u0254': '\u30BE',  # zɔ -> ゾ (Short stressed "so" as in "SOmmer")
    '\u0073\u0254': '\u30BE',  # sɔ -> ゾ (Short stressed "so" as in "SOmmer")
    '\u007A\u0075': '\u30BA',  # zu -> ズ (Long stressed "su" as in "SUche") 
    '\u0283\u0061': '\u30B7\u30E3',  # ʃa -> シャ (Short stressed "scha" as in "entSCHEIden")
    '\u0283\u0259': '\u30B7\u30A7',  # ʃə -> シェ (Short "sche" as in "taSCHE")    
    '\u0283\u025B': '\u30B7\u30A7',  # ʃɛ -> シェ (Short "sche" as in "geSCHEnk")
    '\u0283\u0254': '\u30B7\u30E7',  # ʃɔ -> ショ (Short stressed "scho" as in "SCHOrnstein")
    '\u0283\u006F': '\u30B7\u30E7',  # ʃo -> ショ (Short "scho" as in "SCHOn")
    '\u0283\u0075': '\u30B7\u30E5',  # ʃu -> シュ (Long stressed "schu" as in "SCHUle")
    '\u0283\u00F8': '\u30B7\u30E5',  # ʃø -> シュ (Long "schö" as in "SCHÖn")
    '\u0283\u006C\u0329': '\u30B7\u30A7\u30EB',  # ʃl̩ -> シェル (Short "schel" as in "raSCHELn")
    '\u007A\u006E\u0329': '\u30BC\u30F3',  # zn̩ -> ゼン (Short "sen" as in "tauSENd")
    '\u007A\u006C\u0329': '\u30BC\u30EB',  # zl̩ -> ゼル (Short "sel" as in "inSEL")
    '\u0283\u006E\u0329': '\u30B7\u30A7\u30F3',  # ʃn̩ -> シェン (Short "schen" as in "rauSCHENden")

    # T
    '\u0074': '\u30C8',  # t -> ト (Short "t" as in "alT")
    '\u0074\u0061': '\u30BF',  # ta -> タ (Short "ta" as in "sTAnd")
    '\u0074\u0250': '\u30BF',  # tɐ -> タ (Short "ter" as in "mutTER")
    '\u0074\u0259': '\u30C6',  # tə -> テ (Short "te" as in "heuTE")
    '\u0074\u025B': '\u30C6',  # tɛ -> テ (Short stressed "te" as in "hoTEl")
    '\u0074\u0065': '\u30C6',  # te -> テ (Long "te" as in "sTEhen") 
    '\u0074\u0069': '\u30C6\u30A3',  # ti -> ティ (Long "tie" as in "TIEr")
    '\u0074\u006F': '\u30C8',  # to -> ト (Short "to" as in "auTO")
    '\u0074\u0075': '\u30C8\u30A5',  # tu -> トゥ (Short "tu" as in "sTUdent")
    '\u0074\u028A': '\u30C8\u30A5',  # tʊ -> トゥ (Short "tu" as in "sTUdent")
    '\u0074\u028F': '\u30C8\u30A5',  # tʏ -> トゥ (Short "tü" as in "frühsTÜck)
    '\u0074\u0079': '\u30C8\u30A5',  # ty -> トゥ (Long "tü" as in "TÜr")
    '\u0074\u0361\u0283': '\u30C1\u30E5',  # t͡ʃ -> チュ (Short "tsch" as in "deuTSCHland")
    '\u0074\u0361\u0073': '\u30C4',  # t͡s -> ツ (Short "ts" as in "geburTStag")
    '\u0074\u006E\u0329': '\u30C6\u30F3',  # tn̩ -> テン (Short "ten" as in "antworTEN")
    '\u0074\u0361\u0073\u0259': '\u30C3\u30C4\u30A7',  # t͡sə -> ッツェ (Short "tze" as in "kaTZE")
    '\u0074\u0361\u0283\u0250': '\u30C1\u30E3',  # -> チャ (Short "tsche" as in "zwiTSCHErn")

    # V
    '\u0066\u0061': '\u30D5\u30A1',  # fa -> ファ (Long secondary stressed "va" as in "großVAter")
    '\u0066\u025B': '\u30D5\u30A7',  # fɛ -> フェ (Short "ve" as in "VErsank")
    '\u0076\u025B': '\u30F4\u30A7',  # vɛ -> ヴェ (Short stressed "ve" as in "noVEmber")
    '\u0076\u0069': '\u30F4\u30A3',  # vi -> ヴィ (Short "vi" as in "VIolett")
    '\u0066\u0069': '\u30D5\u30A3',  # fi -> フィ (Short "vie" as in "VIElleicht")
    '\u0066\u0069': '\u30D5\u30A3',  # fi -> フィ (Long "vie" as in "VIEr")
    '\u0066\u006F': '\u30D5\u30A9',  # fo -> フォ (Long "vo" as in "VOr")
    '\u0066\u00F8': '\u30D5\u30A9\u30A8',  # fø -> フォエ (Long stressed "vö" as in "VÖgeln")

    # W
    '\u0076\u0061': '\u30F4\u30A1',  # va -> ヴァ (Short "wa" as in "schWArz")
    '\u0076\u025B': '\u30F4\u30A7',  # vɛ -> ヴェ (Short "we" as in "schWEster")
    '\u0076\u0065': '\u30F4\u30A7',  # ve -> ヴェ (Long "weh" as in "WEHt")
    '\u0076\u026A': '\u30F4\u30A3',  # vɪ -> ヴィ (Short "wi" as in "WInd")
    '\u0076\u0254': '\u30F4\u30A9',  # vɔ -> ヴォ (Short "wo" as in "WOrt")
    '\u0076\u006F': '\u30F4\u30A9',  # vo -> ヴォ (Long stressed "woh" as in "WOHnen")
    '\u0076\u028A': '\u30F4',  # vʊ -> ヴ (Short stressed "wu" as in "WUrde")
    '\u0076\u00F8': '\u30F4\u30A9\u30A8',  # vø -> ヴォエ (Long stressed "wöh" as in "geWÖHnlich")
    '\u0076\u006E\u0329': '\u30F4\u30A7\u30F3',  # vn̩ -> ヴェン (Short "wen" as in "möWEN")

    # Z
    '\u0074\u0361\u0073\u0061': '\u30C4\u30A1',  # t͡sa -> ツァ (Short "za" as in "ZEIt")
    '\u0074\u0361\u0073\u0065': '\u30C4\u30A7',  # t͡se -> ツェ (Long "zeh" as in "ZEHn")
    '\u0074\u0361\u0073\u025B': '\u30C4\u30A7',  # t͡sɛ -> ツェ (Short stressed "ze" as in "deZEmber")
    '\u0074\u0361\u0073\u026A': '\u30C4\u30A3',  # t͡sɪ -> ツィ (Short stressed "zi" as in "ZImmer")
    '\u0074\u0361\u0073\u0069': '\u30C4\u30A3',  # t͡si -> ツィ (Long stressed "zieh" as in "ZIEHen")
    '\u0074\u0361\u0073\u006F': '\u30C4\u30A9',  # t͡so -> ツォ (Long "zo" as in "ZOg")
    '\u0074\u0361\u0073\u0254': '\u30C4\u30A9',  # t͡sɔ -> ツォ (Short stressed "zo" as in "horiZOnt")
    '\u0074\u0361\u0073\u0075': '\u30C4',  # t͡su -> ツ (Short "zu" as in "ZUrück")
    '\u0074\u0361\u0073\u028F': '\u30C4',  # t͡sʏ -> ツ (Short secondary stressed "zü" as in "angeZÜndet"W)
    '\u0074\u0361\u0073\u006E\u0329': '\u30C4\u30A7\u30F3',  # t͡sn̩ -> ツェン (Short "zen" as in "ächZEN")
    '\u0361\u0073\u0074\u006E\u0329': '\u30C4\u30C6\u30F3',  # ͡stn -> ツテン (Short "zten" as in "letZTEN")

    # Ü
    '\u0079': '\u30E6',  # y -> ユ (Long stressed "ü" as in "Über")

    # Edge cases for T with preceding short vowel
    '\u0062\u025B\u0074': '\u30D9\u30C3\u30C8',  # bɛt -> ベット (Short "t" with preceding short vowel as in "BETT")
    '\u0074\u0061\u0074': '\u30BF\u30C3\u30C8',  # tat -> タット (Short "t" with preceding short vowel as in "sTADT")
    '\u02C8\u006C\u025B\u0074': '\u30EC\u30C3\u30C8',  # ˈlɛt -> レット (Short "t" with preceding short vowel as in "vioLETT")
    '\u02C8\u006D\u026A\u0074': '\u30DF\u30C3\u30C8',  # ˈmɪt -> ミット (Short "t" with preceding short vowel as in "miTTwoch")

    # Edge cases for CH "x" (Pronunciation of "ch" depends on the preceding vowel
    '\u0078\u0259': '\u30C3\u30D8',  # xə -> ッヘ (Short "che" as in "spraCHE")
    '\u028A\u032F\u0078\u0259': '\u30A6\u30C3\u30D8',  # ʊ̯xə -> ウッヘ (Short "uche" as in "braUCHE")
    '\u0078\u0074\u0259': '\u30C3\u30D8\u30C6',  # xtə -> ッヘテ (Short "chte" as in "daCHTE")
    '\u0061\u0078\u0074': '\u30A2\u30C3\u30CF\u30C8',  # axt -> アッハト (Short "cht" with preceding "a" as in "ACHT")
    '\u006E\u0061\u0078': '\u30CA\u30C3\u30CF',  # nax -> ナッハ (Short "ch" with preceding "na" as in "NACH")
    '\u006E\u0061\u02D0\u0078': '\u30CA\u30C3\u30CF',  # naːx -> ナッハ (Short "ch" with preceding "na" as in "NACH")
    '\u006E\u0254\u0078': '\u30CE\u30C3\u30DB',  # nɔx -> ノッホ (Short "ch" with preceding "no" as in "NOCH")
    '\u0064\u0254\u0078': '\u30C9\u30C3\u30DB',  # dɔx -> ドッホ (Short "ch" with preceding "do" as in "DOCH")
    '\u0078\u006E\u0329': '\u30C3\u30D8\u30F3',  # xn̩ -> ッヘン (Short "chen" as in "spraCHEN")
    '\u028A\u032F\u0078': '\u30A6\u30C3\u30D5',  # ʊ̯x -> ウッフ (Short "uch" as in "raUCH")
    '\u0062\u0061\u0078': '\u30D0\u30C3\u30CF',  # bax -> バッハ (Short "ch" with preceding "ba" as in "BACH")
    '\u0062\u0075\u02D0\u0078': '\u30D6\u30FC\u30C3\u30D5',  # buːx -> ブーッフ (Short "ch" with preceding "bu" as in "BUCH")
    '\u02C8\u0074\u0254\u0078': '\u30C8\u30C3\u30DB',  # ˈtɔx -> トッホ (Short "ch" with preceding "to" as in "toCHter")
    '\u02CC\u0076\u0254\u0078': '\u30F4\u30A9\u30C3\u30DB',  # ˌvɔx -> ヴォッホ (Short "ch" with preceding "wo" as in "mittWOCH")
    '\u02C8\u006E\u0061\u02D0\u0078\u02CC': '\u30CA\u30C3\u30CF',  # ˈnaːxˌ -> ナッハ
    
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
    '\u0076\u026A\u0073\u0259': '\u30F4\u30A3\u30C3\u30BB',  # vɪsə -> ヴィッセ (Short "wisse" as in "geWISSE")
    '\u02C8\u006E\u025B\u02D0\u0259': '\u30CD\u30FC\u30D8',  # ˈnɛːə -> ネーヘ ("nähe")

    # Special characters
    '\u0000': '',  # NULL character should not map to anything, if not used
    '\u0020': '\u0020',  # Space character just maps to space again
    '\u002D': '',  # - -> 
    '\u0294': '',  # ʔ ->
    '\u02C8': '',  # ˈ -> 
    '\u02D0': '\u30FC',  # ː -> ー
    '\u02CC': '',  # ˌ ->
    '\u032F': '',  # ̯  ->
    '\u0303': '',  # ̃ -> 
}
