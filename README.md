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

For example: The sound  "au" ("aʊ̯") in "Frau" includes the "s"

> [!NOTE]
> Pronunciation remarks for Japanese speakers:
>  - If the word ends in 「ス」, in 99% of the cases it is pronounced just *s*, instead of *su*.
>    - 「ハウス」 is pronounced *Haus*
>    (not *Hausu*)
>  - If the word ends in 「ト」, there is a chance that the *o* in *to* is either silent or not. In that case the reader
>is forced to look at its German counterpart and make a case-by-case decision.
>    - If the German word ends with *to* like in *Auto*, it is pronounced. But if it ends with *t*, *tt*, *dt* or *d*, then
>  the *o* in *to* is silent like in ![*alt*](https://www.youtube.com/watch?v=d8XzbxmtrbY) (「アルト」), *Bett* (「ベット」), *Stadt* (「シュタット」) and *Fahrrad* 
>  (「ファーラート」).



![*alt*](https://github.com/user-attachments/assets/6cbc6337-6594-4651-809a-08ecce93a1b3)



