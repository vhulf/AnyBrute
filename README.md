# AnyBrute.py

A script for generating wordlists of feasibly guessable IDs, (intruder is BAD at this...)
Output to a wordlist for use in any program, or can be set into copyable mode with -pb which
allows piping into pbcopy for VERY easy importing into BurpSuite's wordlist via the "paste" button

## Some Examples:::
`python3 GenerateWordlist.py -h`
 - Shows help information.

```
python3 GenerateWordlist.py -c 4 --charset hex --form XXXXX-XXXXXX -pb
  768a4-bb080f
  9c03f-710e13
  8bd20-fa1599
  8f2bc-9b24bb
```

```
python3 GenerateWordlist.py -c 1 --form "X-Client-ID: ZZZZ-ZZZZZZZZ-ZZZZZZ" -cc Z -pb
  X-Client-ID: 1126-87505ffc-32cb81
```

```
python3 GenerateWordlist.py -c 1 --form XXXXXXXXXXXX-XX-XXXXXXXX -pb
  c7438b28394b-70-ce8b0f54
```

`python3 GenerateWordlist.py -l 16 -c 50 -pb | pbcopy`
 - Copies fifty 16-length randomized hex strings to your clipboard for pasting directly into Intruder


<br>
---
Additionally, AnyBrute.py itself can be utilized as a library for other scripts where applicable.
