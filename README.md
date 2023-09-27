# AnyBrute.py

A script for generating wordlists of feasibly guessable IDs, (intruder is BAD at this...)
Output to a wordlist for use in any program, or can be set into copyable mode with -pb which
allows piping into pbcopy for VERY easy importing into BurpSuite's wordlist via the "paste" button

## Some Examples:::
`python3 GenerateWordlist.py -h`
 
 _Shows help information._

---
`python3 GenerateWordlist.py -c 4 --charset hex --form XXXXX-XXXXXX -pb`

_Outputs:_
```
  768a4-bb080f
  9c03f-710e13
  8bd20-fa1599
  8f2bc-9b24bb
```
---
`python3 GenerateWordlist.py -c 1 --form "X-Client-ID: ZZZZ-ZZZZZZZZ-ZZZZZZ" -cc Z -pb`

_Outputs:_
```
  X-Client-ID: 1126-87505ffc-32cb81
```
---
`python3 GenerateWordlist.py -c 1 --form XXXXXXXXXXXX-XX-XXXXXXXX -pb`

_Outputs:_
```
  c7438b28394b-70-ce8b0f54
```
---
`python3 GenerateWordlist.py -l 16 -c 50 -pb | pbcopy`

_Copies fifty 16-length randomized hex strings to your clipboard for pasting directly into Intruder_

---
<br>

Additionally, anyBrute.py itself can be utilized as a library for other scripts where applicable...

## All Charset Options
`nums`:                       `1234567890`

`hex_upper`:                  `ABCDEF1234567890`

`hex_lower`:                  `abcdef1234567890`

`ascii_upper`:                `ABCDEFGHIJKLMNOPQRSTUVWXYZ`

`acii_lower`:                 `abcdefghijklmnopqrstuvwxyz`

`ascii_upper_and_nums`:       `ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890`

`ascii_lower_and_nums`:       `abcdefghijklmnopqrstuvwxyz1234567890`

`ascii_upper_lower_and_nums`: `ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890`

`ascii_all_printable`:        ```ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890<>?,./:;'{}|[]\"\\~`!@#$%^&*()-_=+ ```

---
__Additionally, any custom character set can be defined by assigning a charset value which does not aline with the above named conventions__, for instance...

`ABC123!@#`:                  `ABC123!@#`
