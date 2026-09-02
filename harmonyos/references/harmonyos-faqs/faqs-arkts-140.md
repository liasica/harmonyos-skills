---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-140
title: 如何实现匿名内部类
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > 方舟编程语言（ArkTS） > 如何实现匿名内部类
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:53+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:3eab55f5a724024c33cc07e8dcb469c16e2b1d29a3230be17c9fe49d92cfc0f3
---

ArkTS不支持匿名类，建议使用嵌套类。匿名类创建的对象类型未知，与ArkTS不支持structural typing和对象字面量的规则冲突。示例如下：

```ts
class A {
  foo() {
    class B {
      v: number = 123;
    }
    let b = new B();
  }
}
```

或者采用以下写法：

```ts
export interface AnonymousInnerClass<T> {
  onSuccess: (t: T) => void;
  onFailed: (code: string, reason: string) => void;
}

let AnonymousInnerClassInstance: AnonymousInnerClass<void> = {
  onSuccess: () => {
    console.log('success');
  },
  onFailed: () => {
    console.log('failed');
  }
}
```
