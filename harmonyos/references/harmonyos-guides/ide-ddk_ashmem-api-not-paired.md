---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ddk_ashmem-api-not-paired
title: DDK_Ashmem API Not Paired
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Scanner代码检查规则 > CPP代码检查规则 > DDK_Ashmem API Not Paired
category: harmonyos-guides
scraped_at: 2026-11-12T09:53:00+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:0999820e617213fad73fd36210f79a2be64a9260c13f5e95853ad73fe4711134
---

使用OH\_DDK\_CreateAshmem()创建的共享内存，使用完毕后，需及时调用OH\_DDK\_DestroyAshmem()进行销毁，避免共享内存资源无法回收，造成内存泄漏。

**说明** 

此规则要求使用2in1使用设备。

## 规则配置

```json
// rules.json

{
  "rules": {
     "cpp": {
       "ResourceLeak": [
         {
           "ruleId": "DDK_Ashmem API Not Paired",
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

#include "ddk/ddk_api.h"
void CreateAshmemWithDestroy() 
{
    const uint8_t *name = (uint8_t*)"shared_mem";
    uint32_t size = 1024;
    DDK_Ashmem *ashmem;
    
    // 创建共享内存
    DDK_RetCode ret = OH_DDK_CreateAshmem(name, size, &ashmem);
    
    if (ret != DDK_SUCCESS || ashmem == nullptr) {
        return;
    }
    
    // 使用 ashmem 进行跨进程数据共享...
    
    // 正确销毁共享内存
    OH_DDK_DestroyAshmem(ashmem);
}
```

## 反例

```c
// 反例代码

#include "ddk/ddk_api.h"
void CreateAshmemWithoutDestroy() 
{
    const uint8_t *name = (uint8_t*)"shared_mem";
    uint32_t size = 1024;
    DDK_Ashmem *ashmem;
    
    // 创建共享内存
    DDK_RetCode ret = OH_DDK_CreateAshmem(name, size, &ashmem);
    
    if (ret != DDK_SUCCESS || ashmem == nullptr) {
        return;
    }
    
    // 使用 ashmem...
    // 未销毁 - 内存泄漏！
}
```

Code Scanner代码检查规则的配置指导请参考[1.6.3 代码检查工具（codescanner）](ide-command-line-codescanner.md)

## 反例

```screen
// 反例代码
#include "web/arkweb_scheme_handler.h"
void CreateResponseWithoutDestroy()
{
    ArkWeb_Response *response;
    // 创建 ArkWeb 响应
    OH_ArkWeb_CreateResponse(&response);
    
    if (response == nullptr) {
        return;
    }
    
    // 使用 response...
    
    // 未销毁 - 内存泄漏！
}
```

Code Scanner代码检查规则的配置指导请参考[1.6.3 代码检查工具（codescanner）](ide-command-line-codescanner.md)
