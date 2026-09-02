---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-stability-address-sanitizer-opt
title: 地址越界类问题优化建议
breadcrumb: 最佳实践 > 稳定性 > 稳定性优化 > 地址越界类问题优化建议
category: best-practices
scraped_at: 2026-09-02T15:03:24+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:b324611365057552663f65cffedb68496dcd0fc88495c97619931f3fc2d97c46
---

## 优化建议1：增加返回值校验

在正常情况下，napi\_get\_value\_string\_utf8接口会在字符串末尾添加\0结束符；但若发生异常（如参数非法或类型不符），该接口会提前返回，导致缓冲区未被写入任何内容，也不会添加结束符。这可能导致申请的内存与实际使用不一致，从而引发越界错误。

```cpp
static std::string GetStringParam1(napi_env env, napi_value arg)
{
    size_t size;
    napi_get_value_string_utf8(env, arg, nullptr, 0, &size);
    size_t str_size = size + 1;
    char *buf = new char[str_size];
    napi_get_value_string_utf8(env, arg, buf, str_size, nullptr); // 未进行校验
    std::string str(buf);
    delete[] buf;
    return str;
}
```

建议：增加返回值校验。

```cpp
static std::string GetStringParam2(napi_env env, napi_value arg)
{
    size_t size;
    // 增加校验
    if (napi_get_value_string_utf8(env, arg, nullptr, 0, &size) != napi_ok || size == 0) {
        return "";
    }
    size_t str_size = size + 1;
    char *buf = new char[str_size];
    // 增加校验
    if (napi_get_value_string_utf8(env, arg, buf, str_size, nullptr) != napi_ok) {
        delete[] buf;
        return "";
    }
    std::string str(buf);
    delete[] buf;
    return str;
}
```

## 优化建议2：异步任务传递this引用

当一个lambda表达式不止在局部作用域中使用，而是被传递到外部函数或另一个线程中时，禁止按引用（&）捕获局部变量（包括 this）。lambda按引用捕获就是把局部对象的引用存储起来，如果lambda的生命周期会超过局部变量生命周期，则可能导致内存不安全。

```cpp
class Task1 {
public:
    void Start() {
        std::thread([this]() {
            std::this_thread::sleep_for(std::chrono::milliseconds(100));
            DoWork(); // 如果 Task 已析构，这里是悬空调用
        }).detach();
    }

    void DoWork() {
        std::cout << "Doing work\n";
    }

    ~Task1() {
        std::cout << "Task destructed\n";
    }
};

void Run() {
    Task1* task = new Task1();
    task->Start();
    delete task; // 析构发生在 lambda 执行前
    std::this_thread::sleep_for(std::chrono::milliseconds(1));
}
```

建议：

1. 异步或跨线程场景中禁止使用[&]捕获局部变量或this
2. 采用智能指针管理对象生命周期结合weak\_from\_this获取弱指针，保证对象在访问时仍然有效。

实现步骤：

1. 对象要从std::enable\_shared\_from\_this继承。

   ```cpp
   class Task2 : public std::enable_shared_from_this<Task2> {
   ```
2. 采用智能指针初始化对象。

   ```cpp
   auto task = std::make_shared<Task2>();
   ```
3. lambda表达式中调用weak\_from\_this捕获this。

   ```cpp
   void Start(std::shared_ptr<Task2> task)
   {
      auto weak = task->weak_from_this();
      std::thread([weak]() {
          std::this_thread::sleep_for(std::chrono::milliseconds(100));
          auto strong = weak.lock();
          if (!strong) {
              return;
          }
          strong->DoWork();
      }).detach();
   }
   ```

**注意** 

1. weak\_from\_this在C++17开始支持，且对象必须由智能指针管理，否则调用weak.lock()会为空，导致回调不执行。
2. 如果无法使用weak\_from\_this，可用C++11支持的shared\_from\_this方式。

## 优化建议3：指针操作前都增加判空处理，优先使用智能指针代替裸指针

主线程将指针销毁后，子线程依然对此指针变量进行操作导致的崩溃。

```cpp
int* g_ptr1 = nullptr;

void WorkerThread1()
{
    std::this_thread::sleep_for(std::chrono::milliseconds(100));
    *g_ptr1 = 24; // 子线程访问已释放的对象，UAF问题
}

int Demo3()
{
    g_ptr1 = new int(42);
    std::thread t(WorkerThread1);
    delete g_ptr1; // 主线程提前释放
    t.join();
    return 0;
}
```

建议：

1. 在指针销毁时，对指针置空。
2. 在子线程对主线程的指针进行操作时，都增加判空处理，以此来避免子线程在主线程销毁时依旧执行后续操作。
3. 建议使用智能指针代替裸指针。

   ```cpp
   int* g_ptr2 = nullptr;

   void WorkerThread2()
   {
       std::this_thread::sleep_for(std::chrono::milliseconds(100));
       if (g_ptr2 != nullptr) { // 判空处理
           *g_ptr2 = 24;
       }
   }

   int Demo4() {
       g_ptr2 = new int(42);
       std::thread t(WorkerThread2);
       delete g_ptr2; // 主线程提前释放
       g_ptr2 = nullptr; // 指针置空
       t.join();
       return 0;
   }
   ```
