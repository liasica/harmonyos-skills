---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/native-fence-guidelines
title: GPU/CPU内存访问同步操作开发指南 (C/C++)
breadcrumb: 指南 > 图形 > ArkGraphics 2D（方舟2D图形服务） > 图形缓冲区 > GPU/CPU内存访问同步操作开发指南 (C/C++)
category: harmonyos-guides
scraped_at: 2026-04-28T07:47:20+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:c95d97c4b2537e0675517a70e21dbe710b9c0e281171c1fbbc8abe272bb2ddcf
---

## 场景介绍

NativeFence是管理fenceFd同步状态的模块。开发者可通过其接口实现以下功能：设置阻塞时间、永久阻塞、关闭fenceFd以及检查其有效性。

## 接口说明

| 接口名 | 描述 |
| --- | --- |
| OH\_NativeFence\_IsValid (int fenceFd) | 检查fenceFd是否有效。 |
| OH\_NativeFence\_Wait (int fenceFd, uint32\_t timeout) | 阻塞传入的fenceFd，超时参数指定了允许等待的最长时间。 |
| OH\_NativeFence\_WaitForever (int fenceFd) | 永久阻塞传入的fenceFd。 |
| OH\_NativeFence\_Close (int fenceFd) | 关闭fenceFd。 |

详细的接口说明请参考[NativeFence](../harmonyos-references/capi-nativefence.md)。

## 开发步骤

以下步骤描述了如何使用NativeFence提供的Native API接口。

**添加动态链接库**

CMakeLists.txt中添加以下库文件。

```
1. libnative_fence.so
```

**头文件**

```
1. #include <native_fence/native_fence.h>
2. #include <cstring>
3. #include <iostream>
4. #include <linux/sync_file.h>
5. #include <signal.h>
6. #include <sys/signalfd.h>
7. #include <unistd.h>
```

1. **使用signalfd()接口创建fenceFd**。

   ```
   1. sigset_t mask;
   2. sigemptyset(&mask);
   3. sigaddset(&mask, SIGINT); // Monitor SIGINT signal (Ctrl C)
   4. sigaddset(&mask, SIGURG); // Generated when urgent data or out of band data arrives at the socket
   5. sigprocmask(SIG_BLOCK, &mask, NULL);
   6. int sfd = signalfd(-1, &mask, 0);
   ```

   [napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/NdkNativeFence/entry/src/main/cpp/napi_init.cpp#L75-L82)
2. **判断传入的fenceFd是否合法**。

   ```
   1. bool isValid = OH_NativeFence_IsValid(INVALID_FD);
   2. if (!isValid) {
   3. DRAWING_LOGW("fenceFd is invalid");
   4. }
   ```

   [napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/NdkNativeFence/entry/src/main/cpp/napi_init.cpp#L67-L72)
3. **调用OH\_NativeFence\_Wait阻塞接口，等待fence完成后进行下一步操作**。

   ```
   1. constexpr uint32_t TIMEOUT_MS = 5000;
   2. // ...
   3. bool result = OH_NativeFence_Wait(INVALID_FD, TIMEOUT_MS);
   ```

   [napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/NdkNativeFence/entry/src/main/cpp/napi_init.cpp#L33-L102)
4. **调用OH\_NativeFence\_WaitForever阻塞接口，等待fence完成后进行下一步操作**。

   ```
   1. bool result2 = false;
   2. auto startTime = std::chrono::steady_clock::now();
   3. result2 = OH_NativeFence_WaitForever(sfd);
   4. auto endTime = std::chrono::steady_clock::now();
   5. auto duration = std::chrono::duration_cast<std::chrono::milliseconds>(endTime - startTime).count();
   6. if (result2) {
   7. DRAWING_LOGI("SyncFenceWaitForever has an event occurring result2 %{public}d, cost_time: %{public}d",
   8. result2, duration);
   9. } else {
   10. DRAWING_LOGI("SyncFenceWaitForever timeout with no event occurrence"
   11. "result2 %{public}d, cost_time: %{public}d", result2, duration);
   12. }
   ```

   [napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/NdkNativeFence/entry/src/main/cpp/napi_init.cpp#L136-L149)
5. **GPU或CPU发送同步信号(signal)，通知fenceFd解除阻塞**。
6. **关闭fenceFd**。

   ```
   1. OH_NativeFence_Close(sfd);
   ```

   [napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/NdkNativeFence/entry/src/main/cpp/napi_init.cpp#L160-L162)
