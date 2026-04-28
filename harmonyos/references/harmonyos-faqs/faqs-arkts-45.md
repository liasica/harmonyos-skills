---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-45
title: ArkTS类的方法是否支持重载
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > 方舟编程语言（ArkTS） > ArkTS类的方法是否支持重载
category: harmonyos-faqs
scraped_at: 2026-04-28T08:24:00+08:00
doc_updated_at: 2026-03-17
content_hash: sha256:15c903d7a405020d9a1bf87b7dfdad6b6bd9d10a23a74b1efca25552d8dffb6c
---

ArkTS支持TS中的重载，包括多个重载签名及一个实现签名。函数签名仅在编译期进行类型检查，不保留到运行时。

ArkTS不支持多个函数体的重载。示例如下：

```
1. // declare
2. function test(param: User): number;
3. function test(param: number, flag: boolean): number;
4. // implement
5. function test(param: User | number, flag?: boolean) {
6. if (typeof param === 'number') {
7. return param + (flag ? 1 : 0)
8. } else {
9. return param.age
10. }
11. }
```
