int fibonacci(int n) {
    if (n <= 1){// caso base
        return n;
    } 
    return fibonacci(n - 1) + fibonacci(n - 2);// caso general
}