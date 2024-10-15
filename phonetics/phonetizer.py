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
        ipa_transcription = None
        special_char_included = True
        if not self.lookup_table:
            raise Exception('Lookup table empty. Initialize it first with init_lookup_table.')
        word = word.lower()
        entry = self.__get_entry(word)
        if not entry:
            # Sanitize word and try again
            word = re.sub('[^A-Za-z0-9]+', '', word)
            entry = self.__get_entry(word)
            special_char_included = False
        # Backup logic if word is not in dictionary
        if not entry:
            # Check if word is a noun compound
            substring, substring_ipa = self.__compound_word_check(word)
            if substring == word:
                ipa_transcription = substring_ipa
            # TODO
            # - Check for verb endings
            # - Check for noun endings
            # - Date https://pypi.org/project/text2numde/
        else:
            ipa_transcription = self.__get_ipa(entry)
        if word and not special_char_included:
            if not word[0].isalnum():
                ipa_transcription = word[0] + ipa_transcription
            if not word[-1].isalnum():
                ipa_transcription = ipa_transcription + word[0]
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
        return substring, substring_ipa

    def __get_entry(self, word):
        if isinstance(word, str):
            return self.lookup_table.get(word.lower())

    @staticmethod
    def __get_ipa(entry):
        if entry.get('ipa'):
            return entry.get('ipa')[0]
