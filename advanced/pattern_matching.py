#!/usr/bin/env python

# This has an O(nm) complexity
def simple_matcher(pattern, text):
    i = 0
    j = 0

    while True:
        if text[i] == pattern[j]:
            j += 1
        else:
            j = 0
        i += 1

        if i == len(text):
            return -1
        if j == len(pattern):
            return i - j


def mismatch_links(pattern):
    aug_pattern = "@" + pattern
    links = {1: 0}
    for k in range(2, len(aug_pattern)):
        s = links[k - 1]
        while s >= 1:
            if aug_pattern[s] == aug_pattern[k - 1]:
                break
            else:
                s = links[s]
        links[k] = s + 1

    return links


if __name__ == "__main__":
    pass
