public class Parser {
    
    public static int parseInt(String numStr) {
        String[] StrArray = numStr.split("[\\s+-]");
        int finalNumber = 0;
        boolean saidMillion = false;
        boolean saidThousand = false;
      
        for (String word : StrArray ){
          System.out.println(word);
        }
        for (String word : StrArray) {
            if(word.equals("hundred")){
              if(saidMillion || saidThousand){
                int pushUp = finalNumber % 10;
                finalNumber -= pushUp;
                finalNumber += 100 * pushUp;
              }
              else{
                finalNumber *= 100;
              }
            }
            if(word.equals("thousand")){
              if(saidMillion){
                int pushUp = finalNumber % 1000;
                finalNumber -= pushUp;
                finalNumber += 1000 * pushUp;
              }
              else{
                finalNumber *= 1000;
              }
              saidThousand = true;
            }
          
            switch(word)
            {
                case "one":finalNumber++;break;
                case "two":finalNumber += 2;break;
                case "three":finalNumber += 3;break;
                case "four":finalNumber += 4;break;
                case "five":finalNumber += 5;break;
                case "six":finalNumber += 6;break;
                case "seven":finalNumber += 7;break;
                case "eight":finalNumber += 8;break;
                case "nine":finalNumber += 9;break;
                case "ten":finalNumber += 10;break;
                case "eleven":finalNumber += 11;break;
                case "twelve":finalNumber += 12;break;
                case "thirteen":finalNumber += 13;break;
                case "fourteen":finalNumber += 14;break;
                case "fifteen":finalNumber += 15;break;
                case "sixteen":finalNumber += 16;break;
                case "seventeen":finalNumber += 17;break;
                case "eighteen":finalNumber += 18;break;
                case "nineteen":finalNumber += 19;break;
                case "twenty":finalNumber += 20;break;
                case "thirty":finalNumber += 30;break;
                case "forty":finalNumber += 40;break;
                case "fifty":finalNumber += 50;break;
                case "sixty":finalNumber += 60;break;
                case "seventy":finalNumber += 70;break;
                case "eighty":finalNumber += 80;break;
                case "ninety":finalNumber += 90;break;
                case "million":finalNumber *= 1000000;saidMillion=true;break;
            }
        }
        return finalNumber;
    }
}
