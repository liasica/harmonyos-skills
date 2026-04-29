---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-stability-leak-opt
title: 资源泄漏类问题优化建议
breadcrumb: 最佳实践 > 稳定性 > 稳定性优化 > 资源泄漏类问题优化建议
category: best-practices
scraped_at: 2026-04-29T14:14:14+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:3166e059b27a8cabce983bbc264689aea3955b76fcc2571c5bf30615836043bd
---

## 内存泄漏问题优化建议

### 优化建议1：使用定时器组件销毁时一定要调用clearTimeout和clearInterval，否则对象无法析构

定时器未清理导致组件一直没有析构。

```
1. export default class test {
2. private timer: number | null = null; // 正确声明类属性

4. onInit() {
5. this.timer = setInterval(() => {
6. this.updateData(); // 通过this调用类方法
7. }, 1000);
8. }

10. private updateData() {
11. // 定时任务具体逻辑
12. }
13. }
```

[MemoryLeakDetection.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/MemoryDetection/entry/src/main/ets/pages/MemoryLeakDetection.ets#L43-L55)

**优化建议：**

使用定时器组件销毁时一定要调用clearTimeout和clearInterval，否则对象无法析构。

```
1. export default class test {
2. private timer: number | null = null; // 正确声明类属性

4. onInit() {
5. this.timer = setInterval(() => {
6. this.updateData(); // 通过this调用类方法
7. }, 1000);
8. }

10. private updateData() {
11. // 定时任务具体逻辑
12. }

14. onDestroy() {
15. if (this.timer !== null) {
16. clearInterval(this.timer); // 清理定时器
17. this.timer = null;
18. }
19. }
20. }
```

[MemoryLeakDetection2.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/MemoryDetection/entry/src/main/ets/pages/MemoryLeakDetection2.ets#L16-L35)

### 优化建议2：异常分支需要关注释放申请的内存

申请堆内存但是没有在异常分支进行释放。

```
1. static bool InjectNativeLeak1()
2. {
3. char* p = (char*)malloc(g_cmdLen + 1);
4. if (!p) {
5. return false;
6. }
7. auto err = memset(p, 'a', g_cmdLen);
8. if (err) {
9. // 异常分支退出未释放
10. return false;
11. }
12. free(p);
13. return true;
14. }
```

[resource\_leak.cpp](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/MemoryDetection/entry/src/main/cpp/resource_leak.cpp#L35-L48)

**优化建议：**

在代码开发中需要特别注意以下场景：

1. 同一函数内，异常分支未释放资源。
2. 构造函数中申请资源，析构函数未释放资源。
3. 资源申请释放有配对，但配对函数或变量不匹配。
4. 指针地址偏移等原因导致申请的内存地址丢失。

```
1. static bool InjectNativeLeak2()
2. {
3. char* p = (char*)malloc(g_cmdLen + 1);
4. if (!p) {
5. return false;
6. }
7. auto err = memset(p, 'a', g_cmdLen);
8. if (err) {
9. free(p);
10. return false;
11. }
12. free(p);
13. return true;
14. }
```

[resource\_leak.cpp](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/MemoryDetection/entry/src/main/cpp/resource_leak.cpp#L52-L65)

## ashmem/ION泄漏问题优化建议

### 优化建议1：调用命名API接口，设定ashmem和ION的名字，与pixmap绑定，来提高这类内存泄漏的定位效率

未释放的共享内存映射。

```
1. void processWithLeak1(int fd, size_t size) {
2. void* ptr = mmap(nullptr, size, PROT_READ | PROT_WRITE, MAP_SHARED, fd, 0);
3. if (ptr == MAP_FAILED) {
4. return;
5. }
6. // 使用共享内存
7. processData(ptr);
8. // 忘记调用munmap(ptr, size);
9. // 每一次调用都会泄漏一块映射内存
10. }
```

[resource\_leak.cpp](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/MemoryDetection/entry/src/main/cpp/resource_leak.cpp#L78-L87)

**优化建议：**

及时释放内存映射。

```
1. void processWithLeak2(int fd, size_t size) {
2. void* ptr = mmap(nullptr, size, PROT_READ | PROT_WRITE, MAP_SHARED, fd, 0);
3. if (ptr == MAP_FAILED) {
4. return;
5. }
6. // 使用共享内存
7. processData(ptr);
8. munmap(ptr, size);
9. }
```

[resource\_leak.cpp](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/MemoryDetection/entry/src/main/cpp/resource_leak.cpp#L91-L99)

针对ION和ashmem内存泄漏，开发者可以调用命名API接口，设定ashmem和ION的名字，与pixmap绑定，来提高这类内存泄漏的定位效率。

提供的API接口使用方法可参考：

JS层API：**[setMemoryNameSync()](../harmonyos-references/arkts-apis-image-pixelmap.md#setmemorynamesync13)**

NATIVE层API：**[OH\_PixelmapNative\_SetMemoryName()](../harmonyos-references/capi-pixelmap-native-h.md#oh_pixelmapnative_setmemoryname)**

建议Name按照窗口+组件+图片序号自定义，如果出现批量组件图片内存未释放，可快速定位。

修改方法示例**：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/U3awnLDUQMiIS-8TxIUq5Q/zh-cn_image_0000002370405688.png?HW-CC-KV=V1&HW-CC-Date=20260429T061413Z&HW-CC-Expire=86400&HW-CC-Sign=A41B2FB6D1ECE7D79D838D6EB958BA62508D41268678DF8E27EFB5F1343CE32C "点击放大")

ashmem日志结果示例展示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0e/v3/Ccl3Y3IcS7GHKnMQajPMFg/zh-cn_image_0000002404045417.png?HW-CC-KV=V1&HW-CC-Date=20260429T061413Z&HW-CC-Expire=86400&HW-CC-Sign=F7A7A33F665B636E08F04733E1B3B0AA1F3ADCBC30705BBD7817945208387947 "点击放大")

ION日志结果示例展示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/YGKcXKxMRgmxvmJSuYBkOQ/zh-cn_image_0000002370565600.png?HW-CC-KV=V1&HW-CC-Date=20260429T061413Z&HW-CC-Expire=86400&HW-CC-Sign=89F62811E6D7FC139D4A59D3D3F060925187161C561E5CFDC6C1B04530D2A7F0 "点击放大")

## 句柄泄漏问题优化建议

### 优化建议1：函数各个异常分支及时增加关闭句柄的操作

代码打开文件句柄，但是没有释放造成句柄泄漏。

```
1. void InjectContinuingFileFdLeak1(std::string path) {
2. mode_t fileMode = 0644;
3. int fd = open(path.c_str(), O_CREAT | O_RDWR, fileMode);
4. if (fd < 0) {
5. return;
6. }

8. if (!CheckStatus()) {
9. // 异常分支未关闭句柄
10. return;
11. }
12. close(fd); // 正常业务流程关闭句柄
13. }
```

[resource\_leak.cpp](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/MemoryDetection/entry/src/main/cpp/resource_leak.cpp#L111-L123)

优化建议：在创建文件句柄的同时在函数出口（含函数各个异常分支）及时增加关闭句柄的操作，防止句柄未正常关闭导致的泄漏。

```
1. void InjectContinuingFileFdLeak2(std::string path) {
2. mode_t fileMode = 0644;
3. int fd = open(path.c_str(), O_CREAT | O_RDWR, fileMode);
4. if (fd < 0) {
5. return;
6. }

8. if (!CheckStatus()) {
9. close(fd);
10. return;
11. }
12. close(fd); // 正常业务流程关闭句柄
13. }
```

[resource\_leak.cpp](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/MemoryDetection/entry/src/main/cpp/resource_leak.cpp#L127-L139)

## 线程泄漏问题优化建议

### 优化建议1：严格控制线程生命周期

未正确管理线程对象，无法知道线程何时结束，可能导致资源泄漏。

```
1. void riskyThreadFunction(int num) {
2. for (int i = 0; i < num; i++) { // 创建 Num 个线程
3. pthread_t thread;
4. pthread_create(&thread, NULL, LeadThreadFn, NULL);
5. // ...
6. }
7. // ...
8. return;
9. }
```

[resource\_leak.cpp](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/MemoryDetection/entry/src/main/cpp/resource_leak.cpp#L153-L161)

优化建议：

1. 严格控制线程的生命周期，尽量避免大量线程同时存在以及线程生命周期脱离控制的情况；
2. 保证异常场景的线程安全，补充异常场景下的线程管理机制，推荐使用线程池来进行管理；
3. 创建线程时为线程取名（默认继承父进程名，导致大量同名线程），便于出现线程泄漏后的快速定位；
4. pthread\_create后需要调用pthread\_join或者pthread\_detach确保线程资源能回收掉。

```
1. class ThreadPool { // 线程池实现，支持线程生命周期管理和回收
2. public:
3. // ...
4. static bool addTask(const Task& task) {
5. // ...
6. return true;
7. }
8. };

10. void safeThreadFunction(int num) {
11. for (int i = 0; i < num; i++) { // 创建 Num 个线程
12. Task task;
13. bool ret = ThreadPool::addTask(task); // 使用线程池管理线程
14. if (ret) {
15. break;
16. }
17. // ...
18. }
19. // ...
20. return;
21. }
```

[resource\_leak.cpp](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/MemoryDetection/entry/src/main/cpp/resource_leak.cpp#L167-L187)
