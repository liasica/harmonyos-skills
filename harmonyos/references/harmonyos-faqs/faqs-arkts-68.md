---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-68
title: 如何判断是否为主线程
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > ArkTS线程模型和并发 > 如何判断是否为主线程
category: harmonyos-faqs
scraped_at: 2026-04-28T08:24:26+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:64cf3a3dc47a43223b57dbe12a6d7f411da477fdfc680379e786dfee7a36a2ca
---

通过Process获取当前的进程号和线程号。如果二者相同，表示当前执行环境为主线程。

**参考代码：**

```
1. import { process } from '@kit.ArkTS'

3. function isMainThread(): boolean {
4. return process.pid == process.tid;
5. }
```

[IsMainThread.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkTS/entry/src/main/ets/pages/IsMainThread.ets#L21-L25)

对于Native侧，通过getpid()方法获取进程ID，通过syscall方式获取线程ID。

**参考代码：**

```
1. #include <unistd.h>
2. #include <thread>
3. #include <sys/syscall.h>

5. bool isMainThread() {
6. pid_t pid = getpid();
7. pid_t tid = syscall(SYS_gettid);
8. if (pid == tid) {
9. return true;
10. } else {
11. return false;
12. }
13. }
```

[IsMainThread2.cpp](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkTS/entry/src/main/ets/pages/IsMainThread2.cpp#L21-L33)
