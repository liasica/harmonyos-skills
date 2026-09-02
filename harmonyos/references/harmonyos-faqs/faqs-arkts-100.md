---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-100
title: 如何对异步方法进行插桩/替换
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > ArkTS线程模型和并发 > 如何对异步方法进行插桩/替换
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:54+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:cfb23a7bafe09436be1a549ed48ab442be4b0416f2d24dae0895c572947933a2
---

开发者可通过Aspect类封装提供切面能力的接口，用于对类方法进行前后插桩或替换实现，其中[addBefore()](../harmonyos-references/js-apis-util.md#addbefore11)方法可在指定的类对象的原方法执行前插入一个函数，[replace()](../harmonyos-references/js-apis-util.md#replace11)方法可将指定类的原方法替换为另一个函数。

参考如下示例：

```ts
import { util } from '@kit.ArkTS';

class Test1 {
  static data: string = 'initData';

  static async printData(arg: string) { // asynchronous method
    console.log('execute original printData');
    console.log('Test.data is' + Test1.data);
    console.log('arg', arg);
    return 0;
  }
}

// Pile insertion
util.Aspect.addBefore(Test1, 'printData', true,
  (classObj: Object, arg: string): void => {
    console.log('execute before');
    Reflect.set(classObj, 'data', 'dataChangedByBefore');
    console.log('arg is ' + arg);
  }
);

Test1.printData('m1').then((res) => {
  console.log('res = ' + res.toString());
  console.log('Test.data = ' + Test1.data);
});

class Test2 {
  static data: string = 'initData';

  static async printData(arg: string) { // asynchronous method
    console.log('execute original printData');
    console.log('Test.data is' + Test2.data);
    console.log('arg', arg);
    return 0;
  }
}

// replace
util.Aspect.replace(Test2, 'printData', true,
  // Replace with another asynchronous function
  async (classObj: Object, arg: string): Promise<number> => {
    console.log('execute instead');
    Reflect.set(classObj, 'data', 'dataChangedByInstead');
    console.log('arg is ' + arg);
    return Promise.resolve(100);
  });

Test2.printData('m1').then((res) => {
  console.log('res = ' + res.toString());
  console.log('Test.data = ' + Test2.data);
});
```
