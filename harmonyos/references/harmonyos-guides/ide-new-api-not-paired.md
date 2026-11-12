---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-new-api-not-paired
title: New API Not Paired
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Scanner代码检查规则 > CPP代码检查规则 > New API Not Paired
category: harmonyos-guides
scraped_at: 2026-11-12T09:53:01+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:d237acd7cece33773478993f80c4d23f21bcbf1acc1880640274e1822cf36a98
---

使用operator new[]分配的内存，使用完毕后，需及时调用operator delete[]进行释放，避免申请的资源无法回收，造成内存泄漏。

## 规则配置

```json
// rules.json

{
  "rules": {
     "cpp": {
       "ResourceLeak": [
         {
           "ruleId": "New API Not Paired",
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

#include <new>
class MyClass {
public:
    MyClass() {}
    ~MyClass() {}
};
void NewWithDelete() 
{
    MyClass *obj = new MyClass();
    
    // 使用 obj...
    
    // 正确释放内存
    delete obj;
    obj = nullptr;
}
void NewNoThrowWithDelete() 
{
    MyClass *obj = new (std::nothrow) MyClass();
    
    if (obj == nullptr) {
        return;
    }
    
    // 使用 obj...
    
    // 正确释放内存
    delete obj;
    obj = nullptr;
}
```

## 反例

```c
// 反例代码

#include <new>
class MyClass {
public:
    MyClass() {}
    ~MyClass() {}
};
void NewWithoutDelete() 
{
    // new 分配
    MyClass *obj = new MyClass();
    
    // 使用 obj...
    
    // 未释放 - 内存泄漏！
}
void NewNoThrowWithoutDelete() 
{
    // nothrow 版本
    MyClass *obj = new (std::nothrow) MyClass();
    
    if (obj == nullptr) {
        return;
    }
    
    // 使用 obj...
    
    // 未释放 - 内存泄漏！
}
```

Code Scanner代码检查规则的配置指导请参考[1.6.3 代码检查工具（codescanner）](ide-command-line-codescanner.md)
