---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1528
title: router参数传递和接收示例
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > router参数传递和接收示例
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:11+08:00
doc_updated_at: 2026-08-05
content_hash: sha256:893234d6b475f652075f9442150a70d909182e12a04d6bdb890a9f45f4a0dfc8
---

## 问题现象

在使用router进行页面路由跳转时，数据从页面一传输到页面二后，有以下常见问题：

1. 无法获取参数。
2. 参数里封装了函数，却无法调用。

## 背景知识

[router](../harmonyos-references/arkts-apis-uicontext-router.md)通过[pushUrl](../harmonyos-references/arkts-apis-uicontext-router.md#pushurl)、[replaceUrl](../harmonyos-references/arkts-apis-uicontext-router.md#replaceurl)、[pushNamedRoute](../harmonyos-references/arkts-apis-uicontext-router.md#pushnamedroute)、[replaceNamedRoute](../harmonyos-references/arkts-apis-uicontext-router.md#replacenamedroute)四种方式跳转并传递参数页面。

跳转方法的参数形式：

* pushUrl与replaceUrl描述页面信息的参数为[RouterOptions](../harmonyos-references/js-apis-router.md#routeroptions)，传递参数结构形式为：

  ```ts
  {
    url: 'page/onePage', // 传递的方式，必填参数
    params: Object, // 传递的数据，必填参数
    recoverable: true // 页面是否可恢复，该参数为非必填参数，默认为true
  }
  ```
* pushNamedRoute与replaceNamedRoute描述页面信息的参数为[NamedRouterOptions](../harmonyos-references/js-apis-router.md#namedrouteroptions10)，传递参数结构形式为：

  ```ts
  {
    name: 'Welcome', // 传递的方式，必填参数
    params: Object, // 传递的数据，必填参数
    recoverable: true // 页面是否可恢复，该参数为非必填参数，默认为true
  }
  ```

* 注意事项：params不支持传递方法和系统返回的复杂对象。

获取参数的方式：[getParams](../harmonyos-references/arkts-apis-uicontext-router.md#getparams)。获取的参数数据结构和传递的参数一致。

## 问题定位

对于跳转后调用方法失败的问题，需先确认params传递的数据类型是否合法，特别注意params参数不能传递方法和系统接口返回的复杂对象，仅能包含基础类型的数据；

若无法获取参数，可以按照以下步骤进行定位：

1. 首先确定页面跳转时params参数是否为空或有效；
2. 其次，确保正确获取params参数，接收params参数的变量类型与params类型必须一致。

## 分析结论

* 当跳转传递的参数不为空时，考虑创建的params是否有效并检查params传递的类型情况。若params也没有问题，则考虑接收参数的问题；以pushUrl为例，参考以下形式：

  ```ts
  this.getUIContext().getRouter().pushUrl({
    url: 'pages/routerpage2',
    params: new routerParams('message', [123, 456, 789])
  })
  ```
* router传递的参数会经过序列化，过程中会丢失方法。

## 修改建议

完整参数传递代码如下：

* 页面一：

  ```ts
  // 定义公共参数类
  export class InfoTmp {
    age: number = 0;
  }

  export class ParamInfo {
    name: string = '';
    info: InfoTmp = new InfoTmp();
  }

  // 通过this.getUIContext().getRouter().pushUrl跳转至目标页携带params参数
  @Entry
  @Component
  struct Index {
    build() {
      Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
        Text('这是第一页')
          .fontSize(50)
          .fontWeight(FontWeight.Bold);
        Button() {
          Text('next page')
            .fontSize(25)
            .fontWeight(FontWeight.Bold)
            .margin(10);
        }
        .type(ButtonType.Capsule)
        .margin({ top: 20 })
        .backgroundColor('#F1F3F5')
        .onClick(() => {
          const params = new ParamInfo();
          params.name = 'Welcome';
          params.info.age = 20;
          this.getUIContext().getRouter().pushUrl({
            url: 'pages/Second',
            params: params
          });
        });
      }
      .width('100%')
      .height('100%');
    }
  }
  ```
* 页面二：

  ```ts
  import { ParamInfo } from './Index';

  // 在second页面中接收传递过来的参数
  @Entry
  @Component
  struct Second {
    @State params: ParamInfo = this.getUIContext().getRouter().getParams() as ParamInfo;

    aboutToAppear(): void {
      // 方案一
      let params = (this.getUIContext().getRouter().getParams() as Record<string, object>);
      let name = params.name;
      let info = params.info;
      console.info(`Succeeded in completing PlanOne. params:{name: ${name}, info: ${info}}. `);
      // 方案二
      let paramInfo: ParamInfo = this.getUIContext().getRouter().getParams() as ParamInfo;
      console.info(`Succeeded in completing PlanTwo. params:{name: ${paramInfo.name}, info.age: ${paramInfo.info.age}}. `);
    }

    build() {
      Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
        Text(`第一页传来的数值:${this.params.name}`)
          .fontSize(20)
          .margin({ top: 20 })
          .backgroundColor(Color.Transparent);
      }
      .width('100%')
      .height('100%');
    }
  }
  ```

  页面二参数接收有以下两种方式，对比如下：

  | 方案 | 优点 | 缺点 | 应用场景 |
  | --- | --- | --- | --- |
  | 方案一：转成Record | 无需定义数据类 | 遇到嵌套类型数据处理麻烦 | 适用于只有基本类型场景 |
  | 方案二：转成特定的类 | 嵌套类型数据处理简单 | 需要事先定义好数据类 | 适用于嵌套数据类型场景 |

## 常见FAQ

Q：params是否支持抽象类的传递？

A：不支持，复杂的页面传参建议使用Navigation。

Q：params传递HashMap类型数据，目标页面无法获取到内容如何解决？

A：router传递的参数会经过序列化，过程中会丢失方法。所以无法使用map，list传参。推荐使用Navigation。

Q：router路由跳转时params传入callback类型无效？

A：callback为回调函数方法，router的params参数不支持传递方法，因此无效。可以尝试使用[EventHub](../harmonyos-references/js-apis-inner-application-eventhub.md)实现类似的效果。

Q：params如何传递属性字符串、ArrayBuffer、PixelMap类型的数据？

A：router不支持传递函数和嵌套复杂结构类型的数据，可使用[AppStorage](../harmonyos-guides/arkts-appstorage.md)或[EventHub](../harmonyos-references/js-apis-inner-application-eventhub.md)实现类似的效果。推荐使用Navigation。

Q：router获取的参数为什么无法清空？

A：router.getParams()获取的是路由记录中的只读参数副本，参数与页面实例绑定。每次onPageShow显示时都会读取同一份参数。需主动修改参数对象，每次跳转时强制传递新对象，参考代码如下：

```ts
this.getUIContext().getRouter().pushUrl({
  url: 'pages/Page',
  params: {} // 若不传递参数，传空对象，覆盖旧对象。
});
```

Q：如何使用router.back()返回上一个界面并传参？

A：[RouterOptions](../harmonyos-references/js-apis-router.md#routeroptions)中url设置为空字符，params传入传递的参数数据。
