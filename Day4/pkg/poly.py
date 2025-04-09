class Poly:
    def __init__(self,*args):
        self.args = args
        
    def __str__(self):
        return f"{self.args}"
    
    
    def __add__(self, b):
        a_len = len(self.args)
        b_len = len(b.args)
        c = []
        if a_len > b_len:
            c.extend(self.args[:a_len - b_len])
            for i in range(b_len):
                c.append(self.args[a_len - b_len + i] + b.args[i])
        else:
            c.extend(b.args[:b_len - a_len])
            for i in range(a_len):
                c.append(b.args[b_len - a_len + i] + self.args[i])
            
        return Poly(*c)
            
                
                
                
         
    
