#include <stdio.h>
#include <math.h>

#define R 6371.0 // Radius of the Earth in kilometers
#define PI 3.14159265358979323846

// Function to convert degrees to radians
double deg2rad(double degrees) {
    return degrees * (PI / 180.0);
}

// Function to convert radians to degrees
double rad2deg(double radians) {
    return radians * (180.0 / PI);
}

// Function to find the geographic midpoint of three points on a spherical Earth
void find_geographic_midpoint(double lat1, double lon1, double lat2, double lon2, double lat3, double lon3, double *mid_lat, double *mid_lon) {
    // Convert latitude and longitude from degrees to radians
    lat1 = deg2rad(lat1);
    lon1 = deg2rad(lon1);
    lat2 = deg2rad(lat2);
    lon2 = deg2rad(lon2);
    lat3 = deg2rad(lat3);
    lon3 = deg2rad(lon3);

    // Convert the latitude/longitude coordinates into Cartesian coordinates (x, y, z)
    double x1 = cos(lat1) * cos(lon1);
    double y1 = cos(lat1) * sin(lon1);
    double z1 = sin(lat1);

    double x2 = cos(lat2) * cos(lon2);
    double y2 = cos(lat2) * sin(lon2);
    double z2 = sin(lat2);

    double x3 = cos(lat3) * cos(lon3);
    double y3 = cos(lat3) * sin(lon3);
    double z3 = sin(lat3);

    // Compute the average of the Cartesian coordinates
    double x = (x1 + x2 + x3) / 3;
    double y = (y1 + y2 + y3) / 3;
    double z = (z1 + z2 + z3) / 3;

    // Convert the average Cartesian coordinates back to latitude and longitude
    double hyp = sqrt(x * x + y * y);
    *mid_lat = atan2(z, hyp); // latitude in radians
    *mid_lon = atan2(y, x);   // longitude in radians

    // Convert latitude and longitude from radians to degrees
    *mid_lat = rad2deg(*mid_lat);
    *mid_lon = rad2deg(*mid_lon);

    // Ensure longitude is between -180 and 180 degrees
    if (*mid_lon > 180.0) {
        *mid_lon -= 360.0;
    }
}

int main() {
    // Coordinates of the three points (in degrees)
    double lat1 = 38.02362567465393, lon1 = 46.36740105104086;
    double lat2 = 38.24829879437154, lon2 = 48.29124638967477;
    double lat3 = 29.62581320033086, lon3 = 52.55850268818534;

    // Variables to store the midpoint coordinates
    double mid_lat, mid_lon;

    // Calculate the geographic midpoint
    find_geographic_midpoint(lat1, lon1, lat2, lon2, lat3, lon3, &mid_lat, &mid_lon);

    // Output the result in the format: latitude, longitude
    printf("Midpoint coordinates: %.5lf, %.5lf\n", mid_lat, mid_lon);

    return 0;
}
