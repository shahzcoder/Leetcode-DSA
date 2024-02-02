class Solution {
    public boolean divisorGame(int n) {
        if (n%2 == 0) {
            n = n - 1;
            return true;
        }
        return false;
    }
}