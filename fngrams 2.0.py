def fngrams(text, ngrams):
    """ function to make n-grams"""
    amount = ngrams
    nlist = []
    for i, x in enumerate(text):
        trlist = text[i:amount]
        nlist.append(trlist)
        if amount == len(text):
            break
        i += 1
        amount += 1
    return nlist
print(fngrams(["python", "awesome", "programming", "language", "cpp", "faster", "golang", "easy", "rust", "like", "javascript"], 5))
