---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-getcontext
title: getContext
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS API > UI界面 > getContext
category: harmonyos-references
scraped_at: 2026-09-02T15:00:51+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:76a5e85cbe651f5865152d1bd2bf0842d5f81c71faaf607db62e4f86e6bde930
---

如果需要在页面中获得当前Ability的Context，可调用getContext接口获取当前页面关联的[UIAbilityContext](js-apis-inner-application-uiabilitycontext.md)或[ExtensionContext](js-apis-inner-application-extensioncontext.md)。

**说明** 

* 本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 该接口仅限Stage模型使用。

## getContext(deprecated)

getContext(component?: Object):Context

获取与页面上下文组件关联的Context对象。

**说明** 

从API version 9开始支持，从API version 18开始废弃，建议使用[getHostContext](arkts-apis-uicontext-uicontext.md#gethostcontext12)替代。[getHostContext](arkts-apis-uicontext-uicontext.md#gethostcontext12)需先通过getUIContext()获取[UIContext](arkts-apis-uicontext-uicontext.md)实例后再调用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| component | Object | 否 | 当前自定义组件的实例。当需要获取指定自定义组件关联的Context时，传入该组件实例；不传入component或传入的参数类型非法时，返回默认上下文。默认上下文是指通过追溯当前方法的调用链所跟踪到的Context。传入component时返回该组件关联的Context，不传入时返回通过当前方法调用链跟踪到的默认上下文。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Context](js-apis-getcontext.md#context) | 返回当前组件所在Ability的Context，Context的具体类型为当前Ability关联的Context对象。例如：在UIAbility（用户界面Ability）窗口中的页面调用该接口，返回类型为UIAbilityContext。在ExtensionAbility（扩展Ability）窗口中的页面调用该接口，返回类型为ExtensionContext。 |

## Context

type Context = import('../api/application/Context').default

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**模型约束：** 此接口仅可在Stage模型下使用。

| 类型 | 说明 |
| --- | --- |
| import('../api/application/[Context](../harmonyos-guides/application-context-stage.md)').default | 返回当前组件所在Ability的[Context](../harmonyos-guides/application-context-stage.md)，Context的具体类型为当前Ability关联的Context对象。例如：在UIAbility窗口中的页面调用该接口，返回类型为UIAbilityContext。在ExtensionAbility窗口中的页面调用该接口，返回类型为ExtensionContext。 |

**说明** 

直接使用getContext可能导致[UI上下文不明确](../harmonyos-guides/arkts-global-interface.md#ui上下文不明确)的问题，建议使用getUIContext()获取[UIContext](arkts-apis-uicontext-uicontext.md)实例，并使用[getHostContext](arkts-apis-uicontext-uicontext.md#gethostcontext12)获取绑定实例的Context。

**示例：**

在UIAbility中通过windowStage.loadContent加载具体页面。

```ts
// EntryAbility.ets
import { UIAbility, AbilityConstant, Want } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { window } from '@kit.ArkUI';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onCreate');
  }

  onDestroy() {
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onDestroy');
  }

  onWindowStageCreate(windowStage: window.WindowStage) {
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageCreate');

    windowStage.loadContent('pages/Index', (err, data) => {
      if (err.code) {
        console.error(`Failed to load the content. Code: ${err.code}, message: ${err.message}`);
        return;
      }
      hilog.info(0x0000, 'testTag', 'Succeeded in loading the content. Data: %{public}s', JSON.stringify(data) ?? '');
    });
  }

  onWindowStageDestroy() {
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageDestroy');
  }

  onForeground() {
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onForeground');
  }

  onBackground() {
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onBackground');
  }
}
```

在Index.ets中可以通过getContext接口获取Context，本示例返回的Context类型为UIAbilityContext。

```ts
// pages/Index.ets
@Entry
@Component
struct Index {
  @State message: string = 'Hello World'

  build() {
    Row() {
      Column() {
        Text(this.message)
          .fontSize(50)
          .fontWeight(FontWeight.Bold)
          .onClick(() => {
            // 建议使用this.getUIContext().getHostContext()
            let context: Context = getContext(this) as Context;
            console.info('CacheDir:' + context.cacheDir);
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}
```
