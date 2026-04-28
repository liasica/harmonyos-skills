---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/use-jsvm-about-wrapper-object
title: 使用JSVM-API接口进行Wrapper object相关开发
breadcrumb: 指南 > NDK开发 > 代码开发 > 使用JSVM-API实现JS与C/C++语言交互 > JSVM-API使用指导 > 使用JSVM-API接口进行Wrapper object相关开发
category: harmonyos-guides
scraped_at: 2026-04-28T07:54:24+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:f8c1f9043439df148ae33cc2ac2577b90143a70f1a1e6517b63e78f0a5e4a3b4
---

## 简介

JSVM-API中，装箱类型(Wrapper object)判断相关接口支持通过不同API快速判断object的装箱类型。

## 基本概念

在JSVM-API中，装箱类型相关接口提供快速判断5种装箱类型的能力。

## 接口说明

| 接口 | 功能说明 |
| --- | --- |
| OH\_JSVM\_IsNumberObject | 判断是否是Number Object。 |
| OH\_JSVM\_IsBooleanObject | 判断是否是Boolean Object。 |
| OH\_JSVM\_IsBigIntObject | 判断是否是BigInt Object。 |
| OH\_JSVM\_IsStringObject | 判断是否是String Object。 |
| OH\_JSVM\_IsSymbolObject | 判断是否是Symbol Object。 |

## 使用示例

JSVM-API接口开发流程参考[使用JSVM-API实现JS与C/C++语言交互开发流程](use-jsvm-process.md)，本文仅展示接口对应的C++代码。

### 使用接口判断是否是Number Object

cpp部分代码：

```
1. #include <string>

3. static JSVM_Value WrapperObject(JSVM_Env env, JSVM_CallbackInfo info) {
4. JSVM_VM vm;
5. OH_JSVM_GetVM(env, &vm);

7. JSVM_HandleScope handleScope;
8. OH_JSVM_OpenHandleScope(env, &handleScope);
9. std::string src = R"JS(new Number(42))JS";
10. JSVM_Value jsSrc;
11. JSVM_Script script;
12. JSVM_Value result;

14. OH_JSVM_CreateStringUtf8(env, src.c_str(), JSVM_AUTO_LENGTH, &jsSrc);
15. OH_JSVM_CompileScript(env, jsSrc, nullptr, 0, true, nullptr, &script);
16. OH_JSVM_RunScript(env, script, &result);
17. bool isNumberObject = false;
18. OH_JSVM_IsNumberObject(env, result, &isNumberObject);
19. OH_LOG_INFO(LOG_APP, "JSVM OH_JSVM_IsNumberObject: %{public}d\n", isNumberObject);
20. OH_JSVM_CloseHandleScope(env, handleScope);

22. return nullptr;
23. }

25. static JSVM_CallbackStruct param[] = {
26. {.data = nullptr, .callback = WrapperObject},
27. };

29. static JSVM_CallbackStruct *method = param;

31. // wrapperObject方法别名，供JS调用
32. static JSVM_PropertyDescriptor descriptor[] = {
33. {"wrapperObject", nullptr, method++, nullptr, nullptr, nullptr, JSVM_DEFAULT},
34. };

36. // 样例测试JS
37. const char *srcCallNative = R"JS(wrapperObject();)JS";
```

预期输出：

```
1. JSVM OH_JSVM_IsNumberObject: 1
```
