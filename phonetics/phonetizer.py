import json
import re

SUPPORTED_LANGS = {
    'lang-de': 'lang-de.json'
}


class IPATranscription:
    def __init__(self, lang):
        self.lang = lang
        self.lookup_table = None
        self.LOOKUP_FUNCTIONS = [self.__get_entry, 
                                 self.__try_sanitized, 
                                 self.__try_lowercase, 
                                 self.__try_first_letter_capitalized]

    def init_lookup_table(self):
        if SUPPORTED_LANGS.get(self.lang) is None:
            raise Exception('The given language {} does is not supported. List of supported languages are {}.'
                            .format(self.lang, list(SUPPORTED_LANGS.keys())))
        file_handle = open('./phonetics/' + SUPPORTED_LANGS[self.lang])
        self.lookup_table = json.load(file_handle)

    def lookup_word(self, word):
        if not self.lookup_table:
            raise Exception('Lookup table empty. Initialize it first with init_lookup_table.')
        ipa_transcription = ''
        special_char_included = True
        entry = {'size': 0}
        for lookup_func in self.LOOKUP_FUNCTIONS:
            new_entry = lookup_func(word)
            if new_entry is not None and new_entry['size'] > entry['size']:
                entry = new_entry
                ipa_transcription = self.__get_ipa(entry)
                if len(word) != len(re.sub('[^A-Za-z0-9üäöß]+', '', word)):
                    special_char_included = False
        if entry['size'] == 0:
            ipa_transcription = self.__compound_word_check(word)
        return '\u0000' + ipa_transcription + '\u0000', special_char_included  # Null character to mark the start and end of the IPA-string

    def __compound_word_check(self, word):
        substring = ''
        substring_ipa = ''
        while len(substring) != len(word):
            unchanged = True
            for i in range(len(word), len(substring), -1):
                entry = self.__get_entry(word[len(substring):i])
                if entry:
                    substring += word[len(substring):i]
                    substring_ipa += self.__get_ipa(entry)
                    unchanged = False
                    break
            if unchanged:
                break
        return substring_ipa

    def __get_entry(self, word):
        if isinstance(word, str):
            return self.lookup_table.get(word)
        
    def __try_sanitized(self, word):
        word = re.sub('[^A-Za-z0-9üäöß]+', '', word)
        entry = self.__get_entry(word)
        return entry
    def __try_lowercase(self, word):
        word = word.lower()
        return self.__get_entry(word)
    
    def __try_first_letter_capitalized(self, word):
        word = word[0].upper() + word[1:]
        return self.__get_entry(word)

    @staticmethod
    def __get_ipa(entry):
        if entry.get('ipa'):
            return entry.get('ipa')
        