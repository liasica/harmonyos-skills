---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/use-jsvm-about-version
title: 使用JSVM-API接口获取JSVM API的版本号
breadcrumb: 指南 > NDK开发 > 代码开发 > 使用JSVM-API实现JS与C/C++语言交互 > JSVM-API使用指导 > 使用JSVM-API接口获取JSVM API的版本号
category: harmonyos-guides
scraped_at: 2026-04-28T07:54:20+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:70284416208971986ab80886d2f0cb12beec919862f17155d63c2a604cf8a709
---

## 简介

用于获取当前JSVM API的版本信息。

## 接口说明

| 接口 | 功能说明 |
| --- | --- |
| OH\_JSVM\_GetVersion | 获取JSVM运行时支持的最高JSVM API版本。 |
| OH\_JSVM\_GetVMInfo | 获取虚拟机的信息。 |

## 使用示例

JSVM-API接口开发流程参考[使用JSVM-API实现JS与C/C++语言交互开发流程](use-jsvm-process.md)，本文仅对接口对应C++相关代码进行展示。

### OH\_JSVM\_GetVersion && OH\_JSVM\_GetVMInfo

获取当前环境支持的JSVM API的最高版本号和当前虚拟机的信息。

cpp部分代码

```
1. // hello.cpp
2. #include <string.h>

4. // OH_JSVM_GetVersion的样例方法
5. static JSVM_Value GetVersion(JSVM_Env env, JSVM_CallbackInfo info)
6. {
7. uint32_t jsVersion = 0;
8. // 调用接口，获取当前JSVM运行时支持的最高JSVM API版本
9. JSVM_CALL(OH_JSVM_GetVersion(env, &jsVersion));
10. int value = static_cast<int>(jsVersion);
11. OH_LOG_INFO(LOG_APP, "JSVM GetVersion success:%{public}d", value);
12. return nullptr;
13. }

15. // OH_JSVM_GetVMInfo的样例方法
16. // 打印JSVM（JavaScript虚拟机）的各项信息
17. void PrintVmInfo(JSVM_VMInfo vmInfo) {
18. OH_LOG_INFO(LOG_APP, "JSVM API apiVersion: %{public}d", vmInfo.apiVersion);
19. OH_LOG_INFO(LOG_APP, "JSVM API engine: %{public}s", vmInfo.engine);
20. OH_LOG_INFO(LOG_APP, "JSVM API version: %{public}s", vmInfo.version);
21. OH_LOG_INFO(LOG_APP, "JSVM API cachedDataVersionTag: 0x%{public}x", vmInfo.cachedDataVersionTag);
22. }

24. static JSVM_Value GetVMInfo(JSVM_Env env, JSVM_CallbackInfo info)
25. {
26. // 调用接口，获取虚拟机的信息
27. JSVM_VMInfo result;
28. JSVM_CALL(OH_JSVM_GetVMInfo(&result));
29. // 输出VM虚拟机信息
30. PrintVmInfo(result);
31. return nullptr;
32. }

34. // 待执行的js代码
35. static const char *srcCallNative = R"JS(getVersion();getVMInfo();)JS";

37. // GetVersion, GetVMInfo注册回调
38. static JSVM_CallbackStruct param[] = {
39. {.data = nullptr, .callback = GetVersion},
40. {.data = nullptr, .callback = GetVMInfo},
41. };
42. static JSVM_CallbackStruct *method = param;
43. // GetVersion, GetVMInfo方法别名，供JS调用
44. static JSVM_PropertyDescriptor descriptor[] = {
45. {"getVersion", nullptr, method++, nullptr, nullptr, nullptr, JSVM_DEFAULT},
46. {"getVMInfo", nullptr, method++, nullptr, nullptr, nullptr, JSVM_DEFAULT},
47. };
```

预期结果：

```
1. JSVM GetVersion success:9
2. JSVM API apiVersion: 1
3. JSVM API engine: v8
4. JSVM API version: 13.2.152.41
5. JSVM API cachedDataVersionTag: 0x81ff9402
```
