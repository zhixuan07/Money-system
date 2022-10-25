
#include <iostream>
using namespace std;

double TempAvg(double *,int);
void Sorted(double*,int);


int main()
{
    int size,i;
    double *ptr;

    double avg=0.0;

    cout <<"enter how many number of temperature"<< endl;
    cin >> size;

    if(ptr==NULL)
    {
    cout <<"cant create:\n";
    }
    ptr=new double[size];

    for(i=0;i<size;i++)
    {

    cout <<"\nenter test score of student "<< i+1 <<":";
    cin >> *(ptr+i);
    }
    Sorted(ptr,size);

    avg=TempAvg(ptr,size);
    cout <<"test score in ascending order:/n";

    for(i=0;i<size;i++)
    {
    cout <<ptr[i] <<endl;
    }
    cout <<"avg test score= "<<avg<<endl;
    delete [] ptr;
    return 0;
}

double TempAvg(double*array,int size)
{
    double sum=0;
    for(int i=0;i<size;i++)
    {
        sum+=array[i];
    }
    cout <<"avg="<<sum/(double)size<<endl;

    sum=sum/((double)size);
    return sum;
}

void Sorted(double* ptr,int size)
{
    double mainnum;
    int i=0,j,mainindex;

    for(i=0;i<size;i++)
    {
    mainindex=i;
    mainnum=ptr[i];
    for(j=i+1;j<size;j++)
    {
    if(ptr[j]>mainnum)
    {
    mainnum=ptr[j];
    mainindex=j;
    }
    }
    ptr[mainindex]=ptr[i];
    ptr[i]=mainnum;
    }
}

