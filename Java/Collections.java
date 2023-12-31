import java.util.*;

public class Collections {
    /**
     * @param args
     */
    public static void main(String args[]) {
        /*ArrayList */
        ArrayList<String> list=new ArrayList<String>();//Creating arraylist
        list.add("Ravi");//Adding object in arraylist
        list.add("Ravi");  
        list.add("Ajay");
        //Traversing list through Iterator  
        Iterator<String> itr=list.iterator();  
        while(itr.hasNext()){  
            System.out.println(itr.next());  
        }

        /*LinkedList */
        LinkedList<String> al=new LinkedList<String>();  
        al.add("Ravi");  
        al.add("Vijay");  
        al.add("Ravi");  
        al.add("Ajay");  
        Iterator<String> itr1=al.iterator();  
        while(itr1.hasNext()){  
            System.out.println(itr.next());  
        }

        /* Other data structures
         * Vector
         * Stack - lifo
         * Queue Interface PQ - fifo
         * PriorityQueue
         * ArrayDeque - remove and add elements on both sides
         * HashSet
         * LinkedHashSet
         * HashMap
         * 
         */
    }
    
}
