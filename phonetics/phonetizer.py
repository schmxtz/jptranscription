import json
import re

SUPPORTED_LANGS = {
    'lang-de': 'lang-de.json'
}


class IPATranscription:
    def __init__(self, lang):
        self.lang = lang
        self.lookup_table = None

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
        target = re.sub('[^A-Za-z0-9üäöß ]+', '', word.lower())
        entry = self.__get_entry(target)
        if not entry:
            entry['ipa_transcription'] = self.__compound_word_check(word.lower())
        ipa_transcription = self.__get_ipa(entry)
        return '\u0000' + ipa_transcription + '\u0000', self.__get_original_word(entry)  # Null character to mark the start and end of the IPA-string

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
    
    @staticmethod
    def __get_ipa(entry):
        if entry.get('ipa'):
            return entry.get('ipa')
        
    @staticmethod
    def __get_original_word(entry):
        if entry.get('original_word'):
            return entry.get('original_word')
        