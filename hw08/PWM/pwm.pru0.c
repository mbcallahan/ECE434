#include <stdint.h>
#include <pru_cfg.h>
#include "resource_table_empty.h"
#include "prugpio.h"

//In order to have a 50MHz signal, there needs to be 20ns period. This means there needs to be four instructions. to have it symmetric, there can be one write instruction so there is only one instruction between the writes.
volatile register uint32_t __R30;
volatile register uint32_t __R31;

void main(void)
{
  uint32_t gpio = (1<<0);//select P9_31 which connects to PRUR30[0]
  
    /* Clear SYSCFG[STANDBY_INIT] to enable OCP master port */
    CT_CFG.SYSCFG_bit.STANDBY_INIT = 0;

    while(1) {
        __R30 ^= gpio;      // toggle the gpio pin
        
    }
}


