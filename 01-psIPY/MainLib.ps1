function MainEntry( $curcfg1 , $pythonExecName,$Scripts,$PythonFolder){
    pushd ../
    if (test-path -path  glbcfg.py ) {
        rm "glbcfg.py"
    }
    out-host -inputObject $curcfg1
    copy $curcfg1 "glbcfg.py" 
    dir "glbcfg.py"

    pushd $PythonFolder
    
    $a = $Scripts -split ";"
    # out-host $a 
    foreach($item in $a) {
        out-host -inputobject $item
        . $pythonExecName $item 
     }
    popd 
    popd
}