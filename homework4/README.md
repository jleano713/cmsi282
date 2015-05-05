#CMSI282: Homework 4
## Authors: Brian Ku, Janine Leano, Justin Sanny 

###Problems
1.) 4.2
(a) Draw a table showing the intermediate distance values of all the nodes at each iteration of the algorithm.
```
		0   1   2    3    4    5
	S | 0 | 0 | 0  | 0  | 0  | 0
	A | ∞ | 7 | 7  | 7  | 7  | 7
	B | ∞ | ∞ | 11 | 11 | 11 | 11
	C | ∞ | 6 | 5  | 5  | 5  | 5
	D | ∞ | ∞ | 8  | 7  | 7  | 7
	E | ∞ | 6 | 6  | 6  | 6  | 6
	F | ∞ | 5 | 4  | 4  | 4  | 4
	G | ∞ | ∞ | ∞  | 9  | 8  | 8
	H | ∞ | ∞ | 9  | 7  | 7  | 7
	I | ∞ | ∞ | ∞  | ∞  | 8  | 7
```
![Graph1](http://puu.sh/hzlC6/42ad2129cc.png)

2.) 4.8
Professor F. Lake suggests the following algorithm for finnding the shortest path from node s to node t in a directed graph with some negative edges: add a large constant to each edge weight so that all the weights become positive, then run Dijkstra's algorithm starting at node s, and return the shortest path found to node t.
Is this a valid method? Either prove that it works correctly, or give a counterexample.

Assume the graph above in 4.2a. We then add 10 to al the weights which makes all the weights postive. So in the orginal graph the shortest path with negative weights was S-A-B-H = 7, while the path S-E-H = 9. This would make S-A-B-H the shortest path. However in the modified positive graph, S-A-B-H = 37 while S-E-H = 29. Therefore S-E-H would be the shortest path, disproving Professor F. Lakes algortihm.

3.) 4.17 Suppose we want to run Dijkstra's algorithm on a graph whose edge weights are integers in the
range 0,1,..., W, where W is a relatively small number.
(a) Show how Dijkstra's algorithm can be made to run in time O(W|V| + |E|). I found an answer on the internet that helped me understand the problem and how to solve it. It is detailed and outlined beneath.
http://www.ece.northwestern.edu/~dda902/336/hw5-sol.pdf
![4.17](http://puu.sh/hBlY6/6798164621.png)

4.) 5.2
(a) Run Prim's algorithm; whenever there is a choice of nodes, always use alphabetic ordering (e.g., start from node A). Draw a table showing the intermediate values of the cost array.
```
	Vertex | Cost
	A  		 0
	B  		 1
	C  		 3
	D  		 6
	E  		 12
	F  		 7
	G  		 5
	H 		 8
```
![graph2](http://puu.sh/hzn9Y/83f748f033.png)

(b) Run Kruskal's algorithm on the same graph. Show how the disjoint-sets data structure looks at every intermediate stage (including the structure of the directed trees), assuming path compression is used.

![graph3](http://puu.sh/hzntS/7e98f2218b.png)

![graph4](http://puu.sh/hzplf/a95dafe424.png)
![graph5](http://puu.sh/hzpi6/3c5a272c0a.png)

5.) Write a function in Python or Julia or JavaScript or Java that uses dynamic programming to determine whether a numeric list has a subset of elements that sums to a given value. 
```Python
def sum_of_subset(lst,target):
    lst.sort()
    length = len(lst)+1
    target +=1
    subset = [[0 for i in xrange(length)] for j in xrange(target)]
    for i in xrange(length):
        subset[0][i] = True
    for i in xrange(1,target):
        subset[i][0] = False
    for i in xrange(1,target):
        for j in xrange(1,length):
            subset[i][j] = subset[i][j-1]
            if (i >= lst[j-1] and lst[j-1] >= 0):
                subset[i][j] = subset[i][j] or subset[i-lst[j-1]][j-1]
    return subset[target-1][length-1]
```

6.)
```Java
CURRENTLY UNFINISHED
ORIGINAL AUTHOR/ALL THE CREDIT GOES TO: KELLY SUTTON
https://code.google.com/p/ksutton/source/browse/trunk/cmsi282/hw4/edu/lmu/cs/ksutton/hw4/?r=349
package algorithms.homework4;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Stack;

import org.junit.Assert;

public class SchoolSolver {

        /**
         * hasStoodNextTo is a table of past standings-next-to. A true value at
         * hasStoodNextTo[i][j]indicates that schoolgirl number i has stood next to
         * schoolgirl j.
         * 
         * hasStoodNextTo[i][j] == hasStoodNextTo[j][i]
         */
        protected static boolean[][] hasStoodNextTo;

        /**
         * usedToday is an array of booleans that keeps track of whether or not the
         * girl has already been placed in a slot for the day.
         */
        protected static boolean[] usedToday;

        /**
         * rows is quite simply the organization of schoolgirls into their
         * respective rows.
         * 
         * rows[i][j] represents the the ith row at position j. (i = {0, 1, 2, 3, 4}
         * and j = {0, 1, 2})
         */
        // private static RowStack rows;
        /**
         * The week object is a stack of stacks of stacks. Each week holds its own
         * days which then holds in own rows stack. The stacks inside a stack make
         * it easy to backtrack.
         */

        private static WeekStack week = new WeekStack();

        private static int nodes = 0;

        private static final int DAYS = 7;

        private static final int NUM_GIRLS = 15;

        private static final int NUM_ROWS = 5;

        private static final int NUM_GIRLS_IN_A_ROW = 3;

        public static void main(String[] args) {

                hasStoodNextTo = fillMatrixWithFalse();

                boolean dayFailed = false;

                while (week.size() < DAYS) { // 7 days

                        // Add a new empty RowStack to our DayStack
                        week.push(new DayStack(NUM_GIRLS));

                        DayStack currentDay = week.peek();
                        SchoolgirlQueue girlQueue = currentDay.getSchoolgirlQueue();
                        while (currentDay.size() < NUM_ROWS) { // 5 rows

                                // we need to pop back
                                // this should be rare or should never happen
                                if (dayFailed) {
                                        week.pop();
                                        week.peek().peek().pop();
                                        week.peek().peek().add(
                                                        week.peek().getSchoolgirlQueue().dequeue());

                                        dayFailed = false;
                                        break;
                                }

                                // try to add three schoolgirls
                                // days.peek().push(tryToAddNewRow(new Integer[] { 0, 1, 2 }));

                                currentDay.push(new RowStack());

                                RowStack currentRow = currentDay.peek();

                                while (currentRow.size() < NUM_GIRLS_IN_A_ROW) { // 3 girls
                                        // to a row

                                        // we've already been through the girls once
                                        if (girlQueue.getFlag() == true) {

                                                // the current row is no good
                                                if (currentDay.size() == 1) {
                                                        dayFailed = true;
                                                }

                                                girlQueue.enqueue(currentDay.pop());

                                                // step one back one row and pop
                                                girlQueue.enqueue(currentDay.peek().pop());

                                                // when we break, we'll reset the currentRow and try to
                                                // add the next girl in the queue. Hopefully we can
                                                // avoid
                                                // a freak bug where we get caught in an infinite loop
                                                break;
                                        }

                                        currentRow.push(girlQueue.dequeue());

                                        if (isRowOkay(currentRow)) { // march on
                                                girlQueue.setFlag(false);

                                                if (currentRow.size() == NUM_GIRLS_IN_A_ROW)
                                                        break;
                                        }

                                        else { // pop off and try adding the next
                                                Schoolgirl popped = currentRow.pop();
                                                eraseAdjacents(currentRow, popped);
                                                girlQueue.enqueue(popped);
                                        }
                                }

                                // addAdjacents(currentRow, currentRow.peek()); //our day checks
                                // out
                                addAdjacents(currentRow);
                        }
                        // usedToday = returnArrayFullOfFalse(15);
                }

                System.out.println(week);
        }

        private static boolean[][] fillMatrixWithFalse() {
                boolean[][] tmp = new boolean[15][15];

                for (int i = 0; i < tmp.length; i++) {
                        for (int j = 0; j < tmp[i].length; j++) {
                                tmp[i][j] = false;
                        }
                }

                return tmp;
        }

        private static boolean[] returnArrayFullOfFalse(int size) {
                boolean[] tmp = new boolean[size];

                for (int i = 0; i < tmp.length; i++)
                        tmp[i] = false;

                return tmp;
        }

        /**
         * This messy private helper method returns whether or not r is a valid row
         * 
         * @param r
         * @return
         */
        private static boolean isRowOkay(RowStack r) {

                if (r.size() == 3) {
                        if (hasStoodNextTo[r.elementAt(0).getIndex()][r.elementAt(1)
                                        .getIndex()]
                                        || hasStoodNextTo[r.elementAt(1).getIndex()][r.elementAt(2)
                                                        .getIndex()]
                                        || hasStoodNextTo[r.elementAt(0).getIndex()][r.elementAt(2)
                                                        .getIndex()])
                                return false;
                }

                else if (r.size() == 2) {
                        if (hasStoodNextTo[r.elementAt(0).getIndex()][r.elementAt(1)
                                        .getIndex()]
                                        || hasStoodNextTo[r.elementAt(1).getIndex()][r.elementAt(0)
                                                        .getIndex()])
                                return false;
                }

                return true;
        }

        /**
         * addAdjacents updates the hasStoodNextTo table with the appropriate values
         * 
         * @param r
         *            the row to add
         * @param girl
         *            the Schoolgirl to be added
         */
        public static void addAdjacents(RowStack r, Schoolgirl girl) {

                // this nastiness logs the students walking next to each other
                for (Object o : r.toArray()) {
                        Schoolgirl s;
                        if (o instanceof Schoolgirl)
                                s = (Schoolgirl) o;

                        else
                                throw new IllegalArgumentException();
                        // TODO what type of exception should this be?
                        SchoolSolver.hasStoodNextTo[girl.getIndex()][s.getIndex()] = true;
                        SchoolSolver.hasStoodNextTo[s.getIndex()][girl.getIndex()] = true;
                }
        }

        /**
         * Updates the hasStoodNextTo table with the an entire row's Schoolgirls
         * 
         * @param r
         *            A Row
         */
        public static void addAdjacents(RowStack r) {

                assert (r.size() == 3);

                for (Object o : r.toArray()) {
                        Schoolgirl s;
                        if (o instanceof Schoolgirl)
                                s = (Schoolgirl) o;

                        else
                                throw new IllegalArgumentException();

                        addAdjacents(r, s);
                }
        }

        /**
         * Flips the values to false for the corresponding cells in hasStoodNextTo
         * 
         * @param r
         *            Row to remove
         * @param girl
         *            The Schoolgirl to remove
         */
        public static void eraseAdjacents(RowStack r, Schoolgirl girl) {

                // this nastiness undoes addAdjacents
                for (Object o : r.toArray()) {

                        Schoolgirl s;
                        if (o instanceof Schoolgirl)
                                s = (Schoolgirl) o;
                        else
                                throw new IllegalArgumentException();
                        // TODO what type of exception should this be?

                        SchoolSolver.hasStoodNextTo[girl.getIndex()][s.getIndex()] = false;
                        SchoolSolver.hasStoodNextTo[s.getIndex()][girl.getIndex()] = false;
                }
        }
}

```