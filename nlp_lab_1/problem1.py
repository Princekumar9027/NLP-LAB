import re

# 1. Find URL
example1 = "I love spending time at https://www.xy123z.com/"
urls = re.findall(r"https?://[^\s]+", example1)
print("URLs:", urls)


# 2. Get email id
example2 = "My email id is xyz111@gmail.com"
emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-z]{2,}", example2)
print("Emails:", emails)


# 3. Find hashtags
example3 = "#Sushant is trending now in the world."
hashtags = re.findall(r"#\w+", example3)
print("Hashtags:", hashtags)


# 4. Find mentions (@)
example4 = "@Ajit, please help me"
mentions = re.findall(r"@\w+", example4)
print("Mentions:", mentions)


# 5. Find numbers
example5 = "8853147 sq. km of area washed away in floods"
numbers = re.findall(r"\d+", example5)
print("Numbers:", numbers)


# 6. Find punctuations
example6 = "Corona virus killed #24506 people. #Corona is un(tolerable)"
punctuations = re.findall(r"[^\w\s]", example6)   # anything not word/space
print("Punctuations:", punctuations)


# 7. Validate PAN Number
# Format: 5 Capital Letters + 4 Digits + 1 Capital Letter
example7a = "ABCED3193P"
example7b = "lEcGD012eg"
pan_pattern = r"^[A-Z]{5}[0-9]{4}[A-Z]$"
print("PAN Valid (Ex1):", bool(re.match(pan_pattern, example7a)))
print("PAN Valid (Ex2):", bool(re.match(pan_pattern, example7b)))


# 8. Remove repetitive characters
example8 = "heyyy this is a verrrry loong texttt"
no_repeats = re.sub(r"(.)\1+", r"\1", example8)
print("Removed Repetitions:", no_repeats)


# 9. Find Indian mobile numbers (10 digits starting 6-9)
example9 = "9990001796 is a phone number of PMO office"
mobiles = re.findall(r"\b[6-9]\d{9}\b", example9)
print("Indian Mobile Numbers:", mobiles)


# 10. Extract words starting with capital letters
example10 = "Ajit Doval is the best National Security Advisor so far."
cap_words = re.findall(r"\b[A-Z][a-zA-Z]*\b", example10)
print("Capitalized Words:", cap_words)
