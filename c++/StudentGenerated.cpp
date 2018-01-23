/*
Jake Gadaleta
1/18/18
number sorter
*/

#include<iostream>
#include<fstream>
#include<time.h>
using namespace std;

const int MAXSIZE = 50;		// Max size of the arry
int numbers[MAXSIZE];		// arry to hold numbers

                                            

void RandomArray();			// fills a file with random numbers 
void GenerateArray();		// reads file to fill array
void SortArray1();			// sorts the array
int SearchEntry();			// saves a search to be used in BinarySearch()
int BinarySearch(int);		// preforms a binary search to find an entry for SearchEntry()
int MeanGernerator();		// finds the mean by taking the array and dividing
void Display(int, int, int);// Displays all information

void main()
{
	/*
	For explanation see above
	*/
	char select;
	cout << "would you like to randomize the array: y for yes anythin else for not	";
	cin >> select;
	if (select == 'y' || select == 'Y')
		RandomArray();
	GenerateArray();
	SortArray1();
	int search = SearchEntry();
	int position = BinarySearch(search);
	int mean = MeanGernerator();
	Display(search, position, mean);
}

void RandomArray()
{
	ofstream outfile;
	outfile.open("D:\\Code Workstation\\Robots Autimate code\\Cplusplus\\Numbers.txt"); //opens file to write to it
	srand(time(NULL)); //seeds random
	int random; // to hold a random vaule 
	
	for (int i = 0; i < MAXSIZE; i++)// to write the vaule
	{
		outfile << rand() % 500 + 1 << endl;
	}
	outfile.close();//closes file
}

void GenerateArray()
{
	ifstream infile;
	infile.open("D:\\Code Workstation\\Robots Autimate code\\Cplusplus\\Numbers.txt"); //reads in the numbers
	cout << "Pulling " << MAXSIZE << " entries from Numbers.txt" << endl;
	for (int i = 0; i < MAXSIZE; i++) // assigns the numbers from the text document
	{
		infile >> numbers[i];
	}
	
}

void SortArray1()
{
	bool swap = true; 
	int temp;
	int bottom = MAXSIZE - 1;     
	while (swap != false) // runs as long as 
	{
		swap = false; // sets swap = to false as an exit statment
		for (int count = 0; count < bottom; count++)//checks to see if there is room to switch 
		{
			if (numbers[count] < numbers[count + 1])//will swap the numbers but storing one in a temp variable
			{	            
				temp = numbers[count];
				numbers[count] = numbers[count + 1];
				numbers[count + 1] = temp;
				swap = true; // resets
			}
		}
		bottom--;// measures how manytimes to ensure an exit     

	}
	

}

int SearchEntry()
{
	int search;
	cout << "What search vaule would you like to use?";
	cin >> search;
	return search; // assigns a vaule for the search
}

int BinarySearch(int value)
{
	cout << "Enter a vaule";
	cin >> value;
	int first = 0, last = MAXSIZE - 1, middle, position = -1; 
	bool found = false; // Flag
	while (!found && first <= last)
	{
		middle = (first + last) / 2; // Calculate midpoint
		if (numbers[middle] == value) // If value is found at mid
		{
			found = true;
			position = middle;
		}
		else if (numbers[middle] > value) // If value is in lower half
			last = middle - 1;
		else
			first = middle + 1; // If value is in upper half
	}
	return position;
}

int MeanGernerator()
{
	int total = 0; 
	int counter = 0;
	int test = 0;
	for (int i = 0; i < MAXSIZE; i++)
	{
		total = total + numbers[i]; // adds array elements to total
		if (numbers[i] != 0 && numbers[i + 1] != 0) // ensure that it is not taking in extra zero's
		{
			counter += 1;
			test += 1;
		}
	}
	if (test == 1)
		counter -= 1;
	int mean = total / counter;
	return mean;
}

void Display(int search, int position, int mean)
{
	// displays all data
	if (position != -1)
		cout << "The vaule " << search << " was found at postion " << position + 1 << " In the binary search" << endl;
	else
		cout << "The vaule " << search << " was not found" << endl;
	cout << "The array is sorted" << endl;
	for (int i = 0; i < MAXSIZE; i++)
	{ 
		cout << numbers[i] << ", ";
	}
	cout << endl << "The mean is " << mean << endl;
}
