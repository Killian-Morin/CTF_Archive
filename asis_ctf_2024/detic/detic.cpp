#include <iostream>
#include <cmath>

#define R 6371.0 // Radius of Earth in kilometers
#define PI 3.14159265358979323846

// Function to convert degrees to radians (encapsulated here)
double deg2rad(double degrees) {
    return degrees * (PI / 180.0);
}

// Function to convert radians to degrees (encapsulated here)
double rad2deg(double radians) {
    return radians * (180.0 / PI);
}

// Wrapper functions that use degrees directly but convert to radians internally
double sin_deg(double degrees) {
    return sin(deg2rad(degrees));
}

double cos_deg(double degrees) {
    return cos(deg2rad(degrees));
}

double atan2_deg(double y, double x) {
    return rad2deg(atan2(y, x));
}

// Function to find the geographic midpoint of three points on a spherical Earth
void find_geographic_midpoint(double lat1, double lon1, double lat2, double lon2, double lat3, double lon3, double &mid_lat, double &mid_lon) {
    // Convert the latitude/longitude coordinates into Cartesian coordinates (x, y, z)
    double x1 = cos_deg(lat1) * cos_deg(lon1);
    double y1 = cos_deg(lat1) * sin_deg(lon1);
    double z1 = sin_deg(lat1);

    double x2 = cos_deg(lat2) * cos_deg(lon2);
    double y2 = cos_deg(lat2) * sin_deg(lon2);
    double z2 = sin_deg(lat2);

    double x3 = cos_deg(lat3) * cos_deg(lon3);
    double y3 = cos_deg(lat3) * sin_deg(lon3);
    double z3 = sin_deg(lat3);

    // Compute the average of the Cartesian coordinates
    double x = (x1 + x2 + x3) / 3;
    double y = (y1 + y2 + y3) / 3;
    double z = (z1 + z2 + z3) / 3;

    // Convert the average Cartesian coordinates back to latitude and longitude
    double hyp = sqrt(x * x + y * y);
    mid_lat = atan2_deg(z, hyp); // latitude in degrees
    mid_lon = atan2_deg(y, x);   // longitude in degrees

    // Ensure longitude is between -180 and 180 degrees
    if (mid_lon > 180.0) {
        mid_lon -= 360.0;
    }
}

int main() {
    // Coordinates of the three passengers (in degrees)
    double lat1 = 29.62581320033086, lon1 = 52.55850268818534;
    double lat2 = 38.24829879437154, lon2 = 48.29124638967477;
    double lat3 = 36.15158614723986, lon3 = 60.54987387810325;

    // Variables to store the midpoint coordinates
    double mid_lat, mid_lon;

    // Calculate the geographic midpoint
    find_geographic_midpoint(lat1, lon1, lat2, lon2, lat3, lon3, mid_lat, mid_lon);

    // Output the result in the format: latitude, longitude
    std::cout << "Midpoint coordinates: " << mid_lat << ", " << mid_lon << std::endl;

    return 0;
}
