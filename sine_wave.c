#include <reg51.h>

#define DAC P1 //for mapping Port 1 in 8051 to the digital to analog converter

unsigned char sine_table[20] = {
    128, 167, 203, 231, 249, 255, 249, 231, 203, 167,
    128,  89,  53,  25,   7,   1,   7,  25,  53,  89
}; //this is our binary numbers list (their decimal equivalent) which will be directed to prot1 for conversion

unsigned char index = 0;
// The following is the interrupt service routine for timer 0. It fires when Timer 0 overflow
void timer0_ISR(void) __interrupt(1) {
    DAC = sine_table[index++]; // The index increases whenever timer 0 overflows to sample the next element
    if (index >= 20) index = 0; // It restart to zero when it reaches 20 so we can generate the sine function again
    TH0 = 0xF0;
}

void main(void) {
    TMOD =0x02; // this set sets Timer 0 at 8-bit mode
    TH0 = 0xF0; // We want a dely of 15 micro seconds

    ET0 = 1; //to enable timer 0 interrupts     
    EA = 1; //to enable global interrupts     
    TR0 = 1; //to enable timer 0    

    while (1); //this is set so our 8051 program runs indefinitely (until we stop it) so it generates multiple sine waves.
}
