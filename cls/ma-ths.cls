\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{cls/ma-ths}[2023/10/01 v1.0 Master's Thesis Class]

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% Base Class & Package Loading
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Load a standard base class (scrreprt) that defines default font sizes, etc.
\LoadClass[a4paper,12pt]{scrreprt}

% Required packages
\RequirePackage{geometry}     % Page geometry setup
\RequirePackage{fontspec}       % Font selection (requires LuaLaTeX or XeLaTeX)
\RequirePackage{hyperref}       % Hypertext links
\RequirePackage{setspace}       % Line spacing control
\RequirePackage{titlesec}       % Section title formatting
\RequirePackage{fancyhdr}       % Header and footer customization
\RequirePackage{graphicx}       % Graphics inclusion
\RequirePackage{amsmath}        % Advanced math typesetting
\RequirePackage{amsfonts}       % Math fonts
\RequirePackage{amssymb}        % Additional math symbols
\RequirePackage[toc,acronym,nonumberlist,style=long]{glossaries} % Glossary handling - using simpler style
\RequirePackage{listings}       % Code listings
\RequirePackage{minted}         % Enhanced code highlighting
\RequirePackage{xcolor}         % Color management

% Note: Removed apacite package to avoid conflicts with biblatex

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% Page Layout & Geometry
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\geometry{
    a4paper,
    left=3.0cm,
    right=2.5cm,
    top=2cm,
    bottom=1.8cm,
    headheight=12pt,
    headsep=8pt,
    footskip=25pt
}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% Font Settings
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\setmainfont[
  BoldFont={Times New Roman Bold},
  ItalicFont={Times New Roman Italic},
  BoldItalicFont={Times New Roman Bold Italic}
]{Times New Roman} % Requires LuaLaTeX or XeLaTeX

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% Paragraph & Line Spacing
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\setlength{\parindent}{0pt}
\setlength{\parskip}{3pt plus 1pt minus 1pt}
%\setlength{\parskip}{1em}
\setstretch{1.2} % Or try 1.35, 1.3 etc.
%\onehalfspacing

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% Title & Section Formatting
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\titleformat{\chapter}
  {\normalfont\Huge\bfseries}
  {\chaptername\ \thechapter:}{1em}{\Huge}

\titleformat{\section}
  {\normalfont\Large\bfseries}
  {\thesection}{1em}{}

\titleformat{\subsection}
  {\normalfont\normalsize\bfseries}
  {\thesubsection}{1em}{}

\titleformat{\subsubsection}
  {\normalfont\small\bfseries}
  {\thesubsubsection}{1em}{}

\titleformat{\paragraph}[runin]
  {\normalfont\normalsize\bfseries}
  {\theparagraph}{1em}{}[.]

\titlespacing*{\chapter}{\parindent}{*1.8}{*1.2}
\titlespacing*{\section}{\parindent}{*1.5}{*1.0} % Example: Reduce space below section titles
\titlespacing*{\subsection}{\parindent}{*1.2}{*0.8}
\titlespacing*{\subsubsection}{\parindent}{*1.0}{*0.6}
\titlespacing*{\paragraph}{\parindent}{1.1em}{1em}
% Adjust the {beforesep} (*1.5 etc) and {aftersep} (*1.0 etc) multipliers.
% Using \parindent (0pt here) for left margin alignment. Decrease the multipliers.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% Header and Footer Configuration
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\pagestyle{fancy}
\fancyhf{} % Clear default header and footer
\fancyhead[L]{\leftmark}
\fancyhead[R]{\thepage}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% Custom Commands & Environments
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Enhanced title page command
\newcommand{\frontpage}{%
    \newgeometry{top=2.5cm, bottom=1.5cm, left=2.5cm, right=2cm}
    \begin{titlepage}
        \centering
        \vspace*{1.2cm}
        {\LARGE\bfseries HOCHSCHULE BIELEFELD\\[0.5em]
        UNIVERSITY OF APPLIED SCIENCES AND ARTS\\[2em]}
        
        {\large\bfseries MASTER'S DEGREE PROGRAMME\\[0.5em]
        DATA SCIENCE (RESEARCH MASTER)\\[2em]}
        
        {\usefont{T1}{ppl}{b}{n}
        \fontsize{22pt}{28pt}\selectfont
        \begin{center}
          \begin{minipage}{0.9\textwidth}
            \centering
            Automatic Verification and Validation of Automatically Generated Simulation-Based Digital Twins for Discrete Material Flow Systems
          \end{minipage}
        \end{center}
        }
        
        \vspace{2em}
        {\large Master's Thesis\\[2em]}
        
        {\Large\bfseries Daniel Fischer\\[0.5em]
        Matriculation Number: 50008155\\[1.5em]}
        
        {\normalsize
        Degree: Master of Science (M.Sc.)\\
        Study model: Full-Time Study\\
        Faculty: Engineering and Mathematics\\
        Study location: Gütersloh\\[1.5em]
        Supervisor: Prof. Christian Schwede\\[1.5em]
        Submission Date: \today
        }
        
        \vfill
        \vspace*{1.2cm}
    \end{titlepage}
    \restoregeometry
}

% Define a default background color for minted code blocks
\definecolor{bgcolor}{rgb}{0.95,0.95,0.95}

% In your preamble:
\usepackage{enumitem}
\setlist{nosep}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% Chapter Configuration (Allow chapters to start on any page)
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\makeatletter
\let\old@chapter\@chapter
\def\@chapter[#1]#2{\ifnum \c@secnumdepth >\m@ne
    \if@mainmatter
      \refstepcounter{chapter}%
      \typeout{\@chapapp\space\thechapter.}%
      \addcontentsline{toc}{chapter}%
      {\protect\numberline{\thechapter}#1}%
    \else
      \addcontentsline{toc}{chapter}{#1}%
    \fi
  \else
    \addcontentsline{toc}{chapter}{#1}%
  \fi
  \chaptermark{#1}%
  \addtocontents{lof}{\protect\addvspace{10\p@}}%
  \addtocontents{lot}{\protect\addvspace{10\p@}}%
  \if@twocolumn
    \@topnewpage[\@makechapterhead{#2}]%
  \else
    \@makechapterhead{#2}%
    \@afterheading
  \fi}
\makeatother

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% End of Class Definition
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\endinput
