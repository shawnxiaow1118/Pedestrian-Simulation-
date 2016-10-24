#include <iostream>
#include <fstream>
#include <vector> 
using namespace std;

void Lee(int k, int i, int j, vector<vector<int> > &map, vector<vector<int> > &dist);
int row = 140;
int col = 200;

int main()
{
	vector<vector<int> > map(row, vector<int>(col));
	vector<vector<int> > dist(row, vector<int>(col));
	
	ifstream input("map.txt");
	if (!input.is_open())
	{
		cout << "File not exists" << endl;
		exit(1);
	}

	for (int i = 0; i < row; i++)
	{
		for (int j = 0; j < col; j++)
		{
			input >> map[i][j];
		}
	}

	for (int i = 0; i < row; i++)
	{
		for (int j = 0; j < col; j++)
		{
			dist[i][j] = 1000;
		}
	}
	int id[] = {25,26,27,28,29,30};
	for (int k = 0; k< sizeof(id)/sizeof(int);k++)
	{
		dist[139][id[k]] = 0;
		Lee(0,139,id[k],map,dist);
	    ofstream outfile ("static8.txt");
	    for (int i = 0; i < row; i++)
	    {
	    	for (int j = 0; j < col; j++)
	    	{
	    		outfile << dist[i][j] << " ";
	    	}
	    	outfile << endl;
	    }
	}
}

void Lee(int k, int i, int j,vector<vector<int> > &map, vector<vector<int> > &dist)
{
	if ((i+1) < row && map[i+1][j] == 1)
	{
    	if(dist[i+1][j] > k+1)
    		{
    			//cout << dist[i+1][j] << endl;
    			dist[i+1][j] = k+1;
    			Lee(k+1,i+1,j,map,dist);  			
    		}
	}

	if ((i-1) > -1 && map[i-1][j] == 1)
	{
    	if(dist[i-1][j] > k+1)
    		{
    			dist[i-1][j] = k+1;
    			Lee(k+1,i-1,j,map,dist);  			
    		}
	}

	if ((j+1) < col && map[i][j+1] == 1)
	{
    	if(dist[i][j+1] > k+1)
    		{
    			dist[i][j+1] = k+1;
    			Lee(k+1,i,j+1,map,dist);   			
    		}
	}

	if ((j-1) > -1 && map[i][j-1] == 1)
	{
    	if(dist[i][j-1] > k+1)
    		{
    			dist[i][j-1] = k+1;
    			Lee(k+1,i,j-1,map,dist) ;  			
    		}
	}
}