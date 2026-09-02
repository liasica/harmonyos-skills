---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-179
title: ASON.parse生成的Sendable对象和@Sendable注解类的实例对象的差异
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > 方舟编程语言（ArkTS） > ASON.parse生成的Sendable对象和@Sendable注解类的实例对象的差异
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:54+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:191e528759357dabcfaa6e81e3550d938ef8e372790208d3d3134239935d1ce9
---

## 问题现象

使用ArkTSUtils.ASON.parse生成的Sendable对象，和通过类（@Sendable装饰器）构造函数实例化出来的对象，有什么区别？

## 背景知识

[ASON解析与生成](../harmonyos-guides/ason-parsing-generation.md)：[ASON工具](../harmonyos-references/arkts-apis-arkts-utils-ason.md)提供了[Sendable对象](../harmonyos-guides/arkts-sendable.md)的序列化、反序列化能力。使用ASON.stringify方法可将对象转换为字符串，使用ASON.parse方法可将字符串转换为Sendable对象，从而实现对象在并发任务间的高性能引用传递。

## 解决方案

相同点：

* 都是Sendable对象，可以跨线程通信。
* 都可以获取和修改属性值，但是无法增加和删除。

不同点：ASON.parse生成的Sendable对象无法调用类成员方法。原因是使用ArkTSUtils.ASON.parse()解析JSON生成Sendable对象时，生成的仅是数据结构的副本，不会保留原始类的原型链和方法，所以无法调用方法。

```screen
import { ArkTSUtils, lang, taskpool } from '@kit.ArkTS';
import { BusinessError } from '@kit.BasicServicesKit';

@Sendable
class TestClass {
  name: string = 'Bob';
  age: number = 18;
  city: string = 'ct';

  info() {
    this.age += 1;
    console.info(`name: ${this.name} age: ${this.age} city: ${this.city}`);
  }
}

@Concurrent
function method(testClass: TestClass) {
  testClass.name = 'Cici';
  console.info('modify name to Cici');
}

@Entry
@Component
struct Index {
  build() {
    Column() {
      Button('ASON')
        .onClick(async () => {
          type ISendable = lang.ISendable;
          let jsonText = '{"name": "John", "age": 30, "city": "ct"}';
          let obj = ArkTSUtils.ASON.parse(jsonText) as ISendable;

          // 在线程中传递
          try {
            let task = new taskpool.Task(method, (obj as TestClass));
            await taskpool.execute(task);
            console.info((obj as TestClass).name); // 打印Cici
          } catch (e) {
            let err: BusinessError = e as BusinessError;
            console.error(`执行失败，${err.code}, ${err.message}`);
          }

          // 获取和修改属性值
          try {
            (obj as TestClass).name = 'Alice';
            console.info((obj as TestClass).name); // 打印Alice
            jsonText = ArkTSUtils.ASON.stringify(obj);
            console.info(`${jsonText}`); // 打印{"name":"Alice","age":30,"city":"ct"}
          } catch (e) {
            let err: BusinessError = e as BusinessError;
            console.error(`修改失败，${err.code}, ${err.message}`);
          }

          // 无法调用类成员方法
          try {
            (obj as TestClass).info();
            console.info('调用成功');
          } catch (e) {
            let err: BusinessError = e as BusinessError;
            console.error(`调用失败，${err.code}, ${err.message}`); // 无法调用，打印：调用失败，undefined, undefined is not callable
          }
        });
    }
    .height('100%')
    .width('100%')
    .justifyContent(FlexAlign.Center);
  }
}
```
