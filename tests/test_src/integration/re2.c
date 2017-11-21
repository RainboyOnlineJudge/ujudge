#include <stdio.h>
#include <signal.h>

int main()
{
    /*raise(SIGSEGV);*/
    char *p = NULL;
    printf("%c",*p);//读操作
    *p='A';//写操作。
    return 0;
}
