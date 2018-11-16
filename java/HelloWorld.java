public class HelloWorld {

    public static void main(String[] args) {
    	String[] bob = {"i","am","super","duper","coolio"};
    	String coolio = "";
    	for (String item: bob){
    		coolio =  coolio + item + " ";
    	}
    	System.out.println(coolio);
    }

}