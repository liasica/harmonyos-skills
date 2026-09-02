---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-507
title: 如何通过PersistentStorage持久化储存把对象类型数据存储到硬盘里
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何通过PersistentStorage持久化储存把对象类型数据存储到硬盘里
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:17+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:a5f686ce88ff5c9cd0e78eddd7622383cd50d07bba7594ae14408afdeca439c4
---

## 问题现象

PersistentStorage本身不支持对象或者数组类型的存储，如何处理数据才能满足存储的条件，实现对象和数组类型的存储？

## 背景知识

* [AppStorage](../harmonyos-guides/arkts-appstorage.md)：应用全局的UI状态存储，是和应用的进程绑定的，由UI框架在应用程序启动时创建，为应用程序UI状态属性提供中央存储。
* [PersistentStorage](../harmonyos-guides/arkts-persiststorage.md)：持久化存储选定的AppStorage属性，以确保这些属性在应用程序重新启动时的值与应用程序关闭时的值相同。

因为PersistentStorage允许的类型为number，string，boolean，enum等简单类型，所以考虑转为string类型存储。JSON.stringify()可以将一个对象或值转换为JSON字符串，尝试利用该方法转成字符串后再存储。

## 解决方案

* **场景一**：储存没有方法的对象数组。

  对于没有方法的类，把数组数据通过JSON.stringify()转换为字符串，然后再进行存储。读取的时候，直接用JSON.parse()解析后进行使用即可。

  ```ts
  class SceneOneStudent {
    name: string;
    age: number;

    constructor(name: string, age: number) {
      this.name = name;
      this.age = age;
    }
  }

  PersistentStorage.persistProp('studentArr',
    JSON.stringify([new SceneOneStudent('Tom', 16), new SceneOneStudent('Gina', 18)]));

  @Entry
  @Component
  struct SceneOne {
    @State studentArr: Array<SceneOneStudent> = [];
    @StorageLink('studentArr') @Watch('onStrChange') studentArrStr: string = ' '; // 获取对象数组序列化字符串

    onStrChange() {
      this.studentArr = JSON.parse(this.studentArrStr);
    }

    aboutToAppear(): void {
      // 组件初始化时不会触发Watch事件，通过aboutToAppear事件来初始化数组
      this.studentArr = JSON.parse(this.studentArrStr);
    }

    build() {
      Column({ space: 8 }) {
        ForEach(this.studentArr, (item: SceneOneStudent) => {
          Column() {
            Text(`Student Name: ${item.name}`)
              .width('100%');
            Text(`Student Age: ${item.age}`)
              .width('100%');
          }
          .borderRadius(12)
          .width('100%')
          .backgroundColor(Color.White)
          .padding(16);
        }, (item: SceneOneStudent) => JSON.stringify(item));
      }
      .width('100%')
      .height('100%')
      .backgroundColor('# f1f3f5')
      .padding(12);
    }
  }
  ```
* **场景二**：储存自带方法的对象数组。

  对于有方法函数的类，需要先把字符串转成数据数组，然后调用类的构造函数利用每个数据创建出一个对象，这样创建的对象才有原型链，才能调用对应的方法。

  ```ts
  class SceneTwoStudent {
    name: string;
    age: number;

    constructor(name: string, age: number) {
      this.name = name;
      this.age = age;
    }

    selfIntroduction() {
      console.info(`My name is ${this.name} and I'm ${this.age} years old.`);
    }
  }

  PersistentStorage.persistProp('studentArr',
    JSON.stringify([new SceneTwoStudent('Tom', 16), new SceneTwoStudent('Gina', 18)]));

  @Entry
  @Component
  struct SceneTwo {
    @State studentArr: Array<SceneTwoStudent> = [];
    @StorageLink('studentArr') @Watch('onStrChange') studentArrStr: string = ' '; // 获取对象数组序列化的字符串

    onStrChange() {
      const dataArr: Array<SceneTwoStudent> = JSON.parse(this.studentArrStr); // 转化为对象数组
      this.studentArr = dataArr.map((item: SceneTwoStudent) => new SceneTwoStudent(item.name, item.age)); // 重新构造对象数组
    }

    aboutToAppear(): void {
      // 组件初始化时不会触发Watch事件，通过aboutToAppear事件来初始化数组
      const dataArr: Array<SceneTwoStudent> = JSON.parse(this.studentArrStr); // 转化为对象数组
      this.studentArr = dataArr.map((item: SceneTwoStudent) => new SceneTwoStudent(item.name, item.age)); // 重新构造对象数组
    }

    build() {
      Column({ space: 8 }) {
        ForEach(this.studentArr, (item: SceneTwoStudent) => {
          Column() {
            Text(`Student Name: ${item.name}`)
              .width('100%');
            Text(`Student Age: ${item.age}`)
              .width('100%');
            Button('Get Self-introduction')
              .onClick(() => {
                item.selfIntroduction();
              });
          }
          .borderRadius(12)
          .width('100%')
          .backgroundColor(Color.White)
          .padding(16);
        }, (item: SceneTwoStudent) => JSON.stringify(item));
      }
      .width('100%')
      .height('100%')
      .backgroundColor('# f1f3f5')
      .padding(12);
    }
  }
  ```

## 总结

想通过PersistentStorage把元素为对象的数组数据存储到硬盘中，需要用JSON.stringify()将对象转换为字符串，然后再进行存储。使用时根据类中是否包含方法对数据进行不同处理，对于没有方法的数据类，用JSON.parse()解析后使用即可；对于有方法的类，需要调用类的构造方法生成对象后，对象才能调用对应的方法，否则大概率会出现应用崩溃的情况。
