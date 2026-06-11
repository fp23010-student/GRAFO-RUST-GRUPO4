#include "header.h"
#include <iostream>
#include <vector>

Node* createListFromArray(const std::vector<int>& arr) {
    Node* head = nullptr;
    for (int i = static_cast<int>(arr.size()) - 1; i >= 0; --i) {
        head = new Node(arr[i], head);
    }
    return head;
}
void freeList(Node* head) {
    while (head) {
        Node* tmp = head;
        head = head->next;
        delete tmp;
    }
}
std::pair<long long, long long> sumParity(Node* head, bool isOdd) {
    if (!head) return {0LL, 0LL};
    auto rest = sumParity(head->next, !isOdd);
    if (isOdd) rest.first += head->value;
    else        rest.second += head->value;
    return rest;
}
bool equalOddEvenSums(Node* head) {
    auto sums = sumParity(head, true);
    return sums.first == sums.second;
}
int main() {
    struct Test { std::vector<int> arr; const char* desc; };
    std::vector<Test> tests = {
        { {}, "Lista vacía" },
        { {5}, "Un solo nodo" },
        { {1, 1}, "Par - suma impar == suma par (1,1)" },
        { {1, 2, 3, 4}, "Par - 1+3 != 2+4" },
        { {1, 2, 1}, "Impar - 1+1 == 2" },
        { {-3, 3, 0}, "Impar con negativos y cero: -3+0 == 3?" }
    };
    for (const auto& t : tests) {
        Node* head = createListFromArray(t.arr);
        bool eq = equalOddEvenSums(head);
        auto sums = sumParity(head, true);
        std::cout << t.desc << " -> ";
        std::cout << "suma_impares=" << sums.first << ", suma_pares=" << sums.second
                  << " => " << (eq ? "IGUALES" : "DIFERENTES") << '\n';
        freeList(head);
    }
    return 0;
}