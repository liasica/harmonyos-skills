---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-fullscreenlaunchcomponent
title: FullScreenLaunchComponent
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 系统预置UI组件库 > FullScreenLaunchComponent
category: harmonyos-references
scraped_at: 2026-09-02T15:01:08+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:8e8b8175c6a15f3aa91fcffddde8ffa911e90f995b30dc1e48e41c43b51c5a05
---

全屏启动元服务组件，当提供方授权使用方嵌入式运行元服务时，使用方全屏嵌入式运行元服务；未授权时，使用方跳出式拉起元服务。

**说明** 

该组件从API version 12开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

当需要在该组件中实现可嵌入式运行的元服务，必须继承自[EmbeddableUIAbility](js-apis-app-ability-embeddableuiability.md)。否则，系统无法保证元服务功能正常。

## 导入模块

```ts
import { FullScreenLaunchComponent } from '@kit.ArkUI';
```

## 子组件

无。

## 属性

不支持[通用属性](ts-component-general-attributes.md)。

## 事件

不支持[通用事件](ts-component-general-events.md)。

## FullScreenLaunchComponent

FullScreenLaunchComponent({ content: Callback<void>, appId: string, options?: AtomicServiceOptions, onError?: ErrorCallback, onTerminated?: Callback<TerminationInfo>, onReceive?: Callback<Record<string, Object>> })

**装饰器类型：**[@Component](../harmonyos-guides/arkts-create-custom-components.md#component)

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 名称 | 类型 | 必填 | 装饰器类型 | 说明 |
| --- | --- | --- | --- | --- |
| content | [Callback](js-apis-base.md#callback)<void> | 是 | [@BuilderParam](../harmonyos-guides/arkts-builderparam.md) | 可以使用组件组合来自定义拉起元服务前的占位图标，实现类似大桌面应用图标的效果。点击占位组件后，将拉起元服务。 |
| appId | string | 是 | - | 需要拉起的元服务appId，appId是元服务的唯一标识。 |
| options | [AtomicServiceOptions](js-apis-app-ability-atomicserviceoptions.md) | 否 | - | 拉起元服务的参数。不填时使用默认参数拉起元服务。 |
| onError18+ | [ErrorCallback](js-apis-base.md#errorcallback) | 否 | - | 被拉起的嵌入式运行元服务在运行过程中发生异常时触发本回调。可通过回调参数中的code、name和message获取错误信息并做处理。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| onTerminated18+ | [Callback](js-apis-base.md#callback)<[TerminationInfo](ts-container-embedded-component.md#terminationinfo)> | 否 | - | 被拉起的嵌入式运行元服务通过点击元服务退出按钮、手势侧滑、调用[terminateSelfWithResult](js-apis-inner-application-uiabilitycontext.md#terminateselfwithresult)或者[terminateSelf](js-apis-inner-application-uiabilitycontext.md#terminateself)正常退出时，触发本回调函数。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| onReceive20+ | [Callback](js-apis-base.md#callback)<Record<string, Object>> | 否 | - | 被拉起的嵌入式运行元服务通过[@ohos.window (窗口)](arkts-apis-window.md)调用相关API时，触发本回调。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |

**说明** 

* 若元服务通过调用[terminateSelfWithResult](js-apis-inner-application-uiabilitycontext.md#terminateselfwithresult)退出，其携带的信息会传给回调函数的入参；
* 若元服务通过调用[terminateSelf](js-apis-inner-application-uiabilitycontext.md#terminateself)退出，上述回调函数的入参中，"code"取默认值"0"，"want"为"undefined"；
* 从API version 26.0.0开始，元服务通过手势侧滑退出触发onTerminated回调。

## 示例

本示例展示组件使用方法和提供方元服务的实现。实际运行时请使用开发者自己的元服务appId。

FullScreenLaunchComponent组件需要由使用方调用。在提供方完成本地的安装后，即可在使用方应用或者元服务中全屏嵌入式拉起提供方的元服务。

**说明** 

由于嵌入式元服务运行在独立进程，其崩溃异常不会直接暴露在宿主的日志中。本地调试时可通过以下方式查看真实报错栈：

1. 打开DevEco Studio的HiLog面板。
2. 将左上角的模式切换为User logs of selected app。
3. 在右侧进程列表中，选择被拉起的元服务进程（被拉起元服务的包名，且后缀带有embeddable字样）。

**使用方**

```ts
// 使用方入口界面Index.ets内容如下：
import { FullScreenLaunchComponent } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  @State appId: string = '6917573653426122083'; // 元服务appId

  build() {
    Row() {
      Column() {
        FullScreenLaunchComponent({
          content: ColumnChild,
          appId: this.appId,
          options: {},
          onTerminated: (info) => {
            console.info(`onTerminated code: ${info.code.toString()}`);
          },
          onError: (err) => {
            console.error(`onError code: ${err.code}, message: ${err.message}`);
          },
          onReceive: (data) => {
            console.info(`onReceive, data: ${JSON.stringify(data)}`);
          }
        }).width('80vp').height('80vp')
      }
      .width('100%')
    }
    .height('100%')
  }
}

@Builder
function ColumnChild() {
  Column() {
    Image($r('app.media.startIcon'))
    Text('test')
  }
}
```

**组件提供方**

元服务提供方需要修改两个文件：

* 提供方入口文件：/src/main/ets/entryability/EntryAbility.ets。

```ts
import { AbilityConstant, Want, EmbeddableUIAbility } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { window } from '@kit.ArkUI';

const DOMAIN = 0x0000;

export default class EntryAbility extends EmbeddableUIAbility {
  storage = new LocalStorage();
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onCreate');
  }

  onDestroy(): void {
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onDestroy');
  }

  onWindowStageCreate(windowStage: window.WindowStage): void {
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onWindowStageCreate');
    let mainWindow = windowStage.getMainWindowSync();
    this.storage.setOrCreate('window', mainWindow);
    this.storage.setOrCreate('windowStage', windowStage);
    windowStage.loadContent('pages/Index', this.storage);
  }

  onWindowStageDestroy(): void {
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onWindowStageDestroy');
  }

  onForeground(): void {
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onForeground');
  }

  onBackground(): void {
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onBackground');
  }
}
```

* 提供方扩展Ability入口页面文件：/src/main/ets/pages/Index.ets。

```ts
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  private storage: LocalStorage | undefined = this.getUIContext().getSharedLocalStorage();

  build() {
    Row() {
      Column() {
        GridRow({ columns: 2 }) {
          GridCol() {
            Button('setWindowSystemBar')
              .onClick(() => {
                this.testSetSystemBarEnable();
              }).width(120)
          }.height(60)

          GridCol() {
            Button('setGestureBack')
              .onClick(() => {
                this.testSetGestureBackEnable();
              }).width(120)
          }.height(60)

          GridCol() {
            Button('setImmersive')
              .onClick(() => {
                this.testSetImmersiveEnable();
              }).width(120)
          }.height(60)

          GridCol() {
            Button('setSpecificSystemBarEnabled')
              .onClick(() => {
                this.testSetSpecificSystemBarEnabled();
              }).width(120)
          }.height(60)
        }
      }
      .width('100%')
    }
    .height('100%')
  }

  testSetSystemBarEnable() {
    let window: window.Window | undefined = this.storage?.get('window');
    let promise = window?.setWindowSystemBarEnable(['status']);
    promise?.then(() => {
      console.info('setWindowSystemBarEnable success');
    }).catch((err: BusinessError) => {
      console.error(`setWindowSystemBarEnable failed, code: ${err.code}, message: ${err.message}`);
    });
  }

  testSetGestureBackEnable() {
    let window: window.Window | undefined = this.storage?.get('window');
    let promise = window?.setGestureBackEnabled(true);
    promise?.then(() => {
      console.info('setGestureBackEnabled success');
    }).catch((err: BusinessError) => {
      console.error(`setGestureBackEnabled failed, code: ${err.code}, message: ${err.message}`);
    });
  }

  testSetImmersiveEnable() {
    let window: window.Window | undefined = this.storage?.get('window');
    try {
      window?.setImmersiveModeEnabledState(true);
    } catch (err) {
      console.error(`setImmersiveModeEnabledState failed, code: ${err.code}, message: ${err.message}`);
    }
  }

  testSetSpecificSystemBarEnabled() {
    let window: window.Window | undefined = this.storage?.get('window');
    let promise = window?.setSpecificSystemBarEnabled('navigationIndicator', false, false);
    promise?.then(() => {
      console.info('setSpecificSystemBarEnabled success');
    }).catch((err: BusinessError) => {
      console.error(`setSpecificSystemBarEnabled failed, code: ${err.code}, message: ${err.message}`);
    });
  }
}
```
