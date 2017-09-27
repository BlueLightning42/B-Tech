//made by blue when he was playing around with learning overloaded operators nu bully

#include "Imagin_A_Library.h"
#include <iostream>
#include "ImaginaryNumberLibrary.h"



int main(){
	ComplexNum a(4, 28.2), b, c(0,0);
	std::cout << "This Program calculates a few random equations using complex numbers.\n"
		      << "Please provide the real part of a complex number: (b) ";
    b.setR();
	std::cout << "Please provide the imaginary part of a complex number: (b) ";
    b.setI();
    std::cout << "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n";

    a.print_rectAndPolar(" of (a)");
    b.print_rectAndPolar(" of (b)");

    c = a + b;
    std::cout << "\n\na + b = \n";
    c.print_rectAndPolar("");

    c = b - a;
    std::cout << "\n\nb - a = \n";
    c.print_rectAndPolar("");

    c = b / a;
    std::cout << "\n\nb / a = \n";
    c.print_rectAndPolar("");

    c = a * b;
    std::cout << "\n\na * b = \n";
    c.print_rectAndPolar("");

	std::cin.get(); std::cin.ignore();//pause
    return 0;
}

