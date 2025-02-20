
#include <iostream>
using namespace std;
int main() {
  //Q1
   string name;
    string studentId;

    cout << "What is your name?" << endl;
    cin >> name;
    cout << "Hello " << name << "." << endl;

   
    cout << "What is your Student ID?" << endl;
    cin >> studentId;
    cout << "Your ID is " << studentId << "." << endl;



//Q2
 double var1, var2, sum, diff, prod;

    
    cout << "Enter the first number: ";
    cin >> var1;

    cout << "Enter the second number: ";
    cin >> var2;

   
    sum = var1 + var2;
    diff = var1 - var2;
    prod = var1 * var2;

    
    cout << "var1: " << var1 << endl;
    cout << "var2: " << var2 << endl;
    cout << "Sum: " << sum << endl;
    cout << "Difference: " << diff << endl;
    cout << "Product: " << prod << endl;
    
    
    //Q3
    string name;
    double lab, midterm, final, lastScore;

    
    cout << "Enter student's name: "<<endl;
    cin>> name;

    
    cout << "Enter Lab grade: ";
    cin >> lab;

    cout << "Enter Midterm grade: ";
    cin >> midterm;

    cout << "Enter Final grade: ";
    cin >> final;

    
    lastScore = (lab * 0.25) + (midterm * 0.35) + (final * 0.40);

   
    cout << "Name: " << name << endl;
    cout << "Lab: " << lab << endl;
    cout << "Midterm: " << midterm << endl;
    cout << "Final: " << final << endl;
    cout << "Last Score: " << lastScore << endl;

   
    
     
     //Q4
      std::cout << "*\n**\n***\n**\n*";

 return 0;
     
}
