// GLOBAL VARIABLES grid world dimensions
const int x_size = 10;
const int y_size = 5;

// GLOBAL ARRAY representation of grid world using a 2-Dimensional array
// 0  = open space
// 1  = barrier
// 2  = goal
// 99 = robot
int map[x_size][y_size] = 
 {{0,0,0,0,0},
  {0,1,99,1,0},
  {0,1,1,1,0},
  {0,0,0,0,0},
  {0,0,0,0,0},
  {0,0,0,0,0},
  {0,0,0,0,0},
  {0,0,2,0,0},
  {0,0,0,0,0},
  {0,0,0,0,0}};

// FUNCTION move forward for a variable number of grid blocks
void moveForward(int blocks)
{
  // convert number of blocks to encoder counts
  // wheel circumference = 17.6 cm
  // one block = 23.7 cm
  int countsToTravel = (23.7/17.6)*(360)*blocks;

  // encoder target for countsToTravel
  nMotorEncoder[motorB] = 0;
  nMotorEncoder[motorC] = 0;
  nMotorEncoderTarget[motorB] = countsToTravel;
  nMotorEncoderTarget[motorC] = countsToTravel;
  motor[motorB] = 50;
  motor[motorC] = 50;
  while(nMotorRunState[motorB] != runStateIdle && nMotorRunState[motorC] != runStateIdle) {}

  // stop for half second at end of movement
  motor[motorB] = 0;
  motor[motorC] = 0;
  wait1Msec(500);
}

// FUNCTION left point turn 90 degrees
void turnLeft90()
{
  // distance one wheel must travel for 90 degree point turn = 8.6 cm
  // wheel circumference = 17.6 cm
  int countsToTravel = (8.6/17.6)*(360);

  // encoder target for countsToTravel
  nMotorEncoder[motorB] = 0;
  nMotorEncoder[motorC] = 0;
  nMotorEncoderTarget[motorB] = countsToTravel;
  nMotorEncoderTarget[motorC] = countsToTravel;
  motor[motorB] = 50;
  motor[motorC] = -50;
  while(nMotorRunState[motorB] != runStateIdle && nMotorRunState[motorC] != runStateIdle) {}

  // stop for half second at end of movement
  motor[motorB] = 0;
  motor[motorC] = 0;
  wait1Msec(500);
}

// FUNCTION right point turn 90 degrees
void turnRight90()
{
  // distance one wheel must travel for 90 degree point turn = 8.6 cm
  // wheel circumference = 17.6 cm
  int countsToTravel = (8.6/17.6)*(360);

  // encoder target for countsToTravel
  nMotorEncoder[motorB] = 0;
  nMotorEncoder[motorC] = 0;
  nMotorEncoderTarget[motorB] = countsToTravel;
  nMotorEncoderTarget[motorC] = countsToTravel;
  motor[motorB] = -50;
  motor[motorC] = 50;
  while(nMotorRunState[motorB] != runStateIdle && nMotorRunState[motorC] != runStateIdle) {}

  // stop for half second at end of movement
  motor[motorB] = 0;
  motor[motorC] = 0;
  wait1Msec(500);
}

// FUNCTION print wavefront map to NXT screen
void PrintWavefrontMap()
{
  int printLine = y_size-1;
  for(int y = 0; y < y_size; y++)
  {
    string printRow = "";
    for(int x=0; x < x_size; x++)
    {
      if(map[x][y] == 99)
        printRow = printRow + "R ";
      else if(map[x][y] == 2)
        printRow = printRow + "G ";
      else if(map[x][y] == 1)
        printRow = printRow + "X ";
      else if(map[x][y] < 10)
        printRow = printRow + map[x][y] + " ";
      else if(map[x][y] == '*')
        printRow = printRow + "* ";
      else
        printRow = printRow + map[x][y];
    }
    nxtDisplayString(printLine, printRow);
    printLine--;
  }
}

// FUNCTION wavefront algorithm to find most efficient path to goal
void WavefrontSearch()
{
  int goal_x, goal_y;
  bool foundWave = true;
  int currentWave = 2; // Looking for goal first

  while(foundWave == true)
  {
    foundWave = false;
    for(int y=0; y < y_size; y++)
    {
      for(int x=0; x < x_size; x++)
      {
        if(map[x][y] == currentWave)
        {
          foundWave = true;
          goal_x = x;
          goal_y = y;

          if(goal_x > 0)
            if(map[goal_x-1][goal_y] == 0)
              map[goal_x-1][goal_y] = currentWave + 1;

          if(goal_x < (x_size - 1))
            if(map[goal_x+1][goal_y] == 0)
              map[goal_x+1][goal_y] = currentWave + 1;

          if(goal_y > 0)
            if(map[goal_x][goal_y-1] == 0)
              map[goal_x][goal_y-1] = currentWave + 1;

          if(goal_y < (y_size - 1))
            if(map[goal_x][goal_y+1] == 0)
              map[goal_x][goal_y+1] = currentWave + 1;
        }
      }
    }
    currentWave++;
    PrintWavefrontMap();
    wait1Msec(500);
  }
}

// FUNCTION follow most efficient path to goal
void NavigateToGoal()
{
  int robot_x, robot_y;

  for(int x=0; x < x_size; x++)
  {
    for(int y=0; y < y_size; y++)
    {
      if(map[x][y] == 99)
      {
        robot_x = x;
        robot_y = y;
      }
    }
  }

  int current_x = robot_x;
  int current_y = robot_y;
  int current_facing = 0;
  int next_Direction = 0;
  int current_low = 99;

  while(current_low > 2)
  {
    current_low = 99;
    next_Direction = current_facing;
    int Next_X = 0;
    int Next_Y = 0;

    // Check directions and move
    // (code logic continues here...)

    moveForward(1);
    PrintWavefrontMap();
    wait1Msec(500);
  }
}

task main()
{
  WavefrontSearch();
  NavigateToGoal();
  wait1Msec(5000);
}
