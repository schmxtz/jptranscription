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
        file_handle = open('./transcription/' + SUPPORTED_LANGS[self.lang])
        self.lookup_table = json.load(file_handle)

    def lookup_word(self, word):
        if not self.lookup_table:
            raise Exception('Lookup table empty. Initialize it first with init_lookup_table.')
        result = self.__get_entry(word)
        # Backup logic if word is not in dictionary
        if not result:
            # Check if word is a noun compound
            substring, substring_ipa = self.__compound_word_check(word)
            if substring == word:
                return substring_ipa
        else:
            return result
        return None

    def __compound_word_check(self, word):
        substring = ''
        substring_ipa = ''
        while len(substring) != len(word):
            unchanged = True
            for i in range(len(word), len(substring), -1):
                entry = self.__get_entry(word[len(substring):i])
                if entry:
                    print(word[len(substring):i])
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


ipa = IPATranscription('lang-de')
ipa.init_lookup_table()