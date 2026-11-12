---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-malloc-api-not-paired
title: Malloc API Not Paired
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Scanner代码检查规则 > CPP代码检查规则 > Malloc API Not Paired
category: harmonyos-guides
scraped_at: 2026-11-12T09:53:01+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:670cc26fb8a884820ff65ebd5165bcaf85538b8969aaa14bb6f839107b175b31
---

使用malloc()、calloc()或realloc()分配的内存，使用完毕后，需及时调用free()进行释放，避免申请的资源无法回收，造成内存泄漏。

## 规则配置

```json
// rules.json

{
  "rules": {
     "cpp": {
       "ResourceLeak": [
         {
           "ruleId": "Malloc API Not Paired",
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

#include <stdlib.h>
void AllocateMemoryWithFree() 
{
    int *arr = (int *)malloc(100 * sizeof(int));
    
    if (arr == nullptr) {
        return;
    }
    
    arr[0] = 10;
    
    // 正确释放内存
    free(arr);
    arr = nullptr;
}
void AllocateWithCallocWithFree() 
{
    char *buffer = (char *)calloc(256, sizeof(char));
    
    if (buffer == nullptr) {
        return;
    }
    
    // 使用 buffer...
    
    // 正确释放内存
    free(buffer);
    buffer = nullptr;
}
```

## 反例

```c
// 反例代码

#include <stdlib.h>
void AllocateMemoryWithoutFree() 
{
    // malloc 分配
    int *arr = (int *)malloc(100 * sizeof(int));
    
    if (arr == nullptr) {
        return;
    }
    
    arr[0] = 10;
    
    // 未释放 - 内存泄漏！
}
void AllocateWithCallocWithoutFree() 
{
    // calloc 分配
    char *buffer = (char *)calloc(256, sizeof(char));
    
    if (buffer == nullptr) {
        return;
    }
    
    // 使用 buffer...
    
    // 未释放 - 内存泄漏！
}
```

Code Scanner代码检查规则的配置指导请参考[1.6.3 代码检查工具（codescanner）](ide-command-line-codescanner.md)
