def urtext(text):
    text = text.replace(" ,", ",")
    text = text.replace(" .", ".")

    pmarks = [".", ",", ":", ";", "!", "?"]
    for mark in pmarks:
        text = text.replace(mark, mark + " ")

    text = " ".join(text.split())
    sentences = text.split(". ")
    print(sentences)
    tsentences = []
    for sentence in sentences:
        tsentence = sentence.capitalize()
        tsentences.append(tsentence)
        trtext = ". ".join(tsentences)
    print(trtext)




    return trtext
text = input("Введите текст: ")
print(urtext(text))
