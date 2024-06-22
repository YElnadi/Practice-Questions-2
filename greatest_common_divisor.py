'''
For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

 

Example 1:

Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"
Example 2:

Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"
Example 3:

Input: str1 = "LEET", str2 = "CODE"
Output: ""

'''

def gcdOfStrings(word1, word2):
    divisor = []
    i = 0 
    j = 0

    while len(word2) <= len(word1):
        if word2[i] == word1[i]:
            divisor.append(word1[i])
            i += 1
        else:
            return ""
        
    return "".join(divisor)


