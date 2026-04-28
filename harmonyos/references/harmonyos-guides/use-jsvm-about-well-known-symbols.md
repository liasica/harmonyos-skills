---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/use-jsvm-about-well-known-symbols
title: 使用JSVM-API接口进行Well-known symbols相关开发
breadcrumb: 指南 > NDK开发 > 代码开发 > 使用JSVM-API实现JS与C/C++语言交互 > JSVM-API使用指导 > 使用JSVM-API接口进行Well-known symbols相关开发
category: harmonyos-guides
scraped_at: 2026-04-28T07:54:25+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:aa812c49d77ceda1d4722580e96e6f7069090ff949e96976340852714a1c3729
---

## 简介

JSVM-API中Well-known symbols相关接口可以通过不同API直接获取对应的11个Well-known symbols。

## 基本概念

在JSVM-API中，Well-known symbols相关接口能够给用户提供快速获取对应的11个Well-known symbols的能力。

## 接口说明

| 接口 | 功能说明 |
| --- | --- |
| OH\_JSVM\_GetSymbolToStringTag | 等价于JS中的Symbol.toStringTag。 |
| OH\_JSVM\_GetSymbolToPrimitive | 等价于JS中的Symbol.toPrimitive。 |
| OH\_JSVM\_GetSymbolSplit | 等价于JS中的Symbol.split。 |
| OH\_JSVM\_GetSymbolSearch | 等价于JS中的Symbol.search。 |
| OH\_JSVM\_GetSymbolReplace | 等价于JS中的Symbol.replace。 |
| OH\_JSVM\_GetSymbolMatch | 等价于JS中的Symbol.match。 |
| OH\_JSVM\_GetSymbolIsConcatSpreadable | 等价于JS中的Symbol.isConcatSpreadable。 |
| OH\_JSVM\_GetSymbolHasInstance | 等价于JS中的Symbol.hasInstance。 |
| OH\_JSVM\_GetSymbolUnscopables | 等价于JS中的Symbol.unscopables。 |
| OH\_JSVM\_GetSymbolAsyncIterator | 等价于JS中的Symbol.asyncIterator。 |
| OH\_JSVM\_GetSymbolIterator | 等价于JS中的Symbol.iterator。 |

## 使用示例

参考[使用JSVM-API实现JS与C/C++语言交互开发流程](use-jsvm-process.md)中的JSVM-API接口开发流程，本文仅展示接口对应的C++代码。

### 使用接口获取Well-known symbols（以OH\_JSVM\_GetSymbolToStringTag为例）

cpp部分代码：

```
1. #include <string>

3. static JSVM_Value WellKnownSymbols(JSVM_Env env, JSVM_CallbackInfo info) {
4. JSVM_VM vm;
5. OH_JSVM_GetVM(env, &vm);

7. JSVM_HandleScope handleScope;
8. OH_JSVM_OpenHandleScope(env, &handleScope);
9. std::string src = R"JS(Symbol.toStringTag)JS";
10. JSVM_Value jsSrc;
11. JSVM_Script script;
12. JSVM_Value result1;

14. OH_JSVM_CreateStringUtf8(env, src.c_str(), JSVM_AUTO_LENGTH, &jsSrc);
15. OH_JSVM_CompileScript(env, jsSrc, nullptr, 0, true, nullptr, &script);
16. OH_JSVM_RunScript(env, script, &result1);
17. JSVM_Value result2;
18. OH_JSVM_GetSymbolToStringTag(env, &result2);
19. bool is_equals = false;
20. OH_JSVM_StrictEquals(env, result1, result2, &is_equals);
21. OH_LOG_INFO(LOG_APP, "JSVM OH_JSVM_GetSymbolToStringTag result is correct : %{public}d\n", is_equals);
22. OH_JSVM_CloseHandleScope(env, handleScope);

24. return nullptr;
25. }

27. static JSVM_CallbackStruct param[] = {
28. {.data = nullptr, .callback = WellKnownSymbols},
29. };

31. static JSVM_CallbackStruct *method = param;

33. // wellKnownSymbols方法别名，供JS调用
34. static JSVM_PropertyDescriptor descriptor[] = {
35. {"wellKnownSymbols", nullptr, method++, nullptr, nullptr, nullptr, JSVM_DEFAULT},
36. };

38. // 样例测试JS
39. const char *srcCallNative = R"JS(wellKnownSymbols();)JS";
```

预期输出：

```
1. JSVM OH_JSVM_GetSymbolToStringTag result is correct : 1
```
