# Installation
~~No external libary dependencies except the wikitionary database.~~ I'm using the following libraries:
* [Splitter](https://github.com/dtuggener/CharSplit) to split compound nouns IPA lookup

But before using this library you need to run the file [wikitionary_processor.py](./jptranscription/phonetics/wikitionary_processor.py) to generate a slimmer version of  the dictionary for the IPA lookup. 

Afterwards you need to move the generated file to jptranscription\phonetics\lang-de.json

# Introduction
I'm developing a script to transcribe German words into Japanese sounds using IPA. 

For example the IPA of "Auto" is "aʊ̯to", the first sound "Au" ("aʊ̯") is transcribed as "アオ". 

My first idea was to break the German words into their syllables and then create a Katakana mapping for all syllables. 
But since there are [*WAYYYYY*](https://german.stackexchange.com/questions/70223/how-many-different-syllables-does-the-german-language-have "How many different syllables does the German language have?") 
too many German syllables (> 100.000), this approach is not feasible. 
Then I remembered that there are way less sounds and sound-combinations when converting the words into their respective 
IPA reading.

So this project attempts to generate the Katakana pronunciation of all German words using IPA.

Since some sound-combinations include shorter sounds/sound-combinations that might be pronounced differently, I'll start
looking for a match starting from the longest possible substring.

I'm using the Wikipedia [Wiktionary](https://de.wiktionary.org/) as a lookup table for most German words. It has as an IPA entry for most of them. Then each word is transcribed into Katakana using the IPA sounds. I changed the entries to only contain the pairs (word, phonetics). This is allowed as per the 
[Creative Commons](https://creativecommons.org/licenses/by-sa/4.0/) license.


> [!NOTE]
> Pronunciation remarks for Japanese speakers:
>  - If the word ends in 「ス」, in 99% of the cases it is pronounced just *s*, instead of *su*.
>    - 「ハウス」 is pronounced [*Haus*](https://www.youtube.com/watch?v=9fWPnlSXThg)
>    (not *Hausu*)
>  - If the word ends in 「ト」, there is a chance that the *o* in *to* is either silent or not. In that case the reader
>is forced to look at its German counterpart and make a case-by-case decision.
>    - If the German word ends with *to* like in *Auto*, it is pronounced. But if it ends with *t*, *tt*, *dt* or *d*, then
>  the *o* in *to* is silent like in [*alt*](https://www.youtube.com/watch?v=d8XzbxmtrbY) (「アルト」), [*Bett*](https://www.youtube.com/watch?v=nLU6-9qDJMA) (「ベット」), [*Stadt*](https://www.youtube.com/watch?v=Q-qnZiMsD_U) (「シュタット」) and *Fahrrad* 
>  (「ファーラート」).
> - It is not possible to faithfully represent German words with *ö* and *ü* in Japanese. I'm still working on a way to make them sound as close to German a possible


# Contributions:
- I want to thank [rhasspy](https://github.com/rhasspy) whose library [gruut](https://github.com/rhasspy/gruut) helped me get a basic understanding of German words and their IPA
- I want to thank [dmort27](https://github.com/dmort27) whose library [epitran](https://github.com/dmort27/epitran) made me come across the wikitionary library
- [This](https://ttsmp3.com/text-to-speech/Japanese/) website helped me check my Transcription if it sounded similar
- I want to thank the author of [this](https://doitsugo-yarouze.com/german-words-200/) blogpost who helped me as a starting point 