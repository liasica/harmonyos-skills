---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/arkui-kit-troubleshooting-0008
title: router参数传递和接收示例
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 故障排查 > router参数传递和接收示例
category: harmonyos-faqs
scraped_at: 2026-10-21T07:10:33+08:00
doc_updated_at: 2026-10-20
content_hash: sha256:14cfbb687ced1902c4a02e2f260a48136d9f27c12de9c88dfd6752205c616e79
---

## 问题现象

在使用router进行页面路由跳转时，数据从页面一传输到页面二后，有以下常见问题：

1. 无法获取参数。
2. 参数里封装了函数，却无法调用。

## 定位过程

对于跳转后调用方法失败的问题，需先确认params传递的数据类型是否合法，特别注意params参数不能传递方法和系统接口返回的复杂对象，仅能包含基础类型的数据；

若无法获取参数，可以按照以下步骤进行定位：

1. 首先确定页面跳转时params参数是否为空或有效；
2. 其次，确保正确获取params参数，接收params参数的变量类型与params类型必须一致。

## 分析结论

* 当跳转传递的参数不为空时，考虑创建的params是否有效并检查params传递的类型情况。若params也没有问题，则考虑接收参数的问题；以pushUrl为例，参考以下形式：

  ```screen
  this.getUIContext().getRouter().pushUrl({   url: 'pages/routerpage2',   params: new routerParams('message', [123, 456, 789]) })
  ```
* router传递的参数会经过序列化，过程中会丢失方法。

## 修改建议

完整参数传递代码如下：

页面一：

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

页面二：

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
