#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <stdbool.h>

#define MAXSIZE 256
#define TABLESIZE 10

typedef struct
{
	char name[MAXSIZE];
	int age;
}person;

unsigned int hash(char *name)
{
	int i, length = strlen(name);
	unsigned int hash_value = 0;
	for (i = 0; i < length; i++)
	{
		hash_value += name[i];
		hash_value = (hash_value * name[i]) % TABLESIZE;
	}
	return (hash_value);
}

person *hash_table[TABLESIZE];

void init_hash_table()
{
	int i;

	for (i = 0; i < TABLESIZE; i++)
		hash_table[i] = NULL;
}

void print_hash_table()
{
	int i;

	for (i = 0; i < TABLESIZE; i++)
	{
		if (hash_table[i] == NULL)
			printf("\t%i\t-----\n", i);
		else
			printf("\t%i\t%s\n", i, hash_table[i]->name);
	}
}

bool hash_table_insert(person *p)
{
	if (p == NULL)
		return (false);
	int index = hash(p->name);
	if (hash_table[index] != NULL)
		return (false);
	hash_table[index] = p;
	return (true);
}

int main(void)
{
	init_hash_table();
	printf("/t---------\n");
	print_hash_table();
	printf("/t---------\n");

	
	/**
	printf("Jacob => %u\n", hash("Jacob"));
	printf("Kofi => %u\n", hash("Kofi"));
	printf("Yaw => %u\n", hash("Yaw"));
	printf("Ama => %u\n", hash("Ama"));
	printf("Abena => %u\n", hash("Abena"));
	printf("Jake => %u\n", hash("Jake"));
	printf("Job => %u\n", hash("Job"));
	printf("Koby => %u\n", hash("Koby"));
	return (0);*/
}
