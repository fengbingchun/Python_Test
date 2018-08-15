#! /bin/bash

real_path=$(realpath $0)
dir_name=`dirname "${real_path}"`
echo "real_path: ${real_path}, dir_name: ${dir_name}"

new_dir_name=${dir_name}/build
mkdir -p ${new_dir_name}
cd ${new_dir_name}
cmake ..
make

cd -

name="Python_DLL_1.py"
if [ -f ${name} ]; then
	rm ${name}
fi

ln -s ../../Demo/Python_Cplusplus/Python_DLL_1/${name} .

python3 ${name}

