public class Basic_Linked_List {
    Node head;

    public void insert(int element) {
        Node node = new Node();
        node.element = element;
        node.next = null;

        if (head == null) {
            head = node;
        } else {
            Node n = head;
            while (n.next != null) { // as long as the pointer to the next node is not null, keep looping
                n = n.next;
            }
            n.next = node;
        }

    }

    public void show() {

        Node node = head;
        while (node.next != null) {
            System.out.println(node.element);
            node = node.next;
        }
        System.out.println(node.element); // printing the last element after the loop
    }

}