#include <stdio.h>

int main() {
    FILE *fp;
    char data[100];

    fp = fopen("sample.txt", "w");

    printf("Enter text: ");
    gets(data);

    fprintf(fp, "%s", data);

    fclose(fp);

    printf("Data written successfully.");

    return 0;
}