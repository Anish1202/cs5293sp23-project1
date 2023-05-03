# CS5293sp23 – Project1

Name: Anish Sunchu     OU ID: 113583802

### Project Description
This project involves designing a system using Python and Text Analytics to redact sensitive information from plain text documents. The system accepts plain text documents and detects and redacts sensitive information such as names, genders, dates, phone numbers, and physical addresses. The program is executed using command line arguments, including input and output file paths and redaction flags. The redacted files are stored in a specified output directory with the same name as the original file, with ".redacted" appended to the file name. The program also includes a stats option that generates a summary of the redaction process, including the types and counts of redacted terms and the statistics of each redacted file. The redacted characters in the document are replaced with a character of choice, such as the Unicode full block character █. The README file discusses the parameters applied to each redaction flag and may include additional redaction options.

### How to install

### Spacy Installation:
Open a command prompt or terminal window.

Install spaCy using pip, the package installer for Python:

`pipenv install spacy`

Download the English language model:

`python -m spacy download en_core_web_sm`


we can start using spaCy in our project by importing the spacy library and loading the language model:

`import spacy`

`nlp = spacy.load('en_core_web_sm')`


<b> Steps for Installation: </b>

-Create e new repository in github with name cs5293sp23-project1. Download the project file from git
-create a directory in above project 'mkdir project1'
-create one more module for tests 'mkdir tests'
-add all the functional code in project1 and pytests in tests directory
-now install pyenv using 'pip install pipenv'
-install all required libraries
-Now we are all set to run code
-use command 'pipenv run python redactor.py --input '*.txt' \
                    --names --dates --phones --genders --address\
                    --output 'files/' \
                    --stats stderr'
-'run pipenv run python' -m pytest to run tests

### **Functions:**

**read_fun():**

* This is a Python function named read_fun() that reads all text files in a specified directory and performs redaction on the content of each file. The function starts by defining the directory where the files are located and the file extension of the files to be read.
* It uses the glob module to get a list of all the files in the specified directory that match the file extension. The glob.glob() function is used to find all the files with the specified extension.
* The function then loops through the list of files and reads the contents of each file using the open() function. The content of each file is stored in the text variable.
* The function then calls several other redaction functions (redact_genders(), redact_phone_numbers(), redact_dates(), redact_names(), and redact_address()) on the text variable to perform the redaction process. The output of each redaction function is passed as input to the next redaction function in the chain.
* Finally, the redacted text is printed to the console using the print() function.

**redact_names():**

* This method, named "redact_names," takes in a string of text and replaces any occurrence of a name with a redaction placeholder, represented by three black rectangles (unicode character "\u2588").

* The method uses regular expressions to match different formats of names, such as first name followed by last name, last name followed by first name, first name followed by middle initial followed by last name, last name followed by first name followed by middle initial, prefix followed by first name followed by last name, and first name followed by middle name(s) followed by last name.

* Each regular expression pattern is compiled using the "re.compile" function, which returns a regular expression object that can be used to match patterns in a string. The "sub" method of the regular expression object is then used to replace all matched patterns with the redaction placeholder.

* Finally, the method returns the modified string of text with the names redacted.

**redact_genders():**

* This method, named "redact_genders," takes in a string of text and replaces any occurrence of gender pronouns with a redaction placeholder, represented by three black rectangles (unicode character "\u2588").
* The method defines a list of gender pronouns to redact, including variations of he/him/his, she/her/hers, and titles such as Mr., Mrs., etc. It then iterates over the list of pronouns and creates a regular expression pattern to match each pronoun with word boundaries using the "re.escape" function to escape any special characters. The "flags=re.IGNORECASE" parameter makes the pattern match case-insensitive.
* For each pronoun, the "sub" method of the "re" module is used to replace all matched pronouns with the redaction placeholder.
* Finally, the method returns the modified string of text with the gender pronouns redacted.

**redact_dates():**

* The redact_dates function is a Python function that helps you remove dates from a string of text by replacing them with a specific string.
* For example, if you have a sentence like "I will be out of town on January 1, 2023," the function can replace the date "January 1, 2023" with a redacted string like "XXX-XXX-XXXX."
* The function works by using a regular expression pattern to match the date format in the text. The regular expression is a string of characters that define the pattern of the date you want to match. For example, the regular expression in this function looks for dates in the format of "month day, year" (e.g. January 1, 2023) and includes different patterns to match the day, month, year, and other details of the date.
* Once the regular expression has identified the dates in the text, the function uses the pattern.sub method to replace them with a redacted string. In this case, the redacted string is made up of three Unicode characters that represent a solid block.
* Finally, the function returns the modified text with the dates redacted.

**redact_phone_numbers():**

* This function is designed to replace phone numbers in a string of text with a specific string. For example, if you have a sentence like "Please call me at 555-123-4567," the function can replace the phone number "555-123-4567" with a redacted string like "XXX-XXX-XXXX."
* The function works by using a regular expression pattern to match phone numbers in the text. The regular expression is a string of characters that define the pattern of the phone number you want to match. For example, the regular expression in this function looks for phone numbers in the format of "XXX-XXX-XXXX," where "X" can be any digit from 0 to 9.
* Once the regular expression has identified the phone numbers in the text, the function uses the pattern.sub method to replace them with a redacted string. In this case, the redacted string is made up of three Unicode characters that represent a solid block.
* Finally, the function returns the modified text with the phone numbers redacted.

**redact_address():**

* This function is designed to replace US-style street addresses and zip codes in a string of text with a specific string. For example, if you have a sentence like "My address is 123 Main St, Anytown, CA 12345," the function can replace the address and zip code with a redacted string like "XXX."
* The function works by using a regular expression pattern to match US-style street addresses and zip codes in the text. The regular expression is a string of characters that define the pattern of the address and zip code you want to match. For example, the regular expression in this function looks for US-style street addresses in the format of "123 Main St" or "123 Main St., Anytown, CA 12345".
* Once the regular expression has identified the addresses and zip codes in the text, the function uses the pattern.sub method to replace them with a redacted string. In this case, the redacted string is made up of three Unicode characters that represent a solid block.
* Finally, the function returns the modified text with the addresses and zip codes redacted.

### **Test Functions:**

**1. test_redact_dates():**

* This test case is for testing the functionality of a redact_dates function. The function takes a text string as input and replaces all the occurrences of dates in the format "month day, year" with a string of redaction characters (in this case, Unicode character U+2588, which is a solid block). 
* In this particular test case, the input text contains a date string in the format "Mon, 28 Aug 2000 06:40:00 -0700 (PDT)". The expected output is a string that has the date redacted with the solid block characters, while the rest of the text remains unchanged. So, the expected output is "On \u2588\u2588\u2588, something happened."
* The purpose of this test case is to ensure that the redact_dates function correctly identifies and redacts date strings in the specified format. If the function works correctly, it should replace the date string with the solid block characters and return a string that matches the expected output. If the function does not work correctly, the assertion in the test case will fail, indicating that the function needs to be fixed or improved.

**2. test_redact_phone_numbers():**

* This test case is for testing the functionality of a redact_phone_numbers function. The function takes a text string as input and replaces all the occurrences of phone numbers in the format "###-###-####" with a string of redaction characters (in this case, Unicode character U+2588, which is a solid block).
* In this particular test case, the input text contains a phone number string in the format "555-123-4567". The expected output is a string that has the phone number redacted with the solid block characters, while the rest of the text remains unchanged. So, the expected output is "My phone number is \u2588\u2588\u2588."
* The purpose of this test case is to ensure that the redact_phone_numbers function correctly identifies and redacts phone number strings in the specified format. If the function works correctly, it should replace the phone number string with the solid block characters and return a string that matches the expected output. If the function does not work correctly, the assertion in the test case will fail, indicating that the function needs to be fixed or improved.

**3. test_redact_names():**

* This test case is for testing the functionality of a redact_names function. The function takes a text string as input and replaces all the occurrences of person names with a string of redaction characters (in this case, Unicode character U+2588, which is a solid block).
* In this particular test case, the input text contains two person names: "John Doe" and "Jane Smith". The expected output is a string that has both names redacted with the solid block characters, while the rest of the text remains unchanged. So, the expected output is " Hello! \u2588\u2588\u2588, I'm \u2588\u2588\u2588. How are you doing today?"
* The purpose of this test case is to ensure that the redact_names function correctly identifies and redacts person names in the specified format. If the function works correctly, it should replace the person names with the solid block characters and return a string that matches the expected output. If the function does not work correctly, the assertion in the test case will fail, indicating that the function needs to be fixed or improved.

**4. test_redact_genders():**

* This test case is for testing the functionality of a redact_genders function. The function takes a text string as input and replaces all the occurrences of gender-specific pronouns (e.g., "he", "she", "his", "her") with a string of redaction characters (in this case, the Unicode character U+2588, which is a solid block).
* In this particular test case, the input text contains several gender-specific pronouns. The expected output is a string that has all of the gender-specific pronouns redacted with the solid block characters, while the rest of the text remains unchanged. So, the expected output is "███ went to see ███ ███, but ███ was not there. ███ said ███ was going to meet ███ friend at the park."
* The purpose of this test case is to ensure that the redact_genders function correctly identifies and redacts gender-specific pronouns in the specified format. If the function works correctly, it should replace the gender-specific pronouns with the solid block characters and return a string that matches the expected output. If the function does not work correctly, the assertion in the test case will fail, indicating that the function needs to be fixed or improved.                                 

**5. test_redact_address():**

* The test case defines a function named test_redact_address, which includes three assertions to test the behavior of the redact_address function.
* The first assertion tests the redact_address function with a string that contains a street address in Norman, Oklahoma, USA. The expected output is the same string, but with the zip code redacted using the Unicode character "\u2588".
* The second assertion tests the redact_address function with a string that contains a more complex address with a suite number and a zip code in New York City, USA. The expected output is the same string, but with the zip code and part of the city name redacted using the Unicode character "\u2588".
* The third assertion tests the redact_address function with a string that does not contain any addresses. The expected output is the same string, as there are no addresses to redact.
* Each assertion uses the assert statement to compare the actual output of the redact_address function with the expected output. If the actual output matches the expected output, the assertion passes. Otherwise, it fails and raises an AssertionError.

### **Redaction Flags:**

* --names: This flag indicates that the program should extract any person names that appear in the input documents. Extracting names can be useful for various reasons, such as identifying key individuals mentioned in a document or for personalization purposes.
* --genders: This flag indicates that the program should extract any gender information that appears in the input documents. This could include gendered pronouns, titles, or other gender-related information. Extracting gender information can be helpful for understanding the demographics or preferences of the document's audience.
* --dates: This flag indicates that the program should extract any dates that appear in the input documents. Extracting dates can be useful for tracking deadlines, understanding the historical context of a document, or identifying patterns over time.
* --phones: This flag indicates that the program should extract any phone numbers that appear in the input documents. Extracting phone numbers can be helpful for contact purposes or for understanding the communication channels used by the document's author or intended audience.
* --address: This flag indicates that the program should extract any postal addresses that appear in the input documents. Extracting addresses can be useful for identifying the location of the document's author or intended audience, or for analyzing the geographic distribution of a particular topic or issue.

### **--Stats:**
* The --stats redaction flag generates a summary of the redaction process that can be used to gain insights into the types and counts of redacted terms, as well as the statistics of each redacted file. The purpose of this flag is to provide developers with useful information that can help them improve their redaction algorithm.
* When the --stats flag is used, the program will output a file that contains a summary of the redaction process. The format of the outfile should be described in the README file. Some of the statistics that can be included in the output are:
* Total number of documents processed
* Total number of terms redacted
* Types and counts of redacted terms
* Statistics of each redacted file, such as the number of redacted terms, the length of the file, and the time taken to redact the file
* Beginning and end index of each redacted item

### **Bugs:**
* The function redact_address replaces only some parts of the matched string with asterisks, rather than the entire match.
* The list of gender pronouns in redact_genders includes some gender-neutral words (e.g. "person", "they/them/theirs") that are not being redacted.
* The redact_dates function is using a regular expression pattern that will match dates in a specific format, but there may be other valid date formats that it is not capturing.
* There is no input validation or error handling in any of the functions, so passing invalid input could cause the program to crash or behave unexpectedly.

### **Assumptions:**
* The desired output of redact_address is to replace the entire matched string with asterisks, rather than just some parts of it.
* The redact_genders function is intended to redact only binary gendered pronouns (i.e. he/him/his, she/her/hers), and not gender-neutral language.
* The redact_dates function is intended to match dates in the specific format given in the regular expression pattern, and not other date formats.