import jptranscription.transcription.ipakatamapping as ipakatamapping


SUPPORTED_LANGS = {
    'lang-de': ipakatamapping.GERMAN_IPA_TO_KATAKANA_MAP,
}


class Katakanizer:
    def __init__(self, language: str = 'lang-de'):
        self.language = language
        self.mapping = SUPPORTED_LANGS[self.language]
        self.max_ipa_substring_length = len(max(self.mapping, key=len))

    def transcribe_word(self, ipa: str):
        katakana_word = []
        start = 0
        ipa = '\u0000' + ipa + '\u0000'
        while start < len(ipa):
            modified = False
            # Take minimum so that we don't look ahead of the actual string
            look_ahead_counter = min(len(ipa) - start, self.max_ipa_substring_length)
            # Decrease it until we find the longest substring
            for i in range(look_ahead_counter, 0, -1):
                if ipa[start:start + i] in self.mapping:
                    katakana_word.append(self.mapping[ipa[start:start + i]])
                    # print(ipa[start:start + i], self.mapping[ipa[start:start + i]])  # debugging
                    start += i
                    modified = True
                    break
            if not modified:
                raise Exception(f'Error converting the word {ipa} with katakana so far {katakana_word}')
        return ''.join(katakana_word)
