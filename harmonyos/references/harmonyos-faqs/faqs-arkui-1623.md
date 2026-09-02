---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1623
title: 接收网络数据时，如何解决无法刷新@LocalBuilder装饰的组件的问题
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 接收网络数据时，如何解决无法刷新@LocalBuilder装饰的组件的问题
category: harmonyos-faqs
scraped_at: 2026-09-02T15:03:49+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:8ffa5bb7730d1733b2bbaaead26f312be848bdc8adbde124ef0a61f7ad832ba3
---

## 问题现象

已采用@ObservedV2/@Trace修饰嵌套类和UIUtils.makeObserved对接收的数据转化为可深度观测的状态变量的情况下，目前this.person在aboutToAppear中的修改，以及后续onClick中的修改中，无法触发LocalBuilder中UI刷新。什么原因导致的无法刷新，且应该如何实现LocalBuilder中UI刷新？

代码示例如下：

```ts
import { UIUtils } from '@kit.ArkUI'

@Entry
@ComponentV2
export struct Index {
  @Local person: Person = new Person()

  aboutToAppear(): void {
    // 模拟发送接口请求数据
    setTimeout(() => {
      this.person = UIUtils.makeObserved(
        {
          mine: {
            size: '大',
            color: '蓝色'
          }
        })
    }, 1000)
  }

  @LocalBuilder
  myBuilder(item: Bag) {
    Column() {
      Text(item.size)
      Text(item.color)
    }
  }

  build() {
    Column() {
      this.myBuilder(this.person.mine)
      Button('change')
        .onClick(() => {
          let num = Math.random() * 100
          this.person.mine.color = `红${num}`
        })
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center)
  }
}

@ObservedV2
class Bag {
  @Trace size: string = '初始size小'
  @Trace color: string = '初始color红色';
}

class Person {
  mine: Bag = new Bag()
}
```

截图如下，渲染结果值依然为初始值，没有变化，点击change也没有变化。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/6HK55yvRS7yKdomD7z43Hg/zh-cn_image_0000002628777468.png "点击放大")

## 背景知识

* [@LocalBuilder](../harmonyos-guides/arkts-localbuilder.md)：自定义构建函数按引用/回调传递参数，且传递的参数为状态变量时，可以触发@LocalBuilder自定义构建函数内的UI刷新。参数传递规则详见：[按回调传递参数](../harmonyos-guides/arkts-localbuilder.md#按回调传递参数)、[按引用传递参数](../harmonyos-guides/arkts-localbuilder.md#按引用传递参数)、[按值传递参数](../harmonyos-guides/arkts-localbuilder.md#按值传递参数)。
* [@ObservedV2和@Trace](../harmonyos-guides/arkts-new-observedv2-and-trace.md)：该装饰器可以使类中的属性具有深度观测的能力，对于深层次嵌套类的监听，详见[嵌套类场景](../harmonyos-guides/arkts-new-observedv2-and-trace.md#嵌套类场景)。
* [makeObserved](../harmonyos-guides/arkts-new-makeobserved.md)：该接口能将非观察数据变为可观察数据。使用场景详见[概述](../harmonyos-guides/arkts-new-makeobserved.md#概述)。

## 问题定位

网络数据接收UI不刷新一般可参考以下方案排查：

1. 是否使用@Observed/@ObservedV2装饰要监听的类。由问题代码可知，需要监听的是Bag类中属性对应的UI刷新，已经使用@ObservedV2装饰器装饰Bag类，并用@Trace装饰器装饰需要监听的属性。该项排查内容无问题。
2. 使用的是状态管理V2下的@ObservedV2装饰器的情况下是否满足其使用的限制条件，详见[概述](../harmonyos-guides/arkts-new-observedv2-and-trace.md#概述)、[使用限制](../harmonyos-guides/arkts-new-observedv2-and-trace.md#使用限制)等。由问题代码可知，代码中接收数据时，并没有通过new操作符重新构造，而是通过字面量直接赋值。但是，由于使用了makeObserved方法将字面量转换为了可深度观测的状态变量。该项排查内容无问题。

**说明** 

接收网络返回的数据时，返回的是一整个类的序列化字符串。通过JSON.parse()进行反序列化后整体赋值给this.person，或类似字面量方式整体赋值给this.person时，由于该方式没有通过new操作符创建为状态变量，所以修改后无法刷新UI。需要用makeObserved等方法转换为可深度观测的状态变量。

3. 代码中存在@LocalBuilder装饰的自定义构建函数，需要判断是否是值传递导致的UI不刷新。

   从问题代码中可以看到，@LocalBuilder自定义构建函数内传递的参数是Bag类型，实际调用时是直接传递的Bag类：this.person.mine。使用的是引用传递的方式，所以当this.person修改时，没有触发UI刷新。该项排查内容存在问题。
4. 未使用ForEach等渲染组件，所以不是键值问题导致的UI不刷新。ForEach键值渲染不刷新问题，详见官方文档：[ForEach：循环渲染](../harmonyos-guides/arkts-rendering-control-foreach.md)。该项排查内容无问题。

## 分析结论

问题代码中，@LocalBuilder自定义构建函数使用了值传递的方式，导致了UI不刷新。

## 修改建议

* 方案一：采用引用传递或回调传递的方式刷新UI。

  通过引用传参的方式向this.myBuilder内部传递参数，促使@LocalBuilder自定义构建函数内部UI刷新。接收数据时，可以采用UIUtils.makeObserved观测返回的类，直接返回一个可观测的状态变量，此时可不用@ObservedV2对原class进行观测声明。引用传递完整示例代码如下：

  ```ts
  import { UIUtils } from '@kit.ArkUI';

  @Entry
  @ComponentV2
  export struct refreshIndex {
    @Local person: Person = new Person();

    aboutToAppear(): void {
      // 模拟发送接口请求数据，并返回可观测数据
      setTimeout(() => {
        this.person = UIUtils.makeObserved(
          {
            mine: {
              size: '大2',
              color: '蓝色2'
            }
          });
      }, 1000);
    }

    @LocalBuilder
    myBuilder(item: Bag) {
      Column() {
        Text(item.size);
        Text(item.color);
      };
    }

    build() {
      Column() {
        // @LocalBuilder引用传参，同步修改
        this.myBuilder({
          size: this.person.mine.size,
          color: this.person.mine.color
        });
        Button('change')
          .onClick(() => {
            let num = Math.random() * 100;
            this.person.mine.color = `红${num}`;
          });
      }
      .width('100%')
      .height('100%')
      .justifyContent(FlexAlign.Center);
    }
  }

  class Person {
    mine: Bag = new Bag();
  }

  class Bag {
    size: string = '初始size小';
    color: string = '初始color红色';
  }
  ```
* 方案二：使用值传递时，通过@ObservedV2和@Trace修饰的状态变量的特性，刷新UI。

  该方式使用的@ObservedV2和@Trace装饰器的特性刷新@LocalBuilder自定义构建函数内的UI，详见：[@Builder函数联合V2装饰器](../harmonyos-guides/arkts-builder.md#builder函数联合v2装饰器)。完整示例代码如下：

  ```ts
  @Entry
  @ComponentV2
  export struct refreshIndex {
    @Local person: Person = new Person();

    aboutToAppear(): void {
      // 模拟发送接口请求数据，此时由于返回的值不是可观测的类，所以不能用方案一中的方法直接替换this.person，替换后会变成普通字面量。
      setTimeout(() => {
        this.person.mine.size = '大2';
        this.person.mine.color = '蓝色2';
      }, 1000);
    }

    @LocalBuilder
    myBuilder(item: Person) {
      Column() {
        Text(item.mine.size);
        Text(item.mine.color);
      };
    }

    build() {
      Column() {
        this.myBuilder(this.person);
        Button('change')
          .onClick(() => {
            let num = Math.random() * 100;
            this.person.mine.color = `红${num}`;
          });
      }
      .width('100%')
      .height('100%')
      .justifyContent(FlexAlign.Center);
    }
  }

  class Person {
    mine: Bag = new Bag();
  }

  @ObservedV2
  class Bag {
    @Trace size: string = '初始size小';
    @Trace color: string = '初始color红色';
  }
  ```

  **说明** 

  方案二中，当类的属性过多时，按照属性进行赋值修改，会比较麻烦，可将属性的修改封装进函数内，由于本示例属性较少，未进行封装。

## 总结

以上方案通过V2版本的状态管理器特性以及引用传递/回调传递的方式实现@LocalBuilder自定义构建函数内UI刷新。
