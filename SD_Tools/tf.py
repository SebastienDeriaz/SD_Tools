from scipy import signal
from scipy.signal import TransferFunction

from IPython.display import display, Math, Latex

def print_tf_simplified(tf: TransferFunction, precision=2):
    num = ""
    den = ""
    c = "s" if TransferFunction.dt is None else "z"
    if(len(tf.num) > 0):
        exponent = len(tf.num) - 1
        for n in tf.num:
            if(n > 0):
                if(exponent < len(tf.num) - 1):
                    num += "+"
                if(n != 1 and n != 1.0):
                    num += "%.*f" % (precision, n)
                if(exponent > 1):
                    num += "%c^{%d}" % (c, exponent)
                elif(exponent > 0):
                    num += c
            exponent -= 1
    if(len(tf.den) > 0):
        exponent = len(tf.den) - 1
        for d in tf.den:
            if(d > 0):
                if(exponent < len(tf.den) - 1):
                    den += "+"
                    
                if(d != 1 and d != 1.0):
                    den += "%.*f" % (precision, d)
                if(exponent > 1):
                    den += "%c^{%d}" % (c, exponent)
                elif(exponent > 0):
                    den += c
            
            exponent -= 1
    
    if(len(tf.num) > 0 and len(tf.den) > 0):
        display(Latex(r"$\Large\frac{%s}{%s}$" % (num, den)))
    elif(len(tf.num) > 0):
        display(Latex(r"$%s$" % num))
    else:
        print("Error displaying transfer function")

def print_tf_factorized(tf: TransferFunction, precision=2):
    zeros, poles, K = signal.tf2zpk(tf.num, tf.den)
    num = ""
    den = ""
    gain = "%.*f" % (precision, K)
    c = "s" if TransferFunction.dt is None else "z"
    if(len(zeros) > 0):
        num += "("
        for z in zeros:
            if(z == 0 or z == 0.0):
                num += c
            else:
                num += "(%.*f - %c)" % (precision, z, c)
        num += ")"
    if(len(poles) > 0):
        for p in poles:
            if(p == 0 or p == 0.0):
                den += c
            elif(p > 0):
                den += "(%c - %.*f)" % (c, precision, p)
            else:
                den += "(%c + %.*f)" % (c, precision, abs(p))
                
    
    
    if(len(tf.num) > 0 and len(tf.den) > 0):
        display(Latex(r"$\Large\frac{%s%s}{%s}$" % (gain, num, den)))
    elif(len(tf.num) > 0):
        display(Latex(r"$%s * %s$" % (gain, num)))
    else:
        print("Error displaying transfer function") 
    
    
    
    
    
    
    
    
    
    
    