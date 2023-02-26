#include<pybind11/pybind11.h>
#include<iostream>
#include<string>
using namespace std;

size_t billion() {
	size_t n = 0;
	while (n < 1000000000) {
		n++;
	}
	return n;
}

int million() {
	int l = 0;
	for (int i = 0; i < 1000000; i++) {
		l++;
	}
	return l;
}

int mil(int number) {

	for (int i = 0; i < 1000000; i++) {
		number++;
	}
	return number;
}

PYBIND11_MODULE(pybind11module, module) {
	module.doc() = "Pybind11Module";
	module.def("million", &million);
	module.def("mil", &mil);
	module.def("billion", &billion);
}