---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/capi-nativechildprocess-exit-info
title: 获取Native子进程退出信息
breadcrumb: 指南 > 应用框架 > Ability Kit（程序框架服务） > Native子进程开发指导 > 获取Native子进程退出信息
category: harmonyos-guides
scraped_at: 2026-04-28T07:38:06+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:a9c9073cbb4442be02b724bd01b66fe10870b2b10f97803d6bd851b41514ba66
---

## 场景介绍

从API version 20开始，支持父进程通过注册回调函数监听子进程，获取子进程异常退出信息，以便父进程做后续优化处理。这里支持监听的子进程必须为[OH\_Ability\_StartNativeChildProcess](../harmonyos-references/capi-native-child-process-h.md#oh_ability_startnativechildprocess)、[OH\_Ability\_StartNativeChildProcessWithConfigs](../harmonyos-references/capi-native-child-process-h.md#oh_ability_startnativechildprocesswithconfigs)或[startNativeChildProcess](../harmonyos-references/js-apis-app-ability-childprocessmanager.md#childprocessmanagerstartnativechildprocess13)接口创建的子进程。

## 接口说明

| 名称 | 描述 |
| --- | --- |
| [Ability\_NativeChildProcess\_ErrCode](../harmonyos-references/capi-native-child-process-h.md#ability_nativechildprocess_errcode) [OH\_Ability\_RegisterNativeChildProcessExitCallback](../harmonyos-references/capi-native-child-process-h.md#oh_ability_registernativechildprocessexitcallback) ([OH\_Ability\_OnNativeChildProcessExit](../harmonyos-references/capi-native-child-process-h.md#oh_ability_onnativechildprocessexit) onProcessExit) | 注册子进程退出回调函数。 |
| [Ability\_NativeChildProcess\_ErrCode](../harmonyos-references/capi-native-child-process-h.md#ability_nativechildprocess_errcode) [OH\_Ability\_UnregisterNativeChildProcessExitCallback](../harmonyos-references/capi-native-child-process-h.md#oh_ability_unregisternativechildprocessexitcallback) ([OH\_Ability\_OnNativeChildProcessExit](../harmonyos-references/capi-native-child-process-h.md#oh_ability_onnativechildprocessexit) onProcessExit) | 解注册子进程退出回调函数。 |

## 开发步骤

**动态库文件**

```
1. libchild_process.so
```

**头文件**

```
1. #include <AbilityKit/native_child_process.h>
```

[MainProcessFile.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Ability/NativeChildProcessExit/entry/src/main/cpp/MainProcessFile.cpp#L21-L23)

1. 主进程-注册和解注册Native子进程异常退出回调。

   调用[OH\_Ability\_RegisterNativeChildProcessExitCallback](../harmonyos-references/capi-native-child-process-h.md#oh_ability_registernativechildprocessexitcallback)注册Native子进程，如果返回值为NCP\_NO\_ERROR表示注册成功。

   调用[OH\_Ability\_UnregisterNativeChildProcessExitCallback](../harmonyos-references/capi-native-child-process-h.md#oh_ability_unregisternativechildprocessexitcallback)解注册Native子进程，如果返回值为NCP\_NO\_ERROR表示解注册成功。

   ```
   1. #include <AbilityKit/native_child_process.h>
   2. #include <hilog/log.h>

   4. // ···

   6. void OnNativeChildProcessExit(int32_t pid, int32_t signal)
   7. {
   8. OH_LOG_INFO(LOG_APP, "pid: %{public}d, signal: %{public}d", pid, signal);
   9. }

   11. void RegisterNativeChildProcessExitCallback()
   12. {
   13. Ability_NativeChildProcess_ErrCode ret =
   14. OH_Ability_RegisterNativeChildProcessExitCallback(OnNativeChildProcessExit);
   15. if (ret != NCP_NO_ERROR) {
   16. OH_LOG_ERROR(LOG_APP, "register failed.");
   17. }
   18. // ···
   19. }

   21. void UnregisterNativeChildProcessExitCallback()
   22. {
   23. Ability_NativeChildProcess_ErrCode ret =
   24. OH_Ability_UnregisterNativeChildProcessExitCallback(OnNativeChildProcessExit);
   25. if (ret != NCP_NO_ERROR) {
   26. OH_LOG_ERROR(LOG_APP, "unregister failed.");
   27. }
   28. // ···
   29. }
   ```

   [MainProcessFile.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Ability/NativeChildProcessExit/entry/src/main/cpp/MainProcessFile.cpp#L20-L60)
2. 主进程-添加编译依赖项。

   修改CMaklist.txt添加必要的依赖库，假设主进程所在的so名称为libmainprocesssample.so（主进程和子进程的实现也可以选择编译到同一个动态库文件）。

   ```
   1. target_link_libraries(mainprocesssample PUBLIC
   2. # 添加依赖的元能力动态库
   3. libchild_process.so

   5. # 其它依赖的动态库
   6. # ...
   7. )
   ```
