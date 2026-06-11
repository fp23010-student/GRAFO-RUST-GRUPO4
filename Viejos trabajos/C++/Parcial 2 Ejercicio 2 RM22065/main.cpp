#include "header.h"
#include <iostream>
#include <cstddef>
static bool isPrime(std::size_t n) {
    if (n < 2) return false;
    if (n % 2 == 0) return n == 2;
    for (std::size_t i = 3; i * i <= n; i += 2)
        if (n % i == 0) return false;
    return true;
}
Node* createCircularListFromArray(const std::vector<const char*>& arr) {
    if (arr.empty()) return nullptr;
    Node* head = nullptr;
    Node* tail = nullptr;
    for (const char* s : arr) {
        std::string* strptr = nullptr;
        if (s != nullptr) strptr = new std::string(s);
        Node* node = new Node(strptr, nullptr);
        if (!head) {
            head = tail = node;
            tail->next = head;
        } else {
            tail->next = node;
            tail = node;
            tail->next = head;
        }
    }
    return head;
}
void freeCircularList(Node* head) {
    if (!head) return;
    Node* cur = head->next;
    while (cur != head) {
        Node* nxt = cur->next;
        if (cur->data) delete cur->data;
        delete cur;
        cur = nxt;
    }
    if (head->data) delete head->data;
    delete head;
}
Node* filterPrimeLengthCircular(Node* head) {
    if (!head) return nullptr;
    Node* resHead = nullptr;
    Node* resTail = nullptr;
    Node* cur = head;
    bool firstIter = true;
    do {
        if (cur->data != nullptr && !cur->data->empty()) {
            std::size_t len = cur->data->size();
            if (isPrime(len)) {
                std::string* copy = new std::string(*cur->data);
                Node* newNode = new Node(copy, nullptr);
                if (!resHead) {
                    resHead = resTail = newNode;
                    resTail->next = resHead;
                } else {
                    resTail->next = newNode;
                    resTail = newNode;
                    resTail->next = resHead;
                }
            }
        }
        cur = cur->next;
        firstIter = false;
    } while (cur != head);
    return resHead;
}
void printCircularList(Node* head, const char* title) {
    std::cout << title << ": ";
    if (!head) {
        std::cout << "(vacía)\n";
        return;
    }
    Node* cur = head;
    bool first = true;
    do {
        if (!first) std::cout << " -> ";
        if (cur->data) std::cout << "\"" << *cur->data << "\"(" << cur->data->size() << ")";
        else std::cout << "NULL";
        first = false;
        cur = cur->next;
    } while (cur != head);
    std::cout << " [circular]\n";
}
int main() {
    {
        std::vector<const char*> arr = {};
        Node* head = createCircularListFromArray(arr);
        printCircularList(head, "Original (vacía)");
        Node* filtered = filterPrimeLengthCircular(head);
        printCircularList(filtered, "Filtrada");
        freeCircularList(head);
        freeCircularList(filtered);
    }
    {
        std::vector<const char*> arr = { nullptr };
        Node* head = createCircularListFromArray(arr);
        printCircularList(head, "Original (una nula)");
        Node* filtered = filterPrimeLengthCircular(head);
        printCircularList(filtered, "Filtrada");
        freeCircularList(head);
        freeCircularList(filtered);
    }
    {
        std::vector<const char*> arr = { "" };
        Node* head = createCircularListFromArray(arr);
        printCircularList(head, "Original (una vacía)");
        Node* filtered = filterPrimeLengthCircular(head);
        printCircularList(filtered, "Filtrada");
        freeCircularList(head);
        freeCircularList(filtered);
    }
    {
        std::vector<const char*> arr = { "hi" };
        Node* head = createCircularListFromArray(arr);
        printCircularList(head, "Original (una 'hi')");
        Node* filtered = filterPrimeLengthCircular(head);
        printCircularList(filtered, "Filtrada");
        freeCircularList(head);
        freeCircularList(filtered);
    }
    {
        std::vector<const char*> arr = {
            nullptr,
            "a",
            "",
            "ab",
            "abc",
            "abcd",
            "abcde",
            "abcdef",
        };
        Node* head = createCircularListFromArray(arr);
        printCircularList(head, "Original (mezcla)");
        Node* filtered = filterPrimeLengthCircular(head);
        printCircularList(filtered, "Filtrada (solo primas)");
        freeCircularList(head);
        freeCircularList(filtered);
    }
    return 0;
}