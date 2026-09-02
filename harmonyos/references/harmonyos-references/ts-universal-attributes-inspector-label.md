---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-inspector-label
title: 节点调测标签
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 通用属性 > 其他 > 节点调测标签
category: harmonyos-references
scraped_at: 2026-09-02T14:51:26+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:b3b71ec7e946477991e17f75a1c79d026dabd6e391759abb3b1d93d0c725fa39
---

为组件节点设置调测标签。该标签作为节点的自定义标识会展示在DevEco Studio的Inspector组件树中，便于开发者在调试阶段分辨同类节点、快速定位组件，提升开发与分析调试的效率。

**起始版本：** 26.0.0

## inspectorLabel

inspectorLabel(label: string | undefined): T

设置组件的调测标签。未设置时，组件调测标签默认为空字符串。对同一组件多次调用本接口时，后设置的标签会覆盖先前的标签。

**起始版本：** 26.0.0

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| label | string | undefined | 是 | 组件的调测标签，需在整个应用内保持唯一，以便在调测时准确定位和区分节点。对同一组件多次调用本接口时，后设置的标签会覆盖先前的标签。传入undefined时清除调测标签，调测标签默认为空字符串。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件，可用于链式调用。 |

**示例：**

```ts
@Entry
@Component
struct ComponentPage {
  build() {
    Column() {
      Text('Hello World')
        .fontSize(20)
        .inspectorLabel('TEXT')
        .onClick(() => {
          console.info(`Text is clicked`);
        })
    }
    .width('100%')
    .height('100%')
  }
}
```
