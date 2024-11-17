import json
import re
from pathlib import Path
from split_words import Splitter

SUPPORTED_LANGS = {
    'lang-de': 'lang-de.json'
}


class IPATranscription:
    def __init__(self, lang: str = 'lang-de'):
        self.lang = lang
        self.lookup_table = None
        assert(SUPPORTED_LANGS.get(self.lang) is not None)
        # Init lookup table
        file_path = Path(__file__).parent.joinpath(SUPPORTED_LANGS[self.lang])
        file_handle = open(str(file_path))
        self.lookup_table = json.load(file_handle)
        # Init compound splitter
        self.splitter = Splitter()

    def lookup_word(self, word: str, pos: str):
        if pos == 'NOUN' or pos == 'PROPN':
            new_target = pos.capitalize()
        else:
            new_target = word.lower()
        ipa_transcription = self._get_entry(new_target)
        if not ipa_transcription:
            ipa_transcription = self._get_entry(self._sanitize_word(word))
        if not ipa_transcription:
            ipa_transcription = self._compound_word_check(word)
        return ipa_transcription
    
    def _compound_word_check(self, word):
        compounds_list = self.splitter.split_compound(word)
        ipa_compounds = []
        for compound_entry in compounds_list:
            ipa_compounds = []
            for compound in compound_entry[1:]:
                if (entry := self._get_entry(compound)): ipa_compounds.append(entry)
                else: break
            if len(ipa_compounds) == len(compound_entry) - 1: return ''.join(ipa_compounds)
        return ''.join(ipa_compounds)

    def _get_entry(self, word):
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
    