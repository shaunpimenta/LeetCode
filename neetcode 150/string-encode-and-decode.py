class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded=""
        for i in strs:
            encoded+=i+"|"
        return encoded

    def decode(self, s: str) -> List[str]:
        return s.split("|")[:-1]

# Encoding: Append a delimiter (e.g., '|') after each string to separate them.
# Decoding: Split the encoded string by the delimiter to retrieve the original strings.
#Another way using 4# with 4 denoting length of string

class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded=""
        for i in strs:    
            encoded+=str(len(i))+"#"+i
        return encoded
    def decode(self, s: str) -> List[str]:
        decoded=[]
        i=0
        while i<len(s):
            j=i
            while s[j]!='#':
                j+=1
            length=int(s[i:j])
            i=j+1
            decoded.append(s[i:i+length])
            i+=length
        return decoded