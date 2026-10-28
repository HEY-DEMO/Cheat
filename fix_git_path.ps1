# Backup current PATH
$regKey = 'HKLM:\SYSTEM\CurrentControlSet\Control\Session Manager\Environment'
$raw = (Get-ItemProperty -Path $regKey).Path

# Save backup to user registry just in case
Set-ItemProperty -Path 'HKCU:\Environment' -Name 'PATH_SYSTEM_BACKUP' -Value $raw -Force

$entries = $raw -split ';'
$cleaned = @()

foreach ($e in $entries) {
    # Remove quotes and whitespace
    $trimmed = $e.Trim().Trim('"').Trim('\"')
    while ($trimmed.EndsWith('\') -and $trimmed.Length -gt 3) {
        $trimmed = $trimmed.Substring(0, $trimmed.Length - 1)
    }
    if (-not [string]::IsNullOrWhiteSpace($trimmed) -and $cleaned -notcontains $trimmed) {
        $cleaned += $trimmed
    }
}

# Ensure Git cmd is included
$gitPath = 'C:\Program Files\Git\cmd'
if ($cleaned -notcontains $gitPath) {
    $cleaned += $gitPath
}

$newPath = $cleaned -join ';'

# Update System PATH
Set-ItemProperty -Path $regKey -Name 'Path' -Value $newPath -Force

# Notify Windows of environment change
Add-Type -Namespace Win32 -Name NativeMethods -MemberDefinition @"
[System.Runtime.InteropServices.DllImport("user32.dll", SetLastError = true, CharSet = System.Runtime.InteropServices.CharSet.Auto)]
public static extern IntPtr SendMessageTimeout(IntPtr hWnd, uint Msg, UIntPtr wParam, string lParam, uint fuFlags, uint uTimeout, out UIntPtr lpdwResult);
"@
$HWND_BROADCAST = [IntPtr]0xffff
$WM_SETTINGCHANGE = 0x001A
$result = [UIntPtr]::Zero
[Win32.NativeMethods]::SendMessageTimeout($HWND_BROADCAST, $WM_SETTINGCHANGE, [UIntPtr]::Zero, "Environment", 2, 5000, [ref]$result)

Write-Host "System PATH successfully repaired and updated!" -ForegroundColor Green
Write-Host "Git path verified: $gitPath" -ForegroundColor Cyan
Write-Host "Backup saved to HKCU:\Environment\PATH_SYSTEM_BACKUP" -ForegroundColor Gray
Start-Sleep -Seconds 3
