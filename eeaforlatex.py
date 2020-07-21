

import sys,math # für argv und floor funktion
import pyperclip #latextext wird direkt in die zwischenablage reingeballert

howto="""
HOW TO USE:
python eeaforlatex.py a p
 - returns a^b mod p calculated
 - represented for latex for easy copy paste
"""

if(len(sys.argv)<3):
    print("##########################\nNot enough arguments used!\n##########################"+howto)
    exit()
 
a=int(sys.argv[1])
p=int(sys.argv[2])
result=0

kopf=f"""\\textbf{{Berechnung der Inversen mittels EEA}}\\\\
\\begin{{tabular}}{{|c|c|c|c|c|}}
\hline
i & $q_{{i-1}}$ & $r_i$ & $s_i$ & $t_i$ \\\\ %header
\hline \hline
"""
# nutze den erweiterten euklidischen algorithmus mod inv. algorithmus
# aus dem buch "kryptographie einfach erklärt" von christof paar
i=2
q=[0,0]
r=[p,a]
s=[1,0]
t=[0,1]
while(True):
    q.append(0)  
    r.append(".")  
    s.append(".") 
    t.append(".") 
    r[i]=r[i-2]%r[i-1]
    if(r[i]==0):
        result=(t[i-1])%p
        break
    else:
        q[i]=math.floor(r[i-2]/r[i-1])    
        s[i]=s[i-2]-q[i]*s[i-1]
        t[i]=t[i-2]-q[i]*t[i-1]
        i+=1

#latexmacherei
text=""
for e in range(i-1):
    text+=f"{e} & {q[e]} & {r[e]} & {s[e]} & {t[e]} \\\\ \hline\n"
text+=f"{i} & {q[i-1]} & {r[i-1]} & {s[i-1]} & \\textbf{{{t[i-1]}}} \\\\ \hline\n"
text+=f"{i+1} & & \\textbf{{0}} & & \\\\ \hline\n"


end=f"""\end{{tabular}}\\\\
Lösung: Die Inverse von {a} ist {result} mod {p}\\\\"""
#print(end)

print(kopf+text+end)
pyperclip.copy(kopf+text+end)
