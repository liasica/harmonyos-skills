---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-stability-cpp-crash-opt
title: CppCrash类问题优化建议
breadcrumb: 最佳实践 > 稳定性 > 稳定性优化 > 应用异常退出类问题优化建议 > CppCrash类问题优化建议
category: best-practices
scraped_at: 2026-09-02T15:03:24+08:00
doc_updated_at: 2026-05-22
content_hash: sha256:74fad4f84863a391bf5394e1768ed4e811888309e65eabc5e682ab147a6d25c8
---

## 优化建议1：使用map\vector\list\set等STL库时，要避免数据竞争

错误示例：

```cpp
void EraseMapItem1(int key)
{
    appRunningRecordMap_.erase(key);
}
```

如果存在多个线程同时操作同一个map时，此处将map元素删除，另一个线程同时操作map会产生崩溃问题。

正确示例：

```cpp
void EraseMapItem2(int key)
{
    // 加锁
    std::lock_guard<std::mutex> lock(mutex_);
    appRunningRecordMap_.erase(key);
}

void FindMapItem(int key)
{
    // 加锁
    std::lock_guard<std::mutex> lock(mutex_);
    appRunningRecordMap_.find(key);
}
```

## 优化建议2：多线程访问全局变量/静态变量/类成员变量，如果涉及修改删除操作，对其所有操作都要加锁保护

错误示例：

```cpp
std::list<std::shared_ptr<Object>> g_list;

void MainFunc()
{
    auto xxx = std::make_shared<Object>();
    g_list.push_back(xxx);
}

// 线程1
void Thread1Func()
{
    for (auto &ptr : g_list) {
        ptr->method();
    }
}

// 线程2
void Thread2Func()
{
    g_list.clear(); // 此处清空list，可能会造成线程1使用g_list时发生崩溃
}
```

正确示例：

```cpp
// 线程1
void Thread1FuncEx()
{
    std::lock_guard<std::mutex> lock(mutexEx_);
    for (auto &ptr : g_list) {
        ptr->method();
    }
}

// 线程2
void Thread2FuncEx()
{
    std::lock_guard<std::mutex> lock(mutexEx_);
    g_list.clear();
}
```

## 优化建议3：谨慎在异步场景lambda表达式中使用引用捕获，注意变量生命周期

错误示例：

```cpp
void Checker::Detection(std::string& url)
{
    handler.PostAsyncTask(
        [this, &url]() {
            if (!Checker::DoCheck(url)) {
                // ...
            }
        }
    );
    // 这里url变量即将析构
}

bool Checker::DoCheck(const std::string& url)
{
    // ...
    return true;
}
```

正确示例：

```cpp
void Checker::Detection2(std::string& url)
{
    handler.PostAsyncTask(
        [this, url]() {
            if (!Checker::DoCheck(url)) {
                // ...
            }
        }
    );
    // 这里url变量即将析构，但lambda已经有自己的拷贝
}
```

## 优化建议4：智能指针和裸指针使用前，都要进行判空

错误示例：

```cpp
std::shared_ptr<Object> smartPointer = nullptr;
smartPointer->method();
```

正确示例：

```cpp
std::shared_ptr<Object> smartPointer = nullptr;
if (smartPointer != nullptr) {
    smartPointer->method();
}
```

## 优化建议5：不要使用多个智能指针管理同一个裸指针

错误示例：

```cpp
Object* xxx = new Object();
std::shared_ptr<Object> xxx1(xxx); // xxx1引用计数减为0时析构一次xxx
std::shared_ptr<Object> xxx2(xxx); // xxx2引用计数减为0时析构一次xxx
```

正确示例：

```cpp
std::shared_ptr<Object> xxx = std::make_shared<Object>();
```

## 优化建议6：不要从智能指针中取出裸指针继续使用

错误示例：

```cpp
auto smartPointer = std::make_shared<Object>(); // smartPointer引用计数减为0时析构
auto pointer = smartPointer.get();
pointer->method(); // 当smartPinter析构后继续使用pointer可能发生crash
```

正确示例：

```cpp
auto smartPointer = std::make_shared<Object>();
smartPointer->method();
```

## 优化建议7：禁止将裸指针构造为智能指针后，继续使用或主动释放裸指针

错误示例：

```cpp
Object* pointer = new Object();
std::shared_ptr<Object> smartPointer(pointer); // smartPointer引用计数减为0时析构
pointer->method(); // 当smartPointer析构后继续使用pointer可能发生crash
delete pointer; // 主动释放裸指针发生crash
```

正确示例：

```cpp
auto smartPointer = std::make_shared<Object>();
smartPointer->method();
```

## 优化建议8：禁止在信号处理流程中调用非异步安全函数和使用map\vector\list\set等STL库

错误示例：

```cpp
static void SignalHandler(int signo, siginfo_t* si, void* context) // 信号处理函数
{
    char *c = (char*)malloc(10); // 禁止使用malloc，malloc是非异步安全函数
}
```

正确示例：

```cpp
static void SignalHandlerEx(int signo, siginfo_t* si, void* context) // 信号处理函数
{
    char c[10] = {0};
}
```

**注意** 

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

```cpp
void Object1::Run()
{
    startThread_ = std::shared_ptr<std::thread>(new std::thread([this] { // 将this指针传递给其他线程
        if (this == nullptr) {
            return;
        }
        this->GetInfo();
        // ...
    }));
    // ...
}
```

正确示例：

```screen
class Object2 : public std::enable_shared_from_this<Object2> {
public:
    void Run();
    void GetInfo() {}
    // ...

private:
    std::shared_ptr<std::thread> startThread_;
    // ...
};

void Object2::Run()
{
    std::weak_ptr<Object2> weakPtr = shared_from_this(); // 调用shared_from_this捕获this(c++17开始可使用weak_from_this)
    startThread_ = std::shared_ptr<std::thread>(new std::thread([weakPtr] { // weakPtr传递给其他线程
        auto ptr = weakPtr.lock();
        if (ptr == nullptr) {
            return;
        }
        ptr->GetInfo();
        // ...
    }));
    // ...
}

void MainFuncEx()
{
    auto object = std::make_shared<Object2>(); // 必须使用智能指针初始化Object对象
    object->Run();
}
```

## 优化建议10：禁止接口返回局部变量的引用

错误示例：

```cpp
std::string& GetString()
{
    std::string result = "this is string";
    return result; // 禁止返回局部变量result的引用
}
```

正确示例：

```screen
std::string GetStringEx()
{
    std::string result = "this is string";
    return result; // 返回局部变量的值
}
```
