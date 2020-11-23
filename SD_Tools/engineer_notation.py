from IPython.display import display, Math

def to_units(prefix : str, num : float, extension : str, precision : int = 2):
    if(extension == "kg" or extension == "$kg$"):
        num = num * 1000
        mag = 1
        etension.replace("k", "")
    else:
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
    formattedExtension = __latexDisplay(" " + indices[mag+8] + extension)
    evaluatedExpression = "%.*f %s" %(precision, num, formattedExtension)
    
    formattedPrefix = __latexDisplay(prefix)
    mathExpression = formattedPrefix + evaluatedExpression
    display(Math(mathExpression))
    

def __latexDisplay(strIn : str):
    strOut = list(strIn)
    for i in range(0, len(strIn)):
        if(i == 0):
            if(strIn[i] == "$"):
                #On entre en mode équation
                equationMode = True
            else:
                #On entre en mode texte
                strOut[i] = r"\text{" + strIn[i]
                equationMode = False
        if(i == len(strIn)-1): #Dernier élément
            if(not equationMode):
                strOut[i] =  strIn[i] + "}"
            else:
                strOut[i] = ' '
        elif(strIn[i] == "$" and i > 0):
            if(equationMode):
                equationMode = False
                strOut[i] = r"\text{"
            else:
                equationMode = True
                strOut[i] = "}"
    strOut = "".join(strOut)
    return strOut

def to_eng(prefix : str, num : float, extension : str, precision : int = 2):
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
    formattedExtension = __latexDisplay(" " + extension)
    evaluatedExpression = r"%.*f\cdot 10^{%d} %s" %(precision, num, mag*3, formattedExtension)
    
    formattedPrefix = __latexDisplay(prefix)
    mathExpression = formattedPrefix + evaluatedExpression
    display(Math(mathExpression))
