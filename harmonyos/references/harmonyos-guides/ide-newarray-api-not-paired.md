---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-newarray-api-not-paired
title: NewArray API Not Paired
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Scanner代码检查规则 > CPP代码检查规则 > NewArray API Not Paired
category: harmonyos-guides
scraped_at: 2026-11-12T09:53:01+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:8c15c33ede9679ba370423a344158e947496af6e61694c2485673670cfbab1de
---

使用operator new[]分配的数组内存，使用完毕后，需及时调用operator delete[]进行释放，避免申请的资源无法回收，造成内存泄漏。

## 规则配置

```json
// rules.json

{
  "rules": {
     "cpp": {
       "ResourceLeak": [
         {
           "ruleId": "NewArray API Not Paired",
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

class MyClass {
public:
    MyClass() {}
    ~MyClass() {}
};
void NewArrayWithDelete()
{
    MyClass *arr = new MyClass[100];
    
    // 使用 arr...
    
    // 正确释放数组内存
    delete[] arr;
    arr = nullptr;
}
```

## 反例

```c
// 反例代码

class MyClass {
public:
    MyClass() {}
    ~MyClass() {}
};
void NewArrayWithoutDelete() 
{
    // new[] 分配
    MyClass *arr = new MyClass[100];
    
    // 使用 arr...
    
    // 未释放 - 内存泄漏！
}
```

Code Scanner代码检查规则的配置指导请参考[1.6.3 代码检查工具（codescanner）](ide-command-line-codescanner.md)
