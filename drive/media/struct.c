#include<stdio.h>
#include<stdlib.h>
#include<malloc.h>
typedef struct list{
	int data;
	struct list *next;
}node;
void sort(node **head){
	node *ptr,*min,*after;
	int temp;
	ptr=*head;
	min=*head;
	after=(*head)->next;
	while(ptr->next!=NULL){
		while(after!=NULL){
			if(min->data>after->data){
				temp=min->data;
				min->data=after->data;
				after->data=temp;
			}
			after=after->next;
		}
		ptr=ptr->next;
		min=ptr;
		after=min->next;
	}
}
void reverse(node **head){
	node *prev=NULL,*after=NULL,*cur=*head;
	while(cur!=NULL){
		after=cur->next;
		cur->next=prev;
		prev=cur;
		cur=after;
	}
	*head=prev;
}
void reverse1(node **head){
	node *ptr=*head,*prev;
	node *temp=*head;
	node *new=(node *)malloc(sizeof(node));
	*head=new;
	while(ptr->next!=NULL){
			while(temp!=NULL){
			prev=temp;	
			temp=temp->next;
		}
		new->data=prev->data;
		new=new->next;
		free(prev);
		temp=ptr;
	}
}
void append(node **head,int y){
	node *new=(node *)malloc(sizeof(node));
	node *last=(node *)malloc(sizeof(node));
	new->data=y;
	new->next=NULL;
	last=*head;
	if((*head)==NULL){
		*head=new;
		return;
	}
	while(last->next!=NULL){
		last=last->next;
	}
	last->next=new;
}

void delete(node **head,int y){
	node *prev=(node *)malloc(sizeof(node));
	node *after=(node *)malloc(sizeof(node));
	after=*head;
	if(after->data==y && after!=NULL){
		*head=after->next;
		free(after);
		return;
	}
	while(after!=NULL&&after->data!=y){
		prev=after;
		after=after->next;
	}
	if(after==NULL){
		return;
	}
	prev->next=after->next;
	free(after);
}
void max(node **head){
	int max=0,flag=0;
	node *ptr=*head,*prev,*after=*head;
	while(ptr!=NULL){
		if(max<(ptr->data))
			max=ptr->data;
		ptr=ptr->next;
	}
	printf("\n\n%d\n\n",max);
	while(after->next!=NULL&&flag!=2){
		if(after->data==max){
			flag++;
		}
		if(flag==2){
			break;
		}
		prev=after;
		after=after->next;
	}
	if(after->next==NULL){
		return;
	}
	printf("\n\n%d %d\n\n",prev->data,after->data);
	prev->next=after->next->next;
	free(after);
}
void printlist(node **head){
	node *ptr=*head;
	printf("\n\n\n\n");
	while(ptr!=NULL){
		printf("%d\n",ptr->data);
		ptr=ptr->next;

	}
}
int main(int argc, char const *argv[])
{
	int x,y;
	scanf("%d",&x);
	node *head=(node *)malloc(sizeof(node));
	node *temphead=(node *)malloc(sizeof(node));
	node *ptr=(node *)malloc(sizeof(node));
	head=NULL;
	for (int i = 0; i < x; ++i)
	{
		scanf("%d",&y);
		append(&head,y);
		append(&temphead,y);
	}
	//max(&head);
	reverse(&head);
	printlist(&head);
	sort(&head);
	printlist(&head);
	

	return 0;
}
