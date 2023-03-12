#include <stdio.h>
#include <conio.h>
int ht[10], i, found = 0, key;
void insert_val();
void search_val();
void delete_val();
void display();
int main()
{
int option;
clrscr();
for ( i = 0;i < 10;i++ ) //to initialize every element as ‘–1’
ht[i] = –1;
do
{
printf( "\n MENU \n1.Insert \n2.Search \n3.Delete \n4.Display \n5.Exit");
printf( "\n Enter your option.");
scanf( "%d", &option);
switch (option)
{
case 1:
insert_val();
break;
case 2:
search_val();
break;
case 3:
delete_val();
break;
case 4:
display();
break;
default:
printf( "\nInvalid choice entry!!!\n" );
break;
}
}while (option!=5);
getch();
return 0;
}
void insert_val()
{
int val, f = 0;
printf( "\nEnter the element to be inserted : " );
scanf( "%d", &val );
key = ( val % 10 ) – 1;
if ( ht[key] == –1 )
{
ht[key] = val;
}
else
{
if ( key < 9 )
{
for ( i = key + 1;i < 10;i++ )
{
if ( ht[i] == –1 )
{
ht[i] = val;
break;
}
}
}
for ( i = 0;i < key;i++ )
{
if ( ht[i] == –1 )
{
ht[i] = val;
break;
}
}
}
}
void display()
{
for (i = 0;i < 10;i++)
printf( "\t%d", ht[ i ] );
}
void search_val()
{
int val, flag = 0;
printf( "\nEnter the element to be searched :: " );
scanf( "%d", &val );
key = ( val % 10 ) – 1;
if ( ht[ key ] == val )
flag = 1;
else
{
for (i = key + 1;i < 10;i++)
{
if(ht[i] == val)
{
flag = 1;
key = i;
break;
}
}
}
if (flag == 0)
{
for (i = 0;i < key;i++)
{
if (ht[ i ] == val)
{
flag = 1;
key = i;
break;
}
}
}
if (flag == 1)
{
found=1;
printf("\n The item searched was found at position %d !", key + 1 );
}
else
{
key = -1;
printf( "\nThe item searched was not found in the hash table" );
}
}
void delete_val()
{
search_val();
if (found==1)
{
if ( key != –1 )
{
printf( "\nThe element deleted is %d ", ht[ key ] );
ht[ key ] = –1;
}
}
}