class new:
    def __init__(self,price,name,period,bill_per_every,bill_period,description=None,date=None,pay_method=None): # initialising class new with variables as listed
        self.price =price
        self.name=name
        self.description= description
        self.period=period
        self.bpe=bill_per_every  # Day/Week/Month/Year
        self.bp=bill_period
        self.des=description
        if self.period=='Recurring':  
            self.fp=date # if recurring can give First Pay
        else: self.ex_d=date # if One time can give expiry date
        self.pm=pay_method
        

    def bill_pay(self,time):
        if self.period=='Recurring':
            if time =='Weekly':
                if self.bp=='Day':
                    return self.price*7
                elif self.bp=='Week':
                    return self.price
                elif self.bp=='Month':
                    return (self.price/4.34)
                else: return (self.price/52.14)

    
                
            elif time =='Monthly':
                if self.bp=='Day':
                    return self.price*30.41
                elif self.bp=='Week':
                    return self.price*4.28
                elif self.bp=='Month':
                    return (self.price)
                else: return (self.price/12)
        
            else:  # yearly
                if self.bp=='Day':
                    return self.price*365
                elif self.bp=='Week':
                    return self.price*52
                elif self.bp=='Month':
                    return (self.price/12)
                else: return (self.price)
        
        else:   # One Time
            return self.price

# ch1=new(200,'Netflix','Recurring',1,'Month','enjoy','20/05','debit')
# print(ch1.bp)
# print(ch1.bill_pay('Weekly'))