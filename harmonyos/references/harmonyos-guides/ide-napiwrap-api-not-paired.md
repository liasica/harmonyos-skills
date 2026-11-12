---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-napiwrap-api-not-paired
title: NapiWrap API Not Paired
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Scanner代码检查规则 > CPP代码检查规则 > NapiWrap API Not Paired
category: harmonyos-guides
scraped_at: 2026-11-12T09:53:01+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:b7d3a05b43590751c6015329411154140996ab261ba79fc063ad875d7605f548
---

在Node-API中使用napi\_wrap将C++原生对象关联到JavaScript对象时，需要正确配对使用napi\_wrap和napi\_remove\_wrap，以避免原生对象无法回收，造成内存泄漏。

## 规则配置

```json
// rules.json

{
  "rules": {
     "cpp": {
       "ResourceLeak": [
         {
           "ruleId": "NapiWrap API Not Paired",
           "severity": "error",
           "skip": false
         }
       ]
     }
   }
}
```

## 正例

```c
// 正例代码

#include "napi/native_api.h"
class MyNativeClass {
public:
    MyNativeClass() { }
    ~MyNativeClass() { }
};
static void DerefItem(napi_env env, void *data, void *hint)
{
    MyNativeClass *obj = reinterpret_cast<MyNativeClass *>(data);
    if (obj != nullptr) {
        delete obj;
    }
}
static void WrapObject(napi_env env, napi_callback_info info) 
{
    napi_value thisVar;
    napi_get_cb_info(env, info, nullptr, nullptr, &thisVar, nullptr);
    napi_ref* result;
    MyNativeClass* nativeObj = new MyNativeClass();
    
    // 申请包装
    napi_wrap(env, thisVar, nativeObj, DerefItem, nullptr, result);
    
    void* nativePtr = nullptr;
    napi_get_cb_info(env, info, nullptr, nullptr, &thisVar, nullptr);
    // 逻辑操作
    // ......
    
    
    napi_remove_wrap(env, thisVar, &nativePtr);  // 正确释放
    
    if (nativePtr != nullptr) {
        delete static_cast<MyNativeClass*>(nativePtr);
    }
}
```

## 反例

```c
// 反例代码

#include "napi/native_api.h"
class MyNativeClass {
public:
    MyNativeClass() { }
    ~MyNativeClass() { }
};
static void DerefItem(napi_env env, void *data, void *hint)
{
    MyNativeClass *obj = reinterpret_cast<MyNativeClass *>(data);
    if (obj != nullptr) {
        delete obj;
    }
}
static void WrapObject(napi_env env, napi_callback_info info) 
{
    napi_value thisVar;
    napi_get_cb_info(env, info, nullptr, nullptr, &thisVar, nullptr);
    napi_ref* result;
    MyNativeClass* nativeObj = new MyNativeClass();
    
    // 申请包装
    napi_wrap(env, thisVar, nativeObj, DerefItem, nullptr, result);
    // 未释放 - 内存泄漏！
}
```

Code Scanner代码检查规则的配置指导请参考[1.6.3 代码检查工具（codescanner）](ide-command-line-codescanner.md)
