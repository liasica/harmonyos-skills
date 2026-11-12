---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-memorymap-api-not-paired
title: MemoryMap API Not Paired
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Scanner代码检查规则 > CPP代码检查规则 > MemoryMap API Not Paired
category: harmonyos-guides
scraped_at: 2026-11-12T09:53:01+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:1b5d9496e7714706e07a021fb9053ab5424b61f2466d034ac8af2b31902433ae
---

使用mmap()映射内存后，需及时调用munmap()解除映射，避免虚拟地址空间无法回收，造成内存泄漏。

## 规则配置

```json
// rules.json

{
  "rules": {
     "cpp": {
       "ResourceLeak": [
         {
           "ruleId": "MemoryMap API Not Paired",
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

#include <sys/mman.h>
#include <fcntl.h>
#include <unistd.h>
void MapMemoryWithUnmap() 
{
    int fd = open("/path/to/file", O_RDONLY);
    if (fd == -1) return;
    
    void *mapped = mmap(nullptr, 4096, PROT_READ, MAP_PRIVATE, fd, 0);
    
    if (mapped == MAP_FAILED) {
        close(fd);
        return;
    }
    
    // 使用 mapped...
    
    // 正确解除映射
    munmap(mapped, 4096);
    close(fd);
}
```

## 反例

```c
// 反例代码

#include <sys/mman.h>
#include <fcntl.h>
#include <unistd.h>
void MapMemoryWithoutUnmap() 
{
    int fd = open("/path/to/file", O_RDONLY);
    if (fd == -1) return;
    
    // 映射内存
    void *mapped = mmap(nullptr, 4096, PROT_READ, MAP_PRIVATE, fd, 0);
    
    if (mapped == MAP_FAILED) {
        close(fd);
        return;
    }
    
    // 使用 mapped...
    
    // 未解除映射 - 地址空间泄漏！
    close(fd);
}
```

Code Scanner代码检查规则的配置指导请参考[1.6.3 代码检查工具（codescanner）](ide-command-line-codescanner.md)
