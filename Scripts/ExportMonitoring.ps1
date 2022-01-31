	$watcher = New-Object System.IO.FileSystemWatcher
	$watcher.Path = ([System.Environment]::CurrentDirectory)
    $watcher.Filter = "*.zip*"
    $watcher.IncludeSubdirectories = $true
    $watcher.EnableRaisingEvents = $true
		
    $action = { 
				Expand-Archive *.zip -DestinationPath ([System.Environment]::CurrentDirectory)
				
				Get-ChildItem -Path ([System.Environment]::CurrentDirectory) | Where-Object {$_.BaseName -Match 'mvrs-[0-9]{6}-[0-9]{6}'} | Rename-Item -NewName {($_.BaseName -Replace 'mvrs-[0-9]{6}-[0-9]{6}', 'Upload')+$_.Extension}
              }    
			  
    Register-ObjectEvent $watcher "Created" -Action $action
    Register-ObjectEvent $watcher "Changed" -Action $action
    while ($true) {sleep 3}
