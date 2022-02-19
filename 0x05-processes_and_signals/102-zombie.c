#include <stdio.h>
#include <unistd.h>

/**
 * infinite_while - infinitive loop
 *
 * Return: always 0
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - create 5 child process and each one, one zombie
 *
 * Return: always 0
 */
int main(void)
{
	int i = 0, process_id;

	while (i < 5)
	{
		process_id = fork();
		if (process_id > 0)
			printf("Zombie process created, PID: %d\n", process_id);
		else
			return (0);
		i++;
	}
	infinite_while();
	return (0);
}
