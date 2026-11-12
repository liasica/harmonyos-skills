---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-opencl_memobject-api-not-paired
title: OpenCL_MemObject API Not Paired
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Scanner代码检查规则 > CPP代码检查规则 > OpenCL_MemObject API Not Paired
category: harmonyos-guides
scraped_at: 2026-11-12T09:53:01+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:4ae49b4b5878bebc0eda04af6bfe8cd0d946253f83251220bf816b4c631aece3
---

使用clCreateBuffer()或clCreateImage()创建的OpenCL内存对象，使用完毕后，需及时调用clReleaseMemObject()进行释放，避免内存对象无法回收，造成内存泄漏。

## 规则配置

```json
// rules.json

{
  "rules": {
     "cpp": {
       "ResourceLeak": [
         {
           "ruleId": "OpenCL_MemObject API Not Paired",
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

#include <CL/cl.h>

void SecureBuffer(cl_context context)
{
    cl_int err;
    size_t bufferSize = 1024 * 1024;
    // 创建 Buffer
    cl_mem buffer = clCreateBuffer(context, CL_MEM_READ_WRITE, bufferSize, nullptr, &err);
    // 使用 buffer...
    
    // 正确销毁
    clReleaseMemObject(buffer);
}
void SecureImage(cl_context context)
{
    cl_image_format format = { CL_RGBA, CL_UNORM_INT8 };
    cl_image_desc desc = { CL_MEM_OBJECT_IMAGE2D, 1920, 1080, 0, 0, 0, 0, 0, 0, nullptr };
    cl_int err;
    // 创建 Image 对象（引用计数 = 1）
    cl_mem image = clCreateImage(context, CL_MEM_READ_WRITE, &format, &desc, nullptr, &err);
    // 使用 image...
    // 正确销毁
    clReleaseMemObject(image);
}
```

## 反例

```c
// 反例代码

#include <CL/cl.h>

void LeakBufferExample(cl_context context)
{
    cl_int err;
    size_t bufferSize = 1024 * 1024;
    // 创建 Buffer
    cl_mem buffer = clCreateBuffer(context, CL_MEM_READ_WRITE, bufferSize, nullptr, &err);
    // 使用 buffer...
    
    // 未释放 - 内存泄漏！
}
```

Code Scanner代码检查规则的配置指导请参考[1.6.3 代码检查工具（codescanner）](ide-command-line-codescanner.md)
