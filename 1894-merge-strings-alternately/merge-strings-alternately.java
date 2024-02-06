class Solution {
    public String mergeAlternately(String word1, String word2) {
        StringBuilder result = new StringBuilder();

        int p1 = 0;
        int p2 = 0;

        while (p1 < word1.length() && p2 < word2.length()) {

            result.append(word1.charAt(p1));
            p1++;

            result.append(word2.charAt(p2));
            p2++;
        }

        if (p1 < word1.length()) {
            result.append(word1.substring(p1));
        }

        if (p2 < word2.length()) {
            result.append(word2.substring(p2));
        }
        return String.valueOf(result);
    }
}