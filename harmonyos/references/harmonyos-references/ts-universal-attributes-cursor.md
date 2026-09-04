---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-cursor
title: 鼠标光标控制
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 通用属性 > 交互属性 > 鼠标光标控制
category: harmonyos-references
scraped_at: 2026-09-05T06:17:05+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:bfeeaa812b8c953cc4ec654148c312c52bf8a0d628b65e04e377eed45a74b852
---

鼠标光标控制用于控制鼠标光标的显示样式，适用于需要根据组件状态或交互区域切换光标样式的场景，帮助提升用户的交互识别和操作反馈体验。

**说明** 

* 从API version 11开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本模块接口仅可在Stage模型下使用。

## cursorControl

### setCursor

setCursor(value: PointerStyle): void

方法语句中可使用的全局接口，调用该接口可更改当前的鼠标光标样式。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [PointerStyle](ts-universal-attributes-cursor.md#pointerstyle) | 是 | 设置的光标样式。 |

### restoreDefault

restoreDefault(): void

方法语句中可使用的全局接口，调用此接口可将鼠标光标恢复成默认箭头样式。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## PointerStyle

type PointerStyle = import('../api/@ohos.multimodalInput.pointer').default.PointerStyle

光标样式。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| import('../api/@ohos.multimodalInput.pointer').default.[PointerStyle](js-apis-pointer.md#pointerstyle) | 光标样式。 |

**说明** 

直接使用cursorControl可能导致[UI上下文不明确](../harmonyos-guides/arkts-global-interface.md#ui上下文不明确)的问题，建议使用getUIContext()获取[UIContext](arkts-apis-uicontext-uicontext.md)实例，并使用[getCursorController](arkts-apis-uicontext-uicontext.md#getcursorcontroller12)获取绑定实例的cursorControl。

## 示例

该示例通过setCursor实现了鼠标光标样式的更改。

```ts
// xxx.ets
import { pointer } from '@kit.InputKit';

@Entry
@Component
struct CursorControlExample {
  build() {
    Column() {
      Row()
        .height(200)
        .width(200)
        .backgroundColor(Color.Green)
        .position({ x: 60, y: 70 })
        .onHover((flag) => {
          if (flag) {
            // 建议使用this.getUIContext().getCursorController().setCursor()
            cursorControl.setCursor(pointer.PointerStyle.EAST);
          } else {
            // 建议使用this.getUIContext().getCursorController().restoreDefault()
            cursorControl.restoreDefault();
          }
        })
      Row()
        .height(200)
        .width(200)
        .backgroundColor(Color.Blue)
        .position({ x: 130, y: 120 })
        .onHover((flag) => {
          if (flag) {
            // 建议使用this.getUIContext().getCursorController().setCursor()
            cursorControl.setCursor(pointer.PointerStyle.WEST);
          } else {
            // 建议使用this.getUIContext().getCursorController().restoreDefault()
            cursorControl.restoreDefault();
          }
        })
    }.width('100%')
  }
}
```

示意图：

当鼠标悬浮在蓝色区域时，显示：向西箭头光标样式。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/sPiRhGcWSKW3jLqo01L22w/zh-cn_image_0000002742124837.jpg)

当鼠标悬浮在绿色区域时，显示：向东箭头光标样式。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/mI3RfCI6SqeVlw7rPjn1tQ/zh-cn_image_0000002712245930.jpg)
