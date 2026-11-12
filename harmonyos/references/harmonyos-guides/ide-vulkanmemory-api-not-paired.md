---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-vulkanmemory-api-not-paired
title: VulkanMemory API Not Paired
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Scanner代码检查规则 > CPP代码检查规则 > VulkanMemory API Not Paired
category: harmonyos-guides
scraped_at: 2026-11-12T09:53:01+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:c7faf7568a2c4f47b45fcba2888086cf4d243ac75cc26c8c92c17ae787e06b44
---

使用vkAllocateMemory()分配的Vulkan内存，使用完毕后，需及时调用vkFreeMemory()进行释放，避免GPU内存无法回收，造成内存泄漏。

## 规则配置

```json
// rules.json

{
  "rules": {
     "cpp": {
       "ResourceLeak": [
         {
           "ruleId": "VulkanMemory API Not Paired",
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

#include <vulkan/vulkan.h>
void AllocateVulkanMemoryWithFree(VkDevice device) 
{
    VkMemoryAllocateInfo allocInfo = {};
    allocInfo.sType = VK_STRUCTURE_TYPE_MEMORY_ALLOCATE_INFO;
    allocInfo.allocationSize = 1024;
    
    VkDeviceMemory memory;
    
    vkAllocateMemory(device, &allocInfo, nullptr, &memory);
    
    // 使用 memory...
    
    // 正确释放 Vulkan 内存
    vkFreeMemory(device, memory, nullptr);
}
```

## 反例

```c
// 反例代码

#include <vulkan/vulkan.h>
void AllocateVulkanMemoryWithoutFree(VkDevice device) 
{
    VkMemoryAllocateInfo allocInfo = {};
    allocInfo.sType = VK_STRUCTURE_TYPE_MEMORY_ALLOCATE_INFO;
    allocInfo.allocationSize = 1024;
    
    VkDeviceMemory memory;
    
    // 分配内存但
    vkAllocateMemory(device, &allocInfo, nullptr, &memory);
    
    // 使用 memory...
    // 未释放 - GPU 内存泄漏！
}
```

Code Scanner代码检查规则的配置指导请参考[1.6.3 代码检查工具（codescanner）](ide-command-line-codescanner.md)
