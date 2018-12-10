/* Author: Joseph Palmer <joseph.palmer18@imperial.ac.uk>
 * Name: calc.h
 * Desc: Header file for 
 * Date: Dec-2018 */
 
 
#ifndef _CALC_H_
#define _CALC_H_ // header guard

#define _PI_ 3.141592654

// function line macro could be like this bellow.
// #define destroy_intarray(x) _destroy_intarray(x); x = NULL;

float add_floats(float a, float b);
float subtract_floats(float a, float b);
float multiply_floats(float a, float b);
float divide_floats(float a, float b);

#endif
