#include <stdio.h>
#include <string.h>

int main()
{
    fprintf(stdout, "stderr\n");
    fprintf(stdout, "--------------\n");
    fprintf(stdout, "stdout\n");
    fprintf(stdout, "+++++++++++++++\n");
    return 0;
}
