#!/usr/bin/python3
# A script for generating wordlists of feasibly guessable IDs, (intruder is BAD at this...)
# Output to a wordlist for use in any program, or can be set into copyable mode with -pb which
# allows piping into pbcopy for VERY easy importing into BurpSuite's wordlist via the "paste" button

# Some Examples:::
# python3 GenerateWordlist.py -c 4 --charset hex --form XXXXX-XXXXXX -pb
#   768a4-bb080f
#   9c03f-710e13
#   8bd20-fa1599
#   8f2bc-9b24bb

# python3 GenerateWordlist.py -c 1 --form "X-Client-ID: ZZZZ-ZZZZZZZZ-ZZZZZZ" -cc Z -pb
# X-Client-ID: 1126-87505ffc-32cb81

# python3 GenerateWordlist.py -c 1 --form XXXXXXXXXXXX-XX-XXXXXXXX -pb
# c7438b28394b-70-ce8b0f54

# python3 GenerateWordlist.py -l 16 -c 50 -pb | pbcopy
# copies fifty 16-length randomized hex strings to your clipboard for pasting directly into Intruder


# helper function for encoding...
def base64it(string):
    str_bytes = string.encode("ascii") 
    base64_bytes = base64.b64encode(str_bytes) 
    return base64_bytes.decode("ascii") 

# Ensure this is only utilized as a script!
if __name__ == "__main__":
    import argparse
    import textwrap
    import base64
    import anybrute

    parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,
      epilog=textwrap.dedent('''\
        Examples:
          TBDTBDTBD
          TBDTBDTBD
          TBDTBDTBD
         '''))
    parser.add_argument("--count", "-c", default=10, help="Number of IDs to generate. (Default: 10...)")
    parser.add_argument("--length", "-l", default=8, help="Length of generated IDs. (Default: 8...)")
    parser.add_argument("--form", "-f", default="None", help="Specify a form for ID output, overrides length argument... form should utilize 'X' as a control character for brute forced characters, unelss otherwise set. EX: XXXXXXXXXXXX-XXXX-XXXX-XXXXXXXX")
    parser.add_argument("--control-char", "-cc", default="X", help="Sets the control character for input form. Ignored if form is not set. (Default: X...)")
    parser.add_argument("--charset", "-ch", default="hex_upper", help="Sets the charset, via named set or a string of characters to be included. Preloaded sets include: nums, hex_upper, hex_lower, ascii_upper_and_nums, ascii_lower_and_nums, ascii_upper_lower_and_nums, ascii_all_printable (Defaults: hex_upper) EX: ABCabc123!@#")
    parser.add_argument("--copyable", "-pb", default=False, action="store_true", help="Raise this flag to output directly to console (ignores wordlist location), useful for piping into PBCopy and right into Burps wordlist in Intruder.")
    parser.add_argument("--output", "-o", default="NOFILE", help="Location for wordlist to append to. [Will create if doesn't exist, otherwise appends to end.] (Defaults: NOFILE...)")
    parser.add_argument("--encode", "-e", default="NOENCODE", help="Specify an encoding for final output. [Supported: base64 ...]")
    
    args = parser.parse_args()
    finalOut = "\r\n"
    for _ in range(1, int(args.count)):
        if args.form != "None":
            if args.encode == "NOENCODE":
                finalOut += anybrute.generateFromForm(args.form, control_char=args.control_char, charset=args.charset) + '\r\n'
            elif args.encode == "base64":
                finalOut += base64it(anybrute.generateFromForm(args.form, control_char=args.control_char, charset=args.charset)) + '\r\n'
            else:
                print("INVALID ENCODING, STOPPING...")
                exit()
        else:
            if args.encode == "NOENCODE":
                finalOut += anybrute.generate(args.length, charset=args.charset) + '\r\n'
            elif args.encode == "base64":
                finalOut += base64it(anybrute.generate(args.length, charset=args.charset)) + '\r\n'
            else:
                print("INVALID ENCODING, STOPPING...")
                exit()

    if args.copyable:
        finalOut = finalOut.replace("\r\n", "", 1)
        print(finalOut[:-2])
    elif args.output != "NOFILE":
        with open(args.output, "a+") as outputFile:
            outputFile.write(finalOut + '\n')
    else:
        print(finalOut)