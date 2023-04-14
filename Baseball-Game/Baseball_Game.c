/** 
 * This is my Baseball game.
 * I created it for fun while I was traveling to Kansas on the plane.
 * Date: 4/10/23
 * Author: Carson Spaniel
 * 
*/
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>
#include <math.h> // needed for ceil()
#include <Windows.h> // needed for Sleep()

#include <sys/timeb.h>// needed for timing stuff

#include <conio.h> // needed for getch()

/* Global Variables */
int sound = 1;
int pause = 0;

int bot = 0;
int inningNum = 0;
int inning = 0;
int newInning = 0;
int ballCount = 0;
int strikeCount = 0;
int outCount = 0;
int hitZone = 0;
int team1Score = 0;
int team2Score = 0;
int startGame = 0;
int endGame = 0;
int onBase = 0;
int swing = 0;

/* User Difficulty */
int user1 = 150;
int user2 = 250;
int user3 = 300;
int user4 = 500;
int user5 = 700;
int user6 = 1000;

/* Bot Difficulty */
int bot1 = 250;
int bot2 = 500;

/* Defines functions */
void menu();
void settings();
void userDif();
void botDif();
void soundSet();
void playBall();
void tutorial();
void strike();
void ball();
void outCheck();
void baseCheck();
void inningCheck();
void gameEndCheck();
void hit();
void foul();
void noSwing();
void count();
void reset();

/* Songs */
void charge();
void rally();
void inningChange();
void BallGame();
void HomeRun();
void onBaseSound();
void strikeSound();
void ballSound();
void foulSound();


int main(){
    srand((unsigned int)time(NULL));

    //printf("\033[1;31m");
    printf("\nWelcome to Big League Slugger!\n\n");
    //printf("\033[0m");

    menu();
}

void menu(){
    int settings1 = 1;
    while (settings1){
        if(pause == 1){
            printf("\n------- Pause ------- \n\n");
        }
        else{
            printf("------- Menu ------- \n\n");
        }
        printf("1.\t");
        if(pause == 1){
            printf("Resume\n");
        }
        else{
            //printf("\033[1;31m");
            printf("Play ball!\n");
            //printf("\033[0m");
        }
        printf("2.\tSettings\n");
        printf("3.\tQuit game\n\n");
        char choice = getch();
        switch(choice){
            case '1':
                if (pause == 1){
                    settings1 = 0;
                }
                else{
                    playBall();
                }
                break;
            case '2':
                settings();
                break;
            case '3':
                printf("Until next time Slugger!\n");
                Sleep(500);
                printf("Wait! ");
                Sleep(1000);
                printf("One last thing before you go. ");
                Sleep(2000);
                printf("Don't forget your glove!\n");
                Sleep(1000);
                printf("\nSee you later!");
                Sleep(1000);
                exit(0);
            default:
                printf("Invalid option\n");
                break;
        }
    }
}

void botDif(){
    int settings = 1;
    while(settings){
        printf("------- Bot Difficulty ------- \n\n");
        printf("1.\tEasy\n");
        printf("2.\tNormal\n");
        printf("3.\tHard\n");
        printf("4.\tBack\n\n");
        char choice = getch();
        switch(choice){
            case '1':
                bot1 = 0;
                bot2 = 1100;
                printf("Bot Difficulty: ");
                printf("Easy\n\n");
                Sleep(1000);
                break;
            case '2':
                bot1 = 250;
                bot2 = 500;
                printf("Bot Difficulty: ");
                printf("Normal\n\n");
                Sleep(1000);
                break;
            case '3':
                bot1 = 300;
                bot2 = 500;
                printf("Bot Difficulty: ");
                printf("Hard\n\n");
                Sleep(1000);
                break;
            case '4':
                settings = 0;
                break;
            default:
                printf("Invalid option\n");
                break;
        }
    }
}

void userDif(){
    int settings = 1;
    while(settings){
        printf("------- User Difficulty ------- \n\n");
        printf("1.\tEasy\n");
        printf("2.\tNormal\n");
        printf("3.\tHard\n");
        printf("4.\tBack\n\n");
        char choice = getch();
        switch(choice){
            case '1':
                user1 = 100;
                user2 = 150;
                user3 = 200;
                user4 = 550;
                user5 = 800;
                user6 = 1100;
                printf("User Difficulty: ");
                printf("Easy\n\n");
                Sleep(1000);
                break;
            case '2':
                user1 = 150;
                user2 = 250;
                user3 = 300;
                user4 = 500;
                user5 = 700;
                user6 = 1000;
                printf("User Difficulty: ");
                printf("Normal\n\n");
                Sleep(1000);
                break;
            case '3':
                user1 = 325;
                user2 = 350;
                user3 = 400;
                user4 = 500;
                user5 = 650;
                user6 = 675;
                printf("User Difficulty: ");
                printf("Hard\n\n");
                Sleep(1000);
                break;
            case '4':
                settings = 0;
                break;
            default:
                printf("Invalid option\n");
                break;
        }
    }
}

void soundSet(){
    int settings = 1;
    while(settings){
        printf("------- Sound Settings ------- \n\n");
        printf("1.\tOn\n");
        printf("2.\tOff\n");
        printf("3.\tBack\n\n");
        char choice = getch();
        switch(choice){
            case '1':
                sound = 1;
                printf("Sound On\n\n");
                Sleep(1000);
                break;
            case '2':
                sound = 0;
                printf("Sound Off\n\n");
                Sleep(1000);
                break;
            case '3':
                settings = 0;
                break;
            default:
                printf("Invalid option\n");
                break;
        }
    }
}

void settings(){
    int settings = 1;
    while(settings){
        printf("------- Settings ------- \n\n");
        printf("1.\tUser Difficulty\n");
        printf("2.\tBot Difficulty\n");
        printf("3.\tSounds\n");
        printf("4.\tBack\n\n");
        char choice = getch();
        switch(choice){
            case '1':
                userDif();
                break;
            case '2':
                botDif();
                break;
            case '3':
                soundSet();
                break;
            case '4':
                settings = 0;
                break;
            default:
                printf("Invalid option\n");
                break;
        }
    }
}

void playBall(){
    reset();
    char player;
    while(player != '1' && player != '2' && player != '3' && player != '4'){
        printf("1. Single Player\n");
        printf("2. Two Player\n");
        printf("3. Simulation\n");
        printf("4. Back\n\n");
        player = getch();
        if (player == '1'){
            bot = 1;
        }
        else if(player == '2'){
            bot = 0;
        }
        else if(player == '3'){
            bot = 2;
        }
        else if(player == '4'){
            endGame = 1;
        }
        else{
            printf("Invalid Input.\n\n");
            Sleep(1000);
        }
    }
    //inningNum = 17; //16 sets the inning to top of the 9th
    while(endGame != 1){
        if(startGame == 0){
            tutorial();
            charge();
            printf("Play ball!\n\n");
            Sleep(2000);
        }
        startGame = 1;
        if (newInning != 1){
            inningChange();
            newInning = 1;
            onBase = 0;

            if(inningNum == 13){
                printf("Its now time for the 7th inning stretch!\n");
                Sleep(500);
                printf(".");
                Sleep(500);
                printf(".");
                Sleep(500);
                printf(".\n");
                BallGame();
            }

            if (inningNum >= 18){
                onBase = 1;
                printf("In extra innings the game lives on!\n");
            }
            outCount = 0;
            strikeCount = 0;
            ballCount = 0;
            //printf("Inning number is: %d\n",inningNum);
            printf("The score is ");
            if(bot == 2){
                printf("Bot 1: %d to ",team2Score);
            }
            else{
                printf("Player 1: %d to ",team2Score);
            }
            if(bot != 0){
                printf("Bot 2: %d at the ",team1Score);
            }
            else{
                printf("Player 2: %d at the ",team1Score);
            }

            
            inningCheck();
            Sleep(750);
            
        }
        newInning = 1;

        printf("Here comes the pitch");
        Sleep(250);
        printf(".");
        Sleep(250);
        printf(".");
        Sleep(250);
        printf(".\n");
        Sleep(500);
        int ToB = inningNum % 2;
        if(ToB == 0){
            //printf("\033[1;31m");
        }
        else{
            //printf("\033[1;34m");
        }
        if (bot == 1 && ToB == 1){
            Sleep(25);
        }
        else if (bot == 2){
            Sleep(25);
        }
        else{
            int wait = (((int)rand()));
            wait = wait % 1500;
            Sleep(wait);
        }
        
        printf("Hit it!\n");
        //printf("\033[0m");
        
        
        int c = 0;
        int cbot = 0;

        struct _timeb start, end;
        _ftime(&start);

        int inningHalf = inningNum % 2;
        if(bot == 1 && inningHalf == 1){
            cbot = (((int)rand()));
            cbot = cbot % 4;
        }
        else if(bot == 2){
            cbot = (((int)rand()));
            cbot = cbot % 4;
        }
        else{
            c = getch();
            _ftime(&end);
        }
        if(c == 'p' || c == 'P'){
            pause = 1;
            menu();
            printf("Here comes the pitch");
            Sleep(250);
            printf(".");
            Sleep(250);
            printf(".");
            Sleep(250);
            printf(".\n");
            Sleep(500);
            if (bot == 1 && ToB == 1){
                Sleep(25);
            }
            else if (bot == 2){
                Sleep(25);
            }
            else{
                int wait = (((int)rand()));
                wait = wait % 1500;
                Sleep(wait);
            }
        
            printf("Hit it!\n");
            _ftime(&start);

            if(bot == 1 && inningHalf == 1){
                cbot = (((int)rand()));
                cbot = cbot % 4;
            }
            else if(bot == 2){
                cbot = (((int)rand()));
                cbot = cbot % 4;
            }
            else{
                c = getch();
                _ftime(&end);
            }
        }
        int diff;
        if(bot == 1 && inningHalf == 1){
            diff = rand() % (bot2 - bot1 + 1) + bot1;
        }
        else if (bot == 2){
            diff = rand() % (bot2 - bot1 + 1) + bot1;
        }
        else{
            diff = (int) (1000.0 * (end.time - start.time) + (end.millitm - start.millitm));
            //printf("\nThis is the time it took to swing: %d\n",diff);
        }
        
        if(diff < user1){
            printf("He was way out in front of that one.\n");
            Sleep(500);
            strike();
        }
        else if(diff >= user1 && diff < user2){
            printf("A little early on that one.\n");
            Sleep(500);
            foul();
        }
        else if(diff >= user2 && diff < user3){
            strike();
        }
        else if (diff >= user3 && diff < user4){
            hit();
        }
        else if(diff >= user4 && diff < user5){
            printf("A little late on that one.\n");
            Sleep(500);
            foul();
        }
        else if (diff >= user5 && diff < user6){
            noSwing();
        }
        else{
            strike();
        }

    }
    menu();
}

void hit(){
    int b = 20;
    if (inningNum > 18){
        b = 15;
    }
    else if(inningNum == 17 && ballCount == 3 && strikeCount == 2 && outCount == 2 && onBase == 3 && team1Score <= team2Score){
        b = 5;
    }
    int hrChance = (((int)rand()));
    hrChance = hrChance % b;
    if (hrChance == 0){
        strikeCount = 0;
        ballCount = 0;
        printf("Thats a good hit!\n");
        Sleep(1000);
        printf("Its going! ");
        Sleep(1000);
        printf("Going! ");
        Sleep(1000);
        printf("Gone!\n");
        Sleep(1000);
        if (onBase == 3){
            int ToB = inningNum % 2;
            if(ToB == 0){
                //printf("\033[1;31m");
            }
            else{
                //printf("\033[1;34m");
            }
            printf("Its a Grand Slam!\n\n");
            //printf("\033[0m");
        }
        else if(onBase > 0){
            int ToB = inningNum % 2;
            if(ToB == 0){
                //printf("\033[1;31m");
            }
            else{
                //printf("\033[1;34m");
            }
            printf("Its a %d run homerun!\n\n",onBase+1);
            //printf("\033[0m");
        }
        else{
            int ToB = inningNum % 2;
            if(ToB == 0){
                //printf("\033[1;31m");
            }
            else{
                //printf("\033[1;34m");
            }
            printf("Homerun!\n\n");
            //printf("\033[0m");
        }
        if(inningNum % 2 == 0){
            team2Score += 1 + onBase;
        }
        else{
            team1Score += 1 + onBase;
        }
        onBase = 0;
        HomeRun();
        if(team1Score == team2Score){
            printf("Its now a tie game!\n");
        }
        Sleep(1000);
        printf("The score is ");
        if(bot == 2){
            printf("Bot 1: %d to ",team2Score);
        }
        else{
            printf("Player 1: %d to ",team2Score);
        }
        if(bot != 0){
            printf("Bot 2: %d at the ",team1Score);
        }
        else{
            printf("Player 2: %d at the ",team1Score);
        }
        inningCheck();
        Sleep(1000);
    }
    else{
        int dropC = 8;
        if (inningNum > 18){
            dropC = 5;
        }
        int hitR = ((int)rand());
        hitR = hitR % 5;
        if (hitR == 0){
            int catchC = ((int)rand());
            catchC = catchC % dropC;
            ballCount = 0;
            strikeCount = 0;
            printf("Thats a pop fly.\n");
            Sleep(1000);
            printf("And he");
            Sleep(500);
            printf(".");
            Sleep(250);
            printf(".");
            Sleep(250);
            printf(".");
            Sleep(500);
            if (catchC == 0){
                printf(" drops it!\n");
                Sleep(1000);
                printf("And the runner is safe.\n\n");
                baseCheck();
            }
            else{
                printf(" makes the catch!\n");
                Sleep(1000);
                printf("And the runner is out.\n");

                outCount += 1;
                rally();
                outCheck();
            }                
            Sleep(1000);
        }
        else if(hitR == 1){
            int catchC = ((int)rand());
            catchC = catchC % dropC;
            ballCount = 0;
            strikeCount = 0;
            printf("Thats a hit!\n");
            Sleep(500);
            printf("The outfielder is under it.\n");
            Sleep(1000);
            printf("And he");
            Sleep(250);
            printf(".");
            Sleep(250);
            printf(".");
            Sleep(250);
            printf(".");
            Sleep(1000);
            if (catchC == 0){
                printf(" drops it!\n");
                Sleep(1000);
                printf("And the runner is safe.\n\n");
                baseCheck();
            }
            else{
                printf(" makes the catch!\n");
                Sleep(1000);
                printf("And the runner is out.\n");

                outCount += 1;
                rally();
                outCheck();
            }          
        }
        else if(hitR == 2){
            int baseman = (((int)rand()));
            baseman = baseman % 3;
            ballCount = 0;
            strikeCount = 0;
            printf("Ground ball to the");
            if(baseman == 0){
                printf(" 1st baseman.\n");
                Sleep(500);
                printf("And he makes the tag.\n");
                printf("The runner is out.\n");
                outCount += 1;
                rally();
                outCheck();
                if (outCount >= 3){
                    goto end;
                }
            }
            else{
                int doubleP = 0;
                int tripleP = 0;
                int a = 2;
                if(baseman == 1){
                    printf(" 3rd baseman.\n");
                    if(onBase == 1){
                        Sleep(1000);
                        printf("And he throws to second.\n");
                        Sleep(250);
                        printf("He gets that out.\n");
                        outCount +=1;
                        onBase -= 1;
                        doubleP = 1;
                        a = 3;
                        rally();
                        outCheck();
                        if (outCount >= 3){
                            goto end;
                        }
                        Sleep(500);
                        printf("2nd baseman throws to first and its");
                        Sleep(250);
                        printf(".");
                        Sleep(250);
                        printf(".");
                        Sleep(250);
                        printf(".");
                        Sleep(1000);
                        int safe = (((int)rand()));
                        safe = safe % a;
                        if(safe == 0){
                            printf(" in time!\n");
                            printf("The runner is out.\n");
                            outCount += 1;
                            if(doubleP == 1){
                                printf("Its a Double play!\n");
                            }
                            rally();
                            outCheck();
                            if (outCount >= 3){
                                goto end;
                            }
                        }
                        else{
                            printf(" not in time!\n");
                            printf("The runner is safe at first!\n\n");
                            baseCheck();
                        }   
                    }
                    else if(onBase >= 2){
                        Sleep(1000);
                        printf("And he makes the tag.\n");
                        Sleep(250);
                        printf("He gets that out.\n");
                        outCount +=1;
                        onBase -= 1;
                        doubleP = 1;
                        a = 3;
                        rally();
                        outCheck();
                        if (outCount >= 3){
                            goto end;
                        }
                        Sleep(500);
                        printf("3rd baseman throws to second and its");
                        Sleep(250);
                        printf(".");
                        Sleep(250);
                        printf(".");
                        Sleep(250);
                        printf(".");
                        Sleep(1000);
                        int safe = (((int)rand()));
                        safe = safe % a;
                        if(safe == 0){
                            printf(" in time!\n");
                            Sleep(250);
                            printf("The runner is out.\n");
                            Sleep(250);
                            outCount += 1;
                            onBase -= 1;
                            tripleP = 1;
                            doubleP = 0;
                            printf("Its a Double play!\n");
                            rally();
                            outCheck();
                            if (outCount >= 3){
                                goto end;
                            }
                        }
                        else{
                            printf(" not in time!\n");
                            Sleep(250);
                            printf("The runner is safe!\n\n");
                            baseCheck();
                        }
                        Sleep(500);
                        a = 4;
                        printf("2nd baseman throws to first and its");
                        printf(".");
                        Sleep(250);
                        printf(".");
                        Sleep(250);
                        printf(".");
                        Sleep(1000);
                        int tripleC = (((int)rand()));
                        tripleC = tripleC % a;
                        if(tripleC == 0){
                            printf(" in time!\n");
                            printf("The runner is out.\n");
                            outCount += 1;
                            onBase -= 1;
                            if(tripleP == 1){
                                printf("Its a Triple play!\n");
                            }
                            else if(doubleP == 1){
                                printf("Its a Double play!\n");
                            }
                            rally();
                            outCheck();
                            if (outCount >= 3){
                                goto end;
                            }
                        }
                        else{
                            printf(" not in time!\n");
                            printf("The runner is safe!\n\n");
                            baseCheck();
                        }
                    }
                    else{
                        Sleep(1000);
                        printf("And the throw to first is");
                        Sleep(250);
                        printf(".");
                        Sleep(250);
                        printf(".");
                        Sleep(250);
                        printf(".");
                        Sleep(1000);
                        int safe = (((int)rand()));
                        safe = safe % a;
                        if(safe == 0){
                            printf(" in time!\n");
                            printf("The runner is out.\n");
                            outCount += 1;
                            rally();
                            outCheck();
                        }
                        else{
                            printf(" not in time!\n");
                            printf("The runner is safe!\n\n");
                            baseCheck();
                        }   
                    }
                }
                else if (baseman == 2){
                    printf(" shortstop.\n");
                    if (onBase >= 1){
                        Sleep(1000);
                        printf("And he tosses the ball to second.\n");
                        Sleep(250);
                        printf("He gets that out.\n");
                        outCount +=1;
                        doubleP = 1;
                        a = 3;
                        rally();
                        outCheck();
                        if (outCount >= 3){
                            goto end;
                        }
                        Sleep(500);
                        printf("2nd baseman throws to first and its");
                        Sleep(250);
                        printf(".");
                        Sleep(250);
                        printf(".");
                        Sleep(250);
                        printf(".");
                        Sleep(1000);
                        int doubleC = (((int)rand()));
                        doubleC = doubleC % a;
                        if(doubleC == 0){
                            printf(" in time!\n");
                            printf("The runner is out.\n");
                            outCount += 1;
                            if(doubleP == 1){
                                printf("Its a Double play!\n");
                            }
                            rally();
                            outCheck();
                            if (outCount >= 3){
                                goto end;
                            }
                        }
                        else{
                            printf(" not in time!\n");
                            printf("The runner is safe!\n\n");
                            baseCheck();
                        }
                    }
                    else{
                        Sleep(1000);
                        printf("And the throw to first is");
                        Sleep(250);
                        printf(".");
                        Sleep(250);
                        printf(".");
                        Sleep(250);
                        printf(".");
                        Sleep(1000);
                        int safe = (((int)rand()));
                        safe = safe % a;
                        if(safe == 0){
                            printf(" in time!\n");
                            printf("The runner is out.\n");
                            outCount += 1;
                            rally();
                            outCheck();
                        }
                        else{
                            printf(" not in time!\n");
                            printf("The runner is safe!\n\n");
                            baseCheck();
                        }   
                    }
                    
                }
                else{
                    Sleep(1000);
                    printf("And the throw to first is");
                    Sleep(250);
                    printf(".");
                    Sleep(250);
                    printf(".");
                    Sleep(250);
                    printf(".");
                    Sleep(1000);
                    int safe = (((int)rand()));
                    safe = safe % a;
                    if(safe == 0){
                        printf(" in time!\n");
                        printf("The runner is out.\n");
                        outCount += 1;
                        rally();
                        outCheck();
                    }
                    else{
                        printf(" not in time!\n");
                        printf("The runner is safe!\n\n");
                        baseCheck();
                    }   
                }
                end: 
                    printf("");
            }  
        }
        else if(hitR == 3){
            printf("Thats a hit!\n");
            Sleep(1000);
            foul();
        }
        else {
            ballCount = 0;
            strikeCount = 0;
            printf("Thats a hit!\n");
            Sleep(1000);
            printf("Looks like its going to be");
            Sleep(250);
            printf(".");
            Sleep(250);
            printf(".");
            Sleep(250);
            printf(".");
            Sleep(1000);
            printf(" fair!\n");
            Sleep(500);
            printf("Its going to be close!\n");
            Sleep(1000);
            printf("And the runner is");
            Sleep(250);
            printf(".");
            Sleep(250);
            printf(".");
            Sleep(250);
            printf(".");
            Sleep(1000);
            int safe = (((int)rand()));
            safe = safe % 4;
            if(safe == 0){
                printf(" out!\n");
                outCount += 1;
                rally();
                outCheck();
            }
            else{
                printf(" safe!\n\n");
                baseCheck();
            }            
        }
    }
}

void foul(){
    printf("Looks like its going to be");
    Sleep(250);
    printf(".");
    Sleep(250);
    printf(".");
    Sleep(250);
    printf(".");
    Sleep(1000);
    printf(" foul.\n");
    foulSound();
    if (strikeCount+1 != 3){
        strikeCount += 1;
        count();
    }
    else{
        printf("\n");
    }
}

void noSwing(){
    int hitR = ((int)rand());
    hitR = hitR % 20;
    if (hitR == 0){
        printf("And the batter");
        Sleep(250);
        printf(".");
        Sleep(250);
        printf(".");
        Sleep(250);
        printf(".");
        Sleep(250);
        printf(" is hit with the pitch!\n");
        Sleep(1000);
        printf("The batter takes his base.\n\n");
        Sleep(1000);
        baseCheck();
    }
    else{
        printf("And the batter chose not to swing and its a");
        Sleep(500);
        printf(".");
        Sleep(250);
        printf(".");
        Sleep(250);
        printf(".");
        Sleep(250);
        int strikeZone = (((int)rand()));
        strikeZone = strikeZone % 3;
        if (strikeZone == 0){
            printf(" strike!\n");
            swing = 1;
            strike();
        }
        else{
            printf(" ball.\n");
            ball();
        }
    }
}

void tutorial(){
    char c = '0';
    printf("How to play:\n\n");
    Sleep(500);
    printf("When it tells you to hit the ball\n");
    Sleep(750);
    printf("Press any key to hit it ");
    Sleep(500);
    printf("or Press p to pause the game.\n");
    Sleep(1000);
    printf("Don't press the key more than once, ");
    Sleep(500);
    printf("or it'll carry over into the next bat.\n");
    Sleep(1000);
    printf("This game is based on timing,");
    Sleep(1000);
    printf(" so don't swing too fast or too slow.\n");
    Sleep(500);
    printf(".\n");
    Sleep(500);
    printf(".\n");
    Sleep(500);
    printf(".\n");
    Sleep(500);
    printf("Press SPACE to continue...\n");
    while(c != ' '){
        c = getch();
    }
    printf("\n\n");
}

void strike(){
    strikeCount += 1;
    if(swing == 1){
        printf("Fastball right down the middle.\n");
    }
    else{
        printf("Swing and a miss!\n");
    }
    strikeSound();
    Sleep(500);
    swing = 0;
    printf("Strike %d!\n", strikeCount);
    if (strikeCount == 3){
        Sleep(1000);
        printf("You're out!\n");
        outCount += 1;
        rally();
        outCheck();
    }
    else{
        Sleep(1000);
        count();
    }
}

void ball(){
    ballCount += 1;
    ballSound();
    if (ballCount == 4){
        Sleep(1000);
        printf("Runner take your base!\n\n");
        baseCheck();
    }
    else{
        Sleep(1000);
        count();
    }
}

void outCheck(){
    strikeCount = 0;
    ballCount = 0;
    if (outCount >= 3){
        Sleep(1000);
        printf("\n\nAnd thats the end of the ");
        newInning = 0;
        inningCheck();
        inningNum += 1;
    }
    else{
        printf("Thats the %d",outCount);
        if(outCount == 1){
            printf("st out.\n\n");
        }
        else {
            printf("nd out.\n\n");
        }
        Sleep(1000);
    }
}

void baseCheck(){
    ballCount = 0;
    strikeCount = 0;
    if (onBase == 3){
        printf("That will bring home a run.\n");
        if(inningNum % 2 == 0){
            team2Score += 1;
        }
        else{
            team1Score += 1;
        }
        Sleep(1000);
        if(team1Score == team2Score){
            printf("Its now a tie game.\n");
        }
        Sleep(1000);
        printf("The score is ");
        if(bot == 2){
            printf("Bot 1: %d to ",team2Score);
        }
        else{
            printf("Player 1: %d to ",team2Score);
        }
        if(bot != 0){
            printf("Bot 2: %d at the ",team1Score);
        }
        else{
            printf("Player 2: %d at the ",team1Score);
        }
        inningCheck();
        Sleep(1000);
    }
    else{
        onBase += 1;
    }
    onBaseSound();
}

void inningCheck(){
    inning = ceil(inningNum/2);
    int inningHalf = inningNum % 2;
    if (inningHalf == 0){
        printf("top of the ");
    }
    else{
        printf("bottom of the ");
    }
    if(inning+1 == 1){
        printf("%dst.\n\n",inning+1);
    }
    else if(inning+1 == 2){
        printf("%dnd.\n\n",inning+1);
    }
    else if(inning+1 == 3){
        printf("%drd.\n\n",inning+1);
    }
    else{
        printf("%dth.\n\n",inning+1);
    }
    Sleep(1000);
    printf("\n");
    
    if(newInning != 1){
        gameEndCheck();
    }
    else if ( inningNum >= 17 && inningNum % 2 == 1 && team1Score > team2Score){
        endGame = 1;
        printf("And thats the ballgame!\n\n");
        Sleep(1000);
        if (team1Score>team2Score && bot == 2){
            printf("Bot 2 wins the game!\n");
            Sleep(500);
        }
        else if (team1Score>team2Score && bot == 0){
            printf("Player 2 wins the game!\n");
            Sleep(500);
        }
        else if(team2Score>team1Score && bot == 1){
            printf("Bot 1 wins the game!\n");
            Sleep(500);
        }
        else {
            printf("Player 1 wins the game!\n");
            Sleep(500);
        }
        printf("With the final score being %d to %d.\n",team1Score, team2Score);
        Sleep(1000);
        printf("Thanks for playing!\n\n\n");
        //exit(0);
    }
}

void gameEndCheck(){
    if (inningNum < 18){
        if (inningNum == 17 && team1Score != team2Score){
            endGame = 1;
            printf("And thats the ballgame!\n\n");
            Sleep(1000);
            if (team1Score>team2Score && bot == 2){
                printf("Bot 2 wins the game!\n");
                Sleep(500);
            }
            else if (team1Score>team2Score && bot == 0){
                printf("Player 2 wins the game!\n");
                Sleep(500);
            }
            else if(team2Score>team1Score && bot == 1){
                printf("Bot 1 wins the game!\n");
                Sleep(500);
            }
            else {
                printf("Player 1 wins the game!\n");
                Sleep(500);
            }
            printf("With the final score being %d to %d.\n",team1Score, team2Score);
            Sleep(1000);
            printf("Thanks for playing!\n\n\n");
            //exit(0);
        }
        else if(inningNum == 16 && team1Score > team2Score){
            endGame = 1;
            printf("And thats the ballgame!\n\n");
            Sleep(1000);
            if (team1Score>team2Score && bot == 2){
                printf("Bot 2 wins the game!\n");
                Sleep(500);
            }
            else if (team1Score>team2Score && bot == 0){
                printf("Player 2 wins the game!\n");
                Sleep(500);
            }
            else if(team2Score>team1Score && bot == 1){
                printf("Bot 1 wins the game!\n");
                Sleep(500);
            }
            else {
                printf("Player 1 wins the game!\n");
                Sleep(500);
            }
            printf("With the final score being %d to %d.\n",team1Score, team2Score);
            Sleep(1000);
            printf("Thanks for playing!\n\n\n");
            //exit(0);
        }
    }
    else{
        if (inningNum % 2 == 1 && team1Score != team2Score){
            endGame = 1;
            printf("And thats the ballgame!\n\n");
            Sleep(1000);
            if (team1Score>team2Score && bot == 2){
                printf("Bot 2 wins the game!\n");
                Sleep(500);
            }
            else if (team1Score>team2Score && bot == 0){
                printf("Player 2 wins the game!\n");
                Sleep(500);
            }
            else if(team2Score>team1Score && bot == 1){
                printf("Bot 1 wins the game!\n");
                Sleep(500);
            }
            else {
                printf("Player 1 wins the game!\n");
                Sleep(500);
            }
            printf("With the final score being %d to %d.\n",team1Score, team2Score);
            Sleep(1000);
            printf("Thanks for playing!\n\n\n");
            //exit(0);
        }
    }
}

void count(){
    if(ballCount == 3 && strikeCount == 2){
        printf("Its a full count now!\n");
        Sleep(1000);
    }
    printf("The count is %d-%d.\n\n",ballCount,strikeCount);
    Sleep(1000);
}

void reset(){
    bot = 0;
    inningNum = 0;
    inning = 0;
    newInning = 0;
    ballCount = 0;
    strikeCount = 0;
    outCount = 0;
    hitZone = 0;
    team1Score = 0;
    team2Score = 0;
    startGame = 0;
    endGame = 0;
    onBase = 0;
    swing = 0;
}

void charge(){
    if(sound){
        Beep(440, 200);
        Beep(587.33, 250);
        Beep(739.989, 250);
        Beep(880, 225);
        Beep(739.989, 200);
        Beep(880, 700);
        Sleep(50);
    }
    
}

void rally(){
    if(sound){
        Beep(587.33, 250);
        Beep(587.33, 250);
        Beep(523.251, 175);
        Beep(523.251, 175);
        Beep(587.33, 250);
    }
}

void inningChange(){
    if(sound){
        Beep(440, 400);
        Beep(587.33, 300);
        Beep(440, 400);
    }
}

void BallGame(){
    if(sound){
        Beep(523.251, 250);
        Beep(1046.502, 250);
        Beep(880, 250);
        Beep(783.991, 250);
        Beep(659.255, 250);
        Beep(783.991, 700);
        Beep(587.33, 400);
        Sleep(250);
        Beep(523.251, 250);
        Beep(1046.502, 250);
        Beep(880, 300);
        Beep(783.991, 250);
        Beep(659.255, 250);
        Beep(783.991, 700);
        Sleep(250);
        Beep(880, 250);
        Beep(932.328, 250);
        Beep(880, 250);
        Beep(659.255, 250);
        Beep(698.456, 250);
        Beep(783.991, 250);
        Beep(880, 500);
        Beep(698.456, 250);
        Beep(587.33, 700);
        Sleep(250);
        Beep(880, 400);
        Beep(880, 250);
        Beep(880, 250);
        Beep(987.767, 250);
        Beep(1046.502, 250);
        Beep(1174.659, 250);
        Beep(987.767, 250);
        Beep(880, 250);
        Beep(783.991, 250);
        Beep(659.255, 250);
        Beep(587.33, 250);
        Beep(523.251, 500);
        Sleep(250);
        Beep(1046.502, 250);
        Beep(880, 250);
        Beep(783.991, 250);
        Beep(659.255, 250);
        Beep(783.991, 700);
        Beep(587.33, 250);
        Sleep(100);
        Beep(587.33, 250);
        Beep(523.251, 250);
        Beep(587.33, 250);
        Beep(659.255, 250);
        Beep(698.456, 250);
        Beep(783.991, 250);
        Beep(880, 700);
        Sleep(250);
        Beep(880, 250);
        Beep(987.767, 250);
        Beep(1046.502, 500);
        Sleep(300);
        Beep(1046.502, 500);
        Sleep(300);
        Beep(1046.502, 400);
        Beep(987.767, 250);
        Beep(880, 250);
        Beep(783.991, 250);
        Beep(739.989, 250);
        Beep(783.991, 250);
        Beep(880, 500);
        Beep(987.767, 700);
        Beep(1046.502, 900);
    }
}

void HomeRun(){
    if(sound){
        Beep(659.255, 200);
        Beep(659.255, 125);
        Beep(659.255, 125);
        Beep(880, 700);
    }
}

void onBaseSound(){
    if(sound){
        Beep(783.991, 250);
        Beep(880, 500);
    }
}

void strikeSound(){
    if(sound){
        Beep(587.33, 500);
    }
}

void ballSound(){
    if(sound){
        Beep(698.456, 500);
    }
}

void foulSound(){
    if(sound){
        Beep(698.456, 250);
        Beep(587.33, 500);
    }
}
