---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/native-fence-guidelines
title: GPU/CPU内存访问同步操作开发指南 (C/C++)
breadcrumb: 指南 > 图形 > ArkGraphics 2D（方舟2D图形服务） > 图形缓冲区 > GPU/CPU内存访问同步操作开发指南 (C/C++)
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:21+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:0ffeca605188e8954072a8d0a3672e0baaaab33e5434f8e5a3ec4c972f02f026
---

## 场景介绍

NativeFence是管理fenceFd同步状态的模块。fenceFd是一种文件描述符，用于实现GPU和CPU之间的内存访问同步。当GPU或CPU需要访问共享内存时，通过fenceFd进行同步：一方创建fenceFd并设置为阻塞状态，另一方在完成操作后发送同步信号解除阻塞。

开发者可通过其接口实现以下功能：设置阻塞时间、永久阻塞、关闭fenceFd以及检查其有效性。

## 接口说明

| 接口名 | 描述 |
| --- | --- |
| OH\_NativeFence\_IsValid (int fenceFd) | 检查fenceFd是否合法。 |
| OH\_NativeFence\_Wait (int fenceFd, uint32\_t timeout) | 阻塞传入的fenceFd，超时参数指定了允许等待的最长时间。 |
| OH\_NativeFence\_WaitForever (int fenceFd) | 永久阻塞传入的fenceFd。 |
| OH\_NativeFence\_Close (int fenceFd) | 关闭fenceFd。 |

详细的接口说明请参考[NativeFence](../harmonyos-references/capi-nativefence.md)。

## 开发步骤

以下步骤描述了如何使用NativeFence提供的Native API接口。

**添加动态链接库**

CMakeLists.txt中添加以下库文件。

```txt
libnative_fence.so
```

**头文件**

```
#include <native_fence/native_fence.h>
#include <cstring>
#include <iostream>
#include <linux/sync_file.h>
#include <signal.h>
#include <sys/signalfd.h>
#include <unistd.h>
```

1. **使用signalfd()接口创建fenceFd**。

   ```
   sigset_t mask;
   sigemptyset(&mask);
   sigaddset(&mask, SIGINT); // Monitor SIGINT signal (Ctrl C)
   sigaddset(&mask, SIGURG); // Generated when urgent data or out of band data arrives at the socket
   sigprocmask(SIG_BLOCK, &mask, NULL);
   int sfd = signalfd(-1, &mask, 0);
   ```
2. **判断传入的fenceFd是否合法**。

   ```
   bool isValid = OH_NativeFence_IsValid(INVALID_FD);
   if (!isValid) {
       DRAWING_LOGW("fenceFd is invalid");
   }
   ```
3. **调用OH\_NativeFence\_Wait阻塞接口，等待fence完成后进行下一步操作**。

   ```
   constexpr uint32_t TIMEOUT_MS = 5000;
   // ...
   bool result = OH_NativeFence_Wait(INVALID_FD, TIMEOUT_MS);
   ```
4. **调用OH\_NativeFence\_WaitForever阻塞接口，等待fence完成后进行下一步操作**。

   ```
   bool result2 = false;
   auto startTime = std::chrono::steady_clock::now();
   result2 = OH_NativeFence_WaitForever(sfd);
   auto endTime = std::chrono::steady_clock::now();
   auto duration = std::chrono::duration_cast<std::chrono::milliseconds>(endTime - startTime).count();
   if (result2) {
       DRAWING_LOGI("SyncFenceWaitForever has an event occurring result2 %{public}d, cost_time: %{public}d",
           result2, duration);
   } else {
       DRAWING_LOGI("SyncFenceWaitForever timeout with no event occurrence"
           "result2 %{public}d, cost_time: %{public}d", result2, duration);
   }
   ```
5. **GPU或CPU发送同步信号(signal)，通知fenceFd解除阻塞**。
6. **关闭fenceFd**。

   ```
   OH_NativeFence_Close(sfd);
   ```
