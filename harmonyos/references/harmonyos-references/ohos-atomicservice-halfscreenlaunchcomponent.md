---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-atomicservice-halfscreenlaunchcomponent
title: HalfScreenLaunchComponent
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > AtomicService > HalfScreenLaunchComponent
category: harmonyos-references
scraped_at: 2026-09-02T15:01:07+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:74b4a3dd83c2919a2aa663ffdab3e410c44e7105b428ba34b2e0e8d9bf116960
---

半屏嵌入式启动元服务组件，当被拉起方未授权嵌入式运行元服务时，宿主将使用跳出式拉起元服务。

**说明** 

该组件从API version 18开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

当需要在该组件中实现一个可嵌入式运行的元服务时，元服务必须继承自[EmbeddableUIAbility](js-apis-app-ability-embeddableuiability.md)。若不继承自EmbeddableUIAbility，系统无法确保元服务正常运行。

## 导入模块

```ts
import { HalfScreenLaunchComponent } from '@kit.ArkUI';
```

## 子组件

无。

## 属性

不支持[通用属性](ts-component-general-attributes.md)。

## HalfScreenLaunchComponent

HalfScreenLaunchComponent({ content: Callback<void>, appId: string, options?: AtomicServiceOptions, onError?: ErrorCallback, onTerminated?: Callback<TerminationInfo>, onReceive?: Callback<Record<string, Object>> })

**装饰器类型：**[@Component](../harmonyos-guides/arkts-create-custom-components.md#component)

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 名称 | 类型 | 必填 | 装饰器类型 | 说明 |
| --- | --- | --- | --- | --- |
| content | [Callback](js-apis-base.md#callback)<void> | 是 | [@BuilderParam](../harmonyos-guides/arkts-builderparam.md) | 组件显示内容。 |
| appId | string | 是 | - | 元服务appId。 |
| options | [AtomicServiceOptions](js-apis-app-ability-atomicserviceoptions.md) | 否 | - | 拉起元服务参数。不填时使用默认参数拉起元服务。 |
| onError | [ErrorCallback](js-apis-base.md#errorcallback) | 否 | - | 被拉起的元服务在运行过程中发生异常时触发本回调。 |
| onTerminated | [Callback](js-apis-base.md#callback)<[TerminationInfo](ts-container-embedded-component.md#terminationinfo)> | 否 | - | 被拉起的嵌入式运行元服务通过点击元服务退出按钮、手势侧滑、调用[terminateSelfWithResult](js-apis-inner-application-uiabilitycontext.md#terminateselfwithresult)或者[terminateSelf](js-apis-inner-application-uiabilitycontext.md#terminateself)正常退出时，触发本回调。 |
| onReceive20+ | [Callback](js-apis-base.md#callback)<Record<string, Object>> | 否 | - | 被拉起的嵌入式运行元服务通过[@ohos.window (窗口)](arkts-apis-window.md)调用相关API时，触发本回调。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |

**说明** 

* 若元服务通过调用[terminateSelfWithResult](js-apis-inner-application-uiabilitycontext.md#terminateselfwithresult)退出，该方法携带的信息会传给回调函数的入参；
* 若元服务通过调用[terminateSelf](js-apis-inner-application-uiabilitycontext.md#terminateself)退出，上述回调函数的入参中，"code"取默认值"0"，"want"为"undefined"。

## 示例

该示例展示如何嵌入式拉起手机充值服务。

**说明** 

由于嵌入式元服务运行在独立进程，其崩溃异常不会直接暴露在宿主的日志中。本地调试时可通过以下方式查看真实报错栈：

1. 打开DevEco Studio的HiLog面板。
2. 将左上角的模式切换为User logs of selected app。
3. 在右侧进程列表中，选择被拉起的元服务进程（被拉起元服务的包名，且后缀带有embeddable字样）。

```ts
import { HalfScreenLaunchComponent } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  appId: string = '576****************'; // 元服务appId。

  build() {
    Column() {
      HalfScreenLaunchComponent({
        appId: this.appId,
        options: {},
        onTerminated: (info: TerminationInfo) => {
          console.info('onTerminated info = ' + info.want);
        },
        onError: (err: BusinessError) => {
          console.error(`onError code: ${err.code}, message: ${err.message}`);
        },
        onReceive: (data: Record<string, Object>) => {
          console.info('onReceive, data: ' + data['ohos.atomicService.window']);
        }
      }) {
        Column() {
          Image($r('app.media.app_icon'))
          Text('拉起手机充值')
        }.width('80vp').height('80vp').margin({bottom:30})
      } // 通过尾随闭包形式传入content。
    }
  }

}
```
