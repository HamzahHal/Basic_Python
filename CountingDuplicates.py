text = "ssHsnidasndisaNSAI"
def duplicate_count(text):
    lowerText = text.lower()
    found = []
    for char in lowerText:
        if not (char in found) and lowerText.count(char) > 1:
            found.append(char)

    #return len(found)
    return found



print(duplicate_count(text))