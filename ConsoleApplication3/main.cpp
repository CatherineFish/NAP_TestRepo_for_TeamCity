#include <iostream>

void func_to_handle_mem_leak()
{
	int* ptr = new int(5);
}

int main()
{
	func_to_handle_mem_leak();
	return 0;
}
