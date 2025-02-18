\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{cls/ma-ths}[2023/10/01 v1.0 Master's Thesis Class]

% Load a standard base class that defines default font sizes etc.
\LoadClass[a4paper,12pt,twoside]{scrreprt}

% Load necessary packages
\RequirePackage{geometry}
\RequirePackage{fontspec} % Requires LuaLaTeX or XeLaTeX
\RequirePackage{hyperref}
\RequirePackage{setspace}
\RequirePackage{titlesec}
\RequirePackage{fancyhdr}
\RequirePackage{graphicx}
\RequirePackage{amsmath}
\RequirePackage{amsfonts}
\RequirePackage{amssymb}
\RequirePackage[toc]{glossaries}
\RequirePackage{listings} % Code listing
\RequirePackage{minted} % For better code highlighting
\RequirePackage{xcolor} % Added package
% \RequirePackage{apacite} % Removed to avoid conflict with biblatex

% Set up page dimensions
\geometry{
    a4paper,
    left=1.5in,
    right=1.5in,
    top=1in,
    bottom=1in,
    headheight=15pt,
    headsep=10pt,
    footskip=30pt
}

% Set font
\setmainfont[
  BoldFont={Times New Roman Bold},
  ItalicFont={Times New Roman Italic},
  BoldItalicFont={Times New Roman Bold Italic}
]{Times New Roman} % Requires LuaLaTeX or XeLaTeX
\setlength{\parindent}{0pt}
\setlength{\parskip}{1em}

% Line spacing
\onehalfspacing

% Title formatting
\titleformat{\chapter}[display]
  {\normalfont\huge\bfseries}
  {\chaptername\ \thechapter}{20pt}{\Huge}
  
\titleformat{\section}
  {\normalfont\Large\bfseries}
  {\thesection}{1em}{}

\titleformat{\subsection}
  {\normalfont\normalsize\bfseries}
  {\thesubsection}{1em}{}

\titleformat{\subsubsection}
  {\normalfont\small\bfseries}
  {\thesubsubsection}{1em}{}

% Header and footer
\pagestyle{fancy}
\fancyhf{}
\fancyhead[L]{\leftmark}
\fancyhead[R]{\thepage}
\fancyfoot[C]{\thepage}


% Title Page Setup (0_frontpage.tex)
\newcommand{\frontpage}{%
    \begin{titlepage}
        \centering
        \vspace*{1.5in} % Adjust top space as needed
        % Increased line spacing for the title lines
        {\fontsize{32}{40}\selectfont\bfseries Automatic Generation and Validation of Simulation Based Digital Twins}\\[2em]
        {\fontsize{28}{36}\selectfont\bfseries A Data-driven Framework and Case Study Application}\\[2.5em]
        \rule{\textwidth}{1pt}\\[2em]
        \begin{tabular}{rl}
            \textbf{Author:} & Daniel Fischer\\[1em]
            \textbf{Supervisor:} & Prof. Christian Schwede\\[1em]
            \textbf{Program:} & Research Master Data Science\\[1em]
            \textbf{Institution:} & Hochschule Bielefeld (HSBI)\\[1em]
            \textbf{Submission Date:} & \today\\[1em]
        \end{tabular}
        \vfill
    \end{titlepage}
}

% Example minted configuration for Python code
\definecolor{bgcolor}{rgb}{0.95,0.95,0.95} % Background color for code blocks
\newenvironment{pythoncode}{%
    \VerbatimEnvironment
    \begin{minted}[bgcolor=bgcolor,fontsize=\small,breaklines,linenos]{python}%
}{%
    \end{minted}%
}

% Example minted configuration for algorithms/pseudo code
\newenvironment{algocode}{%
    \VerbatimEnvironment
    \begin{minted}[bgcolor=bgcolor,fontsize=\small,breaklines,linenos]{text}%
}{%
    \end{minted}%
}

% Define the document class
\endinput
