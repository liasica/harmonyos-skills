---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-threading-model-new-000001
title: 多线程消费场景中while循环加锁及wait_for的作用
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > ArkTS线程模型和并发 > 多线程消费场景中while循环加锁及wait_for的作用
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:54+08:00
doc_updated_at: 2026-07-22
content_hash: sha256:0ae161c321e5be1152efb3ee7aed32349b4b617a9785c46428be409f031c5c54
---

## 问题现象

在多线程消费场景中，使用while循环、加锁、再调用wait\_for(lock, std::chrono::seconds(1))的三层嵌套结构为何要这样写？每层的作用是什么？

完整代码示例：

```cpp
#include <iostream>
#include <queue>
#include <mutex>
#include <condition_variable>
#include <chrono>
#include <thread>

std::queue<int> bufferQueue;
std::mutex mtx;
std::condition_variable cond;
bool finished = false;

// 编码器回调线程（生产者）
void callbackThread() {
    for (int i = 0; i < 10; i++) {
        std::this_thread::sleep_for(std::chrono::milliseconds(100));
        std::unique_lock<std::mutex> lock(mtx);
        bufferQueue.push(i);
        cond.notify_one();
    }
    std::unique_lock<std::mutex> lock(mtx);
    finished = true;
    cond.notify_one();
}

// 喂入线程（消费者）
void feedThread() {
    while (true) {
        std::unique_lock<std::mutex> lock(mtx);
        cond.wait_for(lock, std::chrono::seconds(1), [] {
            return !bufferQueue.empty() || finished;
        });
        if (finished && bufferQueue.empty()) {
            break;
        }
        if (!bufferQueue.empty()) {
            int buffer = bufferQueue.front();
            bufferQueue.pop();
            lock.unlock();
            // 处理buffer，填入数据，推给编码器
            std::cout << "Processing buffer: " << buffer << std::endl;
        }
    }
}

int main() {
    std::thread cb(callbackThread);
    std::thread ft(feedThread);
    cb.join();
    ft.join();
    return 0;
}
```

## 解决方案

这段代码的三层嵌套是一个经典的条件变量消费者模式，每一层都有不可替代的作用：

1. **第1层：while (true)循环**

   喂入线程是一个长期运行的工作线程，需要持续不断地从队列中取出buffer、填入数据、推给编码器，直到文件读完发送EOS才退出。如果没有while循环，线程只处理一次就会结束。
2. **第2层：unique\_lock lock(mutex)加锁**

   用于保护喂入线程和编码器回调线程并发访问的共享队列。每次循环重新加锁的原因是：unique\_lock在作用域结束或执行continue时会自动释放锁。释放锁后，编码器回调线程才有机会获取锁来push新buffer。如果一直持有锁，回调线程始终无法push，队列始终为空，会形成死锁。
3. **第3层：cond.wait\_for(lock, 1s)等待**

   喂入线程作为消费者，依赖编码器回调线程生产buffer。当队列为空时，喂入线程无事可做，必须等待回调提供新的buffer。wait\_for会释放锁并阻塞线程（让出CPU，防止CPU空转），等待notify或超时后会重新获取锁并唤醒线程，防止永久阻塞。
