#!/bin/sh

declare script_name="ocr"
declare personal_bin="/Users/$USER/bin"
declare cfg=".bash_profile"

eval pip3 install -r requirements.txt

[ -n $ZSH_VERSION ] && 
cfg=".zprofile"

[[ -d $personal_bin ]] || mkdir $personal_bin &&
echo export PATH="$personal_bin:\$PATH" >> /Users/$USER/$cfg

chmod +x ./${script_name}.py &&
cp ./${script_name}.py $personal_bin/${script_name}