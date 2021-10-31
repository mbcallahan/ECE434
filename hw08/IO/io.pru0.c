#include <stdint.h>
#include <pru_cfg.h>
#include "resource_table_empty.h"
#include "prugpio.h"

#define DELAY 200/5 //want to wait 200ns, 5ns per clock cycle
volatile register uint32_t __R30;
volatile register uint32_t __R31;

void main(void)
{
  uint32_t gpio = (1<<0);//select P9_31 which connects to PRUR30[0]
  uint32_t inMask = (1<<1); //select P9_25 as in example. The bit position in the example is wrong
    /* Clear SYSCFG[STANDBY_INIT] to enable OCP master port */
    CT_CFG.SYSCFG_bit.STANDBY_INIT = 0;

    //flash led as test
    __R30 |= gpio;
    __delay_cycles(1000000);
    __R30 &= ~gpio;

    while(1) {
      //no good way to set individual bits, so need to have a if statement
      if(__R31&inMask){
	__R30 |= gpio;
      }
      else
	__R30 &= ~gpio;
    }
}


