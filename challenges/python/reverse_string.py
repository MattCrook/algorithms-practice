#------------------------------------------------#
# Reverse an input of a given string.
#------------------------------------------------#

# class Solution:
#     def reverseString(self, s):
#         for i in range(len(s)//2):
#             s[i], s[~i] = s[~i], s[i]

# s = Solution()
# print(s.reverseString("cat"))



#------------------------------------------------#
# Challenge #2: Use a python decorator to reverse an input of a given string.
#------------------------------------------------#
def reversal(sentence_func):
    def reversed_sentence(*args, **kwargs):
        original_sentence = sentence_func(*args, **kwargs)
        return f"Reversed: {''.join(reversed(original_sentence))}"
    return reversed_sentence


@reversal
def letterPress(sentence):
    return sentence
  
print(letterPress("cat"))
