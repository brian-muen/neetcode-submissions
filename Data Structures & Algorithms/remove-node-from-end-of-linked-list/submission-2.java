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
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode prev = null;
        while (head != null) {
            ListNode temp = head.next;
            head.next = prev;
            prev = head;
            head = temp;
        }

        head = prev; 
        prev = null;
        ListNode tracker = head;

        int index = 1;
        if (index == n) {
            head = head.next;
        }

        while (head != null) {
            if (index == n - 1) head.next = head.next.next;
            ListNode temp = head.next;
            head.next = prev;
            prev = head;
            head = temp;
            index++;
        }

        return prev;
    }
}
