@echo off
setlocal EnableDelayedExpansion
title Git PATH Fixer
echo ========================================================
echo   Repairing System PATH and Enabling Git...
echo ========================================================
echo.

:: Check for administrative rights
net session >nul 2>&1
if %errorlevel% neq 0 (
    echo Requesting Administrator permissions...
    powershell -NoProfile -ExecutionPolicy Bypass -Command "Start-Process cmd.exe -ArgumentList '/c \"\"%~f0\"\"' -Verb RunAs"
    exit /b
)

:: Run cleanup in PowerShell
powershell -NoProfile -ExecutionPolicy Bypass -Command ^
  "$regKey = 'HKLM:\SYSTEM\CurrentControlSet\Control\Session Manager\Environment';" ^
  "$raw = (Get-ItemProperty -Path $regKey).Path;" ^
  "Set-ItemProperty -Path 'HKCU:\Environment' -Name 'PATH_SYSTEM_BACKUP' -Value $raw -Force;" ^
  "$cleaned = @();" ^
  "foreach ($e in ($raw -split ';')) {" ^
  "    $trimmed = $e.Trim().Trim('\"');" ^
  "    while ($trimmed.EndsWith('\') -and $trimmed.Length -gt 3) { $trimmed = $trimmed.Substring(0, $trimmed.Length - 1) };" ^
  "    if (-not [string]::IsNullOrWhiteSpace($trimmed) -and $cleaned -notcontains $trimmed) { $cleaned += $trimmed };" ^
  "};" ^
  "$gitPath = 'C:\Program Files\Git\cmd';" ^
  "if ($cleaned -notcontains $gitPath) { $cleaned += $gitPath };" ^
  "$newPath = $cleaned -join ';';" ^
  "Set-ItemProperty -Path $regKey -Name 'Path' -Value $newPath -Force;" ^
  "Add-Type -Namespace Win32 -Name NativeMethods -MemberDefinition '[System.Runtime.InteropServices.DllImport(\"\"user32.dll\"\", SetLastError = true, CharSet = System.Runtime.InteropServices.CharSet.Auto)] public static extern IntPtr SendMessageTimeout(IntPtr hWnd, uint Msg, UIntPtr wParam, string lParam, uint fuFlags, uint uTimeout, out UIntPtr lpdwResult);';" ^
  "$res = [UIntPtr]::Zero;" ^
  "[Win32.NativeMethods]::SendMessageTimeout([IntPtr]0xffff, 0x001A, [UIntPtr]::Zero, 'Environment', 2, 5000, [ref]$res);"

if %errorlevel% equ 0 (
    echo.
    echo ========================================================
    echo  [SUCCESS] System PATH repaired successfully!
    echo  [SUCCESS] Corrupted quotes removed.
    echo  [SUCCESS] Git (C:\Program Files\Git\cmd) is configured.
    echo ========================================================
    echo.
    echo Please CLOSE your current Command Prompt and open a NEW one.
) else (
    echo.
    echo [ERROR] An error occurred while updating the PATH.
)

echo.
pause
