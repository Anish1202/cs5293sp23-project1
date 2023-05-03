import os
import glob
import re
from typing import Any

def redact_names(text):
    # Define a regular expression pattern to match all types of names
    pattern = re.compile(r'\b(?:[A-Z][a-z]+\s[A-Z][a-z]+|[A-Z][a-z]+,\s[A-Z][a-z]+|(?:Mr\.|Ms\.|Mrs\.|Dr\.)\s[A-Z][a-z]+\s[A-Z][a-z]+|[A-Z][a-z]+\s(?:[A-Z][a-z]+\s)*[A-Z][a-z]+)\b')

    # Replace all matched patterns with a redaction placeholder of the same length
    redacted_text = pattern.sub(lambda match: "\u2588" * len(match.group()), text)

    return redacted_text

def redact_genders(text):
    # Define a list of gender pronouns to redact
    pronouns = [" he", "he/him/his", "she", "she/her/hers", "He", "grandmother" , "He/him/his", "Man", "Men", "She", "She/her/hers", "Woman", "Women", "boy", "boys", "dad", "daddy", "father", "girl", "girls", "he", "he/him/his", "her", "hers", "him", "his", "man", "men", "mom", "mommy", "mother", "nephew", "nephews", "niece", "nieces", "prince", "princess", "queen", "she", "she/her/hers", "sister", "sisters", "son", "sons", "uncle", "uncles", "aunt", "aunts", "daughter", "daughters", "duchess", "duke", "king", "lady", "lord", "ma'am", "miss", "mr.", "mrs.", "ms.", "sir"]
    
    # Iterate over the list of pronouns and replace them with redaction placeholders
    for pronoun in pronouns:
        # Create a regular expression pattern to match the pronoun with word boundaries
        pattern = r'\b%s\b' % re.escape(pronoun)

        # Replace the pronoun with redaction placeholders
        matches = re.findall(pattern, text, flags=re.IGNORECASE)
        for match in matches:
            redacted = "\u2588" * len(match)
            text = text.replace(match, redacted)

    return text

def redact_dates(text):
    # Match dates in the format of "month day, year" (e.g. January 1, 2023)
    pattern = re.compile(
        r"\b(?:Mon|Tue|Wed|Thu|Fri|Sat|Sun),?\s\d{1,2}\s(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s\d{4}\s\d{1,2}:\d{2}(?::\d{2})?\s[-+]\d{4}\s?\(.*?\)")
    
    # Replace all matches with a redaction placeholder
    matches = pattern.findall(text)
    for match in matches:
        redacted = "\u2588" * len(match)
        text = text.replace(match, redacted)
    
    return text

def redact_phone_numbers(text):
    pattern = re.compile(r'\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}')
    matches = pattern.findall(text)
    for match in matches:
        redacted = "\u2588" * len(match)
        text = text.replace(match, redacted)
    return text

def redact_address(text):
    # Define regular expressions to match different types of addresses
    address_regexes = [
        r'\b\d{1,3}\s\w{2,30}\s\w{2,15}\b',  # Street address
        r'\bPO\sBox\s\d+\b',  # PO Box
        r'\b\d{5}(?:[-\s]\d{4})?\b',  # ZIP code
        # Add additional regexes as needed
    ]

    # Replace matches with asterisks and count the length of the match
    for regex in address_regexes:
        for match in re.finditer(regex, text):
            redacted_text = "\u2588" * len(match.group())
            text = text[:match.start()] + redacted_text + text[match.end():]
            

    return text
