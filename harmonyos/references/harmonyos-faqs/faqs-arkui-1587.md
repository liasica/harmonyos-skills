---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1587
title: "@ObservedV2与@Trace装饰的对象key都带有__ob_导致反序列化异常"
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > @ObservedV2与@Trace装饰的对象key都带有__ob_导致反序列化异常
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:11+08:00
doc_updated_at: 2026-07-15
content_hash: sha256:91943e23b942ab51bcb699352b9dcdd53df4e797aa478f17388691e4a7538b5b
---

## 问题现象

@ObservedV2与@Trace装饰的对象key都带有\_\_ob\_导致反序列化出现异常，无法反序列化。

```text
"dateTimeGroup": {
    "__ob_beginDate": "2024-06-05",
    "__ob_beginTime": "17:00",
    "__ob_endDate": "2024-06-07",
    "__ob_endTime": "17:00"
}
```

## 背景知识

* 状态管理V2装饰器会为装饰的变量生成getter和setter方法，同时为原有变量名添加\_\_ob\_的前缀，出于性能考虑，[getTarget接口](../harmonyos-guides/arkts-new-gettarget.md)不会对V2装饰器生成的前缀进行处理，因此向getTarget接口传入@ObservedV2装饰的类对象实例时，返回的对象依旧为对象本身，且被@Trace装饰的属性名仍有\_\_ob\_前缀。详情请参考官方文档：[获取状态管理V2代理前的原始对象](../harmonyos-guides/arkts-new-gettarget.md#获取状态管理v2代理前的原始对象)。
* @ObservedV2的类实例无法直接使用JSON.parse反序列化获得（直接使用JSON.parse反序列化获得的对象无法观察属性变化），详情请参考[使用限制](../harmonyos-guides/arkts-new-observedv2-and-trace.md#使用限制)。

## 解决方案

\_\_ob\_前缀无法避免，且前缀不影响对象属性的getter和setter方法使用。如果涉及序列化与反序列化，可通过如下示例方法，将前缀去除。

* **方案一**：创建一个新的类，类中属性名和原来的对象相同，用原来对象的值来初始化新类的对象。

  ```ts
  @ObservedV2
  class FormDataClassV2 {
    @Trace name: string = '默认名称';
    @Trace price: number = 0;
  }

  class FormDataClass {
    name: string = '';
    price: number = 0;

    constructor(v: FormDataClassV2) {
      this.name = v.name;
      this.price = v.price;
    }
  }

  @Entry
  @ComponentV2
  struct FormDataClassPage {
    @Local data: FormDataClassV2 = new FormDataClassV2();

    build() {
      Column() {
        Button('序列化')
          .onClick(() => {
            console.info('序列化原始值：', JSON.stringify(this.data));
            console.info('序列化转换后：', JSON.stringify(new FormDataClass(this.data)));
          });
      }
      .height('100%')
      .width('100%');
    }
  }
  ```
* **方案二**：序列化后\_\_ob\_前缀会导致反序列化异常，可以考虑采用修改序列化后的字符串的方式，去除\_\_ob\_前缀。实现方式如下：

  ```ts
  @ObservedV2
  class FormDataClassV2 {
    @Trace name: string = '默认名称';
    @Trace price: number = 0;
  }

  @Entry
  @ComponentV2
  struct FormDataClassPage {
    @Local data: FormDataClassV2 = new FormDataClassV2();

    build() {
      Column() {
        Button('序列化')
          .onClick(() => {
            console.info('序列化原始值：', JSON.stringify(this.data));
            let newData = JSON.stringify(this.data).replace(/__ob_/g, '');
            console.info('序列化过滤后：', newData);
          });
      }
      .height('100%')
      .width('100%');
    }
  }
  ```

## 常见FAQ

Q：如何获取@ObservedV2与@Trace装饰的原始对象？

A：去除\_\_ob\_前缀后，使用JSON.parse反序列化即可，此时反序列化后的原始对象没有深度观测的能力。

Q：如何使反序列化后的对象可观测？

A：若需要序列化后的对象可观察，详情可参考官方文档：[@ObservedV2装饰对象的序列化与反序列化](../harmonyos-guides/arkts-new-observedv2-and-trace.md#observedv2装饰对象的序列化与反序列化)，或使用[makeObserved接口：将非观察数据变为可观察数据](../harmonyos-guides/arkts-new-makeobserved.md)。

Q：getTarget接口的使用场景有哪些？对@ObservedV2类是否有效？

A：getTarget主要用于获取状态管理（V1）代理对象的原始对象，修改原始对象数据不会触发UI刷新。典型场景包括：

使用场景如下：

* 类型比较或序列化：需要获取原始对象进行类型判断或数据转换。
* 三方库集成：需传递原始对象数据给不兼容代理的三方库。
* 批量修改数据：如数组排序、大量数据更新时，直接操作原始对象可避免代理层的性能开销。
