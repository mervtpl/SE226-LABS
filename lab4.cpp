#include <iostream>
using namespace std;
class Node {
public:
    int data;
    Node *next;
    Node(int x, Node *n)
    {data=x; next=n;}
};
class Stack {
    Node* top;
    int capacity;
    int size;

public:

    Stack(int initialCapacity) {
        top = nullptr;
        size = initialCapacity;
        capacity = 0;


    }

    int setSize(int s)
    {
        size = s;
    }
    int getSize() {
        return size;
    }
    int increaseCapacity( ) {
        if (size == capacity) {
            cout<<"Stack is full size increasing "<<endl;
            setSize(getSize()*2);
            cout<<"new size: "<<endl;
            return getSize();
        }
    }
    int push(int x) {

        Node* temp = new Node(x, top);
        top = temp;
        capacity++;
        cout<<"node added : "<<endl;
        cout<<top->data<<endl;
        return 0;
    }
    void pop() {
        if (isEmpty()) {
            return;
        }
        Node* temp = top;
        top = top->next;
        cout<<"top deleted: "<<endl;
        delete temp;
        capacity--;
    }
    int peek() {
        if (isEmpty()) {
            cout<<"Stack is empty"<<endl;
            return -1;
        }
        cout<<"top:" <<endl;
        cout << top->data << endl;

        return top->data;
    }
    bool isEmpty() {
        if (top == nullptr) {
            cout<<"Stack is empty"<<endl;
            return true;
        }
        return false;
    }
    bool deleteElement(int val) {
        if (isEmpty()) return false;
        Node* temp = top;
        Node* prev = nullptr;

        while (temp != nullptr) {
            if (temp->data == val) {
                if (prev == nullptr) {
                    top = temp->next;
                } else {
                    prev->next = temp->next;
                }
                delete temp;
                size--;
                return true;
            }
            prev = temp;
            temp = temp->next;
        }
        return false;
    }





};

    int main() {
        Stack s(5);
        s.push(3);
        s.peek();
        s.push(4);
        s.peek();
      //  s.pop();
       // s.peek();
        s.deleteElement(3);
       


        return 0;
    };
