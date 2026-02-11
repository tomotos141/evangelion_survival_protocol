param([string]$PixivFile, [string]$DraftFile)
$pixiv = Get-Content -Encoding UTF8 $PixivFile -Raw
$draft = Get-Content -Encoding UTF8 $DraftFile -Raw
$caption = ($draft -split '\[caption\]\r?\n',2)[1] -replace '\r?\n\[/caption\][\s\S]*',''
($pixiv + "`n====================`n" + $caption) | Set-Clipboard
