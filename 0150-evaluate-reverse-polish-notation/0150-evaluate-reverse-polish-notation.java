class Solution {
    public int evalRPN(String[] tokens) {
        Stack<Integer> stk = new Stack<>();
        for(String i:tokens){
            if (i.equals("+")){
                int eval = stk.pop() + stk.pop();
                stk.push(eval);
            }else if(i.equals("-")){
                int eval = (stk.pop() - stk.pop())*(-1);
                stk.push(eval);
            }else if(i.equals("*")){
                int eval = stk.pop() * stk.pop();
                stk.push(eval);
            }else if(i.equals("/")){
                int a = stk.pop();
                int b = stk.pop();
                int eval = b/a;
                stk.push(eval);
            }else{
                int val = Integer.parseInt(i);
                stk.push(val);
            }
        }
        return stk.pop();
    }
}