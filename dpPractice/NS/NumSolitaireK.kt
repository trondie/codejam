package numsolitairek

class NumSolitaireK {

companion object {
    
    fun solution(A: IntArray): Int {

            val dpTable = IntArray(A.size)
            dpTable[0] = A[0]

            /**
             * Building up from 1, ... , n - 1
             */
            for (i in 1 until A.size) {
                // Tracker
                var maxValue = Integer.MIN_VALUE
                // Die throws for each index
                for (dieThrow in 1..6) {
                    if (0 <= i - dieThrow) {
                        maxValue = Math.max(dpTable[i - dieThrow] + A[i], maxValue)
                    }
                }
                dpTable[i] = maxValue
            }

            /**
             * The "up" result
             */
            return dpTable[A.size - 1]
        }
    }
}