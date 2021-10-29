#include <stdint.h>
#include <pru_cfg.h>
#include "resource_table_empty.h"
#include "prugpio.h"


#define P931 (1<<14)//it is gpio3[14]

volatile register uint32_t __R30;
volatile register uint32_t __R31;
void main(void) {
	int i;
	uint32_t *gpio1 = (uint32_t *)GPIO1;
	uint32_t *gpio3 = (uint32_t *)GPIO3;
	
	/* Clear SYSCFG[STANDBY_INIT] to enable OCP master port */
	//	CT_CFG.SYSCFG_bit.STANDBY_INIT = 0;
	
	while(1){
	  gpio3[GPIO_SETDATAOUT]   = P931;//que the pin to be set high	

		//see if this is compiled away when set to zero
		__delay_cycles(0);//from experiments, this is removed. 

		gpio3[GPIO_CLEARDATAOUT] = P931;//que the pin to be set low
	
		__delay_cycles(0); 

	}
	__halt();
}

