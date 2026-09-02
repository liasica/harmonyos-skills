---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-45
title: ArkTS类的方法是否支持重载
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > 方舟编程语言（ArkTS） > ArkTS类的方法是否支持重载
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:52+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:c63442e30f08ceb0d6564cedf6ec1873f4d8eb1881efff0448331ef5d2163b5f
---

ArkTS支持TS中的重载，包括多个重载签名及一个实现签名。函数签名仅在编译期进行类型检查，不保留到运行时。

ArkTS不支持多个函数体的重载。示例如下：

```typescript
// declare 
function test(param: User): number; 
function test(param: number, flag: boolean): number; 
// implement 
function test(param: User | number, flag?: boolean) { 
  if (typeof param === 'number') { 
    return param + (flag ? 1 : 0) 
  } else { 
    return param.age 
  } 
}
```
