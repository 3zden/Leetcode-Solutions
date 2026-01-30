class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == [] :
            return ""
        elif strs == [""]:
            return "\\x"
        h = {}
        inn = set()
        out = []
        for st in strs:
            dst = ""
            for c in st:
                dst += chr(ord(c)+1)
            out.append(dst)
        return " ".join(out)
                


    def decode(self, s: str) -> List[str]:
        if s == "":
            return []
        elif s == "\\x": return [""]
        h = {}
        inn = set()
        out = []
        spl = s.split(" ")
        for st in spl:
            dst = ""
            for c in st:
                dst += chr(ord(c)-1)
            out.append(dst)
            print(dst) 
        return out
