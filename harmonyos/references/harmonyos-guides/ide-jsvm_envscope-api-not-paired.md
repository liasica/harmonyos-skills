---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-jsvm_envscope-api-not-paired
title: JSVM_EnvScope API Not Paired
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Scanner代码检查规则 > CPP代码检查规则 > JSVM_EnvScope API Not Paired
category: harmonyos-guides
scraped_at: 2026-11-12T09:53:01+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:923ec31b1c74cf19b64df5b443af519a370da97e1c4e00eb26084d60bda8438a
---

使用OH\_JSVM\_OpenEnvScope()打开的环境作用域，使用完毕后，需及时调用OH\_JSVM\_CloseEnvScope()进行关闭，避免作用域内的对象无法回收，造成内存泄漏。

## 规则配置

```json
// rules.json

{
  "rules": {
     "cpp": {
       "ResourceLeak": [
         {
           "ruleId": "JSVM_EnvScope API Not Paired",
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
void OpenScopeWithClose(JSVM_Env env) 
{
    JSVM_EnvScope scope;
    
    if (OH_JSVM_OpenEnvScope(env, &scope) == JSVM_OK) {
        // 在作用域内进行 JSVM 操作...
        
        // 正确关闭作用域
        OH_JSVM_CloseEnvScope(env, scope);
    }
}
```

## 反例

```c
// 反例代码

#include <ark_runtime/jsvm.h>
void OpenScopeWithoutClose(JSVM_Env env) 
{
    JSVM_EnvScope scope;
    
    // 打开作用域
    OH_JSVM_OpenEnvScope(env, &scope);
    
    // 在作用域内进行 JSVM 操作...
    
    // 未关闭 - 内存泄漏！
}
```

Code Scanner代码检查规则的配置指导请参考[1.6.3 代码检查工具（codescanner）](ide-command-line-codescanner.md)
