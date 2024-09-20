# Function to get battery status
function Get-BatteryStatus {
    $battery = Get-WmiObject -Class Win32_Battery
    $batteryStatus = $battery | Select-Object -ExpandProperty BatteryStatus
    $batteryLevel = $battery | Select-Object -ExpandProperty EstimatedChargeRemaining
    return @{
        Status = $batteryStatus
        Level = $batteryLevel
    }
}

# Function to send alert
function Send-Alert {
    param (
        [string]$message
    )
    Add-Type -AssemblyName System.Windows.Forms
    [System.Windows.Forms.MessageBox]::Show($message, "Battery Alert", [System.Windows.Forms.MessageBoxButtons]::OK, [System.Windows.Forms.MessageBoxIcon]::Information)
}

# Main loop to check battery status every minute
while ($true) {
    $batteryStatus = Get-BatteryStatus
    $batteryLevel = $batteryStatus.Level

    $timestamp = Get-Date -Format "HH:mm"
    Write-Host "$timestamp - $batteryLevel%"

    if ($batteryLevel -gt 80) {
        Send-Alert -message "Battery level is over 80%"
    } elseif ($batteryLevel -lt 30) {
        Send-Alert -message "Battery level is under 30%"
    }

    # Wait for 60 seconds (1 minute)
    Start-Sleep -Seconds 60
}
