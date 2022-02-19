#! /bin/bash

real_path=$(realpath $0)
dir_name=`dirname "${real_path}"`
echo "real_path: ${real_path}"
echo "dir_name: ${dir_name}"

# build funset static library
# g++ -O3 -Wall -static -c -std=c++11 src/funset.cpp -Iinclude
# ar -r libfunset.a funset.o

# build funset dynamic library
g++ -O3 -Wall -shared -fPIC -std=c++11 -o libfunset.so -c src/funset.cpp -Iinclude

g++ -O3 -Wall -shared -std=c++11 -fPIC $(python3-config --includes) example.cpp \
    -o example$(python3-config --extension-suffix) \
    -L./ -lfunset \
    -I../../src/pybind11/include \
    -Iinclude

# # delete funset library, example.cpython-38-x86_64-linux-gnu.so has contained relevant export symbols
rm libfunset*

python test.py