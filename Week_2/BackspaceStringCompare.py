class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        string1 = []
        string2 = []
        
        for char in S:
            if char =="#":
                if len(string1) >= 1:
                    string1.pop()
            else:
                string1.append(char)
        
        for char in T:
            if char =="#":
                if len(string2) >= 1:
                    string2.pop()
            else:
                string2.append(char)
        
        return string1==string2
        
        
        
        