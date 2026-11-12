---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-jsvm_reference-api-not-paired
title: JSVM_Reference API Not Paired
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Scanner代码检查规则 > CPP代码检查规则 > JSVM_Reference API Not Paired
category: harmonyos-guides
scraped_at: 2026-11-12T09:53:01+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:b31925aa7eb8f310cebba6e24826f40bfadc68d550aba6e4c13ba73be019983d
---

使用OH\_JSVM\_ReferenceRef()增加的JSVM 引用计数，使用完毕后，需及时调用OH\_JSVM\_ReferenceUnref()对应地减少引用计数，避免JavaScript对象无法回收，造成内存泄漏。

## 规则配置

```json
// rules.json

{
  "rules": {
     "cpp": {
       "ResourceLeak": [
         {
           "ruleId": "JSVM_Reference API Not Paired",
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

#include <ark_runtime/jsvm.h>
void IncreaseRefWithDecrease(JSVM_Env env) 
{
    // 创建 JavaScript 对象
    JSVM_Value obj = nullptr;
    OH_JSVM_CreateObject(env, &obj);
    JSVM_Value value = nullptr;
    OH_JSVM_CreateStringUtf8(env, "UseReference", JSVM_AUTO_LENGTH, &value);
    OH_JSVM_SetNamedProperty(env, obj, "name", value);
    
    JSVM_Ref ref = nullptr;
    // 创建对JavaScript对象的引用
    JSVM_Status status = OH_JSVM_CreateReference(env, obj, 1, &ref);
    if (status != JSVM_OK) {
        return;
    }
    // 增加引用计数
    uint32_t result = 0u;
    OH_JSVM_ReferenceRef(env, ref, &result);
    
    // 使用 jsRef...
    
    // 减少传入引用的引用计数并返回生成的引用计数
    uint32_t num = 0u;
    OH_JSVM_ReferenceUnref(env, ref, &num);
    
    // 不再使用引用，通过调用OH_JSVM_DeleteReference删除对JavaScript对象的引用
    status = OH_JSVM_DeleteReference(env, ref);
}
```

## 反例

```c
// 反例代码

#include <ark_runtime/jsvm.h>
void IncreaseRefWithoutDecrease(JSVM_Env env) 
{
    // 创建 JavaScript 对象
    JSVM_Value obj = nullptr;
    OH_JSVM_CreateObject(env, &obj);
    JSVM_Value value = nullptr;
    OH_JSVM_CreateStringUtf8(env, "UseReference", JSVM_AUTO_LENGTH, &value);
    OH_JSVM_SetNamedProperty(env, obj, "name", value);
    
    JSVM_Ref ref = nullptr;
    // 创建对JavaScript对象的引用
    JSVM_Status status = OH_JSVM_CreateReference(env, obj, 1, &ref);
    if (status != JSVM_OK) {
        return;
    }
    // 增加引用计数
    uint32_t result = 0u;
    OH_JSVM_ReferenceRef(env, ref, &result);
    
    // 使用 jsRef...
    
    // 未对应减少 - 内存泄漏！
}
```

Code Scanner代码检查规则的配置指导请参考[1.6.3 代码检查工具（codescanner）](ide-command-line-codescanner.md)
