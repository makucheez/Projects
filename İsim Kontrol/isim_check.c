#include <stdio.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>

#include <string.h>
using namespace std;

int main(int argc, const char * argv[]) {
    
    label1:
        char isim[30];
        
    std::cout<<"isim giriniz"<<endl;
        
        cin>>isim;
        
        
        for(int i = 0 ; i <= 30 ; i++){
            
            if(isdigit(isim[i])==0 ){
                
            }else{
                printf("hata yaptiniz tekrar gir tekrar denemek icin e tusuna basiniz...\n");
                getch();
                system("cls");
                goto label1;
            }
        }
        
        cout<<isim<<endl;
        
        return 0;
        
    }
}