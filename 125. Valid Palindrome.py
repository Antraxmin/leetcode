class Solution:
    def isPalindrome(self, s: str) -> bool:
        list_str = []
        for char in s:
            if char.isalnum():
                list_str.append(char.lower())
        
        # 팰린드롬인지 확인하는 반복문
        while len(list_str) > 1:
            if list_str.pop(0) != list_str.pop():
                return False
        return True
