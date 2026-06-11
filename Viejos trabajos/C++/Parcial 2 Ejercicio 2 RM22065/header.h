#ifndef HEADER_H
#define HEADER_H
#include <string>
#include <vector>
struct Node {
    std::string* data;
    Node* next;
    Node(std::string* d = nullptr, Node* n = nullptr) : data(d), next(n) {}
};
Node* createCircularListFromArray(const std::vector<const char*>& arr);
void freeCircularList(Node* head);
Node* filterPrimeLengthCircular(Node* head);
#endif