---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-68
title: 如何判断是否为主线程
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > ArkTS线程模型和并发 > 如何判断是否为主线程
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:54+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:82a8027bc81beabc28f11dad3fcbfc72511f5d17bceaf62f754907f22f8a1f58
---

通过Process获取当前的进程号和线程号。如果二者相同，表示当前执行环境为主线程。

**参考代码：**

```ts
import { process } from '@kit.ArkTS'

function isMainThread(): boolean {
  return process.pid == process.tid;
}
```

对于Native侧，通过getpid()方法获取进程ID，通过syscall方式获取线程ID。

**参考代码：**

```cpp
#include <unistd.h> 
#include <thread> 
#include <sys/syscall.h> 
 
bool isMainThread() { 
  pid_t pid = getpid(); 
  pid_t tid = syscall(SYS_gettid); 
  if (pid == tid) { 
    return true; 
  } else { 
    return false; 
  } 
}
```
