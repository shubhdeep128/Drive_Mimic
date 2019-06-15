#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<ctype.h>
char stack[50];
int top=-1;
void push(char c){
	stack[++top]=c;
}
char pop(){
	if(top==-1)
		return -1;
	else
		return stack[top--];
}
int priority(char c){
	if(c=='(')
		return 0;
	if(c=='+'||c=='-')
		return 1;
	if(c=='*'||c=='/')
		return 2;
}
int main(){
	int n;
	scanf("%d",&n);
	for (int i = 0; i < n; ++i)
	{
		char exp[50],*cptr,c;
		scanf("%s",exp);
		cptr=&exp[0];
		while(*cptr!='\0'){
			if(isalnum(*cptr))
				printf("%c",*cptr );
			else if(*cptr=='(')
				push(*cptr);
			else if(*cptr==')')
				{
					while((c=pop())!='(')
						printf("%c",c);
				}	
			else
			{
				while(priority(stack[top])>=priority(*cptr)){
					printf("%c",pop());
				}
				push(*cptr);
			}
			cptr++;
		}
		while(top!=-1){
			printf("%c",pop());
		}
	}
	
	return 0;
}
/*
int n,top;
int stack[50];
int pop(){
	if(top==-1){
		printf("underflow\n");
	}
	else{
		top--;
		return stack[top+1];
	}
}
void push(int y){
	if(top==n-1){
		printf("overflow\n");
	}
	else{
		stack[++top]=y;
	}	
}
void display(){
	if(top==-1){
		printf("Underflow\n");
	}
	for (int i = top; i >-1; --i)
	{
		printf("%d\n",stack[i]);
	}
}
int main(int argc, char const *argv[])
{

	scanf("%d",&n);
	top=-1;
	int c;
	for (int i = 0 ;i<n; ++i)
	{
		scanf("%d",&stack[i]);	
		top++;
	}
	
	c=pop();
	push(4);
	display();
	
	
	return 0;
}*/