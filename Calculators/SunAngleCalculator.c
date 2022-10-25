#include <stdio.h>

int main(void) {
float lat;
float sun;
float angle;
float diff;
  
printf("Enter Latitude: ");
scanf("%f",&lat);
//lat = 38.9072;

printf("\nEnter Sun angle according to analemma: ");
scanf("%f",&sun);

diff = lat - sun;
angle = 90-diff;
printf("angle is %.2f",angle);
}