class Text:
    text = input("Input text, please")  # Sentences must be write by ".", and words must be write by ",".


class Sentences:
    sentences = Text.text.split(".")


class Words:
    words = list()
    for i in Sentences.sentences:
        lst = i.split(",")
        for j in lst:
            words.append(j)
    for i in words:
        if i == '':
            words.remove(i)


class Letters:
    letters = list()
    for i in Words.words:
        for j in i:
            letters.append(j)


class PunctuationMarks:
    # PunctuationMarks is a clear class, because in my variant don`t use punctuation marks.
    pass


class Main:
    text = Text.text.replace(" ", "")
    list_sentences = Sentences.sentences
    list_words = Words.words
    list_letters = Letters.letters
    list_words_new = list()
    for i in list_words:
        j = i.lower()
        f = j[0] + j[1::].replace(j[0], "")
        list_words_new.append(f)


print(Main.list_words_new)





