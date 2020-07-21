# kryptotoolsmitlatex
Scripts, die das Leben bei der Arbeit mit Latex einfacher machen.


### Beispiel für eeaforlatex.py:

##### python eeaforlatex.py 31415 271828

\textbf{Berechnung der Inversen mittels EEA}\\
\begin{tabular}{|c|c|c|c|c|}
\hline
i & $q_{i-1}$ & $r_i$ & $s_i$ & $t_i$ \\ %header
\hline \hline
0 & 0 & 271818 & 1 & 0 \\ \hline
1 & 0 & 31415 & 0 & 1 \\ \hline
2 & 8 & 20498 & 1 & -8 \\ \hline
3 & 1 & 10917 & -1 & 9 \\ \hline
4 & 1 & 9581 & 2 & -17 \\ \hline
5 & 1 & 1336 & -3 & 26 \\ \hline
6 & 7 & 229 & 23 & -199 \\ \hline
7 & 5 & 191 & -118 & 1021 \\ \hline
8 & 1 & 38 & 141 & -1220 \\ \hline
10 & 5 & 1 & -823 & \textbf{7121} \\ \hline
11 & & \textbf{0} & & \\ \hline
\end{tabular}\\
###### Lösung: Die Inverse von 31415 ist 7121 mod 271818\\

### Beispiel für sqmforlatex.py

##### python sqmforlatex.py 123 456 789


\textbf{Berechnung von $123^{456} \textnormal{ mod 789}$ mittels SQM}\\
\begin{tabular}{|c|c c|}
\hline
456 als bits & schrittweise Rechnung & mod 789\\ %header
\hline \hline
1 & $123^1$ = 123 & mod 789\\ \hline 
1 & $123^2 \cdot 123$ = 405 & mod 789\\ \hline 
1 & $405^2 \cdot 123$ = 345 & mod 789\\ \hline 
0 & $345^2$ = 675 & mod 789\\ \hline 
0 & $675^2$ = 372 & mod 789\\ \hline 
1 & $372^2 \cdot 123$ = 135 & mod 789\\ \hline 
0 & $135^2$ = 78 & mod 789\\ \hline 
0 & $78^2$ = 561 & mod 789\\ \hline 
0 & $561^2$ = 699 & mod 789\\ \hline 
\end{tabular}\\
###### Lösung: $123^{456}$ = 699 mod 789\\
