---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/use-jsvm-strict-equals
title: 使用JSVM-API判断给定的两个JS value是否严格相等
breadcrumb: 指南 > NDK开发 > 代码开发 > 使用JSVM-API实现JS与C/C++语言交互 > JSVM-API使用指导 > 使用JSVM-API判断给定的两个JS value是否严格相等
category: harmonyos-guides
scraped_at: 2026-04-28T07:54:23+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:54f9c91edc0a326d00afd3c61a7d50e99a4b857c2c2f4232808e1cc877108bb6
---

## 简介

JSVM-API 中的函数用于判断两个 JavaScript 值是否严格相等，类似于 JavaScript 中的 === 操作符。该函数避免类型转换和松散相等性比较，确保值和类型均相等。

## 基本概念

比较两个JavaScript值是否严格相等。严格相等比较不会进行类型转换，它要求两个值的类型和值完全相同才会返回true。

## 接口说明

| 接口 | 功能说明 |
| --- | --- |
| OH\_JSVM\_StrictEquals | 判断两个JSVM\_Value对象是否相等 |

## 使用示例

JSVM-API接口开发流程参考[使用JSVM-API实现JS与C/C++语言交互开发流程](use-jsvm-process.md)，本文仅对接口对应C++相关代码进行展示。

### OH\_JSVM\_StrictEquals

判断给定的两个JS value是否严格相等。

cpp部分代码：

```
1. // hello.cpp
2. #include "napi/native_api.h"
3. #include "ark_runtime/jsvm.h"
4. #include <hilog/log.h>
5. // OH_JSVM_StrictEquals的样例方法
6. static JSVM_Value IsStrictEquals(JSVM_Env env, JSVM_CallbackInfo info)
7. {
8. // 接受两个入参
9. size_t argc = 2;
10. JSVM_Value args[2] = {nullptr};
11. OH_JSVM_GetCbInfo(env, info, &argc, args, nullptr, nullptr);
12. // 调用OH_JSVM_StrictEquals接口判断给定的两个JavaScript value是否严格相等
13. bool result = false;
14. JSVM_Status status = OH_JSVM_StrictEquals(env, args[0], args[1], &result);
15. if (status != JSVM_OK) {
16. OH_LOG_ERROR(LOG_APP, "JSVM OH_JSVM_StrictEquals: failed");
17. } else {
18. OH_LOG_INFO(LOG_APP, "JSVM OH_JSVM_StrictEquals: success: %{public}d", result);
19. }
20. JSVM_Value isStrictEqual = nullptr;
21. OH_JSVM_GetBoolean(env, result, &isStrictEqual);
22. return isStrictEqual;
23. }
24. // IsStrictEquals注册回调
25. static JSVM_CallbackStruct param[] = {
26. {.data = nullptr, .callback = IsStrictEquals},
27. };
28. static JSVM_CallbackStruct *method = param;
29. // IsStrictEquals方法别名，供JS调用
30. static JSVM_PropertyDescriptor descriptor[] = {
31. {"isStrictEquals", nullptr, method++, nullptr, nullptr, nullptr, JSVM_DEFAULT},
32. };
33. // 样例测试js
34. const char* srcCallNative = R"JS(data = '123';value = '123';isStrictEquals(data,value);)JS";
```

预期的输出结果：

```
1. JSVM OH_JSVM_StrictEquals: success: 1
```
