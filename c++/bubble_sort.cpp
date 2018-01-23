// This program uses a bubble sort to arrange an array of integers in 
// ascending order

#include<iostream>
using namespace std;

// Jake Gadaleta

// function prototypes

void bubbleSortArray(int [], int);
void displayArray(int[], int);

const int SIZE = 5;

int main()
{
	int values[SIZE] = {9,2,0,11,5};

	cout << "The values before the bubble sort is performed are:" << endl;
	displayArray(values,SIZE);
	cout << endl << endl << endl;
	bubbleSortArray(values,SIZE);
	cout << endl << endl << endl;
	cout << "The values after the bubble sort is performed are:" << endl;
	displayArray(values,SIZE);

	return 0;
}
//******************************************************************
//                      displayArray
//
// task:		to print the array
// data in:       the array to be printed, the array size
// data out:      none
//
//******************************************************************

void displayArray(int array[], int elems)    // function heading
{							   // displays the array	
	for (int count = 0; count < elems; count++)
		cout << array[count] << "  " << endl;
}

//******************************************************************
//                      bubbleSortArray
//
// task:		to sort values of an array in ascending order
// data in:       the array, the array size
// data out:      the sorted array
//
//******************************************************************


void bubbleSortArray(int array[], int elems)
{
	bool swap;
	int temp;
	int bottom = elems - 1;     // bottom indicates the end part of the 
	                            // array where the largest values have
	                            // settled in order
do
	{
		swap = false;
		for (int count = 0; count < bottom; count++)
		{
			if (array[count] < array[count+1])
			{	          // the next six lines do a swap   
			   temp = array[count];  
			   cout << "Temp was assnigned a vaule of " << temp << " from the " << count + 1 << " point on the array" << endl;
			   array[count] = array[count+1];
			   cout << count + 1 << " has become" << count + 2 << endl;
			   array[count+1] = temp;
			   cout << count + 2 << " vaule has been saved in temp" << endl;
			   swap = true; // indicates that a swap occurred
			   cout << "A swap has occured";
			}
		}
            bottom--;     // bottom is decremented by 1 since each pass through
	                    // the array adds one more value that is set in order
	            
	} while(swap != false);
              // loop repeats until a pass through the array with
	        // no swaps occurs
}
