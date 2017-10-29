#include <stdio.h>
#include <string.h>

int main(void)
{
    // ask user for input
    char user_input;
    user_input = scanf("%s", user_input);

    // make sure scanf returned
    if (user_input != NULL)
    {
        // iterate over the character
        for (int i = 0, n = strlen(user_input); i < n; i++)
        {
            // print i'th character in user_input
            printf("%c\n", user_input[i]);
        }
    }
}
