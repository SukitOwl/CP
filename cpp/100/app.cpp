#include <sys/types.h>
#include <fcntl.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

#define READ 0
#define WRITE 1

pid_t popen2(const char *command, int *infp, int *outfp)
{
    int p_stdin[2], p_stdout[2];
    pid_t pid;

    if (pipe(p_stdin) != 0 || pipe(p_stdout) != 0)
        return -1;

    pid = fork();
    if (pid < 0)
        return pid;
    else if (pid == 0)
    {
        close(p_stdin[WRITE]);
        dup2(p_stdin[READ], READ);
        close(p_stdout[READ]);
        dup2(p_stdout[WRITE], WRITE);
        execl("/bin/sh", "sh", "-c", command, NULL);
        perror("execl");
        exit(1);
    }

    if (infp == NULL)
        close(p_stdin[WRITE]);
    else
        *infp = p_stdin[WRITE];
    if (outfp == NULL)
        close(p_stdout[READ]);
    else
        *outfp = p_stdout[READ];
    return pid;
}

/*
* now in main... infp will be the stdin (in file descriptor)
* and outfp will be the stdout (out file descriptor)
* have fun
*/

int main(int argc, char **argv)
{
    int infp, outfp;
    char buf[128];

    if (popen2("./100", &infp, &outfp) <= 0)
    {
        printf("Unable to exec your-program\n");
        exit(1);
    }

    write(infp, "10 20\n", 6);
    write(infp, "20 30\n", 6);
    write(infp, "30 40\n", 6);
    write(infp, "40 50\n", 6);
    write(infp, "50 60\n", 6);
    close(infp);
    read(outfp, buf, 512);
    printf("%s", buf);
    return 0;
}