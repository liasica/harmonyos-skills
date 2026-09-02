---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-modifierutils
title: 属性操作工具
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 通用属性 > 动态属性与自定义 > 属性操作工具
category: harmonyos-references
scraped_at: 2026-09-02T15:00:57+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:c0710e5e89d9bf4c07112daa9d010d2058b36c936831f7ffe59bcce242b85a75
---

## ModifierUtils

ModifierUtils是一个[属性修改器](../harmonyos-guides/arkts-user-defined-extension-attributemodifier.md)工具类，用于提供属性操作的方法。例如，可以判断给定的实例是否为指定组件类型，适用于在统一的AttributeModifier中需要区分不同组件类型并进行差异化属性设置的场景。

**起始版本：** 26.0.0

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**模型约束：** 此接口仅可在Stage模型下使用。

### isInstanceOf<T extends CommonMethod<T>>

isInstanceOf<T extends CommonMethod<T>>(instance: T, componentName: string): boolean

检查给定的实例是否为指定组件类型。例如，在自定义属性修改器（AttributeModifier）中为多种组件类型实现统一的属性修改逻辑时，可通过该方法判断当前实例的组件类型，从而对不同组件应用不同的属性设置。

**起始版本：** 26.0.0

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| instance | T | 是 | 要检查的实例，T为继承自[通用属性](ts-component-general-attributes.md)（CommonMethod）的组件属性类型。 |
| componentName | string | 是 | 要检查的组件类型名称，取值为组件类名（如 'Text'、'Button' 等），需与组件类名完全一致（区分大小写）。传入无效或不存在的组件类名时返回false。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果实例是指定的组件类型，则返回true；否则返回false。 |

**示例：**

```ts
// xxx.ets
// 点击按钮，并检查日志，判断组件是否进入独有分支
import { ModifierUtils } from '@kit.ArkUI';

class MyModifier implements AttributeModifier<TextAttribute | ButtonAttribute> {
  isDark: boolean = false;

  constructor(dark?: boolean) {
    this.isDark = dark ?? false;
  }

  applyNormalAttribute(instance: TextAttribute | ButtonAttribute): void {
    if (ModifierUtils.isInstanceOf(instance, 'Text')) {
      console.info('This is TextAttribute');
      const textInstance = instance as TextAttribute;
      if (this.isDark) {
        textInstance.backgroundColor(Color.Blue);
      } else {
        textInstance.backgroundColor(Color.Green);
      }
    } else if (ModifierUtils.isInstanceOf(instance, 'Button')) {
      console.info('This is ButtonAttribute');
      const buttonInstance = instance as ButtonAttribute;
      if (this.isDark) {
        buttonInstance.type(ButtonType.Circle);
        buttonInstance.backgroundColor(Color.Blue);
      } else {
        buttonInstance.type(ButtonType.Normal);
        buttonInstance.backgroundColor(Color.Green);
      }
    }
  }
}

@Entry
@Component
struct MultiComponentAttributeDemo {
  @State myModifier: MyModifier = new MyModifier();

  build() {
    Column() {
      Text('Text')
        .fontSize(50)
        .attributeModifier(this.myModifier)
        .onClick(() => {
          this.myModifier.isDark = !this.myModifier.isDark;
        })
      Button('Button')
        .attributeModifier(this.myModifier)
        .onClick(() => {
          this.myModifier.isDark = !this.myModifier.isDark;
        })
    }
    .justifyContent(FlexAlign.SpaceEvenly)
    .width('100%')
    .height('50%')
  }
}
```
