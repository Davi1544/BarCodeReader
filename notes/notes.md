# How Bar Codes Work (UPC-A)

- A bar code consists of five parts (from left to right):
    1. A 5 unit band that identifies the start of the bar code;
    2. A section of six 7 unit bands (one 7 unit band for the number system and each of the first five numbers);
    3. Another 5 unit band that identifies the middle of the bar code;
    4. Another section of six 7 unit bands for the last 5 digits and the check digit;
    5. A third 5 unit section that identifies the end of the bar code.

# About the left / right encodings

- Numbers are encoded differently based on their location. The "encodings.png" contains all the possible encondings.
- The locational enconding allows bar code reader to read them even if upside down.
- Looking at the encodings, it's easy to see that the right encoding for any digit is the opposite of its left encoding.
- Additionally, as the encodings are 7 units in size and the left encoding always has an odd number of black units, i. e., zeros, that means the right encoding always has an even number of zeros. Therefore, it's easy to identify the side that's being read, as long as the digits are intact.

# About the Check Digit

- The check digit is a security mechanism that allows bar codes to be validated and also allows for them to be read correctly, even if up to one digit is damaged. The check digit can be verified using the following steps
    1. Sum all the numbers in odd positions;
    2. Multiply this result by 3;
    3. Sum to it all the numbers in even positions;
    4. Get the remainder of this sum by 10;
    5. if the remainder isn't 0, then the check digit is equal to *10 - remainder*.

- Using this formula, it is also possible to fix up to one missing digit in the bar code.

# About upside down reading

- As this project aims to also be able to read bar codes upside down, just like bar code readers, reading the center of the bar code seems to be the simplest way to read it correctly in both cases.
