class Solution:
    def validWordAbbreviation(self, word:str, abbr:str) -> bool:
        word_ind = 0
        num = ""
        for i in range(len(abbr)):
            if abbr[i].isnumeric(): # check if the character is a digit
                num += abbr[i] # add character to string
            
            else:
                if num != "":
                    skip = int(num) # cast num to an integer
                    if skip == 0:
                        return False
                    word_ind += skip - 1 # update word_ind to count for the skips
                    
                if word_ind > len(word) or word[word_ind] != abbr[i]: # check if out of index bounds or if the characters are the same
                    return False
                word_ind += 1 # increase word_ind by 1 after the check
                num = "" # reset num
        
        # check if the last number is zero
        if num != "":
            if num == "0": 
                return False
        
        return word_ind == len(word)