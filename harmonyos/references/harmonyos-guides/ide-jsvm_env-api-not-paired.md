---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-jsvm_env-api-not-paired
title: JSVM_Env API Not Paired
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Scanner代码检查规则 > CPP代码检查规则 > JSVM_Env API Not Paired
category: harmonyos-guides
scraped_at: 2026-11-12T09:53:01+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:6959e1abccf2ef5f2aa0ba160df4756cd821602d280b89661839062cf2002cfd
---

使用OH\_JSVM\_CreateEnv()创建的 JSVM 环境，使用完毕后，需及时调用OH\_JSVM\_DestroyEnv()进行销毁，避免环境对象及其资源无法回收，造成内存泄漏。

## 规则配置

```json
// rules.json

{
  "rules": {
     "cpp": {
       "ResourceLeak": [
         {
           "ruleId": "JSVM_Env API Not Paired",
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
void CreateAndDestroyEnv(JSVM_VM vm) 
{
    JSVM_Env env = nullptr;
    
    JSVM_Status status = OH_JSVM_CreateEnv(vm, 0, nullptr, &env);
    
    if (status != JSVM_OK || env == nullptr) {
        return;
    }
    
    // 使用 env...
    
    // 正确销毁环境
    OH_JSVM_DestroyEnv(env);
}
```

## 反例

```c
// 反例代码

#include <ark_runtime/jsvm.h>
void CreateEnvWithoutDestroy(JSVM_VM vm) 
{
    JSVM_Env env = nullptr;
    // 创建环境
    OH_JSVM_CreateEnv(vm, 0, nullptr, &env);
    
    if (env == nullptr) {
        return;
    }
    
    // 使用 env...
    
    // 销毁 - 内存泄漏！
}
```

Code Scanner代码检查规则的配置指导请参考[1.6.3 代码检查工具（codescanner）](ide-command-line-codescanner.md)
