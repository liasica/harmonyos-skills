---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-jsvm_reference_conut-api-not-paired
title: JSVM_Reference_Conut API Not Paired
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Scanner代码检查规则 > CPP代码检查规则 > JSVM_Reference_Conut API Not Paired
category: harmonyos-guides
scraped_at: 2026-11-12T09:53:01+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:3add460f130e98a60e9cfcf47ecb70a3296c995330621de0cda203904a983f3f
---

使用OH\_JSVM\_CreateReference()创建的JSVM引用，使用完毕后，需及时调用OH\_JSVM\_DeleteReference()进行删除，避免JavaScript值无法回收，造成内存泄漏。

## 规则配置

```json
// rules.json

{
  "rules": {
     "cpp": {
       "ResourceLeak": [
         {
           "ruleId": "JSVM_Reference_Conut API Not Paired",
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
void CreateRefWithDelete(JSVM_Env env, JSVM_Value value) 
{
    // 创建 JavaScript 对象
    JSVM_Value obj = nullptr;
    OH_JSVM_CreateObject(env, &obj);
    OH_JSVM_CreateStringUtf8(env, "UseReference", JSVM_AUTO_LENGTH, &value);
    OH_JSVM_SetNamedProperty(env, obj, "name", value);
    
    JSVM_Ref ref = nullptr;
    // 创建对JavaScript对象的引用
    JSVM_Status status = OH_JSVM_CreateReference(env, obj, 1, &ref);
    if (status != JSVM_OK) {
        return;
    }
    
    // 使用 ref...
    
    // 正确删除引用
    OH_JSVM_DeleteReference(env, ref);
    ref = nullptr;
}
```

## 反例

```c
// 反例代码

#include <ark_runtime/jsvm.h>
void CreateRefWithoutDelete(JSVM_Env env, JSVM_Value value) 
{
    // 创建 JavaScript 对象
    JSVM_Value obj = nullptr;
    OH_JSVM_CreateObject(env, &obj);
    OH_JSVM_CreateStringUtf8(env, "UseReference", JSVM_AUTO_LENGTH, &value);
    OH_JSVM_SetNamedProperty(env, obj, "name", value);
    
    JSVM_Ref ref = nullptr;
    // 创建对JavaScript对象的引用
    JSVM_Status status = OH_JSVM_CreateReference(env, obj, 1, &ref);
    if (status != JSVM_OK) {
        return;
    }
    
    // 使用 ref...
    // 未删除 - 内存泄漏！
}
```

Code Scanner代码检查规则的配置指导请参考[1.6.3 代码检查工具（codescanner）](ide-command-line-codescanner.md)
