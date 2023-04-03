#include <iostream>
#include <string>

using namespace std;

int main(){
    int hour, minute, time;
    string amOrPm;
    string input;
    getline(cin, input);
    cin >> time;

    int colon = input.find(':');
    int space = input.find(' ');


    hour = stoi(input.substr(0, colon));
    minute = stoi(input.substr(colon + 1, space));
    amOrPm = input.substr(space + 1);

    if(amOrPm == "PM"){
        hour += 12;
    }

    int hoursNeeded = time / 60;
    int minsNeeded = time % 60;

    hour -= hoursNeeded;
    minute -= minsNeeded;

    if(minute < 0){
        hour -= 1 - (minute / 60);
        minute += 60;
    }

    if(hour - 12 >= 12){
        cout << "balls" << endl;
        if(hour > 13){
            hour -= 12;
        }
        amOrPm = "PM";
    }
    else{
        cout << "teehee" << endl;
        amOrPm = "AM";
    }

    cout << hour << ":" << minute << " " << amOrPm << endl;

    return 0;
}