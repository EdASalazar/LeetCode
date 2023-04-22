from collections import Counter, defaultdict

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        note_letters = Counter(ransomNote)
        magazine_letters = Counter(magazine)
        print('note', note_letters, 'magazine', magazine_letters)
        

        if len(magazine_letters) < len(note_letters): return False
            
        
        for char, count in note_letters.items():
            magazine_letter = magazine_letters[char]
            if magazine_letter < count:
                return False
    
        return True

