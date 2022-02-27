/*Academic Declaration
 * I have read and understood the sections of plagiarism in the College Policy
on Assessment Offences and confirm that the work is my own, with the
work of others clearly acknowledged. I give my permission to submit my
report to the plagiarism testing database that the College is using and test
it using plagiarism detection software, search engines or meta- searching software.
Maksims Frederiks Saldajevs 22 Feb 2022”*/
import java.util.Arrays;
public class ArrayExercises{
    public static void main(String [] args){
    String[] sampArr={"aa", "bb", "bb", "cc", "cc", "dd", "ee"}; 
    System.out.println(Arrays.toString(multiplesOnly(sampArr)));
    }
    public static String [] multiplesOnly(String [] arr){
    int size = arr.length - getNewSize(arr);
    String[] result = new String[size];
    int newArrCurrIndex=0;
    for(int i=0; i<arr.length;i++){
        if(isDupl(arr[i],arr,i)){
            result[newArrCurrIndex]=arr[i];
            newArrCurrIndex++;
        }

    }
    return result; 
    }
    public static int getNewSize(String [] a){
        int count= 0;
        for(int i = 0;i<a.length; i++){
            count++;
            for(int e = 0;e<a.length; e++){
                if(a[i].equals(a[e])){   
                    if(i!=e){
                        count--;
                        /*Below is an alternative to a break statement
                        which has not been covered yet in the lectures.*/
                        e=a.length; 
                    }

                }
            }
            if(count<0)count=0;
        }
        return count;
    }
    public static boolean isDupl(String element, String [] arr, int index){
        for(int i=0;i<arr.length; i++){
            if(i!=index){
                if(arr[i].equals(element))return true;
            }
        }
        return false; 
    }
}