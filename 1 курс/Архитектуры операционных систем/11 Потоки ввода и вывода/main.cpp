#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <sstream>

using namespace std;

class Location {
    double lat;
    double lon;
public:
    Location(double lat, double lon){
        setLat(lat);
        setLon(lon);
    }

    double getLon() const {
        return lon;
    }

    double getLat() const {
        return lat;
    }

private:
    void setLat(double l){
        lat = l;
    }
    void setLon(double l){
        lon = l;
    }
};

std::vector<std::string> readArray() {
    ifstream ifs("coordinates.txt" , ios::in);
    std::vector<std::string> result (100);
    if(ifs.is_open()){
        string line;
        int count = 0;
        int countLine = 0;
        while (ifs >> line) {
            result[countLine] += line;
            if (count % 2 == 0){
                result[countLine] += " ";
            }
            if (count % 2 != 0){
                countLine++;
            }
            count++;
        }
    }
    return result;
}

std::vector<Location> filterArray(std::vector<std::string> arr) {
    std::vector<Location> result(arr.size(), Location(0, 0));
    int addCounter = 0;
    for (int i = 0; i < arr.size(); ++i) {
        string coordinates = arr[i];
        if (coordinates.length() == 0) break;
        stringstream ss(coordinates);
        double lat, lon;
        ss.ignore(1);  // skip '('
        ss >> lat;
        ss.ignore(2);  // skip ", "
        ss >> lon;
        bool conditionLat = lat > 50 && lat < 80;
        bool conditionLon = lon > 20 && lon < 45;
        if (conditionLat && conditionLon) {
            Location l = Location(lat, lon);
            result[addCounter] = l;
            addCounter++;
        }
    }
    return result;
}

void printLocationArray(std::vector<Location> arr) {
    for (int i = 0; i < arr.size(); ++i) {
        Location location = arr[i];
        if (location.getLat() == 0 && location.getLon() == 0) break;
        cout << "Location which in condition of task lat - "<< location.getLat() << ", lon - " << location.getLon() << endl;
    }
}

int main() {
    std::vector arr = readArray();
    std::vector<Location> filteredArray = filterArray(arr);
    printLocationArray(filteredArray);
    return 0;
}