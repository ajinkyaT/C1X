'''
Given a piece of text, create a histogram of letter pairs (order from high to low). For
instance, for the text, “this is a good thing”,
the letter pairs are: th, hi, is, is, go, oo, od, th, hi, in, and ng. (ignore a)
The histogram will be:
th: 2, is: 2, hi: 2 go: 1, oo: 1, od: 1, in: 1, ng: 1

Sample Input/Output:

Enter text: this is a good thing
Histogram: th: 2, is: 2, hi: 2 go: 1, oo: 1, od: 1, in: 1, ng: 1
Enter text: coooooool
Histogram: oo: 6, co: 1, ol: 1
'''
import collections

def create_histogram(text):
    hist = {}
    for i in range(len(text)-1):
        pair = text[i:i+2]
        if ' ' in pair:
            continue
        if pair in hist:
            hist[pair] += 1
        else:
            hist[pair] = 1

    hist_sorted = sorted(hist.items(), key=lambda kv: kv[1], reverse=True)
    hist = collections.OrderedDict(hist_sorted)
    return hist

print(create_histogram('this is a good thing'))