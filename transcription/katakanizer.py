from transcription.phonetic_mappings import *
from phonetics.phonetizer import IPATranscription


SUPPORTED_LANGS = {
    'lang-de': {'map': GERMAN_IPA_TO_KATAKANA_MAP,
                'irrelevant_chars': '\u02C8\u0329\u02CC\u032F\u0361'}
}


class Katakanizer:
    def __init__(self, language: str):
        self.language = language
        self.mapping = SUPPORTED_LANGS[self.language]['map']
        self.irrelevant_characters = SUPPORTED_LANGS[self.language]['irrelevant_chars']
        self.max_ipa_substring_length = None
        self.phonetics_transcriber = None

    def init_katakanizer(self):
        self.max_ipa_substring_length = len(max(SUPPORTED_LANGS[self.language]['map'], key=len))
        self.phonetics_transcriber = IPATranscription(self.language)
        self.phonetics_transcriber.init_lookup_table()

    def transcribe_word(self, word):
        if not self.phonetics_transcriber:
            raise Exception('Katakanizer has not been properly initialized.')
<<<<<<< HEAD
        word_phonetics, original_word = self.phonetics_transcriber.lookup_word(word)
=======
        word_phonetics, special_char_included = self.phonetics_transcriber.lookup_word(word)
>>>>>>> 31a24fe7589748ef2f65f62db560c2c7655432e3
        katakana_word = []
        start = 0
        while start < len(word_phonetics):
            modified = False
            # Take minimum so that we don't look ahead of the actual string
            look_ahead_counter = min(len(word_phonetics) - start, self.max_ipa_substring_length)
            # Decrease it until we find the longest substring
            for i in range(look_ahead_counter, 0, -1):
                if word_phonetics[start:start + i] in self.mapping:
                    katakana_word.append(self.mapping[word_phonetics[start:start + i]])
                    start += i
                    modified = True
                    break
            if not modified:
                raise Exception('Error converting {} with the IPA {} and katakana so far {}'.format(word, word_phonetics, ''.join(katakana_word)))
        # Put the special characters like "." and "," after the conversion into phonetics, since the characters might be relevant in the lookup
        delimiter_token = '\u0000'
<<<<<<< HEAD
        if original_word and not original_word.endswith('.'):
=======
        if not special_char_included and word and len(word) > 1:
>>>>>>> 31a24fe7589748ef2f65f62db560c2c7655432e3
            start = delimiter_token + word[0]
            if not start.isalnum() and start in self.mapping:
                katakana_word.insert(0, self.mapping[start])
            end = word[-1] + delimiter_token
            if not end.isalnum() and end in self.mapping:
                katakana_word.append(self.mapping[end])
        return ''.join(katakana_word), word_phonetics
