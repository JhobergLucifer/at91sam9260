

#define MAX_PATH 3
int convrs[8]={0,0,0,0,0,0,0,0};
//int xn[]={1,2,1};
//int hn[]={1,0,2};

int xn[5]={-2,2,0,-1,1};
int hn[4]={-1,3,-1,-2};


int conv(int top1,int x[],int top2,int h[]);  


int main()
{
  int i;

  printf("[]%d #[]%d #[]%d \n",convrs[0],xn[0],hn[0]);

  conv(5,xn,4,hn);
  for(i=0;i<=8;i++)
    printf("%d ,",convrs[i]);
}




int conv(int top1,int x[],int top2,int h[])
{

int xi=0,topcv=0,hi=0;
printf("top1 %d ,top2 %d \n",top1,top2);
 for(xi=top1-1;xi>=0;xi--)
   {
     topcv=(top1-1)-xi;
     for(hi=top2-1;hi>=0;hi--)
       {
	 convrs[topcv]=(convrs[topcv]+x[xi]*h[hi]);
	 printf("yn:[%d]%d #xn:[%d]%d #hn:[%d]%d \n",topcv,convrs[topcv],xi,xn[xi],hi,hn[hi]);
	 topcv++;
       }
   }
 return 0;
}
