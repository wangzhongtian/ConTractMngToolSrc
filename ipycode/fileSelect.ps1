
$rootdirname="D:\\z\\_a\\nsbd\\ipy\\Excel账务\Log\\"
$dirname=$rootdirname+ "datalib\\"
$tgrName ="dataLibZD"


$tgrfolder = $dirname.Replace("datalib", $tgrname )
Remove-item  -LiteralPath  $tgrfolder -Force 
Copy-Item -Recurse -Force -LiteralPath $dirname -Destination $tgrfolder

$files = Get-ChildItem -Recurse $tgrfolder  | Where-Object   {  $_.Name -like "*.py1" } | Select-Object -Property fullName
$ptfiles =@()
foreach ( $file in $files ){
    $content =""
    $fn = $file.FullName
    $path = $file.Name
    $lines = Get-Content -LiteralPath $file.FullName -encoding Utf8
    #$lines
    #echo  "213432432"
    foreach ($line in $lines )
    {
        $content += $line
    }
    if ( $content -like "*记账单位Cls.zd*" )
    {
      #  write-host -NoNewline  "ZD find " 
       # write-host $fn
    }
    elseif ( $content -like "*记账单位Cls.pt*" )
    {
      #  write-host -NoNewline  "PT find " 
       # write-host $fn
       write-host  $content 
       write-host

       $ptfiles += $fn
    }
}

$ptfiles  | foreach-object -Process { $_; Remove-Item -LiteralPath $_  }