obj-m += tcp_time_shift.o
# Include the json-c header file.
all:
	
	make -C /lib/modules/$(shell uname -r)/build M=$(PWD) modules

clean:
	make -C /lib/modules/$(shell uname -r)/build M=$(PWD) clean

ins:
	sudo dmesg -C
	sudo insmod tcp_time_shift.ko

rm:
	sudo rmmod tcp_time_shift


