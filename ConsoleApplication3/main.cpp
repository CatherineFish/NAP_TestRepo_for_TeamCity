#include <iostream>

void func_to_handle_mem_leak()
{
	int* ptr = new int(5);
	delete ptr;
}

int main()
{
	func_to_handle_mem_leak();
	std::cout << "Hello" << std::endl;
	return 0;
}
