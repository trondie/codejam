#pragma once
#include <condition_variable>
#include <mutex>
#include <thread>
#include <iostream>

using namespace std; 

/**
 * Semaphore for order
 */ 
class Semaphore {

    /**
     * Holds lock on 0
     */ 
	size_t available;

    /**
     * Mutex that is going to block on 
     */ 
	std::mutex internalMutex;

    /**
     * Our condition will be : 0 -> AQUIRED, 1 -> RELEASED
     */ 
	std::condition_variable conditionVariable;

public:

	explicit Semaphore(size_t available = 1) : available(available) { }

	void acquire() {
		std::unique_lock<std::mutex> lock(internalMutex);
		conditionVariable.wait(lock, [this] { return this->available > 0; } );
		available--;
		lock.unlock();
	}

	void release() {
		internalMutex.lock();
		available++;
		internalMutex.unlock();
		conditionVariable.notify_one();
	}

	size_t getAvailable() const {
		return available;
	}
};

class Foo {
    Semaphore r, s;
public:
    Foo() : s(0), s(0) {}

    void first(std::function<void()> printFirst) {
        printFirst();
        r.release();
    }

    void second(std::function<void()> printSecond) {
        r.acquire();
        printSecond();
        s.release();
    }

    void third(std::function<void()> printThird) {
        s.acquire();
        printThird();

    }
};

int main() {
    Foo * foo = new Foo();
    
}