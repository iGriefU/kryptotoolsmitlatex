import sys
try:
    import pyperclip #latextext wird direkt in die zwischenablage reingeballert
except ModuleNotFoundError:
    print("\n#####################\nMODULE pyperclip NOT INSTALLED!\n#####################\nType in terminal: sudo python -m pip install pyperclip\n")
    exit()

howto="""
HOW TO USE:
python sqmforlatex.py a b p
 - returns a^b mod p calculated, represented for latex
 - directly copied to yourt clipboard
"""

if(len(sys.argv)<4):
    print("##########################\nNot enough arguments used!\n##########################"+howto)
 
a=int(sys.argv[1])
b=int(sys.argv[2])
p=int(sys.argv[3])
 
b_bin=bin(b)[2:]

kopf=f"""\\textbf{{Berechnung von ${a}^{{{b}}} \\textnormal{{ mod {p}}}$ mittels SQM}}\\\\
\\begin{{tabular}}{{|c|c c|}}
\hline
{b} als bits & schrittweise Rechnung & mod {p}\\\\ %header
\hline \hline
1 & ${a}^1$ = {a} & mod {p}\\\\ \hline \n"""

temp=a
text=""
for bit in b_bin[1:]: # jede zeile vom latex table wird geprintet
    if bit=="0":
        text+=f"""{bit} & ${temp}^2$ = """
        temp=(temp**2)%p
        text+=f"""{temp} & mod {p}\\\\ \hline \n"""

    else:
        text+=f"""{bit} & ${temp}^2 \\cdot {a}$ = """
        temp=(((temp**2)%p)*a)%p
        text+=f"""{temp} & mod {p}\\\\ \hline \n"""
#am ende ist temp das ergebnis

end=f"""\end{{tabular}}\\\\
Lösung: ${a}^{{{b}}}$ = {temp} mod {p}\\\\"""
#print(end)

print(kopf+text+end)
pyperclip.copy(kopf+text+end)