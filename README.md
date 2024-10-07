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

For example: The sound  "au" ("aʊ̯") in "Frau" includes the ""
