#include <stdio.h>


int get_neg_int();

int main(void)
{
    int i = get_neg_int();
    printf("%i is an negative integer\n", i);
}


int get_neg_int(void)
{
    int n;
    do
    {
        printf("n : ");
        scanf("%i", &n);
    } while (n >= 0);
    return n;

}
