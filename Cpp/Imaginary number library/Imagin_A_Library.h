	#pragma once
	#include <string>
    #include <iostream>
    #include <sstream>
    #include <iomanip>
    #include <math.h>
	#ifndef IMAGINARY
	#define IMAGINARY

	class ComplexNum { 
	public:	
		ComplexNum() { //Default Constructor
			R_ = 0.0; I_ = 0.0;
		}; 
		ComplexNum(double r, double i) { 
			R_ = r; I_ = i;
		}
        void setR() {
            std::cin >> R_;
        }
        void setI() {
            std::cin >> I_;
        }


        void print_rectAndPolar(std::string name) {
            std::string rectForm, polarForm;
            double magnitude, angle;
            if (I_ > 0) {
                rectForm = doubleToString(R_) + " + i" + doubleToString(I_);
            }
            else if (I_ < 0) {
                rectForm = std::to_string(R_) + " + i" + std::to_string(-I_);
            }
            else {
                rectForm = R_;
            }

            magnitude = sqrt(pow(I_,2) + pow(R_,2));
            angle = atan(I_ / R_);
            polarForm = doubleToString(magnitude) + "(cos " + doubleToString(angle) + "    i sin " + doubleToString(angle) + ")";


            std::cout << "rectangular form" << name << ": " << rectForm << "\nand polar form " << name << ": " << polarForm << std::endl << std::endl;
        }

        std::string doubleToString(double value) {
            std::ostringstream stringstream;
            stringstream <<  std::fixed << std::setprecision(2);
            stringstream << value;
            std::string str = stringstream.str();
            return str;
        }
        
		//bunch of basic arithmatic operators
		ComplexNum operator+(ComplexNum &obj) {
			ComplexNum temp;
			temp.I_ = this->I_ + obj.I_;
			temp.R_ = this->R_ + obj.R_;

			return temp;
		}
		ComplexNum operator-(ComplexNum &obj) {
			ComplexNum temp;
			temp.I_ = this->I_ - obj.I_;
			temp.R_ = this->R_ - obj.R_;

			return temp;
		}
		ComplexNum operator*(ComplexNum &obj) {
			ComplexNum temp;
			temp.R_ = (this->R_ * obj.R_) - (this->I_*obj.I_);
			temp.I_ = (this->R_ * obj.I_) + (this->I_ * obj.R_);

			return temp;
		}

		ComplexNum operator/(ComplexNum &obj) {
			ComplexNum temp;
			double denominator;
			denominator = (obj.R_ * obj.R_) + (obj.I_* obj.I_);
			temp.R_ = (this->R_ * this->R_) / denominator + (this->I_ * this->I_) / denominator;
			temp.I_ = (this->R_ * obj.I_ ) / denominator - (this->I_ * obj.R_ ) / denominator;

			return temp;
		}
    private:
        double R_, I_;
	};

	#endif // !IMAGINARY
