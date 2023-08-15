/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode partition(ListNode head, int x) {
        ListNode cur = head;
        ListNode prev = head;
        
        if(cur==null){
            return head;
        }
        
        ListNode endNode=null;
        ListNode gtNode=null;
        while(cur!=null){
            if(cur.val>=x){
                endNode = prev;
                gtNode = cur;
                break;
            }
            prev = cur;
            cur = cur.next;
        }
        
        cur = gtNode;
        prev = endNode;
        
        while(cur!=null){
            if(cur.val<x){
            prev.next = cur.next;
            if(endNode==gtNode){
                cur.next = gtNode;
                head = cur;
            }else{
                endNode.next = cur;
                cur.next = gtNode;
            }
            endNode = cur;
            cur = prev.next;
        }
        else if(cur!=null){
            prev = cur;
            cur = cur.next;
        }
            
        }
        
        return head;
    }
}