---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/use-longque-js-api
title: Longque-JS-API使用指导
breadcrumb: 指南 > NDK开发 > 代码开发 > Longque-JS-API > Longque-JS-API使用指导
category: harmonyos-guides
scraped_at: 2026-09-02T15:00:17+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:9ccf52db43c83bf1ae94cac20fa520446d0e04bc5e09c096892dcb2ad20dd239
---

Longque JS API 由 Longque JS Engine 提供，适用于在 HarmonyOS 平台构建稳定、高性能的应用。所有 API 均位于 \_\_Longque\_\_ 对象下。接口的版本可通过 \_\_Longque\_\_.version 获得，开发者可使用该版本进行特性判断。

**【注意】：Longque JS API 处于实验阶段，使用前请阅读本文档，评估其稳定性和兼容性。**

## 接口说明

| 接口 | 功能说明 |
| --- | --- |
| createDelegate | 创建委托 |

## 属性说明

| 属性 | 功能说明 |
| --- | --- |
| version | 用于表示 Longque JS API 的版本 |
| SKIP\_PROTOTYPE\_CHAIN | createDelegate 的属性过滤器，表示只委托自身属性，不考虑原型链 |
| SKIP\_PREFIX\_UNDERSCORE | createDelegate 的属性过滤器，表示过滤掉名字以 '\_' 开头的属性 |
| SKIP\_PREFIX\_DOLLAR | createDelegate 的属性过滤器，表示过滤掉名字以 '$' 开头的属性 |
| SKIP\_CONSTRUCTOR | createDelegate 的属性过滤器，表示过滤掉 'constructor' 属性 |

## createDelegate接口

接口引入版本 : 1

### 接口描述

| 接口 | 名称 | 说明 |
| --- | --- | --- |
| createDelegate | 创建委托 | 创建 underlyingObject 的委托对象，对委托对象的属性读写操作将映射至 underlyingObject。通过 initObject 指定初始委托对象，通过 propertyFilterFlags 指定属性过滤器。默认情况下，将映射 underlyingObject 及其原型链上所有可枚举的字符串键属性。 |

### 参数

(1) underlyingObject： 必选参数。表示被委托的底层对象。参数要求：

* underlyingObject 必须是对象，否则会抛出 TypeError 异常。
* 若 underlyingObject 是代理对象，将抛出 TypeError 异常。
* 若未指定 SKIP\_PROTOTYPE\_CHAIN 过滤器，且 underlyingObject 原型链上存在代理对象，则抛出 TypeError 异常。

(2) initObject：可选参数。表示初始委托对象。若传入 undefined，表示不指定初始对象，将由接口自动创建。参数要求：

* initObject 必须是对象，否则会抛出 TypeError 异常。
* 若 initObject 是代理对象，将抛出 TypeError 异常。
* 不能将委托对象作为 initObject，否则抛出 TypeError 异常。
* 若 initObject 是不可扩展的，则抛出 TypeError 异常。
* 若 initObject 中某些属性无法定义，将抛出 TypeError 异常，此时 initObject 中仅部分属性定义成功。

(3) propertyFilterFlags：可选参数。表示属性过滤器。如果传入的是 undefined，表示不指定过滤器。参数要求：

* 以下列出了当前支持的属性过滤器（未来可能扩展）。

```sh
__Longque__.SKIP_PROTOTYPE_CHAIN: 只委托 underlyingObject 自身属性，不考虑原型链
__Longque__.SKIP_PREFIX_UNDERSCORE: 过滤掉名字以 '_' 开头的属性
__Longque__.SKIP_PREFIX_DOLLAR: 过滤掉名字以 '$' 开头的属性
__Longque__.SKIP_CONSTRUCTOR: 过滤掉 'constructor' 属性
```

* 必须使用列出的过滤器，否则接口行为未定义，可能导致代码兼容性问题。
* 所有过滤器均为 number 类型，可用 | 运算符同时指定多个。
* 若 propertyFilterFlags 非 number 类型，抛出 TypeError 异常。

### 返回值

只有接口在不抛出异常的情况下，才会正确返回：

* 若未指定初始委托对象，返回新创建的委托对象。
* 若已指定初始委托对象，返回该初始委托对象。

### 注意事项

(1) 委托对象的属性顺序可能与 for-in、Object.keys 方法的结果不一致，请勿依赖属性顺序。

(2) 委托对象的实现是引擎内部机制。请勿依赖在委托对象上调用 Object.getOwnPropertyDescriptor、getOwnPropertyDescriptors、Reflect.getOwnPropertyDescriptor 等接口的返回结果。

### 使用示例

本示例展示了在 JSVM 中使用 Longque JS API 的方式，JSVM-API 接口开发流程参考[使用JSVM-API实现JS与C/C++语言交互开发流程](use-jsvm-process.md)，本文仅对接口对应C++相关代码进行展示。

cpp部分代码：

```cpp
// 待执行的js代码
static const char *STR_TASK = R"JS(
  function createDelegateTest() {
    var myobj = {
      42: 0,
      x: 1,
      _y: 2,
      $z:3
    };

    var proto = {
      foo: 'foo'
    };
    Object.setPrototypeOf(myobj, proto);

    var d1 = __Longque__.createDelegate(myobj, undefined);
    consoleinfo(JSON.stringify(d1)); // {"42":0,"x":1,"_y":2,"$z":3,"foo":"foo"}

    const propertyFilterFlags = __Longque__.SKIP_PREFIX_UNDERSCORE | __Longque__.SKIP_PREFIX_DOLLAR;
    var d2 = __Longque__.createDelegate(myobj, undefined, propertyFilterFlags);
    consoleinfo(JSON.stringify(d2)); // {"42":0,"x":1,"foo":"foo"}

    d2[42] = 100;

    const newFilter = propertyFilterFlags | __Longque__.SKIP_PROTOTYPE_CHAIN;
    var d3 = __Longque__.createDelegate(myobj, undefined, newFilter);
    consoleinfo(JSON.stringify(d3)); // {"42":100,"x":1}
  }
  createDelegateTest();
)JS";

// 保证js代码中的打印信息可以正常输出
static JSVM_Value ConsoleInfo(JSVM_Env env, JSVM_CallbackInfo info) {
    size_t argc = 1;
    JSVM_Value args[1];
    char log[256] = "";
    size_t logLength = 0;
    JSVM_CALL(OH_JSVM_GetCbInfo(env, info, &argc, args, NULL, NULL));

    OH_JSVM_GetValueStringUtf8(env, args[0], log, 255, &logLength);
    log[255] = 0;
    OH_LOG_INFO(LOG_APP, "JSVM API TEST: %{public}s", log);
    return nullptr;
}

// 注册consoleinfo的方法
JSVM_CallbackStruct param[] = {
    {.data = nullptr, .callback = ConsoleInfo},
};
JSVM_PropertyDescriptor descriptor[] = {
    {"consoleinfo", NULL, &param[0], NULL, NULL, NULL, JSVM_DEFAULT},
};

static int32_t TestJSVM() {
    JSVM_InitOptions init_options;
    memset(&init_options, 0, sizeof(init_options));
    if (g_aa == 0) {
        OH_JSVM_Init(&init_options);
        g_aa++;
    }
    // 创建JavaScript虚拟机实例，打开虚拟机作用域
    JSVM_VM vm;
    JSVM_CreateVMOptions options;
    memset(&options, 0, sizeof(options));
    CHECK(OH_JSVM_CreateVM(&options, &vm));
    JSVM_VMScope vm_scope;
    CHECK(OH_JSVM_OpenVMScope(vm, &vm_scope));

    JSVM_Env env;
    CHECK(OH_JSVM_CreateEnv(vm, sizeof(descriptor) / sizeof(descriptor[0]), descriptor, &env));
    JSVM_EnvScope envScope;
    CHECK_RET(OH_JSVM_OpenEnvScope(env, &envScope));
    JSVM_HandleScope handlescope;
    CHECK_RET(OH_JSVM_OpenHandleScope(env, &handlescope));
    JSVM_Value sourcecodevalue;
    CHECK_RET(OH_JSVM_CreateStringUtf8(env, STR_TASK, strlen(STR_TASK), &sourcecodevalue));
    JSVM_Script script;
    CHECK_RET(OH_JSVM_CompileScript(env, sourcecodevalue, nullptr, 0, true, nullptr, &script));
    JSVM_Value result;
    CHECK_RET(OH_JSVM_RunScript(env, script, &result));

    // 关闭并销毁环境和虚拟机
    CHECK_RET(OH_JSVM_CloseHandleScope(env, handlescope));
    CHECK_RET(OH_JSVM_CloseEnvScope(env, envScope));
    CHECK(OH_JSVM_DestroyEnv(env));
    CHECK(OH_JSVM_CloseVMScope(vm, vm_scope));
    CHECK(OH_JSVM_DestroyVM(vm));
    return 0;
}
```

预期的输出：

```ts
JSVM API TEST: {"42":0,"x":1,"_y":2,"$z":3,"foo":"foo"}
JSVM API TEST: {"42":0,"x":1,"foo":"foo"}
JSVM API TEST: {"42":100,"x":1}
```

### 性能测试示例

本示例用于测试使用Longque JS API前后的性能。

cpp部分代码：

```cpp
// 待执行的js代码
static const char *STR_TASK = R"JS(
  // 原始js代码
  function base(underlying) {
    var obj = {};
    var tryDefineProperty = function (key) {
      if (key.indexOf('_') === 0 || key.indexOf('$') === 0 || key === 'constructor') {
        return false;
      }
      Object.defineProperty(obj, key, {
        configurable: true,
        enumerable: true,
        get: function get() {
          return underlying[key];
        },
        set: function set(value) {
          return (underlying[key] = value);
        },
      });
      return true;
    };
    for (var key in underlying) {
      if (!tryDefineProperty(key)) {
        continue;
      }
    }
    return obj;
  }

  // 使用Longque JSVM API之后的代码
  function opt(underlying) {
    var delegate = __Longque__.createDelegate(
      underlying,
      undefined,
      __Longque__.SKIP_PREFIX_UNDERSCORE |
      __Longque__.SKIP_PREFIX_DOLLAR |
      __Longque__.SKIP_CONSTRUCTOR,
    );
    return delegate;
  }

  // 性能测试
  function doTest(tag, func, underlying, times) {
    const begin = Date.now();
    var obj = null;
    for (var i = 0; i < times; ++i) {
      obj = func(underlying);
    }
    const end = Date.now();
    consoleinfo(`[${tag}] Time cost: ${(end - begin).toFixed(0)} ms`);
    return obj;
  }

  function testEntry() {
    var underlying = {
      x: 1,
      y: 2,
      foo: 'foo',
      _bar: '_bar',
      _hi: '_hi',
      $test: '$test',
      constructor: 'ctor',
      pi: 3.14,
    };
    for (var i = 0; i < 100; ++i) {
      underlying[`key_${i}`] = i;
    }
    const n = 10000;
    // 测试原js代码的运行时间
    doTest('base', base, underlying, n);
    // 测试使用Longque JSVM API之后的运行时间
    doTest('opt', opt, underlying, n);
  }

  testEntry();
)JS";

// 保证js代码中的打印信息可以正常输出
static JSVM_Value ConsoleInfo(JSVM_Env env, JSVM_CallbackInfo info) {
    size_t argc = 1;
    JSVM_Value args[1];
    char log[256] = "";
    size_t logLength = 0;
    JSVM_CALL(OH_JSVM_GetCbInfo(env, info, &argc, args, NULL, NULL));
  
    OH_JSVM_GetValueStringUtf8(env, args[0], log, 255, &logLength);
    log[255] = 0;
    OH_LOG_INFO(LOG_APP, "JSVM API TEST: %{public}s", log);
    return nullptr;
}

// 注册consoleinfo的方法
JSVM_CallbackStruct param[] = {
    {.data = nullptr, .callback = ConsoleInfo},
};
JSVM_PropertyDescriptor descriptor[] = {
    {"consoleinfo", NULL, &param[0], NULL, NULL, NULL, JSVM_DEFAULT},
};

static int32_t TestJSVM() {
    JSVM_InitOptions init_options;
    memset(&init_options, 0, sizeof(init_options));
    if (g_aa == 0) {
        OH_JSVM_Init(&init_options);
        g_aa++;
    }
    // 创建JavaScript虚拟机实例，打开虚拟机作用域
    JSVM_VM vm;
    JSVM_CreateVMOptions options;
    memset(&options, 0, sizeof(options));
    CHECK(OH_JSVM_CreateVM(&options, &vm));
    JSVM_VMScope vm_scope;
    CHECK(OH_JSVM_OpenVMScope(vm, &vm_scope));
  
    JSVM_Env env;
    CHECK(OH_JSVM_CreateEnv(vm, sizeof(descriptor) / sizeof(descriptor[0]), descriptor, &env));
    JSVM_EnvScope envScope;
    CHECK_RET(OH_JSVM_OpenEnvScope(env, &envScope));
    JSVM_HandleScope handlescope;
    CHECK_RET(OH_JSVM_OpenHandleScope(env, &handlescope));
    JSVM_Value sourcecodevalue;
    CHECK_RET(OH_JSVM_CreateStringUtf8(env, STR_TASK, strlen(STR_TASK), &sourcecodevalue));
    JSVM_Script script;
    CHECK_RET(OH_JSVM_CompileScript(env, sourcecodevalue, nullptr, 0, true, nullptr, &script));
    JSVM_Value result;
    CHECK_RET(OH_JSVM_RunScript(env, script, &result));
  
    // 关闭并销毁环境和虚拟机
    CHECK_RET(OH_JSVM_CloseHandleScope(env, handlescope));
    CHECK_RET(OH_JSVM_CloseEnvScope(env, envScope));
    CHECK(OH_JSVM_DestroyEnv(env));
    CHECK(OH_JSVM_CloseVMScope(vm, vm_scope));
    CHECK(OH_JSVM_DestroyVM(vm));
    return 0;
}
```

某次测试的输出：

```ts
JSVM API TEST: [base] Time cost: 414 ms
JSVM API TEST: [opt] Time cost: 148 ms
```
