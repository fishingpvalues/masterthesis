# Define the folder containing the LaTeX project
$latexProjectPath = "D:\masterthesis\"
$outputFileName = "output.tex"
$pdfFileName = "output.pdf"
$outputDirectory = "$latexProjectPath\output"

# Set the current location to the LaTeX project folder
Set-Location -Path $latexProjectPath

# Define the list of common LaTeX auxiliary file extensions
# Exclude aux and bbl files from deletion here after FORCED compilation for once at the end.
# These are necessary for the bibliography and cross-referencing.
$auxExtensions = @("*.aux", "*.log", "*.fls", "*.fdb_latexmk", "*.synctex.gz", "*.out", "*.toc", "*.bbl", "*.blg", "*.nav", "*.snm")

# Delete all auxiliary files with matching extensions
foreach ($ext in $auxExtensions) {
    $files = Get-ChildItem -Filter $ext
    foreach ($file in $files) {
        Remove-Item $file.FullName -Force
    }
}

# First compilation using latexmk with biber backend
latexmk -pdf -pdflatex="xelatex %O %S" -quiet -f $outputFileName

# Run makeglossaries to process all glossary entries
# Get the base name (without extension) of the main file
$baseName = [System.IO.Path]::GetFileNameWithoutExtension($outputFileName)
if (Test-Path "$latexProjectPath\$baseName.glo") {
    Write-Host "Running makeglossaries on $baseName..."
    makeglossaries $baseName
}

# Re-compile so the glossary entries are incorporated
latexmk -pdf -pdflatex="xelatex %O %S" -quiet -f $outputFileName

# Check if compilation was successful
if (Test-Path $pdfFileName) {
    # Create output directory if it doesn't exist
    if (-not (Test-Path $outputDirectory)) {
        New-Item -ItemType Directory -Path $outputDirectory
    }

    # Get the current date and time in EU format
    $dateTime = Get-Date -Format "dd-MM-yyyy_HH-mm"
    $draftFileName = "draft_$dateTime.pdf"
    
    # Move the compiled PDF to the output directory with the new name
    Move-Item -Path $pdfFileName -Destination "$outputDirectory\$draftFileName"

    # Open the PDF in the default PDF reader
    Start-Process "$outputDirectory\$draftFileName"
} else {
    Write-Host "Compilation failed. Please check for errors in the LaTeX file."
}