---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-112
title: 如何判断对象的类型
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > 方舟编程语言（ArkTS） > 如何判断对象的类型
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:53+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:c891b6bef6d460f211e022a25e2fbeb434d27d9e3f07db18bbad37d09c92b88c
---

在代码开发中，如果需要对对象的类型做判断，调用不同类的方法，可以使用instanceof进行判断来得知对象的类型，参考代码如下：

```cpp
class BaseClass {
  value: number = 0;

  printf() {
    console.info('base value:' + this.value);
  }

  setValue(val: number) {
    this.value = val;
  }
}

class AClass extends BaseClass {
  value: number = 1;

  setValue(val: number) {
    this.value = val;
  }

  getValue(): number {
    return this.value;
  }
}

class BClass extends BaseClass {
  value: number = 2;

  setValue(val: number) {
    this.value = val;
  }
}

function printValue(base: BaseClass) {
  base.printf();
  let flag = base instanceof AClass;
  console.info('printValue flag:' + flag);
  if (flag) {
    let val = (base as AClass).getValue();
    console.info('printValue val:' + val);
  }
}

@Entry
@Component
struct DetermineObjectType {
  aboutToAppear(): void {
    printValue(new AClass());
    printValue(new BClass());
  }

  build() {
  }
}
```
