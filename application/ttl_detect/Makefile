CC = gcc
LIBS = -lpcap -ljson-c

SRC = ttl_deviation.c
TARGET = packet_capture

all: $(TARGET)

$(TARGET): $(SRC)
	$(CC) $(SRC) -o $(TARGET) $(LIBS)

clean:
	rm -f $(TARGET)

.PHONY: all clean
