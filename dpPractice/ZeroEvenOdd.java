package numsolitairek;

import java.util.concurrent.Semaphore;
import java.util.function.IntConsumer;

public class ZeroEvenOdd {

    private int n;
    private Semaphore zero, odd, even;

    public ZeroEvenOdd(int n) {
        this.n = n;
        this.zero = new Semaphore(1);
        this.even = new Semaphore(0);
        this.odd = new Semaphore(0);
    }

    public void zero(IntConsumer printNumber) throws InterruptedException {
        int localn = this.n;
        for (int i = 0; i < localn; ++i) {
            zero.acquire();
            printNumber.accept(0);
            // Note that this is because of the order, and not 'i' (that is why odd() is released)
            if (i % 2 == 0) {
                odd.release();
            } else {
                even.release();
            }
        }
    }

    public void even(IntConsumer printNumber) throws InterruptedException {
        int localn = this.n;
        for (int i = 2; i <= localn; i += 2) {
            even.acquire();
            printNumber.accept(i);
            zero.release();
        }

    }

    public void odd(IntConsumer printNumber) throws InterruptedException {
        int localn = this.n;
        for (int i = 1; i <= localn; i += 2) {
            odd.acquire();
            printNumber.accept(i);
            zero.release();
        }
    }
}