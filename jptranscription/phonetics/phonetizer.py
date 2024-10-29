import json
import re
from pathlib import Path

SUPPORTED_LANGS = {
    'lang-de': 'lang-de.json'
}


class IPATranscription:
    def _init_(self, lang: str = 'lang-de'):
        self.lang = lang
        self.lookup_table = None
        assert(SUPPORTED_LANGS.get(self.lang) is not None)
        # Init lookup table
        file_path = Path(__file__).parent.joinpath(SUPPORTED_LANGS[self.lang])
        file_handle = open(str(file_path))
        self.lookup_table = json.load(file_handle)     

    def lookup_word(self, word):
        ipa_transcription = ''
        entry = self._get_entry(word)
        if not entry:
            entry = self._get_entry(self._sanitize_word(word))
        if not entry:
            ipa_transcription, matches_original = self._compound_word_check(word)
            if not matches_original: 
                sanitized_ipa_transcription, sanitized_matches_original = self._compound_word_check(self._sanitize_word(word))
                if sanitized_matches_original:
                    ipa_transcription = sanitized_ipa_transcription
                else:
                    ipa_transcription = ipa_transcription if len(ipa_transcription) > len(sanitized_ipa_transcription) else sanitized_ipa_transcription 

        ipa_transcription = ipa_transcription or self._get_ipa(entry) or None
        return ipa_transcription

    def _compound_word_check(self, word):
        substring = ''
        substring_ipa = ''
        while len(substring) != len(word):
            unchanged = True
            for i in range(len(word), len(substring), -1):
                entry = self._get_entry(word[len(substring):i])
                if entry:
                    substring += word[len(substring):i]
                    substring_ipa += self._get_ipa(entry) or ''
                    unchanged = False
                    break
            if unchanged:
                break
        return substring_ipa, word == substring

    def _get_entry(self, word, pos):
        if not word: return ''
        assert(isinstance(word, str))

        entry = self.lookup_table.get(word)  # Try normal word lookup
        if not entry:
            new_target = word.lower()
            entry = self.lookup_table.get(new_target)  # Try all lower-case word
        if not entry:
            new_target = new_target.capitalize()
            entry = self.lookup_table.get(new_target)  # Try captitalized word
        if not entry:
            new_target = new_target.upper()
            entry = self.lookup_table.get(new_target)  # Try all caps word
        return entry
        
    @staticmethod
    def _sanitize_word(word):
        return re.sub('[^A-Za-z0-9üäöß ]+', '', word)
    
    @staticmethod
    def _get_ipa(entry):
        if entry.get('ipa'):
            return entry.get('ipa')
        