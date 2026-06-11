# Compilación de librería estática y programa principal

CXX = g++
CXXFLAGS = -Wall -O2

SRC = src
LIB = lib
BIN = bin

LIB_OBJS = $(SRC)/Pila.o $(SRC)/EvaluadorPostfijo.o
LIB_NAME = $(LIB)/libpostfijo.a

MAIN = main.cpp

all: $(LIB_NAME) build

$(LIB_NAME): $(LIB_OBJS)
	mkdir -p $(LIB)
	ar rcs $(LIB_NAME) $(LIB_OBJS)

$(SRC)/Pila.o: $(SRC)/Pila.cpp $(SRC)/Pila.h
	$(CXX) $(CXXFLAGS) -c $(SRC)/Pila.cpp -o $(SRC)/Pila.o

$(SRC)/EvaluadorPostfijo.o: $(SRC)/EvaluadorPostfijo.cpp $(SRC)/EvaluadorPostfijo.h
	$(CXX) $(CXXFLAGS) -c $(SRC)/EvaluadorPostfijo.cpp -o $(SRC)/EvaluadorPostfijo.o

build:
	mkdir -p $(BIN)
	$(CXX) $(MAIN) -L$(LIB) -lpostfijo -o $(BIN)/programa

clean:
	rm -f $(SRC)/*.o
	rm -f $(LIB)/*.a
	rm -f $(BIN)/*
