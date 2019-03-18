#/bin/bash

set +e

echo "========== 100 ==========\n"
rm 100
g++ -o 100 100.cpp
echo "========== app ==========\n"
rm app
g++ -o app app.cpp
 
