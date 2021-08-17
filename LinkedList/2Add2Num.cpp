// idea: to find the longer number first, so we can do this addition in-place without extra space
// for each node, we just need to add their values and if their digit sum is greater than 10, we take the carry in consideration to the next node

class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        // find the length of those 2 numbers
        int s1 = getSize(l1);
        int s2 = getSize(l2);
        if (s1 < s2)
        {
            // we would always use l1 to store the final answer, so make sure l1 points to the longer number
            ListNode* t = l1;
            l1 = l2;
            l2 = t;
        }
        bool carry = false;
        ListNode* head = new ListNode(); // just a dummy node
        ListNode* temp = head;
        head->next = l1;
        while(l1 || l2)
        {
                l1->val += l2? l2->val : 0; // this line will take care of the situtation when the shorter number ran out
                if(carry) l1->val ++;
                if(l1->val >= 10)
                {
                    carry = true;
                    l1->val -= 10;
                }
                else carry = false;
                temp = l1; // temp is used to store the node previous to the current node
                if(l1)
                    l1 = l1->next;
                if(l2)
                    l2 = l2->next;
        }
     
        if(carry){
            temp->next = new ListNode(1); // take consideration of the last digit
        }
        return head->next;
    }
    // trivial function to get the length of the linked list
    int getSize(ListNode* n)
    {
        int count = 0;
        while(n)
        {
            n = n->next;
            count ++;
        }
        return count;
    }
};
