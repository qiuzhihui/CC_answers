/*
  This program is writing to reverse a null terminated string in C
*/
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char **argv){

	int len=0;
	char tmp,*str;

	//check if has one line string input
	if(argc!=2){
		printf("something wrong!\n");
		return -1;
	}

	printf("we have input: %s\n",argv[1]);
	//while(argv[0])

	while(argv[1][len]){
		len++;
	}

	printf("number:%d\n",len);

	str = (char *) malloc((len+1)*sizeof(char));
	str[len]='\n';


	for(int i=0; i<len ;i++){
		str[i]=argv[1][len-1-i];
	}

	printf("we have output: %s",str);

}