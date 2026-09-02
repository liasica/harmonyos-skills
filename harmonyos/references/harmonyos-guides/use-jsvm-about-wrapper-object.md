---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/use-jsvm-about-wrapper-object
title: 使用JSVM-API接口进行Wrapper object相关开发
breadcrumb: 指南 > NDK开发 > 代码开发 > 使用JSVM-API实现JS与C/C++语言交互 > JSVM-API使用指导 > 使用JSVM-API接口进行Wrapper object相关开发
category: harmonyos-guides
scraped_at: 2026-09-02T15:00:17+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:a3478f54849e782dc29af132c32b7827d7fd65907e80fa813420e35abf076658
---

## 简介

JSVM-API中，装箱类型（Wrapper object）判断相关接口支持通过不同API快速判断object的装箱类型。

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

```cpp
#include <string>

static JSVM_Value WrapperObject(JSVM_Env env, JSVM_CallbackInfo info) {
    JSVM_VM vm;
    OH_JSVM_GetVM(env, &vm);

    JSVM_HandleScope handleScope;
    OH_JSVM_OpenHandleScope(env, &handleScope);
    std::string src = R"JS(new Number(42))JS";
    JSVM_Value jsSrc;
    JSVM_Script script;
    JSVM_Value result;

    OH_JSVM_CreateStringUtf8(env, src.c_str(), JSVM_AUTO_LENGTH, &jsSrc);
    OH_JSVM_CompileScript(env, jsSrc, nullptr, 0, true, nullptr, &script);
    OH_JSVM_RunScript(env, script, &result);
    bool isNumberObject = false;
    OH_JSVM_IsNumberObject(env, result, &isNumberObject);
    OH_LOG_INFO(LOG_APP, "JSVM OH_JSVM_IsNumberObject: %{public}d\n", isNumberObject);
    OH_JSVM_CloseHandleScope(env, handleScope);

    return nullptr;
}

static JSVM_CallbackStruct param[] = {
    {.data = nullptr, .callback = WrapperObject},
};

static JSVM_CallbackStruct *method = param;

// wrapperObject方法别名，供JS调用
static JSVM_PropertyDescriptor descriptor[] = {
    {"wrapperObject", nullptr, method++, nullptr, nullptr, nullptr, JSVM_DEFAULT},
};

// 样例测试JS
const char *srcCallNative = R"JS(wrapperObject();)JS";
```

预期输出：

```txt
JSVM OH_JSVM_IsNumberObject: 1
```
