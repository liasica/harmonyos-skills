---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-filedescriptor-api-not-paired
title: FileDescriptor API Not Paired
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Scanner代码检查规则 > CPP代码检查规则 > FileDescriptor API Not Paired
category: harmonyos-guides
scraped_at: 2026-11-12T09:53:01+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:f0dce924e1b621a11b6768b1f94245f4c39e88ce454341b18bb98c1d2aab22e7
---

使用open()打开的文件描述符，使用完毕后，需及时调用close()关闭，避免文件描述符无法回收，造成内存泄漏。

## 规则配置

```json
// rules.json

{
  "rules": {
     "cpp": {
       "ResourceLeak": [
         {
           "ruleId": "FileDescriptor API Not Paired",
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

#include <fcntl.h>
#include <unistd.h>
void OpenFileWithClose() 
{
    int fd = open("/path/to/file", O_RDONLY);
    
    if (fd == -1) {
        return;
    }
    
    // 读取文件...
    
    // 正确关闭文件描述符
    close(fd);
}
```

## 反例

```c
// 反例代码

#include <fcntl.h>
void OpenFileWithoutClose() 
{
    // 打开文件
    int fd = open("/path/to/file", O_RDONLY);
    
    if (fd == -1) {
        return;
    }
    
    // 读取文件...
    
    // 未关闭 - 文件描述符泄漏！
}
```

Code Scanner代码检查规则的配置指导请参考[1.6.3 代码检查工具（codescanner）](ide-command-line-codescanner.md)
