#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    else:
        out = list(dict(sorted(a_dictionary.items(), key=lambda item: item[1], reverse=True)))[0]
        return(out)
