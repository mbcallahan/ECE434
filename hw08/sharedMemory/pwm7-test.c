/* 
 *
 *  pwm tester
 *  (c) Copyright 2016
 *  Mark A. Yoder, 20-July-2016
 *	The channels 0-11 are on PRU1 and channels 12-17 are on PRU0
 *	The period and duty cycle values are stored in each PRU's Data memory
 *	The enable bits are stored in the shared memory
 *  Modified by MAtthew Callahan
 *
 */

#include <stdio.h>
#include <fcntl.h>
#include <sys/mman.h>

#define MAXCH 2

#define PRU_ADDR		0x4A300000		// Start of PRU memory Page 184 am335x TRM
#define PRU_LEN			0x80000			// Length of PRU memory
#define PRU0_DRAM		0x00000			// Offset to DRAM
#define PRU1_DRAM		0x02000
#define PRU_SHAREDMEM	0x10000			// Offset to shared memory

unsigned int	*pru0DRAM_32int_ptr;		// Points to the start of local DRAM
unsigned int	*pru1DRAM_32int_ptr;		// Points to the start of local DRAM
unsigned int	*prusharedMem_32int_ptr;	// Points to the start of the shared memory

/*******************************************************************************
* int start_pwm_count(int ch, int countOn, int countOff)
* 
* Starts a pwm pulse on for countOn and off for countOff to a single channel (ch)
*******************************************************************************/
int start_pwm_count(int ch, int countOn, int countOff, unsigned int *ptr) {
	unsigned int *pruDRAM_32int_ptr = ptr;
	
	printf("countOn: %d, countOff: %d, count: %d\n", 
		countOn, countOff, countOn+countOff);
	// write to PRU shared memory
	pruDRAM_32int_ptr[2*(ch)+0] = countOn;	// On time
	pruDRAM_32int_ptr[2*(ch)+1] = countOff;	// Off time
	return 0;
}

int main(int argc, char *argv[])
{
	unsigned int	*pru;		// Points to start of PRU memory.
	int	fd;
	printf("Servo tester\n");
	
	fd = open ("/dev/mem", O_RDWR | O_SYNC);
	if (fd == -1) {
		printf ("ERROR: could not open /dev/mem.\n\n");
		return 1;
	}
	pru = mmap (0, PRU_LEN, PROT_READ | PROT_WRITE, MAP_SHARED, fd, PRU_ADDR);
	if (pru == MAP_FAILED) {
		printf ("ERROR: could not map memory.\n\n");
		return 1;
	}
	close(fd);
	printf ("Using /dev/mem.\n");
	
	pru0DRAM_32int_ptr =     pru + PRU0_DRAM/4 + 0x200/4;	// Points to 0x200 of PRU0 memory
	pru1DRAM_32int_ptr =     pru + PRU1_DRAM/4 + 0x200/4;	// Points to 0x200 of PRU1 memory
	prusharedMem_32int_ptr = pru + PRU_SHAREDMEM/4;	// Points to start of shared memory


	int on[]  = {1, 2, 3, 4};
	int off[] = {1, 3, 2, 1};//this line has the first element changed to make the writing to memory more clear

	int ch;
	for(ch=0; ch<MAXCH; ch++) {
		start_pwm_count(ch, on[ch],       off[ch],       pru0DRAM_32int_ptr);
		start_pwm_count(ch, on[ch+MAXCH], off[ch+MAXCH], pru1DRAM_32int_ptr);
	}
	
	if(munmap(pru, PRU_LEN)) {
		printf("munmap failed\n");
	} else {
		printf("munmap succeeded\n");
	}
}

