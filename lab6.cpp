#include <iostream>
using namespace std;
double H(int n) {
    double sum = 0;
    for (int i = 1; i <= n; i++) {
        sum+=1.0/i;
    }
    return sum;


}
double H() {
    int n;
    double sum = 0;
    cout<<"enter a num:"<<endl;
    cin>>n;
    for (int i = 1; i <= n; i++) {
        sum+=1.0/i;
    }
    return sum;

}
int main() {

   cout<< H(2);
    cout<<H();
    return 0;

}
