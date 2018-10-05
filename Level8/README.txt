In the file are a list of hashed passwords, are you able to decode any of them? hint use hashcat

to use hash cat you need to run these 2 commands first

apt remove clang*
apt remove llvm*
apt-get autoremove -y

apt install clang-3.8
apt install libclang-3.8-dev
vim .bashrc -> Add clang to path "PATH=$PATH:/usr/lib/llvm-3.8/bin"

apt-get install libhwloc-dev ocl-icd-dev ocl-icd-opencl-dev
apt-get install pocl-opencl-icd

apt install pkg-config
apt install autotools-dev
apt install cmake
apt install make
apt install libltdl3-dev

git clone https://github.com/pocl/pocl
cd pocl
./autogen.sh
./configure
make
make install

Once done here is a usefull link to help you learn hashcat
https://resources.infosecinstitute.com/hashcat-tutorial-beginners/#gref