def conversion()
{
  with open('test.txt', 'r') as file:
    lines = [line.strip() for line in file.readlines()]
}

def waveFrontSearch(lines)
{
  for i in range(6)
    for j in range(9)
      if lines[i][j] == 'G'
        x_goal = i
        y_goal = j
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
