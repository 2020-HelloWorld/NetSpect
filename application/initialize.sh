#!/bin/bash
cd delay_detect
make clean
make
cd ..

cd delay_queue
make clean
make 
cd ..

cd tcp_override
make clean
make
cd ..

cd ttl_detect
make clean
make 
cd ..

cd ttl_prevent
make clean
make 
cd ..

