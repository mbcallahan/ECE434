#include <stdint.h>
#include <pru_cfg.h>
#include "resource_table_empty.h"
#include "prugpio.h"

volatile register uint32_t __R30;
volatile register uint32_t __R31;

void main(void)
{
  uint32_t gpio = (1<<0);//select P9_31 which connects to PRUR30[0]

    /* Clear SYSCFG[STANDBY_INIT] to enable OCP master port */
    CT_CFG.SYSCFG_bit.STANDBY_INIT = 0;

    while(1) {
        __R30 |= gpio;      // Set the GPIO pin to 1
        __delay_cycles(1000);
        __R30 &= ~gpio;     // Clear the GPIO pin
        __delay_cycles(1000);
    }
}


