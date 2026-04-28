---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-140
title: 如何实现匿名内部类
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > 方舟编程语言（ArkTS） > 如何实现匿名内部类
category: harmonyos-faqs
scraped_at: 2026-04-28T08:24:18+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:2ce8b1d188d20b9a6d045c9a81d841d36b737e73ef1c094aca19d0e111e27b6d
---

ArkTS不支持匿名类，建议使用嵌套类。匿名类创建的对象类型未知，与ArkTS不支持structural typing和对象字面量的规则冲突。示例如下：

```
1. class A {
2. foo() {
3. class B {
4. v: number = 123;
5. }
6. let b = new B();
7. }
8. }
```

[AnonymousInnerClass.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkTS/entry/src/main/ets/pages/AnonymousInnerClass.ets#L21-L28)

或者采用以下写法：

```
1. export interface AnonymousInnerClass<T> {
2. onSuccess: (t: T) => void;
3. onFailed: (code: string, reason: string) => void;
4. }

6. let AnonymousInnerClassInstance: AnonymousInnerClass<void> = {
7. onSuccess: () => {
8. console.log('success');
9. },
10. onFailed: () => {
11. console.log('failed');
12. }
13. }
```

[AnonymousInnerClass.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkTS/entry/src/main/ets/pages/AnonymousInnerClass.ets#L32-L44)
