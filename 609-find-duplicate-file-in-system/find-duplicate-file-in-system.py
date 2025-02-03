class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        ans = []
        for i in range(len(paths)):
            a = paths[i].split(" ")
            for j in range(1,len(a)):
                b= a[j].split(".txt")
                dic[b[1]].append(f"{a[0]}/{b[0]}.txt")
        print(dic)
        for i in dic.values():
            if len(i) > 1:
                ans.append(i)
        
        


        return ans