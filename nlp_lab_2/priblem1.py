import re
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

# ---------- Helper functions ----------

# 1. Lowercasing
def to_lower(text):
    return text.lower()

# 2. Removing Extra Whitespace
def remove_extra_spaces(text):
    return re.sub(r"\s+", " ", text).strip()

# 3. Handling Contractions (basic replacements + <3 to love)
def handle_contractions(text):
    contractions = {
        "can't": "cannot",
        "won't": "will not",
        "n't": " not",
        "i'm": "i am",
        "it's": "it is",
        "i <3": "i love",
        "u're": "you are",
        "ur": "your",
        "u": "you",
        "btw": "by the way",
        "pls": "please",
        "plz": "please",
        "cud": "could",
        "wuz": "was"
    }
    for k, v in contractions.items():
        text = re.sub(rf"\b{k}\b", v, text)
    return text

# 4. Removing Special Characters
def remove_special_chars(text):
    return re.sub(r"[^a-zA-Z0-9\s.,!?]", "", text)

# 5. Reducing Duplicate Letters
def reduce_duplicate_letters(text):
    return re.sub(r"(.)\1{2,}", r"\1\1", text)

# 6. Fixing Punctuation
def fix_punctuation(text):
    text = re.sub(r"([.!?]){2,}", r"\1", text)  # normalize !!!
    return text

# 7. Removing URL Artifacts
def remove_urls(text):
    return re.sub(r"(https?://\S+|www\.\S+)", "", text)

# ---------- Main Cleaning Pipeline ----------
def clean_text(text):
    text = to_lower(text)
    text = handle_contractions(text)
    text = remove_urls(text)
    text = remove_special_chars(text)
    text = reduce_duplicate_letters(text)
    text = fix_punctuation(text)
    text = remove_extra_spaces(text)
    return text


# ---------- Uncleaned Paragraphs ----------
paragraphs = [
    """OMG!! I can't believe I found this aWesoMe article about AI & machine leanring!! 
       It was soooo gooood lol. I <3 nlp butttt i hate spelng errors in textttt. 
       This is gonna be a looong paragraph with looooots of spacesss and weirddddd symbols @#$%. 
       The website's link is www.example.com//// Check it out ASAP!!! #excited""",

    """Oh my gosh!!! Like, I can't even believe what I just stumbled upon on the world wide web. 
       This article, "The Marvels of Artificial General Intelligence & the Future of Humanity," totally blew my mindddd!! 
       It was, like, sooo mind-blowingly awesome, lolz. I mean, I <3 NLP butttt those annoying typos in texts drive me nuts. 
       Brace yourselves, this is gonna be one seriously long paragraph with tons and tons of extraterrestrial spaces and some seriously weird symbols like @#$%. 
       And guess what? The link to the website is www.incrediblenews.com//// So, um, you better check it out like ASAP!!! #excitedmuch""",

    """yaaayyyy!!! just watched thisssss AMAZZZING vid on AI 🤖 & how it’s changin' evrythinggg!! 😱😱 
       it waz soooo dopeee, i can’t even... lolzzz! #blessed #mindblownn... 
       btw, the link is http://coolai.stuff.com//// totally worthhh ittttttt @@@!!! 
       i <3 tech so much but sometimes it's likee realllyyy confusingggg!!!""",

    """nooo waayyyyy!!!! 😲😲 this is, like, the 1000000th time i've seen ppl mess up spellings in their blogsssss 😫😫 
       i mean c'mon, u're writing abt deep learning, not sum joke topic 🙄 
       anywayzzzz... the article was kinda cooool butttt had lotsa weird $$$%%%@@ symbols all over. 
       you can read it @ www.badblogger.ai//// and let me knw ur thots ASAP!!!""",

    """heyyyyy, did u read that crazyyyyyyy article on quantum stuff & ai?? like for realll... 
       it wuz crazzzzy detailed but sooooo complicateddd!!! 
       i cud barely undrstnd half of it 🤯🤯. the diagrams were 🔥🔥 tho!!! 
       i found it here – www.quantmgeekzz.net//// … plz plz plz read n tell me what u thinkk 😩😩"""
]

# ---------- Clean All Paragraphs ----------
cleaned_paragraphs = [clean_text(p) for p in paragraphs]

# ---------- Export to PDF ----------
doc = SimpleDocTemplate("Cleaned_Paragraphs.pdf")
styles = getSampleStyleSheet()
story = []

story.append(Paragraph("Cleaned Paragraphs after Data Cleaning", styles['Heading1']))
story.append(Spacer(1, 12))

for i, cp in enumerate(cleaned_paragraphs, 1):
    story.append(Paragraph(f"<b>Paragraph {i}:</b>", styles['Heading2']))
    story.append(Paragraph(cp, styles['Normal']))
    story.append(Spacer(1, 12))

doc.build(story)
print("✅ PDF generated: Cleaned_Paragraphs.pdf")
