/**
 * LCS for 1..n longest common substrings, Quadratic time & space.
 */
fun lcs(A : String, B : String): String {

    val dpTable : Array<Array<String>> = Array(A.length + 1) { Array(B.length + 1) { "" } }

    (1..A.length).forEach { i ->
        (1..B.length).forEach { j ->
            if (A[i - 1] == B[j - 1]) {
                dpTable[i][j] = dpTable[i - 1][j - 1] + A[i - 1]
            } else {
                dpTable[i][j] = setOf(dpTable[i][j - 1], dpTable[i - 1][j]).maxBy { it.length }!!
            }
        }
    }
    return dpTable[A.length][B.length]
}

