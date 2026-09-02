---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uiinspector
title: Class (UIInspector)
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS API > UI界面 > @ohos.arkui.UIContext (UIContext) > Class (UIInspector)
category: harmonyos-references
scraped_at: 2026-09-02T15:00:50+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:db8bc95f81164c4bdbb5a97dedae974552acaa066c2afd6c0859204a9e50e5ad
---

提供注册组件布局和组件绘制送显完成回调通知的能力。送显指节点的绘制命令发送到图形服务并完成显示。例如，开发者可在组件布局完成后获取组件精确尺寸，或在送显完成后执行截图、动画同步等操作，适用于需要精确感知组件布局和绘制时机的场景。

**说明** 

* 本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本Class首批接口从API version 10开始支持。
* 以下API需先使用UIContext中的[getUIInspector()](arkts-apis-uicontext-uicontext.md#getuiinspector)方法获取到UIInspector对象，再通过该对象调用对应方法。

## createComponentObserver

createComponentObserver(id: string): inspector.ComponentObserver

注册组件布局和组件绘制送显完成回调通知。例如，开发者可在组件布局完成后获取组件精确尺寸，或在送显完成后执行截图、动画同步等操作。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | string | 是 | 指定组件id，该id通过通用属性[id](ts-universal-attributes-component-id.md#id)或者[key](ts-universal-attributes-component-id.md#key12)设置。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [inspector.ComponentObserver](js-apis-arkui-inspector.md#componentobserver) | 组件回调事件监听句柄，用于注册和取消注册监听回调。 |

**示例：**

```ts
import { inspector, UIInspector } from '@kit.ArkUI';

@Entry
@Component
struct UIInspectorExample {
  build() {
    Column() {
      Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Start }) {
        Row({ space: 5 }) {
          Text('UIInspector')
            .width(110)
            .height(110)
            .border({ width: 1 })
            .id('TEXT_ID')
        }.width(80)
      }.width(80)
    }.height(320).width(360).padding({ right: 10, top: 10 })
  }

  uiInspector: UIInspector = this.getUIContext().getUIInspector();
  listener:inspector.ComponentObserver = this.uiInspector.createComponentObserver('TEXT_ID');

  aboutToAppear() {
    let onLayoutComplete: () => void = (): void => {
      console.info('TEXT_ID layout complete');
    }
    let onDrawComplete: () => void = (): void => {
      console.info('TEXT_ID draw complete');
    }

    this.listener.on('layout', onLayoutComplete);
    this.listener.on('draw', onDrawComplete);

    // 通过句柄向对应的查询条件取消注册回调，由开发者自行决定在何时调用。
    // this.listener.off('layout', onLayoutComplete)
    // this.listener.off('draw', onDrawComplete)
  }
}
```

## createComponentObserver23+

createComponentObserver(id: string | number): inspector.ComponentObserver

注册组件布局和组件绘制送显完成回调通知。送显指节点的绘制命令发送到图形服务并完成显示。例如，开发者可在组件布局完成后获取组件精确尺寸，或在送显完成后执行截图、动画同步等操作。

相比[createComponentObserver](arkts-apis-uicontext-uiinspector.md#createcomponentobserver)，新增支持传入UniqueID（系统为节点分配的唯一标识）。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | string | number | 是 | 类型为string时，为指定的组件id，该id通过通用属性[id](ts-universal-attributes-component-id.md#id)或者[key](ts-universal-attributes-component-id.md#key12)设置。使用组件id创建监听句柄时，请确保该id对应的组件已经存在，否则后续监听无法生效。类型为number时，为系统为节点分配的唯一标识UniqueID，UniqueID通过[getUniqueId](js-apis-arkui-framenode.md#getuniqueid12)获取。使用UniqueID创建监听句柄时，请确保UniqueID对应的节点已经存在，否则后续监听无法生效。number的取值范围为1~2147483647的整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [inspector.ComponentObserver](js-apis-arkui-inspector.md#componentobserver) | 组件回调事件监听句柄，用于注册和取消注册监听回调。 |

**示例：**

```ts
import { inspector, UIInspector } from '@kit.ArkUI';

@Entry
@Component
struct UIInspectorExample {
  build() {
    Column() {
      Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Start }) {
        Row({ space: 5 }) {
          Text('UIInspector')
            .width(110)
            .height(110)
            .border({ width: 1 })
            .id('TEXT_ID')
        }.width(80)
      }.width(80)
    }.height(320).width(360).padding({ right: 10, top: 10 })
  }

  uiInspector: UIInspector = this.getUIContext().getUIInspector();
  listener:inspector.ComponentObserver = this.uiInspector.createComponentObserver('TEXT_ID');

  aboutToAppear() {
    let onLayoutComplete: () => void = (): void => {
      console.info('TEXT_ID layout complete');
    }
    let onDrawComplete: () => void = (): void => {
      console.info('TEXT_ID draw complete');
    }
    let onLayoutChildrenComplete: () => void = (): void => {
      console.info('UIInspectorExample children layout');
    }

    this.listener.on('layout', onLayoutComplete);
    this.listener.on('draw', onDrawComplete);

    let listenerForThis = this.getUIContext().getUIInspector().createComponentObserver(this.getUniqueId());
    listenerForThis.onLayoutChildren(onLayoutChildrenComplete);

    // 通过句柄向对应的查询条件取消注册回调，由开发者自行决定在何时调用。
    // this.listener.off('layout', onLayoutComplete)
    // this.listener.off('draw', onDrawComplete)
  }
}
```
