class UserMainCode(object):
    @classmethod
    def findmaximum(cls,input1 ,input2,input3):
        p=0
        ne=0
        for i in range(input3):
            if input2[i]=="P":
                p+=input1[i]
            else:
                ne+=input1[i]
        
        return(abs(ne-p)*100)
   

obj=UserMainCode()
print(obj.findmaximum([3,2],'PN',2))
