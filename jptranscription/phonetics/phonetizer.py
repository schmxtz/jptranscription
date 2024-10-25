import json
import re
from pathlib import Path

SUPPORTED_LANGS = {
    'lang-de': 'lang-de.json'
}


class IPATranscription:
    def __init__(self, lang: str = 'lang-de'):
        self.lang = lang
        self.lookup_table = None
        if SUPPORTED_LANGS.get(self.lang) is None:
            raise Exception('The given language {} does is not supported. List of supported languages are {}.'
                            .format(self.lang, list(SUPPORTED_LANGS.keys())))
        file_path = Path(__file__).parent.joinpath(SUPPORTED_LANGS[self.lang])
        file_handle = open(str(file_path))
        self.lookup_table = json.load(file_handle)     

    def lookup_word(self, word):
        if not self.lookup_table:
            raise Exception('Lookup table empty. Initialize it first with init_lookup_table.')
        ipa_transcription = ''
        target = word.lower()
        entry = self.__get_entry(target)
        if not entry:
            target = self.__sanitize_word(target)
            entry = self.__get_entry(target)
        if not entry:
            ipa_transcription, matches_original = self.__compound_word_check(word.lower())
            if not matches_original: 
                sanitized_ipa_transcription, sanitized_matches_original = self.__compound_word_check(self.__sanitize_word(word.lower()))
                if sanitized_matches_original:
                    ipa_transcription = sanitized_ipa_transcription
                else:
                    ipa_transcription = ipa_transcription if len(ipa_transcription) > len(sanitized_ipa_transcription) else sanitized_ipa_transcription 

        ipa_transcription = ipa_transcription or self.__get_ipa(entry)
        return '\u0000' + ipa_transcription + '\u0000'  # Null character to mark the start and end of the IPA-string

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
        return substring_ipa, word == substring

    def __get_entry(self, word):
        if isinstance(word, str):
            return self.lookup_table.get(word)
        
    @staticmethod
    def __sanitize_word(word):
        return re.sub('[^A-Za-z0-9üäöß ]+', '', word)
    
    @staticmethod
    def __get_ipa(entry):
        if entry.get('ipa'):
            return entry.get('ipa')
        