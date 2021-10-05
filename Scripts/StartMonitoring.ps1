	$watcher = New-Object System.IO.FileSystemWatcher
    #$watcher.Path = "C:\Users\christophers.UNITED-SYSTEMS\Desktop"
	$watcher.Path = ([System.Environment]::CurrentDirectory)
    $watcher.Filter = "*.zip*"
    $watcher.IncludeSubdirectories = $true
    $watcher.EnableRaisingEvents = $true  

    $action = { 
				Expand-Archive *.zip -DestinationPath ([System.Environment]::CurrentDirectory)
              }    
			  
    Register-ObjectEvent $watcher "Created" -Action $action
    Register-ObjectEvent $watcher "Changed" -Action $action
    while ($true) {sleep 5}