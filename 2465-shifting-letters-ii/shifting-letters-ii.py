class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        pref = [0] * (len(s))
        for start,end , direction in shifts:
            if direction == 0:
                pref[start] -= 1
                if end + 1 < len(s):
                    pref[end +1] += 1
            
            else:
                pref[start] += 1
                if end + 1 < len(s):
                    pref[end  +1 ] -= 1
        ps = [0]
        for num in pref:
            ps.append(ps[-1]+num)
        s_list = list(s)
        for idx in range(len(s)):
            s_list[idx] = chr((ord(s_list[idx]) - ord('a') + ps[idx+1]) % 26 + ord('a'))

        
        return "".join(s_list)
