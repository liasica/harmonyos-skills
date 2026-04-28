---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/napi-faq-about-memory-leak
title: 内存泄漏相关问题汇总
breadcrumb: 指南 > NDK开发 > 代码开发 > 使用Node-API实现ArkTS/JS与C/C++语言交互 > Node-API常见问题汇总 > 内存泄漏相关问题汇总
category: harmonyos-guides
scraped_at: 2026-04-28T07:54:13+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:1da5601a5796f86e5f8a97ccbd8fa559dbbd6d5db2c1994914083377f28bb613
---

## 当前是否有机制来检查是否有泄漏的napi\_ref

* 具体问题：napi\_create\_reference可以创建对js对象的引用，保持js对象不释放，正常来说使用完需要使用napi\_delete\_reference进行释放，但怕漏delete导致js对象内存泄漏，当前是否有机制来检查/测试是否有泄漏的napi\_ref？
* 检测方式：

可使用 DevEco Studio（IDE）提供的 Allocation 工具进行检测。

[基础内存分析：Allocation分析](ide-insight-session-allocations.md)

napi\_create\_reference这个接口内部实现会new一个C++对象，因此，如果忘记使用napi\_delete\_reference接口，那这个new出来的C++对象也会泄漏，这时候就可以用Allocation工具来进行检测，这个工具会把未释放的对象的分配栈都打印出来，如果napi\_ref泄漏了，可以在分配栈上看出来。

## napi开发过程中遇见内存泄漏问题要怎么定位解决

点击按钮时内存增加，即使主动触发GC也无法回收。如何在Node-API开发过程中定位和解决内存泄漏问题？

* 解决建议：

需先了解Node-API生命周期机制，相关材料如下：

[使用Node-API接口进行生命周期相关开发](use-napi-life-cycle.md)

使用Node-API时导致内存泄漏的常见原因：

1. napi\_value不在napi\_handle\_scope管理中，导致napi\_value持有的ArkTS对象无法释放，该问题常见于[直接使用uv\_queue\_work的场景](napi-guidelines.md#异步任务)中。解决方法是添加napi\_open\_handle\_scope和napi\_close\_handle\_scope接口。

   此类泄漏可通过snapshot分析定位原因，泄漏的ArkTS对象distance为1，即不知道被谁持有，这种情况下一般就是被native（napi\_value是个指针，指向native持有者）持有了，且napi\_value不在napi\_handle\_scope范围内，可参考[易错API的使用规范](../best-practices/bpta-stability-coding-standard-api.md#section1219614634615)。
2. 使用 napi\_create\_reference 为 ArkTS 对象创建了强引用（initial\_refcount 参数大于 0），且一直未删除，导致 ArkTS 对象无法被回收。napi\_create\_reference 接口内部会创建一个 C++ 对象，因此这种泄漏通常表现为ArkTS对象与Native对象的双重泄漏。可以使用 Allocation 工具捕获Native对象泄漏栈，检查是否存在 napi\_create\_reference 相关的栈帧。

   [基础内存分析：Allocation分析](ide-insight-session-allocations.md)
3. 被其它存活的ArkTS对象持有时，使用snapshot查看泄漏对象的持有者。

## napi\_threadsafe\_function内存泄漏应该如何处理

napi\_threadsafe\_function（下文简称tsfn）在使用时，常常会调用 napi\_acquire\_threadsafe\_function 来更改tsfn的引用计数，确保tsfn不会意外被释放。但在使用完成后，应该及时使用 napi\_tsfn\_release 模式调用 napi\_release\_threadsafe\_function 方法，以确保在所有调用回调都执行完成后，其引用计数能回归到调用 napi\_acquire\_threadsafe\_function 方法之前的水平。当其引用计数归零时，tsfn才能正确的被释放。

当env即将退出，但tsfn的引用计数未归零时，应使用 napi\_tsfn\_abort 模式调用 napi\_release\_threadsafe\_function 方法，确保env释放后不再持有或使用tsfn。env退出后继续持有tsfn将导致未定义行为，可能引发崩溃。

如下代码将展示通过注册 env\_cleanup 钩子函数的方式，以确保在env退出后不再继续持有tsfn。

```
1. //napi_init.cpp
2. #include "napi/native_api.h"
3. #include <hilog/log.h> // hilog, 输出日志, 需链接 libhilog_ndk.z.so
4. #include <thread> // 创建线程
5. #include <unistd.h> // 线程休眠

7. // 定义输出日志的标签和域
8. #undef LOG_DOMAIN
9. #undef LOG_TAG
10. #define LOG_DOMAIN 0x2342
11. #define LOG_TAG "MY_TSFN_DEMO"

13. /*
14. 为构建一个 env 生命周期短于 native 生命周期的场景,
15. 本示例需要使用worker, taskpool 或 napi_create_ark_runtime 等方法,
16. 创建非主线程的ArkTS运行环境，并人为的提前结束掉该线程
17. */

20. // 定义一个数据结构，模拟存储tsfn的场景
21. class MyTsfnContext {
22. public:
23. // 因使用了Node-API方法, MyTsfnContext 应当只在ArkTS线程被构造
24. MyTsfnContext(napi_env env, napi_value workName) {
25. // 注册env销毁钩子函数
26. napi_add_env_cleanup_hook(env, Cleanup, this);
27. // 创建线程安全函数
28. if (napi_create_threadsafe_function(env, nullptr, nullptr, workName, 1, 1, this,
29. TsfnFinalize, this, TsfnCallJs, &tsfn_) != napi_ok) {
30. OH_LOG_INFO(LOG_APP, "tsfn is created failed");
31. return;
32. };
33. };

35. ~MyTsfnContext() { OH_LOG_INFO(LOG_APP, "MyTsfnContext is deconstructed"); };

37. napi_threadsafe_function GetTsfn() {
38. std::unique_lock<std::mutex> lock(mutex_);
39. return tsfn_;
40. }

42. bool Acquire() {
43. if (GetTsfn() == nullptr) {
44. return false;
45. };
46. return (napi_acquire_threadsafe_function(GetTsfn()) == napi_ok);
47. };

49. bool Release() {
50. if (GetTsfn() == nullptr) {
51. return false;
52. };
53. return (napi_release_threadsafe_function(GetTsfn(), napi_tsfn_release) == napi_ok);
54. };

56. bool Call(void *data) {
57. if (GetTsfn() == nullptr) {
58. return false;
59. };
60. return (napi_call_threadsafe_function(GetTsfn(), data, napi_tsfn_blocking) == napi_ok);
61. };

63. private:
64. // 保护多线程读写tsfn的准确性
65. std::mutex mutex_;
66. napi_threadsafe_function tsfn_ = nullptr;

68. // napi_add_env_cleanup_hook 回调
69. static void Cleanup(void *data) {
70. MyTsfnContext *that = reinterpret_cast<MyTsfnContext *>(data);
71. napi_threadsafe_function tsfn = that->GetTsfn();
72. std::unique_lock<std::mutex> lock(that->mutex_);
73. that->tsfn_ = nullptr;
74. lock.unlock();
75. OH_LOG_WARN(LOG_APP, "cleanup is called");
76. napi_release_threadsafe_function(tsfn, napi_tsfn_abort);
77. };

79. // tsfn 释放时的回调
80. static void TsfnFinalize(napi_env env, void *data, void *hint) {
81. MyTsfnContext *ctx = reinterpret_cast<MyTsfnContext *>(data);
82. OH_LOG_INFO(LOG_APP, "tsfn is released");
83. napi_remove_env_cleanup_hook(env, MyTsfnContext::Cleanup, ctx);
84. // cleanup 提前释放线程安全函数, 为避免UAF, 将释放工作交给调用方
85. if (ctx->GetTsfn() != nullptr) {
86. OH_LOG_INFO(LOG_APP, "ctx is released");
87. delete ctx;
88. }
89. };

91. // tsfn 发送到 ArkTS 线程执行的回调
92. static void TsfnCallJs(napi_env env, napi_value func, void *context, void *data) {
93. MyTsfnContext *ctx = reinterpret_cast<MyTsfnContext *>(context);
94. char *str = reinterpret_cast<char *>(data);
95. OH_LOG_INFO(LOG_APP, "tsfn is called, data is: \"%{public}s\"", str);
96. // 业务逻辑已省略，应该包括开发者额外创建的资源的释放逻辑
97. };
98. };

100. // 该方法需注册到模块Index.d.ts, 注册名为 myTsfnDemo, 接口描述如下
101. // export const myTsfnDemo: () => void;
102. napi_value MyTsfnDemo(napi_env env, napi_callback_info info) {
103. OH_LOG_ERROR(LOG_APP, "MyTsfnDemo is called");
104. napi_value workName = nullptr;
105. napi_create_string_utf8(env, "MyTsfnWork", NAPI_AUTO_LENGTH, &workName);
106. MyTsfnContext *myContext = new MyTsfnContext(env, workName);
107. if (myContext->GetTsfn() == nullptr) {
108. OH_LOG_ERROR(LOG_APP, "failed to create tsfn");
109. delete myContext;
110. return nullptr;
111. };
112. char *data0 = new char[]{"Im call in ArkTS Thread"};
113. if (!myContext->Call(data0)) {
114. OH_LOG_INFO(LOG_APP, "call tsfn failed");
115. };

117. // 创建一个线程，模拟异步场景
118. std::thread(
119. [](MyTsfnContext *myCtx) {
120. if (!myCtx->Acquire()) {
121. OH_LOG_ERROR(LOG_APP, "acquire tsfn failed");
122. return;
123. };
124. char *data1 = new char[]{"Im call in std::thread"};
125. // 非必要操作, 仅用于异步流程tsfn仍有效
126. if (!myCtx->Call(data1)) {
127. OH_LOG_ERROR(LOG_APP, "call tsfn failed");
128. };
129. // 休眠 5s, 模拟耗时场景, env退出后, 异步任务仍未执行完成
130. sleep(5);
131. // 此时异步任务已执行完成, 但tsfn已被释放并置为 nullptr
132. char *data2 = new char[]{"Im call after work"};
133. if (!myCtx->Call(data2) && !myCtx->Release()) {
134. OH_LOG_ERROR(LOG_APP, "call and release tsfn failed");
135. delete myCtx;
136. }
137. },
138. myContext)
139. .detach();
140. return nullptr;
141. };
```

```
1. //Index.d.ts
2. export const myTsfnDemo: () => void;
```

以下内容为主线程逻辑，主要用于创建 worker 线程并通知其执行任务。

```
1. // 主线程 Index.ets
2. import  {worker, MessageEvents } from '@kit.ArkTS';

4. const mWorker = new worker.ThreadWorker('../workers/worker');
5. mWorker.onmessage = (e: MessageEvents) => {
6. const action: string | undefined = e.data?.action;
7. if (action === 'kill') {
8. mWorker.terminate();
9. }
10. }

12. // 触发方式的注册已省略
13. mWorker.postMessage({action: 'tsfn-demo'});
```

以下内容为Worker线程逻辑，主要用于触发Native任务。

```
1. // worker.ets
2. import  {worker, ThreadWorkerGlobalScope, MessageEvents} from '@kit.ArkTS';
3. import napiModule from 'libentry.so'; // libentry.so: Node-API 库的模块名称

5. const workerPort: ThreadWorkerGlobalScope = worker.workerPort;

7. workerPort.onmessage = (e: MessageEvents) => {
8. const action: string | undefined = e.data?.action;
9. if (action === 'tsfn-demo') {
10. // 触发 C++ 层的 tsfn demo
11. napiModule.myTsfnDemo();
12. // 通知主线程结束 worker
13. workerPort.postMessage({action: 'kill'});
14. };
15. }
```
