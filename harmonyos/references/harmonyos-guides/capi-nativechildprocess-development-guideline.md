---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/capi-nativechildprocess-development-guideline
title: 创建/终止Native子进程（C/C++）
breadcrumb: 指南 > 应用框架 > Ability Kit（程序框架服务） > Native子进程开发指导 > 创建/终止Native子进程（C/C++）
category: harmonyos-guides
scraped_at: 2026-04-28T07:38:05+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:8543ee8204a8306e580be7b72da99485cdf4a0774aca19f77ce83962a6c1f8f8
---

本模块提供了两种创建[Native子进程](ability-terminology.md#native子进程)的方式，以及一种终止子进程的方式。

* [创建支持IPC通信的Native子进程](capi-nativechildprocess-development-guideline.md#创建支持ipc通信的native子进程)：创建子进程，并在父子进程间建立IPC通道，适用于父子进程需要IPC通信的场景。对[IPCKit](ipc-capi-development-guideline.md)存在依赖。
* [创建支持参数传递的Native子进程](capi-nativechildprocess-development-guideline.md#创建支持参数传递的native子进程)：创建子进程，并传递字符串和fd句柄参数到子进程。适用于需要传递参数到子进程的场景。
* [终止子进程](capi-nativechildprocess-development-guideline.md#终止子进程)：终止当前进程创建的[Native子进程](ability-terminology.md#native子进程)或[ArkTS子进程](ability-terminology.md#arkts子进程)。

说明

创建的子进程会随着父进程的退出而退出，无法脱离父进程独立运行。

## 创建支持IPC通信的Native子进程

### 场景介绍

本章节介绍如何在主进程中创建Native子进程，并在父子进程间建立IPC通道，方便开发者在Native层进行多进程编程。

### 接口说明

| 名称 | 描述 |
| --- | --- |
| int [OH\_Ability\_CreateNativeChildProcess](../harmonyos-references/capi-native-child-process-h.md#oh_ability_createnativechildprocess) (const char \*libName, [OH\_Ability\_OnNativeChildProcessStarted](../harmonyos-references/capi-native-child-process-h.md#oh_ability_onnativechildprocessstarted) onProcessStarted) | 创建子进程并加载参数中指定的动态链接库文件，进程启动结果通过参数中的回调函数onProcessStarted异步通知。回调函数运行在独立线程，如果需要访问共享资源在实现时需要注意线程同步，由于系统对于单个进程拥有的回调线程数量有限制，因此不建议在回调函数中执行高耗时操作。 |

说明

从API version 14开始，支持2in1和Tablet设备。API version 13及之前版本，仅支持2in1设备。

从API version 15开始，单个进程最多支持启动50个Native子进程。API version 14及之前版本，单个进程只能启动1个Native子进程。

### 开发步骤

基于已创建完成的Native应用开发工程，在此基础上介绍如何使用AbilityKit提供的C API接口，创建Native子进程，并同时在父子进程间建立IPC通道。

**动态库文件**

```
1. libipc_capi.so
2. libchild_process.so
```

**头文件**

```
1. #include <IPCKit/ipc_kit.h>
2. #include <AbilityKit/native_child_process.h>
```

[ChildProcessSample.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Ability/NativeChildProcessIpc/entry/src/main/cpp/ChildProcessSample.cpp#L17-L22)

1. 子进程-实现必要的导出方法。

   在子进程中，实现必要的两个函数**NativeChildProcess\_OnConnect**及**NativeChildProcess\_MainProc**并导出（假设代码所在的文件名为ChildProcessSample.cpp）。其中NativeChildProcess\_OnConnect方法返回的OHIPCRemoteStub对象负责与主进程进行IPC通信，具体实现方法请参考[IPC通信开发指导（C/C++)](ipc-capi-development-guideline.md)，本文不再赘述。

   子进程启动后会先调用NativeChildProcess\_OnConnect获取IPC Stub对象，之后再调用NativeChildProcess\_MainProc移交主线程控制权，该函数返回后子进程随即退出。

   ```
   1. #include <IPCKit/ipc_kit.h>
   2. // ...
   3. #include <IPCKit/ipc_cremote_object.h>
   4. #include <IPCKit/ipc_cparcel.h>
   5. #include <IPCKit/ipc_error_code.h>

   7. class IpcCapiStubTest {
   8. public:
   9. explicit IpcCapiStubTest();
   10. ~IpcCapiStubTest();
   11. OHIPCRemoteStub *GetRemoteStub();
   12. static int OnRemoteRequest(uint32_t code, const OHIPCParcel *data, OHIPCParcel *reply, void *userData);

   14. private:
   15. OHIPCRemoteStub *stub_{nullptr};
   16. };

   18. IpcCapiStubTest::IpcCapiStubTest()
   19. {
   20. // 创建stub对象
   21. stub_ = OH_IPCRemoteStub_Create("testIpc", &IpcCapiStubTest::OnRemoteRequest, nullptr, this);
   22. }

   24. IpcCapiStubTest::~IpcCapiStubTest()
   25. {
   26. if (stub_ != nullptr) {
   27. OH_IPCRemoteStub_Destroy(stub_);
   28. }
   29. }

   31. OHIPCRemoteStub *IpcCapiStubTest::GetRemoteStub() { return stub_; }

   33. int IpcCapiStubTest::OnRemoteRequest(uint32_t code, const OHIPCParcel *data, OHIPCParcel *reply, void *userData)
   34. {
   35. return OH_IPC_SUCCESS;
   36. }

   38. IpcCapiStubTest g_ipcStubObj;

   40. extern "C" {
   41. OHIPCRemoteStub *NativeChildProcess_OnConnect()
   42. {
   43. // ipcRemoteStub指向子进程实现的ipc stub对象，用于接收来自主进程的IPC消息并响应
   44. // 子进程根据业务逻辑控制其生命周期
   45. return g_ipcStubObj.GetRemoteStub();
   46. }

   48. void NativeChildProcess_MainProc()
   49. {
   50. // 相当于子进程的Main函数，实现子进程的业务逻辑
   51. // ...
   52. // 函数返回后子进程随即退出
   53. }

   55. } // extern "C"
   ```

   [ChildProcessSample.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Ability/NativeChildProcessIpc/entry/src/main/cpp/ChildProcessSample.cpp#L16-L76)
2. 子进程-编译为动态链接库。

   修改CMakeList.txt文件，编译为动态链接库（假设需要编译出的库文件名称为libchildprocesssample.so），并添加IPC动态库依赖。

   ```
   1. add_library(childprocesssample SHARED
   2. # 实现必要导出方法的源文件
   3. ChildProcessSample.cpp

   5. # 其它代码源文件
   6. # ...
   7. )

   9. target_link_libraries(childprocesssample PUBLIC
   10. # 添加依赖的IPC动态库
   11. libipc_capi.so

   13. # 其它所依赖的动态库
   14. # ...
   15. )
   ```
3. 主进程-实现子进程启动结果回调函数。

   ```
   1. #include <IPCKit/ipc_kit.h>
   2. #include <AbilityKit/native_child_process.h>
   3. // ···
   4. static void OnNativeChildProcessStarted(int errCode, OHIPCRemoteProxy *remoteProxy)
   5. {
   6. if (errCode != NCP_NO_ERROR) {
   7. // 子进程未能正常启动时的异常处理
   8. // ...
   9. return;
   10. }

   12. // 保存remoteProxy对象，后续基于IPC Kit提供的API同子进程间进行IPC通信
   13. // 耗时操作建议转移到独立线程去处理，避免长时间阻塞回调线程
   14. // IPC对象使用完毕后，需要调用OH_IPCRemoteProxy_Destroy方法释放
   15. // ···
   16. }
   ```

   [MainProcessSample.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Ability/NativeChildProcessIpc/entry/src/main/cpp/MainProcessSample.cpp#L17-L155)

   回调函数传递的第二个参数OHIPCRemoteProxy对象，会与子进程实现的**NativeChildProcess\_OnConnect**方法返回的OHIPCRemoteStub对象间建立IPC通道，具体使用方法参考[IPC通信开发指导（C/C++)](ipc-capi-development-guideline.md)，本文不再赘述；OHIPCRemoteProxy对象使用完毕后，需要调用[OH\_IPCRemoteProxy\_Destroy](../harmonyos-references/capi-ipc-cremote-object-h.md#oh_ipcremoteproxy_destroy)函数释放。
4. 主进程-启动Native子进程。

   调用API启动Native子进程，需要注意返回值为NCP\_NO\_ERROR仅代表成功调用native子进程启动逻辑，实际的启动结果通过第二个参数中指定的回调函数异步通知。需注意**仅允许在主进程中创建子进程**。

   ```
   1. #include <IPCKit/ipc_kit.h>
   2. #include <AbilityKit/native_child_process.h>
   3. // ···
   4. static void OnNativeChildProcessStarted(int errCode, OHIPCRemoteProxy *remoteProxy)
   5. {
   6. if (errCode != NCP_NO_ERROR) {
   7. // 子进程未能正常启动时的异常处理
   8. // ...
   9. return;
   10. }

   12. // 保存remoteProxy对象，后续基于IPC Kit提供的API同子进程间进行IPC通信
   13. // 耗时操作建议转移到独立线程去处理，避免长时间阻塞回调线程
   14. // IPC对象使用完毕后，需要调用OH_IPCRemoteProxy_Destroy方法释放
   15. // ...
   16. // ···
   17. }

   19. void CreateNativeChildProcess()
   20. {
   21. // 第一个参数"libchildprocesssample.so"为实现了子进程必要导出方法的动态库文件名称
   22. int32_t ret = OH_Ability_CreateNativeChildProcess("libchildprocesssample.so", OnNativeChildProcessStarted);
   23. if (ret != NCP_NO_ERROR) {
   24. // 子进程未能正常启动时的异常处理
   25. // ...
   26. }
   27. g_result = ret;
   28. }
   ```

   [MainProcessSample.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Ability/NativeChildProcessIpc/entry/src/main/cpp/MainProcessSample.cpp#L16-L167)
5. 主进程-添加编译依赖项。

   修改CMaklist.txt添加必要的依赖库，假设主进程所在的so名称为libmainprocesssample.so（主进程和子进程的实现也可以选择编译到同一个动态库文件）。

   ```
   1. target_link_libraries(mainprocesssample PUBLIC
   2. # 添加依赖的IPC及元能力动态库
   3. libipc_capi.so
   4. libchild_process.so

   6. # 其它依赖的动态库
   7. # ...
   8. )
   ```

## 创建支持参数传递的Native子进程

### 场景介绍

本章节介绍如何创建Native子进程，并传递参数到子进程。

### 接口说明

| 名称 | 描述 |
| --- | --- |
| [Ability\_NativeChildProcess\_ErrCode](../harmonyos-references/capi-native-child-process-h.md#ability_nativechildprocess_errcode) [OH\_Ability\_StartNativeChildProcess](../harmonyos-references/capi-native-child-process-h.md#oh_ability_startnativechildprocess) (const char \*entry, [NativeChildProcess\_Args](../harmonyos-references/capi-nativechildprocess-args.md) args, [NativeChildProcess\_Options](../harmonyos-references/capi-nativechildprocess-options.md) options, int32\_t \*pid) | 启动子进程并返回子进程pid。 |

### 开发步骤

**动态库文件**

```
1. libchild_process.so
```

**头文件**

```
1. #include <AbilityKit/native_child_process.h>
```

[ChildProcessFunc.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Ability/NativeChildProcessParams/entry/src/main/cpp/ChildProcessFunc.cpp#L17-L19)

1. 子进程-实现必要的导出方法。

   在子进程中，实现参数为[NativeChildProcess\_Args](../harmonyos-references/capi-nativechildprocess-args.md)的入口函数并导出（假设代码所在的文件名为ChildProcessSample.cpp）。子进程启动后会调用该入口函数，该函数返回后子进程随即退出。

   ```
   1. #include <AbilityKit/native_child_process.h>
   2. extern "C" {
   3. /**
   4. * 子进程的入口函数，实现子进程的业务逻辑
   5. * 函数名称可以自定义，在主进程调用OH_Ability_StartNativeChildProcess方法时指定，此示例中为Main
   6. * 函数返回后子进程退出
   7. */
   8. void Main(NativeChildProcess_Args args)
   9. {
   10. // 获取传入的entryPrams
   11. char *entryParams = args.entryParams;
   12. // 获取传入的fd列表
   13. NativeChildProcess_Fd *current = args.fdList.head;
   14. while (current != nullptr) {
   15. char *fdName = current->fdName;
   16. int32_t fd = current->fd;
   17. current = current->next;
   18. // 实现业务逻辑
   19. }
   20. }
   21. } // extern "C"
   ```

   [ChildProcessFunc.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Ability/NativeChildProcessParams/entry/src/main/cpp/ChildProcessFunc.cpp#L16-L40)
2. 子进程-编译为动态链接库。

   修改CMakeList.txt文件，编译为动态链接库（假设需要编译出的库文件名称为libchildprocesssample.so），并添加元能力动态库依赖。

   ```
   1. add_library(childprocesssample SHARED
   2. # 实现必要导出方法的源文件
   3. ChildProcessSample.cpp

   5. # 其它代码源文件
   6. # ...
   7. )

   9. target_link_libraries(childprocesssample PUBLIC
   10. # 添加依赖的元能力动态库
   11. libchild_process.so

   13. # 其它所依赖的动态库
   14. # ...
   15. )
   ```
3. 主进程-启动Native子进程。

   调用API启动Native子进程，返回值为NCP\_NO\_ERROR代表成功启动native子进程。

   ```
   1. #include <AbilityKit/native_child_process.h>
   2. #include <cstdlib>
   3. #include <cstring>
   4. #include <fcntl.h>
   5. // ...
   6. int32_t g_fdNameMaxLength = 20;

   8. void StartNativeChildProcess()
   9. {
   10. // ...
   11. NativeChildProcess_Args args;
   12. // 设置entryParams，支持传输的最大数据量为150KB
   13. const size_t entryParamsSize = 10;
   14. args.entryParams = (char *)malloc(sizeof(char) * entryParamsSize);
   15. if (args.entryParams != nullptr) {
   16. (void)strlcpy(args.entryParams, "testParam", entryParamsSize);
   17. }

   19. // 插入节点到链表头节点中
   20. args.fdList.head = (NativeChildProcess_Fd *)malloc(sizeof(NativeChildProcess_Fd));
   21. // fd关键字，最多不超过20个字符
   22. args.fdList.head->fdName = (char *)malloc(sizeof(char) * g_fdNameMaxLength);
   23. if (args.fdList.head->fdName != nullptr) {
   24. (void)strlcpy(args.fdList.head->fdName, "fd1", g_fdNameMaxLength);
   25. }
   26. // 获取fd逻辑
   27. int32_t fd = open("/data/storage/el2/base/haps/entry/files/test.txt", O_RDWR | O_CREAT, 0644);
   28. args.fdList.head->fd = fd;
   29. // 此处只插入一个fd记录，根据需求可以插入更多fd记录到链表中，最多不超过16个
   30. args.fdList.head->next = NULL;
   31. NativeChildProcess_Options options = {.isolationMode = NCP_ISOLATION_MODE_ISOLATED};

   33. // 第一个参数"libchildprocesssample.so:Main"为实现了子进程Main方法的动态库文件名称和入口方法名
   34. int32_t pid = -1;
   35. Ability_NativeChildProcess_ErrCode ret =
   36. OH_Ability_StartNativeChildProcess("libchildprocesssample.so:Main", args, options, &pid);
   37. if (ret != NCP_NO_ERROR) {
   38. // 释放NativeChildProcess_Args中的内存空间防止内存泄漏
   39. // 子进程未能正常启动时的异常处理
   40. // ...
   41. }

   43. // 其他逻辑
   44. // ...

   46. // 释放NativeChildProcess_Args中的内存空间防止内存泄漏
   47. }
   ```

   [MainProcessFunc.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Ability/NativeChildProcessParams/entry/src/main/cpp/MainProcessFunc.cpp#L16-L77)
4. 主进程-添加编译依赖项。

   修改CMaklist.txt添加必要的依赖库，假设主进程所在的so名称为libmainprocesssample.so（主进程和子进程的实现也可以选择编译到同一个动态库文件）。

   ```
   1. target_link_libraries(mainprocesssample PUBLIC
   2. # 添加依赖的元能力动态库
   3. libchild_process.so

   5. # 其它依赖的动态库
   6. # ...
   7. )
   ```

## 子进程获取启动参数

### 场景介绍

从API version 17开始，支持子进程获取启动参数。

### 接口说明

| 名称 | 描述 |
| --- | --- |
| [NativeChildProcess\_Args](../harmonyos-references/capi-nativechildprocess-args.md)\* [OH\_Ability\_GetCurrentChildProcessArgs](../harmonyos-references/capi-native-child-process-h.md#oh_ability_getcurrentchildprocessargs)() | 返回子进程自身的启动参数。 |

### 开发步骤

**动态库文件**

```
1. libchild_process.so
```

**头文件**

```
1. #include <AbilityKit/native_child_process.h>
```

[ChildGetStartParams.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Ability/NativeChildProcessParams/entry/src/main/cpp/ChildGetStartParams.cpp#L17-L19)

**获取启动参数**

[OH\_Ability\_StartNativeChildProcess](../harmonyos-references/capi-native-child-process-h.md#oh_ability_startnativechildprocess)创建子进程后，子进程内的任意so和任意子线程可以通过调用[OH\_Ability\_GetCurrentChildProcessArgs](../harmonyos-references/capi-native-child-process-h.md#oh_ability_getcurrentchildprocessargs)()获取到子进程的启动参数[NativeChildProcess\_Args](../harmonyos-references/capi-nativechildprocess-args.md)，便于操作相关的文件描述符。

```
1. #include <AbilityKit/native_child_process.h>
2. #include <thread>

4. extern "C" {
5. void ThreadFunc()
6. {
7. // 获取子进程的启动参数
8. NativeChildProcess_Args *args = OH_Ability_GetCurrentChildProcessArgs();
9. // 获取启动参数失败时返回nullptr
10. if (args == nullptr) {
11. return;
12. }
13. // 获取启动参数中的entryPrams
14. char *entryParams = args->entryParams;
15. // 获取fd列表
16. NativeChildProcess_Fd *current = args->fdList.head;
17. while (current != nullptr) {
18. char *fdName = current->fdName;
19. int32_t fd = current->fd;
20. current = current->next;
21. // 实现业务逻辑
22. }
23. }

25. /**
26. * 子进程的入口函数，实现子进程的业务逻辑
27. * args是子进程的启动参数
28. */
29. void Main(NativeChildProcess_Args args)
30. {
31. // 实现业务逻辑

33. // 创建线程
34. std::thread tObj(ThreadFunc);
35. }

37. } // extern "C"
```

[ChildGetStartParams.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Ability/NativeChildProcessParams/entry/src/main/cpp/ChildGetStartParams.cpp#L16-L56)

## 终止子进程

### 场景介绍

从API version 22开始，支持根据传入的pid终止当前进程创建的[Native子进程](ability-terminology.md#native子进程)或[ArkTS子进程](ability-terminology.md#arkts子进程)。

### 接口说明

| 名称 | 描述 |
| --- | --- |
| [Ability\_NativeChildProcess\_ErrCode](../harmonyos-references/capi-native-child-process-h.md#ability_nativechildprocess_errcode) [OH\_Ability\_KillChildProcess](../harmonyos-references/capi-native-child-process-h.md#oh_ability_killchildprocess)(int32\_t pid) | 终止当前进程创建的子进程，该接口既可以用来终止[Native子进程](ability-terminology.md#native子进程)，也可以用来终止[ArkTS子进程](ability-terminology.md#arkts子进程)。 |

### 开发步骤

**头文件**

```
1. #include <AbilityKit/native_child_process.h>
```

**终止子进程**

通过[native\_child\_process](../harmonyos-references/capi-native-child-process-h.md)和[childProcessManager](../harmonyos-references/js-apis-app-ability-childprocessmanager.md)（非SELF\_FORK模式）中的接口创建子进程后，主进程可以调用[OH\_Ability\_KillChildProcess](../harmonyos-references/capi-native-child-process-h.md#oh_ability_killchildprocess)(int32\_t pid)根据传入的pid终止相应的子进程。

```
1. #include <AbilityKit/native_child_process.h>
2. // ...
3. void KillChildProcess(int32_t pid)
4. {
5. Ability_NativeChildProcess_ErrCode ret = OH_Ability_KillChildProcess(pid);
6. if (ret != NCP_NO_ERROR) {
7. // 子进程未成功杀死的异常处理
8. }
9. // ...
10. }
```
