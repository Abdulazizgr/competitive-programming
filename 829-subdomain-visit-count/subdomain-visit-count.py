class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domains = defaultdict(int)
        ans = []
        for ele in cpdomains:
            s = ele.split()
            visited = int(s[0])
            a = s[1].split(".")
            if len(a) == 3:
                domains[s[1]] += visited
                domains[a[1]+"."+a[2]] += visited
                domains[a[2]] += visited
            else:
                domains[s[1]] += visited
                a = s[1].split(".")
                domains[a[1]] += visited
        for key,value in domains.items():
            ans.append(f"{value} {key}")
        return ans
        
              


            

        