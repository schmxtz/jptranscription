import json

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
        if not self.lookup_table:
            raise Exception('Lookup table empty. Initialize it first with init_lookup_table.')
        entry = self.__get_entry(word)
        # Backup logic if word is not in dictionary
        if not entry:
            # Check if word is a noun compound
            substring, substring_ipa = self.__compound_word_check(word)
            if substring == word:
                ipa_transcription = substring_ipa
            # TODO
            # - Check if word is an abbreviation
            # - Check for verb endings
            # - Check for noun endings
        else:
            ipa_transcription = self.__get_ipa(entry)
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
