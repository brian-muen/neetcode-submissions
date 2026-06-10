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
    public void reorderList(ListNode head) {
        ListNode slow = head;
        ListNode fast = head.next;

        while (fast != null && fast.next != null) {
            fast = fast.next.next;
            slow = slow.next;
        }

        ListNode mid = new ListNode();

        mid = slow.next;
        slow.next = null;

        ListNode prev = null;

        while (mid != null) {
            ListNode temp = mid.next;
            mid.next = prev;
            prev = mid;
            mid = temp;
        }

        while (prev != null) {
            ListNode temp1 = head.next;
            ListNode temp2 = prev.next;
            head.next = prev;
            prev.next = temp1; 
            head = temp1;
            prev = temp2;
        }
    }
}
