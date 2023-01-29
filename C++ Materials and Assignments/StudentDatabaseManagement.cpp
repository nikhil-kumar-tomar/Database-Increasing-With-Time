// Student management system
// Libraries Used
#include<iostream>
#include<string>
#include<sstream>
#include<vector>
#include<fstream>
using namespace std;

void modify_backend(string delline){
    string line;
    fstream fin;
    fin.open("Data.csv",ios::in);
    fstream temp;
    temp.open("temp.csv",ios::out);
    while (getline(fin,line))
    {
        if (line != delline)
        {
        temp << line << endl;
        }
    }
    temp.close();
    fin.close();
}
void add_backend(string addline){
    int roll_no;
    string name,regis_no;
    fstream fout;
    fout.open("temp.csv", ios::app);
    fout<<addline<<"\n";
    fout.close();
}


void add_data(){
    int roll_no;
    string name,regis_no;
    fstream fout;
    fout.open("Data.csv", ios::app);
    cout<<"Enter roll No: ";
    cin>>roll_no;
    cout<<"Enter name: ";
    cin.ignore();
    getline(cin,name);
    cout<<"Enter Registration No: ";
    cin>>regis_no;
    fout<<roll_no<<','<<name<<','<<regis_no<<"\n";
    cout<<"Data added succesfully"<<endl<<endl;
    fout.close();
}
void read_selected_data(){
    int roll_no,roll2,count=0;
    string name,regis_no;
    fstream fin;
    fin.open("Data.csv", ios::in);
    cout<<"Enter roll No: ";
    cin>>roll_no;
    vector<string> row;
    string line, word, temp;
  
    while (!fin.eof()) {
        row.clear();
        getline(fin, line);
        stringstream new_str(line);
        while (getline(new_str, word, ',')) {
            row.push_back(word);
        }
        roll2=stoi(row[0]);
  
        if (roll2 == roll_no) {
            count = 1;
            cout << "Details Available Below: \n" ;
            cout << "Roll no: " << row[0] << "\n";
            cout << "Name: " << row[1] << "\n";
            cout << "Registration No: " << row[2] << "\n"<<endl;
            break;
        }
    }
    if (count == 0)
        cout << "Record not found\n"<<endl;
    fin.close();
}
void modify_selected_data(){
    int roll_no,roll2,count=0;
    string name,regis_no;
    fstream fin;
    fin.open("Data.csv", ios::in);
    cout<<"Enter roll No: ";
    cin>>roll_no;
    vector<string> row;
    string line, word, temp;
  
    while (!fin.eof()) {
  
        row.clear();
  
        getline(fin, line);
        stringstream new_str(line);
        while (getline(new_str, word, ',')) {
            row.push_back(word);
        }
        roll2=stoi(row[0]);
        if (roll2 == roll_no) {
            int choic;
            string to_del,to_add;
            count = 1;
            cout << "Details Available Below: \n" ;
            cout << "Roll no: " << row[0] << endl;
            cout << "Name: " << row[1] << endl;
            cout << "Registration No: " << row[2] <<endl<<endl;
            cout<<"1.Change Roll No"<<endl;
            cout<<"2.Change Name"<<endl;
            cout<<"3.Change Registration No"<<endl;
            cout<<"Enter Your choice: ";
            cin>>choic;
            if (choic==1){
                to_del=row[0]+','+row[1]+','+row[2];
                modify_backend(to_del);
                string roll_no_temp;
                cout<<"Enter the new roll_no: ";
                cin>>roll_no_temp;
                row[0]=roll_no_temp;
                to_add=row[0]+','+row[1]+','+row[2];
                add_backend(to_add);
                cout<<"Data Manipulated Succesfully"<<endl<<endl;
            }
            else if(choic==2){
                to_del=row[0]+','+row[1]+','+row[2];
                modify_backend(to_del);
                string name;
                cout<<"Enter the new name: ";
                cin>>name;
                row[1]=name;
                to_add=row[0]+','+row[1]+','+row[2];
                add_backend(to_add);
                cout<<"Data Manipulated Succesfully"<<endl<<endl;
            }
            else if(choic==3){
                to_del=row[0]+','+row[1]+','+row[2];
                modify_backend(to_del);
                string registration_no;
                cout<<"Enter the new Registration No: ";
                cin>>registration_no;
                row[2]=registration_no;
                to_add=row[0]+','+row[1]+','+row[2];
                add_backend(to_add);
                cout<<"Data Manipulated Succesfully"<<endl<<endl;
            }
            else{
                cout<<"Invalid Input Provided"<<endl<<endl;
            }
            fin.close();
            if (choic==1 || choic==2 || choic==3){
                remove("Data.csv");
                rename("temp.csv","Data.csv");
                }
            break;
        }
    }
    if (count == 0)
        cout << "Record not found\n"<<endl;
    fin.close();
}
void remove_selected_data(){
    int roll_no,roll2,count=0;
    string name,regis_no;
    fstream fin;
    fin.open("Data.csv", ios::in);
    cout<<"Enter roll No: ";
    cin>>roll_no;
    vector<string> row;
    string line, word, temp;
  
    while (!fin.eof()) {
  
        row.clear();
  
        getline(fin, line);
        stringstream new_str(line);
        while (getline(new_str, word, ',')) {
            row.push_back(word);
        }
  
        roll2=stoi(row[0]);
        if (roll2 == roll_no) {
            int choic;
            string to_del,to_add;
            count = 1;
            cout << "Details Available Below: \n" ;
            cout << "Roll no: " << row[0] << endl;
            cout << "Name: " << row[1] << endl;
            cout << "Registration No: " << row[2] <<endl<<endl;
            to_del=row[0]+','+row[1]+','+row[2];
            modify_backend(to_del);
            cout<<"Data Deleted Succesfully"<<endl<<endl;
            fin.close();
            remove("Data.csv");
            rename("temp.csv","Data.csv");

            break;
        }
    }
    if (count == 0)
        cout << "Record not found\n"<<endl;
    fin.close();
}
int main(){
    while (true){
    int choice;
    cout<<"**************************************************** Welcome to Student Management Portal *************************************************** "<<endl;
    cout<<"                                                          1. Add Student Record                                                     "<<endl;
    cout<<"                                                          2. Remove Student Record                                                     "<<endl;
    cout<<"                                                          3. Modify Student Record                                                     "<<endl;
    cout<<"                                                          4. Read Selected Student Record                                                     "<<endl;
    cout<<"                                                          5. Exit                                                     "<<endl;
    cout<<"Enter Your Choice: ";
    cin>>choice;
    if (choice==1){
        add_data();
    }
    else if (choice==2){
        remove_selected_data();
    }
    else if (choice==3){
        modify_selected_data();
    }
    else if (choice==4){
        read_selected_data();
    }
    else if (choice==5){
        cout<<"GoodBye"<<endl;
        break;
    }
    else{
        cout<<"Invalid input Provided, Please write the Index number of options available"<<endl<<endl;
    }
    }
    return 0;
}
