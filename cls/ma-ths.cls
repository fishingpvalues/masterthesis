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
\RequirePackage[toc]{glossaries} % Glossary handling
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
    headsep=8,
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
\titlespacing*{\chapter}{\parindent}{*1.8}{*1.2}
\titlespacing*{\section}{\parindent}{*1.5}{*1.0} % Example: Reduce space below section titles
\titlespacing*{\subsection}{\parindent}{*1.2}{*0.8}
\titlespacing*{\subsubsection}{\parindent}{*1.0}{*0.6}
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
    \begin{titlepage}
        \centering
        \vspace*{1.8in} % Increased top space for balance
        {\fontsize{34}{90}\selectfont\bfseries Automatic Verification and Validation of Automatically Generated Simulation-Based Digital Twins for Discrete Material Flow Systems}\\[2em] % Increased vertical space after title from 1em to 2em
        \rule{\textwidth}{1pt}\\[2em]
        \begin{tabular}{rl}
            \textbf{Author:}       & Daniel Fischer\\[1em]
            \textbf{Supervisor:}   & Prof. Christian Schwede\\[1em]
            \textbf{Program:}      & Research Master Data Science\\[1em]
            \textbf{Institution:}  & Hochschule Bielefeld (HSBI)\\[1em]
            \textbf{Submission Date:} & \today\\[1em]
        \end{tabular}
        \vfill
    \end{titlepage}
}

% Define a default background color for minted code blocks
\definecolor{bgcolor}{rgb}{0.95,0.95,0.95}

% In your preamble:
\usepackage{enumitem}
\setlist{nosep}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% End of Class Definition
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\endinput
