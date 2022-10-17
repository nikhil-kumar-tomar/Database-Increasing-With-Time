int main(){
    int rows;
    cout<<"Enter number of rows: ";
    cin>>rows;
    for (int x=0;x<=rows;x++){
            cout<<"*";
    }
    cout<<endl;
    for (int x=rows;x>0;x--){
        cout<<"*"<<string(x,' ')<<"*"<<endl;
    }
    cout<<"*";
    return 0;
}
