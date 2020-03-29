#include <sys/types.h>
#include <fcntl.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string>
#include <array>
#include <iostream>
#include <chrono>

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
    char buf[1048576];

    if (popen2("./100", &infp, &outfp) <= 0)
    {
        printf("Unable to exec your-program\n");
        exit(1);
    }

    std::array<std::string, 100> s = {
    "605293 606510\n",
    "956739 956006\n",
    "826611 825983\n",
    "756134 756776\n",
    "478642 479101\n",
    "815892 815933\n",
    "719220 719135\n",
    "929349 929040\n",
    "948351 948681\n",
    "491808 491202\n",
    "504516 507852\n",
    "604712 604712\n",
    "436809 436182\n",
    "630804 630542\n",
    "975948 975688\n",
    "945718 945752\n",
    "747700 747747\n",
    "652581 653137\n",
    "824003 823974\n",
    "655077 655161\n",
    "567537 567893\n",
    "851101 851038\n",
    "524621 524569\n",
    "549210 549073\n",
    "782205 782263\n",
    "422252 422691\n",
    "285142 285524\n",
    "478472 479285\n",
    "485461 484957\n",
    "748121 748121\n",
    "823874 824088\n",
    "359661 358904\n",
    "388654 388444\n",
    "981428 981459\n",
    "830977 832487\n",
    "654572 654612\n",
    "240125 241624\n",
    "532347 536933\n",
    "545105 545167\n",
    "850670 851113\n",
    "978562 976960\n",
    "319662 322868\n",
    "560495 559981\n",
    "831101 831011\n",
    "784445 782843\n",
    "859271 859331\n",
    "998394 998498\n",
    "975465 975228\n",
    "687538 680880\n",
    "786313 786051\n",
    "780568 780732\n",
    "363174 361163\n",
    "261481 261858\n",
    "908012 909802\n",
    "984442 984350\n",
    "931890 931544\n",
    "788836 791387\n",
    "919454 919499\n",
    "575642 575716\n",
    "915504 916839\n",
    "285788 285880\n",
    "919365 918704\n",
    "827554 827930\n",
    "850429 850334\n",
    "737959 737960\n",
    "809210 810518\n",
    "974713 974143\n",
    "456486 455019\n",
    "727712 727631\n",
    "743706 745566\n",
    "465147 463724\n",
    "945152 944673\n",
    "776248 775948\n",
    "541191 542743\n",
    "256518 255672\n",
    "947523 950576\n",
    "423648 421688\n",
    "574485 575669\n",
    "588113 587943\n",
    "748123 748033\n",
    "930036 929896\n",
    "982165 982843\n",
    "806280 806281\n",
    "379341 379868\n",
    "155281 158691\n",
    "854261 855194\n",
    "827665 827456\n",
    "806029 805322\n",
    "276791 280194\n",
    "655238 655329\n",
    "358577 358839\n",
    "842747 844169\n",
    "612687 612358\n",
    "810273 809602\n",
    "431700 431055\n",
    "281758 283365\n",
    "984263 984008\n",
    "884741 885879\n",
    "724852 724070\n",
    "869222 869573\n"};

    auto start = std::chrono::high_resolution_clock::now();
    for(int i = 0; i < s.size(); i++) {
        write(infp, s[i].c_str(), s[i].length());
    }
    close(infp);
    read(outfp, buf, 1048576);
    printf("%s\n\n", buf);
    auto stop = std::chrono::high_resolution_clock::now();
    auto duration = std::chrono::duration_cast<std::chrono::microseconds>(stop - start);
    std::cout << "Execution time: " << duration.count() << std::endl;
    return 0;
}