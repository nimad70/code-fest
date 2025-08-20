// CodeContest.cpp : This file contains the 'main' function. Program execution begins and ends there.

#include <iostream>
#include <string>
#include <cstdlib>
#include <ctime>
#include <math.h>
#include <vector>
#include <fstream>

using namespace std;



int main()
{
	//srand(time(0));
	//int rand_num = rand() % 10;
	//int arr[] = { 1, 2, 3, 4, 5, 6, 7, 8, 9 };
	//vector<int> vec = { 1, 2, 3, 4, 5, 6, 7, 8, 9 };
	//
	////int arra_size = sizeof(arr) / sizeof(arr[0]);
	////cout << "Array size: " << arra_size << endl;

	////Menu menu;
	////menu.display();

	//char res;
	//cin >> res;
	//switch (res)
	//{
	//case '1':
	//	cout << "\nYou selected Factorial" << endl;
	//	cout << "Factorial(3): " << factorial(3) << endl;
	//	break;
	//case '2':
	//	cout << "\nYou selected Fibonacci" << endl;
	//	cout << "Fibonacci(3): " << fibonacci(3);
	//	break;
	//case '3':
	//	cout << "\nYou selected Insert Sort" << endl;
	//	break;
	//default:
	//	break;
	//}


	clock_t before = clock();
	int k = 0;
	for (int i = 0; i < 1000000; i++) {
		k += i;
	}
	clock_t duration = clock() - before;
	cout << "Time taken: " << (float)duration / CLOCKS_PER_SEC << " seconds" << endl;

	return 0;

}

int factorial(int n)
{
	if (n < 0)
		return -1; // Error case for negative input
	else if (n == 0 || n == 1)
		return 1;
	else
		return n * factorial(n - 1);
}

int fibonacci(int n)
{
	if (n < 0)
		return -1; // Error case for negative input
	else if (n == 0)
		return 0;
	else if (n == 1)
		return 1;
	else
		return fibonacci(n - 1) + fibonacci(n - 2);
}
//class Menu {
//	private:
//		int option;
//
//	public:
//		Menu(int option);
//		void display();
//};
//
//
//Menu::Menu(int option) {
//	this->option = option;
//}
//
//void Menu::display() {
//	cout << "Welcome to the Code Contest!" << endl;
//	cout << "1. Factorial" << endl;
//	cout << "2. Fibonacci" << endl;
//	cout << "3. Insert Sort" << endl;
//	cout << "4. Exit" << endl;
//	cout << "Please select an option: ";
//}
//
//
//class BuildArray {
//	protected:
//		int* arr;
//		int size;
//		int value;
//		int min;
//		int max;
//		bool unique;
//	
//	public:
//		BuildArray(int size);
//		int* get_array();
//		void set_array();
//		int* build_array(int size);
//		int* build_array(int size, int value);
//		int* build_array(int size, int min, int max);
//		int* build_array(int size, int min, int max, bool unique);
//
//};
//int* BuildArray::build_array(int size) {
//	int* arr = new int[size];
//	for (int i = 0; i < size; i++) {
//		arr[i] = rand() % 100; // Random number between 0 and 99
//	}
//	return arr;
//}
//
//BuildArray::BuildArray(int size) {
//	this->size = size;
//}
//
//int* BuildArray::get_array() {
//	return arr;
//}
//
//void BuildArray::set_array() {
//	int* arr = new int[size]{2,3,4,5,6,3};
//}
//
//class SearchClass: public BuildArray {
//	public:
//		int linear_search(int arr[], int size, int target);
//		int binary_search(int arr[], int size, int target);
//};
//
//
//class SortClass {
//	public:
//		int insertion_sort(int arr[5]);
//		int insertion_sort(int arr[5], int size);
//};
//
//int SortClass::insertion_sort(int arr[5])
//{
//	return 0;
//}
//
//int SortClass::insertion_sort(int arr[5], int size)
//{
//	return 0;
//}
//
//
//int factorial(int n);
//int fibonacci(int n);