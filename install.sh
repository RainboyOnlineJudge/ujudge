mkdir build
cd build && cmake .. && make && sudo make install
cd .. && python3 setup.py install || exit 1
