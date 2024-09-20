# Get user input for prefix or suffix
$option = Read-Host "Enter 1 for prefix or 2 for suffix"

# Validate the user input
while ($option -ne "1" -and $option -ne "2") {
    $option = Read-Host "Invalid input. Enter 1 for prefix or 2 for suffix"
}

# Get user input for the prefix or suffix value
$value = Read-Host "Enter the value for prefix or suffix"

# Get the current directory
# $folderPath = Get-Location

# Get all files in the folder
# $files = Get-ChildItem -Path $folderPath -File
$files = Get-ChildItem -File

# Iterate over each file
foreach ($file in $files) {
    # Exclude the script file itself from renaming
    if ($file.Name -ne "presuffix.ps1") {
        # Get the current filename
        $currentName = $file.Name
    
        # Create the new filename based on the user input option
        if ($option -eq "1") {
            # Prepend the prefix
            $newName = $value + $currentName
        }
        else {
            # Append the suffix
            $newName = $currentName + $value
        }
    
        # Rename the file
        $file | Rename-Item -NewName $newName
    }
}

# Pause the execution to prevent the console window from closing
# Pause