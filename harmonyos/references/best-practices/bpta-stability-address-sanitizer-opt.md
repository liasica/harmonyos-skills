---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-stability-address-sanitizer-opt
title: 地址越界类问题优化建议
breadcrumb: 最佳实践 > 稳定性 > 稳定性优化 > 地址越界类问题优化建议
category: best-practices
scraped_at: 2026-04-28T08:23:02+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:308a7272de9ddf639fa96284ef6e78d17243b93fd55e1da31f4ad031f83e5b0d
---

## 优化建议1：增加返回值校验

在正常情况下，napi\_get\_value\_string\_utf8接口会在字符串末尾添加\0结束符；但若发生异常（如参数非法或类型不符），该接口会提前返回，导致缓冲区未被写入任何内容，也不会添加结束符。这可能导致申请的内存与实际使用不一致，从而引发越界错误。

```
1. static std::string GetStringParam1(napi_env env, napi_value arg)
2. {
3. size_t size;
4. napi_get_value_string_utf8(env, arg, nullptr, 0, &size);
5. size_t str_size = size + 1;
6. char *buf = new char[str_size];
7. napi_get_value_string_utf8(env, arg, buf, str_size, nullptr); // 未进行校验
8. std::string str(buf);
9. delete[] buf;
10. return str;
11. }
```

[napi\_init.cpp](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/MemoryDetection/entry/src/main/cpp/napi_init.cpp#L24-L34)

建议：增加返回值校验。

```
1. static std::string GetStringParam2(napi_env env, napi_value arg)
2. {
3. size_t size;
4. // 增加校验
5. if (napi_get_value_string_utf8(env, arg, nullptr, 0, &size) != napi_ok || size == 0) {
6. return "";
7. }
8. size_t str_size = size + 1;
9. char *buf = new char[str_size];
10. // 增加校验
11. if (napi_get_value_string_utf8(env, arg, buf, str_size, nullptr) != napi_ok) {
12. delete[] buf;
13. return "";
14. }
15. std::string str(buf);
16. delete[] buf;
17. return str;
18. }
```

[napi\_init.cpp](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/MemoryDetection/entry/src/main/cpp/napi_init.cpp#L42-L59)

## 优化建议2：异步任务传递this引用

当一个lambda表达式不止在局部作用域中使用，而是被传递到外部函数或另一个线程中时，禁止按引用（&）捕获局部变量（包括 this）。lambda按引用捕获就是把局部对象的引用存储起来，如果lambda的生命周期会超过局部变量生命周期，则可能导致内存不安全。

```
1. class Task1 {
2. public:
3. void Start() {
4. std::thread([this]() {
5. std::this_thread::sleep_for(std::chrono::milliseconds(100));
6. DoWork(); // 如果 Task 已析构，这里是悬空调用
7. }).detach();
8. }

10. void DoWork() {
11. std::cout << "Doing work\n";
12. }

14. ~Task1() {
15. std::cout << "Task destructed\n";
16. }
17. };

19. void Run() {
20. Task1* task = new Task1();
21. task->Start();
22. delete task; // 析构发生在 lambda 执行前
23. std::this_thread::sleep_for(std::chrono::milliseconds(1));
24. }
```

[task\_demo1.cpp](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/MemoryDetection/entry/src/main/cpp/task_demo1.cpp#L29-L52)

建议：

1. 异步或跨线程场景中禁止使用[&]捕获局部变量或this
2. 采用智能指针管理对象生命周期结合weak\_from\_this获取弱指针，保证对象在访问时仍然有效。

实现步骤：

1. 对象要从std::enable\_shared\_from\_this继承。

   ```
   1. class Task2 : public std::enable_shared_from_this<Task2> {
   ```

   [task\_demo2.cpp](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/MemoryDetection/entry/src/main/cpp/task_demo2.cpp#L29-L29)
2. 采用智能指针初始化对象。

   ```
   1. auto task = std::make_shared<Task2>();
   ```

   [task\_demo2.cpp](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/MemoryDetection/entry/src/main/cpp/task_demo2.cpp#L55-L55)
3. lambda表达式中调用weak\_from\_this捕获this。

   ```
   1. void Start(std::shared_ptr<Task2> task)
   2. {
   3. auto weak = task->weak_from_this();
   4. std::thread([weak]() {
   5. std::this_thread::sleep_for(std::chrono::milliseconds(100));
   6. auto strong = weak.lock();
   7. if (!strong) {
   8. return;
   9. }
   10. strong->DoWork();
   11. }).detach();
   12. }
   ```

   [task\_demo2.cpp](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/MemoryDetection/entry/src/main/cpp/task_demo2.cpp#L38-L49)

注意

1. weak\_from\_this在C++17开始支持，且对象必须由智能指针管理，否则调用weak.lock()会为空，导致回调不执行。
2. 如果无法使用weak\_from\_this，可用C++11支持的shared\_from\_this方式。

## 优化建议3：指针操作前都增加判空处理，优先使用智能指针代替裸指针

主线程将指针销毁后，子线程依然对此指针变量进行操作导致的崩溃。

```
1. int* g_ptr1 = nullptr;

3. void WorkerThread1()
4. {
5. std::this_thread::sleep_for(std::chrono::milliseconds(100));
6. *g_ptr1 = 24; // 子线程访问已释放的对象，UAF问题
7. }

9. int Demo3()
10. {
11. g_ptr1 = new int(42);
12. std::thread t(WorkerThread1);
13. delete g_ptr1; // 主线程提前释放
14. t.join();
15. return 0;
16. }
```

[address\_sanitizer\_case3.cpp](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/MemoryDetection/entry/src/main/cpp/address_sanitizer_case3.cpp#L22-L37)

建议：

1. 在指针销毁时，对指针置空。
2. 在子线程对主线程的指针进行操作时，都增加判空处理，以此来避免子线程在主线程销毁时依旧执行后续操作。
3. 建议使用智能指针代替裸指针。

   ```
   1. int* g_ptr2 = nullptr;

   3. void WorkerThread2()
   4. {
   5. std::this_thread::sleep_for(std::chrono::milliseconds(100));
   6. if (g_ptr2 != nullptr) { // 判空处理
   7. *g_ptr2 = 24;
   8. }
   9. }

   11. int Demo4() {
   12. g_ptr2 = new int(42);
   13. std::thread t(WorkerThread2);
   14. delete g_ptr2; // 主线程提前释放
   15. g_ptr2 = nullptr; // 指针置空
   16. t.join();
   17. return 0;
   18. }
   ```

   [address\_sanitizer\_case4.cpp](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/MemoryDetection/entry/src/main/cpp/address_sanitizer_case4.cpp#L22-L39)
