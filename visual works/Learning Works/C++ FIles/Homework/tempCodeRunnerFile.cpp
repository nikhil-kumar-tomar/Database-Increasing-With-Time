void odd_even(int x)
{
    if (x % 2 == 0)
    {
        cout << x << " is an even number"<<endl<<endl;
    }
    else
    {
        cout << x << " is an odd number"<<endl<<endl;
    }
}

int main(){
    while (true){
        char choic;
        int num;
        cout <<"Please Enter your number: ";
        cin>>num;
        odd_even(num);
        cout << "Do you want to do more operations (Y/N): ";
        cin >> choic;
        choic = toupper(choic);
        if (choic == 'N')
        {
            cout<<"\nOkay have a nice day :)";
            break;
        }
        else {
            continue;
        }
    }
    return 0;

}
