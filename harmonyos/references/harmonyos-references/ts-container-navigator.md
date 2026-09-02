---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-navigator
title: Navigator
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 已停止维护的组件与接口 > Navigator
category: harmonyos-references
scraped_at: 2026-09-02T15:01:11+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:33bc8b2b8b4b33388b4700e5b87d107e3a0b87970fe8f3f132b72ddb3facdedb
---

路由容器组件，提供路由跳转能力。

**说明** 

从API version 13开始，该组件不再维护，建议使用[Navigation](ts-basic-components-navigation.md)组件进行页面路由。

该组件从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## 子组件

可以包含子组件。

## 接口

### Navigator(deprecated)

Navigator(value?: {target: string, type?: NavigationType})

**说明** 

从API version 7开始支持，从API version 13开始废弃，建议使用[NavPathInfo](ts-basic-components-navigation.md#navpathinfo10)替代。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| target | string | 是 | 指定跳转目标页面的路径。 |
| type | [NavigationType](ts-container-navigator.md#navigationtypedeprecated枚举说明) | 否 | 指定路由方式。  默认值：NavigationType.Push |

### Navigator(deprecated)

Navigator()

**说明** 

从API version 7开始支持，从API version 13开始废弃，建议使用NavigationAttribute替代。NavigationAttribute为[Navigation](ts-basic-components-navigation.md)组件的属性。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## NavigationType(deprecated)枚举说明

路由的跳转方式。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| Push | 1 | 跳转到应用内的指定页面。  **说明：**  从API version 7开始支持，从API version 13开始废弃，建议使用[pushPath](ts-basic-components-navigation.md#pushpath10)替代。 |
| Replace | 2 | 用应用内的某个页面替换当前页面，并销毁被替换的页面。  **说明：**  从API version 7开始支持，从API version 13开始废弃，建议使用[replacePath](ts-basic-components-navigation.md#replacepath11)替代。 |
| Back | 3 | 返回到指定的页面。指定的页面不存在栈中时不响应。未传入指定的页面时返回上一页。  **说明：**  从API version 7开始支持，从API version 13开始废弃，建议使用[pop](ts-basic-components-navigation.md#pop10)替代。 |

## 属性

### active(deprecated)

active(value: boolean)

设置当前路由组件是否处于激活状态，处于激活状态时，会生效相应的路由操作。

**说明** 

从API version 7开始支持，从API version 13开始废弃，建议使用[Navigation](ts-basic-components-navigation.md)替代。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 路由组件是否处于激活状态。设置为true时，组件处于激活态。设置为false时，组件不处于激活态。 |

### params(deprecated)

params(value: object)

设置跳转时传递到目标页面的数据。

**说明** 

从API version 7开始支持，从API version 13开始废弃，建议使用[param](ts-basic-components-navigation.md#属性-1)替代。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | object | 是 | 跳转时要同时传递到目标页面的数据，可在目标页面使用[router.getParams()](js-apis-router.md#routergetparamsdeprecated)获得。 |

### target(deprecated)

target(value: string)

设置跳转目标页面的路径。目标页面需加入main\_pages.json文件中。

**说明** 

从API version 7开始支持，从API version 13开始废弃，建议使用[Navigation](ts-basic-components-navigation.md)替代。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | string | 是 | 跳转目标页面的路径。 |

### type(deprecated)

type(value: NavigationType)

设置路由跳转方式。

**说明** 

从API version 7开始支持，从API version 13开始废弃，建议使用[Navigation](ts-basic-components-navigation.md)替代。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [NavigationType](ts-container-navigator.md#navigationtypedeprecated枚举说明) | 是 | 路由跳转方式。  默认值：NavigationType.Push |

## 示例

```ts
// code.ets
export interface NameObject {
  name: string;
}

export class TextObject {
  text: NameObject;

  constructor(text: NameObject) {
    this.text = text;
  }
}
```

```ts
import { NameObject, TextObject } from '../../code';

@Entry
@Component
struct NavigatorExample {
  @State active: boolean = false
  @State name: NameObject = { name: 'news' }

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Start, justifyContent: FlexAlign.SpaceBetween }) {
      Navigator({ target: 'pages/container/navigator/Detail', type: NavigationType.Push }) {
        Text('Go to ' + this.name.name + ' page')
          .width('100%').textAlign(TextAlign.Center)
      }.params(new TextObject(this.name)) // 传参数到Detail页面

      Navigator() {
        Text('Back to previous page').width('100%').textAlign(TextAlign.Center)
      }.active(this.active)
      .onClick(() => {
        this.active = true
      })
    }.height(150).width(350).padding(35)
  }
}
```

```ts
import { NameObject } from '../../code';

@Entry
@Component
struct DetailExample {
  // 接收Navigator.ets的传参
  params: Record<string, NameObject> = this.getUIContext().getRouter().getParams() as Record<string, NameObject>
  @State name: NameObject = this.params.text

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Start, justifyContent: FlexAlign.SpaceBetween }) {
      Navigator({ target: 'pages/container/navigator/Back', type: NavigationType.Push }) {
        Text('Go to back page').width('100%').height(20)
      }

      Text('This is ' + this.name.name + ' page')
        .width('100%').textAlign(TextAlign.Center)
    }
    .width('100%').height(200).padding({ left: 35, right: 35, top: 35 })
  }
}
```

```ts
// Back.ets
@Entry
@Component
struct BackExample {
  build() {
    Column() {
      Navigator({ target: 'pages/container/navigator/Navigator', type: NavigationType.Back }) {
        Text('Return to Navigator Page').width('100%').textAlign(TextAlign.Center)
      }
    }.width('100%').height(200).padding({ left: 35, right: 35, top: 35 })
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/n2xrOOuUTJqtsaYqifFCjA/zh-cn_image_0000002736315461.gif)
