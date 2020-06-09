class Apple_coding{
    public static void main(String[] args) {
        
        int a[][]={ {1,1,1},
                    {1,0,1},
                    {1,1,1}
                            };
            for(int i=0;i<a.length;i++){
                for(int j=0;j<a[0].length;j++)
                    System.out.print(a[i][j]+"\t");
                System.out.println();
                            }

        for(int i=0;i<a.length;i++){
            for(int j=0;j<a[0].length;j++){

                if(a[i][j]==0){
                    for(int k=0;k<a[0].length;k++)
                    a[i][k]=3;
                    for(int k=0;k<a.length;k++)
                    a[k][j]=3;
                                }
            }
        }

        System.out.println("----------------------------");
        for(int i=0;i<a.length;i++){
            for(int j=0;j<a[0].length;j++){
                if(a[i][j]==3)
                System.out.print(0+"\t");
                else
                System.out.print(1+"\t");
            }
                System.out.println();
        }


        

    }
}