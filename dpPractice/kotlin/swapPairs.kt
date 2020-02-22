/**
 * A node for the list that is to be used .
 */
class ListNode(var `val` : Int ) {
    var next: ListNode? = null
}

/**
 * Simple swap pairs of pointers. So simple, but so easily confusing!
 */
class SolutionSwapPointers {

    fun swapPairs(head: ListNode?): ListNode? {
        var start = ListNode(0)
        start.next = head
        var current : ListNode? = start

        while (current != null) {

            val tempNext = current.next
            val tempNextNext = current.next?.next

            current?.next = current.next?.next
            tempNext?.next = tempNextNext?.next
            current?.next?.next = tempNext

            current = current?.next?.next
        }
        return start.next
    }
}

/**
 * Swap values instead
 */
class SolutionSwapValues {
    fun swapPairs(head: ListNode?): ListNode? {
        var current = head
        while (current?.next != null) {
            val temp = current.`val`
            val nextNode = current.next
            current.`val` = nextNode!!.`val`
            nextNode!!.`val` = temp
            current = nextNode.next
        }
        return head
    }
}