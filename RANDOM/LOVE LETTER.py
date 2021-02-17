class UserMainCode(object):
    @classmethod
    def rotatedWords(cls ,input1, input2):
        input1=input1.split()            
        ans=[]
        for i in input1:
            l=len(i)
            t=""
            for j in range(l):
                t+=i[(j+input2)%l]
            ans.append(t)
        jj=0

        for i in range(len(input1)):
            if input1[i]==ans[i]:
                jj+=1
        return jj
obj=UserMainCode()
print(obj.rotatedWords('adaada',3))
