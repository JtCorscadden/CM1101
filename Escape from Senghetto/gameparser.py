import string

# List of "unimportant" words (feel free to add more)
skip_words = ['a', 'about', 'all', 'an', 'another', 'any', 'around', 'at',
              'bad', 'beautiful', 'been', 'better', 'big', 'can', 'every', 'for',
              'from', 'good', 'have', 'her', 'here', 'hers', 'his', 'how',
              'i', 'if', 'in', 'into', 'is', 'it', 'its', 'large', 'later',
              'like', 'little', 'main', 'me', 'mine', 'more', 'my', 'now',
              'of', 'off', 'oh', 'on', 'please', 'small', 'some', 'soon',
              'that', 'the', 'then', 'this', 'those', 'through', 'till', 'to',
              'towards', 'until', 'us', 'want', 'we', 'what', 'when', 'why',
              'wish', 'with', 'would']


def filter_words(words, skip_words):
    new_list = []
    words = (words.lower()).split()
    for word in words:
        if not word in skip_words:
            new_list.append(word)
    return ' '.join(new_list)

    
def remove_punct(text):
    for c in string.punctuation:
        text = text.replace(c, '')
    return text
    
def remove_spaces(text):
    text = text.lstrip()
    text = text.rstrip()
    return text


def normalise_input(user_input):
    global skip_words
    user_input = remove_punct(user_input)
    user_input = remove_spaces(user_input)
    user_input = filter_words(user_input, skip_words)
    return user_input.lower()
