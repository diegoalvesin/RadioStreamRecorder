# Powershell script to be runned at Jenkins job schedules at the time show starts

$path = 'C:\temp'
if (-not(Test-Path -Path $path))
{
    New-Item -Path $path -ItemType directory
}
Set-Location -Path $path
$url = 'https://raw.githubusercontent.com/pasajero/RadioStreamRecorder/master/RadioRecorder.py'
$pathfinal = $path + '\RadioRecorder.py'
$client = New-Object System.Net.WebClient
$client.DownloadFile($url, $pathfinal)
python $pathfinal -d 2 -u http://lagosdemoreno.radioudg.okhosting.com:8000/ -f FiccionesDeLaPalabra
