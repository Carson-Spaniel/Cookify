#include <stdio.h>

int main() {
  float rent;
  float weeks;
  float hours;
  float totalneeded;
  float month;
  float pay;
  float totalhours;
  float elec;
  float water;
  float food;
  float gas;
  float desired;
  float excess;
  float totalexcess;
  float total;
  
  //printf("Enter rent per month: $");
  //scanf("%f",&rent);
  
  //printf("Enter weeks working: ");
  //scanf("%f",&weeks);
  
  //printf("Enter hours per week: ");
  //scanf("%f",&hours);

  //printf("Enter desired pay: $");
  //scanf("%f",&desired);
  //printf("\n");


  rent = 2000;
  weeks = 12;
  hours = 40;
  desired = 20;
  
  elec = 150;
  water = 75;
  food = 400;
  gas = 100;

  month = weeks / 4.34524;
  rent = rent + elec + water + food + gas;
  totalneeded = (rent * month);
  totalhours = hours * weeks;
  pay = totalneeded / totalhours;

  excess = (((desired - pay) * hours) * 4.34524);
  totalexcess = excess * month;

  total = totalexcess + totalneeded;
  
  printf("\nWith rent and expenses being $%.2f per month your pay must be at the very least $%.2f per hour\n", rent, pay);
  printf("Total needed in the summer is $%.2f\n",totalneeded);
  printf("\nIf you get paid $%.2f per hour, then...\n", desired);
  printf("Amount of spending money per month is $%.2f\n", excess);
  printf("Amount of spending money in total is $%.2f\n", totalexcess);
  printf("\nAmount of money in total is $%.2f\n", total);
}