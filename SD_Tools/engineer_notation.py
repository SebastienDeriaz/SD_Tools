from IPython.display import display, Math

def to_units(prefix : str, num : float, extension : str, precision : int):
    
    mag = 0
    if(num > 0):
        polarity = 0
    else:
        polarity = 1
        num = -num

    indices = ('y', 'z', 'a', 'f', 'p', 'n', u"\u03BC", 'm', '', 'k', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y')

    if(num == 0):
        pass
    elif(num > 1):
        while(num > 1000 and mag < 16):
            num/=1000
            mag+=1
    elif(num < 1):
        while(num < 1 and mag > -8):
            num*=1000
            mag-=1
    
    if(polarity):
        num = -num
    if(mag == -1 and extension == "kg"):
        evaluatedExpression = "%.*f g" %(precision, num)
    else:
        evaluatedExpression = "%.*f %s%s" %(precision, num, indices[mag+8], extension)
    if(prefix[0] == '$' and prefix[-1] == '$'): #latex
        prefix = prefix.replace("$", "")
        display(Math(r"%s\text{%s}" % (prefix, evaluatedExpression)))
    else:
        display(Math(r"\text{%s%s}" % (prefix, evaluatedExpression)))      
    
    
def to_eng(prefix : str, num : float, extension : str, precision : int):
    mag = 0
    if(num > 0):
        polarity = 0
    else:
        polarity = 1
        num = -num
    if(num == 0):
        pass
    elif(num > 1):
        while(num > 1000 and mag < 16):
            num/=1000
            mag+=1
    elif(num < 1):
        while(num < 1 and mag > -8):
            num*=1000
            mag-=1
    if(polarity):
        num = -num
    evaluatedExpression = r"%.*f$\cdot 10^{%d}$ %s" % (precision, num, mag*3, extension)
    if(prefix[0] == '$' and prefix[-1] == '$'): #latex
        prefix = prefix.replace("$", "")
        display(Math(r"%s\text{%s}" % (prefix, evaluatedExpression)))
    else:
        display(Math(r"\text{%s}%s" % (prefix, evaluatedExpression)))  
