
class Main { 
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        StringBuilder concatenatedSentences = new StringBuilder();

        System.out.println("Enter sentences to concatenate (type 'exit' to finish):");

        while (true) {
            String input = scanner.nextLine();
            if (input.equalsIgnoreCase("exit")) {
                break;
            }
            concatenatedSentences.append(input).append(" ");
        }

        System.out.println("Concatenated Sentences:");
        System.out.println(concatenatedSentences.toString().trim());
    }
}