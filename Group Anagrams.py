from collections import defaultdict

def group_anagrams(a):
    dfdict = defaultdict(list)

    for i in a:
        sorted_i = " ".join(sorted(i))
        dfdict[sorted_i].append(i)

    return dfdict.values()

words = ["flea", "raptor", "parrot", "leaf", "poodle", "looped", "lion", "sale", "seal", "loin", "swallow", "throne", "horse", "laden", "hornet", "wallows", "gnat", "shore", "eland", "tang"]
print(group_anagrams(words))
