param(
    [string]$InputPath,
    [string]$OutputPath
)

try {
    # ファイル読み込み
    $content = Get-Content -Path $InputPath -Raw -Encoding UTF8

    # 変換処理
    # 1. タイトル行 (# Title) を削除
    $content = $content -replace '^#\s+.*(\r?\n|\r)', ''
    
    # 2. 区切り線 (***) を改ページ ([newpage]) に
    $content = $content -replace '\*\*\*', '[newpage]'
    
    # 3. 章見出し (## Title) をPixiv記法 ([chapter: Title]) に
    $content = $content -replace '##\s+(.*)', '[chapter: $1]'
    
    # 4. 太字 (**) を削除 (Pixivは太字非対応のため)
    $content = $content -replace '\*\*(.*?)\*\*', '$1'
    
    # 5. 斜体 (*) を削除
    $content = $content -replace '\*(.*?)\*', '$1'

    # 6. [caption] ブロックを削除
    $content = $content -replace '(?s)\[caption\].*?\[/caption\]', ''
    # 余分な改行をトリム
    $content = $content.Trim()

    # 保存
    Set-Content -Path $OutputPath -Value $content -Encoding UTF8
    Write-Host "Success: Converted $InputPath to $OutputPath"

}
catch {
    Write-Error "Conversion Failed: $_"
    exit 1
}
