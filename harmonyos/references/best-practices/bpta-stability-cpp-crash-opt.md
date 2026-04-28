---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-stability-cpp-crash-opt
title: CppCrash类问题优化建议
breadcrumb: 最佳实践 > 稳定性 > 稳定性优化 > 应用异常退出类问题优化建议 > CppCrash类问题优化建议
category: best-practices
scraped_at: 2026-04-28T08:23:04+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:889b77c500d0f9f99bb51d42c9f512d1a4bb9c8aad0c77d6d6547be6dd3a990b
---

## 优化建议1：使用map\vector\list\set等STL库时，要避免数据竞争

错误示例：

```
1. void EraseMapItem1(int key)
2. {
3. appRunningRecordMap_.erase(key);
4. }
```

[CppCrashAdvise1.cpp](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/CppCrash/entry/src/main/cpp/CppCrashAdvise1.cpp#L37-L40)

如果存在多个线程同时操作同一个map时，此处将map元素删除，另一个线程同时操作map会产生崩溃问题。

正确示例：

```
1. void EraseMapItem2(int key)
2. {
3. // 加锁
4. std::lock_guard<std::mutex> lock(mutex_);
5. appRunningRecordMap_.erase(key);
6. }

8. void FindMapItem(int key)
9. {
10. // 加锁
11. std::lock_guard<std::mutex> lock(mutex_);
12. appRunningRecordMap_.find(key);
13. }
```

[CppCrashAdvise1.cpp](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/CppCrash/entry/src/main/cpp/CppCrashAdvise1.cpp#L44-L56)

## 优化建议2：多线程访问全局变量/静态变量/类成员变量，如果涉及修改删除操作，对其所有操作都要加锁保护

错误示例：

```
1. std::list<std::shared_ptr<Object>> g_list;

3. void MainFunc()
4. {
5. auto xxx = std::make_shared<Object>();
6. g_list.push_back(xxx);
7. }

9. // 线程1
10. void Thread1Func()
11. {
12. for (auto &ptr : g_list) {
13. ptr->method();
14. }
15. }

17. // 线程2
18. void Thread2Func()
19. {
20. g_list.clear(); // 此处清空list，可能会造成线程1使用g_list时发生崩溃
21. }
```

[CppCrashAdvise2.cpp](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/CppCrash/entry/src/main/cpp/CppCrashAdvise2.cpp#L33-L53)

正确示例：

```
1. // 线程1
2. void Thread1FuncEx()
3. {
4. std::lock_guard<std::mutex> lock(mutexEx_);
5. for (auto &ptr : g_list) {
6. ptr->method();
7. }
8. }

10. // 线程2
11. void Thread2FuncEx()
12. {
13. std::lock_guard<std::mutex> lock(mutexEx_);
14. g_list.clear();
15. }
```

[CppCrashAdvise2.cpp](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/CppCrash/entry/src/main/cpp/CppCrashAdvise2.cpp#L57-L71)

## 优化建议3：谨慎在异步场景lambda表达式中使用引用捕获，注意变量生命周期

错误示例：

```
1. void Checker::Detection(std::string& url)
2. {
3. handler.PostAsyncTask(
4. [this, &url]() {
5. if (!Checker::DoCheck(url)) {
6. // ...
7. }
8. }
9. );
10. // 这里url变量即将析构
11. }

13. bool Checker::DoCheck(const std::string& url)
14. {
15. // ...
16. return true;
17. }
```

[CppCrashAdvise2.cpp](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/CppCrash/entry/src/main/cpp/CppCrashAdvise2.cpp#L94-L110)

正确示例：

```
1. void Checker::Detection2(std::string& url)
2. {
3. handler.PostAsyncTask(
4. [this, url]() {
5. if (!Checker::DoCheck(url)) {
6. // ...
7. }
8. }
9. );
10. // 这里url变量即将析构，但lambda已经有自己的拷贝
11. }
```

[CppCrashAdvise2.cpp](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/CppCrash/entry/src/main/cpp/CppCrashAdvise2.cpp#L114-L124)

## 优化建议4：智能指针和裸指针使用前，都要进行判空

错误示例：

```
1. std::shared_ptr<Object> smartPointer = nullptr;
2. smartPointer->method();
```

[CppCrashAdvise2.cpp](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/CppCrash/entry/src/main/cpp/CppCrashAdvise2.cpp#L130-L131)

正确示例：

```
1. std::shared_ptr<Object> smartPointer = nullptr;
2. if (smartPointer != nullptr) {
3. smartPointer->method();
4. }
```

[CppCrashAdvise2.cpp](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/CppCrash/entry/src/main/cpp/CppCrashAdvise2.cpp#L138-L141)

## 优化建议5：不要使用多个智能指针管理同一个裸指针

错误示例：

```
1. Object* xxx = new Object();
2. std::shared_ptr<Object> xxx1(xxx); // xxx1引用计数减为0时析构一次xxx
3. std::shared_ptr<Object> xxx2(xxx); // xxx2引用计数减为0时析构一次xxx
```

[CppCrashAdvise2.cpp](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/CppCrash/entry/src/main/cpp/CppCrashAdvise2.cpp#L148-L150)

正确示例：

```
1. std::shared_ptr<Object> xxx = std::make_shared<Object>();
```

[CppCrashAdvise2.cpp](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/CppCrash/entry/src/main/cpp/CppCrashAdvise2.cpp#L157-L157)

## 优化建议6：不要从智能指针中取出裸指针继续使用

错误示例：

```
1. auto smartPointer = std::make_shared<Object>(); // smartPointer引用计数减为0时析构
2. auto pointer = smartPointer.get();
3. pointer->method(); // 当smartPinter析构后继续使用pointer可能发生crash
```

[CppCrashAdvise2.cpp](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/CppCrash/entry/src/main/cpp/CppCrashAdvise2.cpp#L164-L166)

正确示例：

```
1. auto smartPointer = std::make_shared<Object>();
2. smartPointer->method();
```

[CppCrashAdvise2.cpp](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/CppCrash/entry/src/main/cpp/CppCrashAdvise2.cpp#L173-L174)

## 优化建议7：禁止将裸指针构造为智能指针后，继续使用或主动释放裸指针

错误示例：

```
1. Object* pointer = new Object();
2. std::shared_ptr<Object> smartPointer(pointer); // smartPointer引用计数减为0时析构
3. pointer->method(); // 当smartPointer析构后继续使用pointer可能发生crash
4. delete pointer; // 主动释放裸指针发生crash
```

[CppCrashAdvise2.cpp](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/CppCrash/entry/src/main/cpp/CppCrashAdvise2.cpp#L181-L184)

正确示例：

```
1. auto smartPointer = std::make_shared<Object>();
2. smartPointer->method();
```

[CppCrashAdvise2.cpp](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/CppCrash/entry/src/main/cpp/CppCrashAdvise2.cpp#L191-L192)

## 优化建议8：禁止在信号处理流程中调用非异步安全函数和使用map\vector\list\set等STL库

错误示例：

```
1. static void SignalHandler(int signo, siginfo_t* si, void* context) // 信号处理函数
2. {
3. char *c = (char*)malloc(10); // 禁止使用malloc，malloc是非异步安全函数
4. }
```

[CppCrashAdvise2.cpp](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/CppCrash/entry/src/main/cpp/CppCrashAdvise2.cpp#L197-L200)

正确示例：

```
1. static void SignalHandlerEx(int signo, siginfo_t* si, void* context) // 信号处理函数
2. {
3. char c[10] = {0};
4. }
```

[CppCrashAdvise2.cpp](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/CppCrash/entry/src/main/cpp/CppCrashAdvise2.cpp#L204-L207)

注意

信号处理函数直接或间接调用的对象或函数需确保异步安全。

**malloc是非异步安全函数，因此在信号处理函数中，**

1. 禁止在堆上申请内存
2. 禁止使用STL类对象，比如在堆动态分配内存的 string、vector、list、set、map...
3. 调用的外部函数，需确保该函数异步安全，典型非异步安全的getproctid、fgets、fopen...

**异步安全函数列表**

如果可以安全的调用该函数，并且在信号处理程序上文中可以安全的使用，则该函数是异步安全的或异步信号安全的。下表中所列的均为异步安全函数，来自POSIX标准。应用程序可以**在信号处理程序中调用这些异步安全函数**。

|  |  |  |  |
| --- | --- | --- | --- |
| \_Exit() | fexecve() | posix\_trace\_event() | sigprocmask() |
| \_exit() | fork() | pselect() | sigqueue() |
| abort() | fstat() | pthread\_kill() | sigset() |
| accept() | fstatat() | pthread\_self() | sigsuspend() |
| access() | fsync() | pthread\_sigmask() | sleep() |
| aio\_error() | ftruncate() | raise() | sockatmark() |
| aio\_return() | futimens() | read() | socket() |
| aio\_suspend() | getegid() | readlink() | socketpair() |
| alarm() | geteuid() | readlinkat() | stat() |
| bind() | getgid() | recv() | symlink() |
| cfgetispeed() | getgroups() | recvfrom() | symlinkat() |
| cfgetospeed() | getpeername() | recvmsg() | tcdrain() |
| cfsetispeed() | getpgrp() | rename() | tcflow() |
| cfsetospeed() | getpid() | renameat() | tcflush() |
| chdir() | getppid() | rmdir() | tcgetattr() |
| chmod() | getsockname() | select() | tcgetpgrp() |
| chown() | getsockopt() | sem\_post() | tcsendbreak() |
| clock\_gettime() | getuid() | send() | tcsetattr() |
| close() | kill() | sendmsg() | tcsetpgrp() |
| connect() | link() | sendto() | time() |
| creat() | linkat() | setgid() | timer\_getoverrun() |
| dup() | listen() | setpgid() | timer\_gettime() |
| dup2() | lseek() | setsid() | timer\_settime() |
| execl() | lstat() | setsockopt() | times() |
| execle() | mkdir() | setuid() | umask() |
| execv() | mkdirat() | shutdown() | uname() |
| execve() | mkfifo() | sigaction() | unlink() |
| faccessat() | mkfifoat() | sigaddset() | unlinkat() |
| fchdir() | mknod() | sigdelset() | utime() |
| fchmod() | mknodat() | sigemptyset() | utimensat() |
| fchmodat() | open() | sigfillset() | utimes() |
| fchown() | openat() | sigismember() | wait() |
| fchownat() | pause() | signal() | waitpid() |
| fcntl() | pipe() | sigpause() | write() |
| fdatasync() | poll() | sigpending() |  |

## 优化建议9：不要传递this指针到其他模块或者线程

将this指针传递到其他模块或者线程是非常危险的行为，如果其他模块或者线程与this指针指向的对象的生命周期不一致时，很容易造成崩溃问题。

错误示例：

```
1. void Object1::Run()
2. {
3. startThread_ = std::shared_ptr<std::thread>(new std::thread([this] { // 将this指针传递给其他线程
4. if (this == nullptr) {
5. return;
6. }
7. this->GetInfo();
8. // ...
9. }));
10. // ...
11. }
```

[CppCrashAdvise4.cpp](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/CppCrash/entry/src/main/cpp/CppCrashAdvise4.cpp#L32-L42)

正确示例：

```
1. class Object2 : public std::enable_shared_from_this<Object2> {
2. public:
3. void Run();
4. void GetInfo() {}
5. // ...

7. private:
8. std::shared_ptr<std::thread> startThread_;
9. // ...
10. };

12. void Object2::Run()
13. {
14. std::weak_ptr<Object2> weakPtr = shared_from_this(); // 调用shared_from_this捕获this(c++17开始可使用waek_form_this)
15. startThread_ = std::shared_ptr<std::thread>(new std::thread([weakPtr] { // weakPtr传递给其他线程
16. auto ptr = weakPtr.lock();
17. if (ptr == nullptr) {
18. return;
19. }
20. ptr->GetInfo();
21. // ...
22. }));
23. // ...
24. }

26. void MainFuncEx()
27. {
28. auto object = std::make_shared<Object2>(); // 必须使用智能指针初始化Object对象
29. object->Run();
30. }
```

[CppCrashAdvise3.cpp](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/CppCrash/entry/src/main/cpp/CppCrashAdvise3.cpp#L23-L52)

## 优化建议10：禁止接口返回局部变量的引用

错误示例：

```
1. std::string& GetString()
2. {
3. std::string result = "this is string";
4. return result; // 禁止返回局部变量result的引用
5. }
```

[CppCrashAdvise2.cpp](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/CppCrash/entry/src/main/cpp/CppCrashAdvise2.cpp#L211-L215)

正确示例：

```
1. std::string GetStringEx()
2. {
3. std::string result = "this is string";
4. return result; // 返回局部变量的值
5. }
```

[CppCrashAdvise2.cpp](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/CppCrash/entry/src/main/cpp/CppCrashAdvise2.cpp#L219-L223)
