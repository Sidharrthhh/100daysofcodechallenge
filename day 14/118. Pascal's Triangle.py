class Solution:
    def generate(self, nr: int) -> List[List[int]]:
        fn=[]
        fn.append([1])
        for i in range(nr-1):
            nr=[1]
            for j in range(i):
                nr.append(fn[i][j]+fn[i][j+1])
            nr.append(1)
            fn.append(nr)
        return fn        