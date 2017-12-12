mkdir build
cd build && cmake .. && make && make install
cd .. && python3 setup.py install || exit 1
