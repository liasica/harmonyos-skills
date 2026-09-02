---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-113
title: 如何在ArkTS使用Reflect正确绑定this指针
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > 方舟编程语言（ArkTS） > 如何在ArkTS使用Reflect正确绑定this指针
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:53+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:c3bb958e3e08fe1db3718eba3cce61b49c4f7e3c904fc42f0cfbca77c34e8040
---

参考以下示例代码，注意只有对象的get/set方法才能绑定this指针。

```ts
class ReflectClass {
  private a = 'a';

  get getA() {
    return () => {
      return this.a;
    };
  }

  set setA(a: string) {
    this.a = a;
  }
}

function testInvoke() {
  const reflectClass = new ReflectClass();
  const fn: Function = Reflect.get(reflectClass, 'getA', reflectClass);
  console.info(fn());
}

@Entry
@Component
struct ReflectBoundThis {
  aboutToAppear(): void {
    testInvoke();
  }

  build() {
  }
}
```
