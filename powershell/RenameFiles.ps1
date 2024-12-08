# Set the directory containing text files
$directory = "C:\coding\codingInterviewUniversity\powershell"  # Your specific directory path
Set-Location $directory

# Get all .txt files in the directory
$textFiles = Get-ChildItem -Filter "*.txt"

foreach ($file in $textFiles) {
    try {
        # Read the content of the file (first line only)
        $content = Get-Content -Path $file.FullName | Select-Object -First 1

        # Generate a new filename by appending the content to the base name
        if ($content) {
            # Remove invalid characters for filenames
            $content = $content -replace '[<>:"/\\|?*]', ''  # Clean content

            # Create the new filename by appending the content to the base name
            $newName = "$($file.BaseName)_$content$($file.Extension)"

            # Ensure the new filename includes the full path
            $newPath = Join-Path -Path $file.DirectoryName -ChildPath $newName

            # Rename the file if the new name is different
            if ($file.FullName -ne $newPath) {
                Rename-Item -Path $file.FullName -NewName $newPath
                Write-Host "Renamed: $($file.Name) -> $newName"
            } else {
                Write-Host "Skipping: $($file.Name) - name is the same"
            }
        } else {
            Write-Host "Skipping $($file.Name) - file is empty"
        }
    } catch {
        Write-Host "Error processing $($file.Name): $_"
    }
}
