---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-gl_buffer-api-not-paired
title: GL_Buffer API Not Paired
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Scanner代码检查规则 > CPP代码检查规则 > GL_Buffer API Not Paired
category: harmonyos-guides
scraped_at: 2026-11-12T09:53:01+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:ddaa5077681cc8a3819603b4c88b5c3085d07461172cf8a7316fd5e17c4083c8
---

使用glGenBuffers()生成的OpenGL缓冲区，使用完毕后，需及时调用glDeleteBuffers()进行删除，避免GPU内存无法回收，造成内存泄漏。

## 规则配置

```screen
// rules.json
{
  "rules": {
     "cpp": {
       "ResourceLeak": [
         {
           "ruleId": "GL_Buffer API Not Paired",
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

#include <GLES3/gl3.h>
void CreateGLBufferWithDelete() 
{
    GLuint buffer;
    
    glGenBuffers(1, &buffer);
    glBindBuffer(GL_ARRAY_BUFFER, buffer);
    glBufferData(GL_ARRAY_BUFFER, 1024, nullptr, GL_DYNAMIC_DRAW);
    
    // 使用 buffer...
    
    // 正确删除 GL 缓冲区
    glDeleteBuffers(1, &buffer);
}
```

## 反例

```c
// 反例代码

#include <GLES3/gl3.h>
void CreateGLBufferWithoutDelete() 
{
    GLuint buffer;
    
    // 生成缓冲区但未删除 - GPU 内存泄漏！
    glGenBuffers(1, &buffer);
    glBindBuffer(GL_ARRAY_BUFFER, buffer);
    glBufferData(GL_ARRAY_BUFFER, 1024, nullptr, GL_DYNAMIC_DRAW);
    
    // 使用 buffer...
    
    // 未删除 - GPU 内存泄漏！
}
```

Code Scanner代码检查规则的配置指导请参考[1.6.3 代码检查工具（codescanner）](ide-command-line-codescanner.md)
