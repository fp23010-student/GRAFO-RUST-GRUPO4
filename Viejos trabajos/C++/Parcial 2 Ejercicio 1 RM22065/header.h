#ifndef HEADER_H
#define HEADER_H
#include <utility>
#include <vector>
struct Node {
    int value;
    Node* next;
    Node(int v, Node* n = nullptr) : value(v), next(n) {}
};
Node* createListFromArray(const std::vector<int>& arr);
void freeList(Node* head);
std::pair<long long, long long> sumParity(Node* head, bool isOdd);
bool equalOddEvenSums(Node* head);
#endif 