\documentclass[journal,12pt,twocolumn]{IEEEtran}
\usepackage{amsthm}
\usepackage{graphicx}
\usepackage{mathrsfs}
\usepackage{txfonts}
\usepackage{stfloats}
\usepackage{pgfplots}
\usepackage{cite}
\usepackage{cases}
\usepackage{mathtools}
\usepackage{caption}
\usepackage{enumerate}	
\usepackage{enumitem}
\usepackage{amsmath}
\usepackage[utf8]{inputenc}
\usepackage[english]{babel}
\usepackage{multicol}
%\usepackage{xtab}
\usepackage{longtable}
\usepackage{multirow}
%\usepackage{algorithm}
%\usepackage{algpseudocode}
\newcommand*{\Comb}[2]{{}^{#1}C_{#2}}%
\usepackage{enumitem}
\usepackage{mathtools}
\usepackage{gensymb}
\usepackage{hyperref}
%\usepackage[framemethod=tikz]{mdframed}
\usepackage{listings}
    %\usepackage[latin1]{inputenc}                                 %%
    \usepackage{color}                                            %%
    \usepackage{array}                                            %%
    \usepackage{longtable}                                        %%
    \usepackage{calc}                                             %%
    \usepackage{multirow}                                         %%
    \usepackage{hhline}                                           %%
    \usepackage{ifthen}                                         %%
  \providecommand{\nCr}[2]{\,^{#1}C_{#2}}
  \providecommand{\nPr}[2]{\,^{#1}P_{#2}}
  \lstset{
%language=C,
frame=single, 
breaklines=true,
columns=fullflexible
}

\title{Assignment 4
\\Probability and Random Variables }
\author{Swati Mohanty (EE20RESCH11007) }
\date{February 2021}

\begin{document}

\maketitle


\section{Problem}
Find the probability distribution of
\\(i) number of heads in two tosses of a coin.
\\(ii) number of tails in the simultaneous tosses
of three coins.
\\(iii) number of heads in four tosses of a coin.

\section{Solution}
Let Y denote the random variable tossing a coin. Considering a fair coin, the probability of getting a Head or Tail P(Y) = 0.5 =p=1-p
\\In general , the probability of getting of j Head/Tail in n tosses is given as:
\begin{align}
    P(Y = j) = \Comb{n}{j}\times { p^j (1-p)^{(n-j)}} = \Comb{n}{j}\times { p^n } 
\end{align}
The binomial random variable for n tosses with p probability is:
X \textasciitilde B(n, p) 
\\(i)
 X = random variable of number of Heads.
The probability distribution of getting exactly j Heads in 2 tosses of coin is given as: X \textasciitilde B(2, 0.5)
 \[\implies n=2; j \in (0,n)\]
Using equation (1)
\begin{align}
    P(X = j)  =\Comb{2}{j}\times { 0.5^2}
\end{align}
We get the pdf as below:
\begin{align}
    P(X=0) =\Comb{2}{0}\times { 0.5^2}
    =0.25
    \\P(X=1) = \Comb{2}{1}\times { 0.5^2} = 0.5
    \\P(X=2) = \Comb{2}{2}\times { 0.5^2} = 0.25
\end{align}

\\The distribution table is given as:
\begin{center}
\begin{tabular}{ |c|c|c|c| } 
 \hline
 j & 0 & 1 & 2 \\\hline 
 P(X=j) & 0.25 &0.5 & 0.25 \\ 
 \hline
\end{tabular}
\end{center}

(ii)Let X = random variable of number of Tails.
The probability distribution of getting exactly j Tails in 3 tosses of coin is given as: X \textasciitilde B(3, 0.5) 
\[\implies n=3; j \in (0,n)\]
Using equation (1)
\begin{align}
    P(X = j)  =\Comb{3}{j}\times { 0.5^3}
\end{align}
We get the pdf as below:
\begin{align}
    P(X=0) = \Comb{3}{0}\times { 0.5^0 (1-0.5)^{(3-0)}}
    =0.125
    \\P(X=1) = \Comb{3}{1}\times { 0.5^3} = 0.375
    \\P(X=2) = \Comb{3}{2}\times { 0.5^3} = 0.375
    \\P(X=3) = \Comb{3}{3}\times { 0.5^3} = 0.125
\end{align}
\\The probability distribution of X is: 

\begin{center}
\begin{tabular}{ |c|c|c|c|c| } 
 \hline
 j & 0 & 1 & 2 & 3 \\ \hline
 P(X=j) & 0.125& 0.375 & 0.375 & 0.125 \\ 
 \hline
\end{tabular}
\end{center}
(iii)Let X = random variable of number of Heads.
The probability distribution of getting exactly j Heads in 4 tosses of coin is given as:  X \textasciitilde B(4, 0.5) 
\[\implies n=4; j \in (0,n)\]
Using equation (1)
\begin{align}
    P(X = j)  =\Comb{4}{j}\times { 0.5^4}
\end{align}
We get the pdf as below:
\begin{align}
    P(X=0) =(\Comb{4}{0}){ 0.5^0 (1-0.5)^{(4-0)}}
    =0.0625
    \\P(X=1) = \Comb{4}{1}\times { 0.5^4} = 0.25
    \\P(X=2) = \Comb{4}{2}\times { 0.5^4} = 0.375
    \\P(X=3) = \Comb{4}{3}\times { 0.5^4} = 0.25
    \\P(X=4) = \Comb{4}{4}\times { 0.5^4} = 0.0625
\end{align}
\\The probability distribution of X is: 

\begin{center}
\begin{tabular}{ |c|c|c|c|c|c| } 
 \hline
 j & 0 & 1 & 2 & 3 & 4 \\ \hline
 P(X=j) & 0.0625 & 0.25 & 0.375 & 0.25 & 0.0625 \\ 
 \hline
\end{tabular}
\end{center}
The probabilities were simulated using the python code.
\begin{figure}[h]
\renewcommand{\theenumi}{1}
\centering
\includegraphics[ width=\columnwidth , height =3cm]{cointoss.PNG}
\caption{Simulation for tossing a fair coin  }
\label{Fig:1}
\end{figure}

\textbf{Download python code from here}\\
\begin{lstlisting}
https://github.com/Swati-Mohanty/AI5002/blob/main/Assignment_4/codes/cointoss.py
\end{lstlisting}
\\\textbf{Download latex code from here-}\\
\begin{lstlisting}
https://github.com/Swati-Mohanty/AI5002/blob/main/Assignment_4/codes/assignment4.tex
\end{lstlisting}

\end{document}
