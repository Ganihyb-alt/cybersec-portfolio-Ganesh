Write-Host "=== Basic Enumeration Script ==="
Write-Host "User:"; whoami
Write-Host "`nPrivileges:"; whoami /priv
Write-Host "`nSystem Info:"; systeminfo
Write-Host "`nUsers:"; net users
Write-Host "`nNetwork Config:"; ipconfig /all
Write-Host "`nRunning Processes:"; tasklist
Write-Host "`nListening Ports:"; netstat -ano
