#include <iostream>
using namespace std;

class Node {
public:
    int data;
    Node *next;
    Node(int x, Node *n)
    {data=x; next=n;}
};


class Queue {
    Node* front;
    Node* rear;
    int count;

public:

    Queue()
        : front(nullptr)
        , rear(nullptr)
        ,count(0)
    {
    }


    void enqueue(int x)
    {
        Node* newNode = new Node{ x, nullptr };

        if (rear == nullptr) {
            front = rear = newNode;
        }
        else {

            rear->next = newNode;
            rear = newNode;
        }
        count++;
    };

    // çıkartıyo
    void dequeue() {
        if (front == nullptr)
            return;
        Node* temp = front;

        front = front->next;

        if (front == nullptr)

                rear = nullptr;

        delete temp;
        count--;
    }

    int top() {
            return front->data;
    }

    bool isEmpty()
    {
        return front == nullptr;
    }
    int size() {
    return count;
    }


};
int main() {
    Queue q;
    q.enqueue(10);
    q.enqueue(20);
    q.enqueue(30);
    cout << q.top() << endl;
     q.dequeue();
    cout<<q.size()<<endl;
    cout << q.top() << endl;
    cout << q.isEmpty() << endl;
    cout<<q.size()<<endl;
    return 0;
};
