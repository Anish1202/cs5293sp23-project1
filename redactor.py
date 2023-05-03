import argparse
import glob
import os
import re
import spacy
import main
import en_core_web_sm

def redactor():
    print(",,,,,,,,,,,,,,,,,,,,,,,")

    parser = argparse.ArgumentParser(description="Redacts personal information from text_files")
    parser.add_argument("--input", type=str, nargs='+', help="glob pattern representing input files")
    parser.add_argument("--output", type=str, help="directory to save redacted files")
    parser.add_argument("--names", action="store_true", help="redact names")
    parser.add_argument("--genders", action="store_true", help="redact gender pronouns")
    parser.add_argument("--dates", action="store_true", help="redact dates")
    parser.add_argument("--phones", action="store_true", help="redact phone numbers")
    parser.add_argument("--address", action="store_true", help="redact US addresses")
    parser.add_argument("--stats", type=str, help="file to write redaction statistics to")
    args = parser.parse_args()
    print(args.output)
    if not os.path.exists(args.output):
        try:
            os.makedirs(args.output)
        except OSError as error:
            print(f"Error: {args.output} cannot be created. {error}")
            return

    # get all file paths from input glob patterns
    file_paths = []
    print(args.input)
    for pattern in args.input:
        file_paths.extend(glob.glob(pattern))

    # initialize redaction statistics
    stats = {"names": 0, "genders": 0, "dates": 0, "phones": 0, "address": 0}

    # load spacy model for redaction
    nlp = en_core_web_sm.load()

    # redact each file and save to output directory
    print(file_paths)
    for path in file_paths:
        print(path)
        try:
            with open(path, 'r') as file:
                contents = file.read()
        except FileNotFoundError:
            print(f"Error: {path} not found.")
            continue
        except PermissionError:
            print(f"Error: {path} cannot be read due to insufficient permissions.")
            continue

        if args.names:
            contents = main.redact_names(contents)
            stats["genders"] = contents.count("\u2588")
        if args.genders:
            contents = main.redact_genders(contents)
            stats["genders"] = contents.count("\u2588")
            stats["genders"]=stats["genders"]//3-stats["names"]
        if args.dates:
            contents = main.redact_dates(contents)
            stats["dates"] = contents.count("\u2588")
            stats["dates"]= stats["dates"]//3-stats["genders"]
        if args.phones:
            contents = main.redact_phone_numbers(contents)
            stats["phones"] = contents.count("\u2588")
            stats["phones"]=stats["phones"]//3-stats["dates"]
        if args.address:
            contents = main.redact_address(contents)
            stats["address"] = contents.count("\u2588")
            stats["address"]=stats["address"]//3-stats["phones"]

     
        outputfile=os.path.join(args.output,os.path.basename(path)+".redacted")
        with open(outputfile, 'w') as file:
            file.write(contents)
        if args.stats:
            with open(args.stats, 'w') as file:
                for key, value in stats.items():
                    file.write(f"{key}: {value}\n")


redactor()
