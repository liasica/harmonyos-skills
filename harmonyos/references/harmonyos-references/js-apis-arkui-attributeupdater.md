---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-attributeupdater
title: AttributeUpdater
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS API > UI界面 > arkui > AttributeUpdater
category: harmonyos-references
scraped_at: 2026-09-05T06:16:54+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:0a60a27377e388b6da0fcd6f0a354a1e085fdd147e44412d15be5333e6239811
---

将属性直接设置给组件，无需标记为状态变量即可直接触发UI更新。适用于需要在不定义状态变量的情况下动态更新组件属性的场景，如动态修改组件构造参数、避免为一次性属性更新定义状态变量等。

**说明** 

* 从API version 12开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* 本模块接口仅可在Stage模型下使用。

## 导入模块

```ts
import { AttributeUpdater } from '@kit.ArkUI';
```

**说明** 

1. 当与属性方法同时设置，或在AttributeUpdater中实现applyNormalAttribute等方法时，AttributeUpdater会与状态管理更新机制同时生效，易出现混淆。因此，不建议在同一组件上同时使用属性方法（状态管理机制）和AttributeUpdater属性直通更新两种方式设置相同属性。
2. 当与属性方法同时设置时，属性生效的原则为：后设置的生效。

   若先进行属性直通更新，后通过状态管理机制更新属性方法，则后更新的属性方法生效；

   若先通过状态管理机制更新属性方法，后进行属性直通更新，则属性直通更新生效。
3. 一个AttributeUpdater对象只能同时关联一个组件，否则将出现设置的属性只在一个组件上生效的现象。
4. 开发者需要自行保障AttributeUpdater中T和C的类型匹配。比如T为ImageAttribute，C要对应为ImageInterface，否则可能导致

   使用updateConstructorParams时功能异常。
5. updateConstructorParams当前只支持Button、Image、Text、Span、SymbolSpan和ImageSpan组件。
6. AttributeUpdater不支持深浅色切换等状态管理相关的操作。
7. 在[UI上下文不明确](../harmonyos-guides/arkts-global-interface.md#ui上下文不明确)的场景中调用[AttributeUpdater](js-apis-arkui-attributeupdater.md#attributeupdatert-c--initializert)对象的接口时，建议使用[UIContext](arkts-apis-uicontext-uicontext.md)的[runScopedTask](arkts-apis-uicontext-uicontext.md#runscopedtask)接口明确UI上下文，参考[执行绑定UI实例的闭包](../harmonyos-guides/arkts-global-interface.md#执行绑定ui实例的闭包)示例。

## Initializer<T>

type Initializer<T> = () => T

组件属性的初始化函数类型，用于创建并返回组件的属性实例。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件的属性实例。 |

## AttributeUpdater<T, C = Initializer<T>>

为[AttributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifiert)的实现类，开发者需要自定义class继承AttributeUpdater。

其中C代表组件的构造函数类型，比如Text组件的TextInterface，Image组件的ImageInterface等，仅在使用updateConstructorParams时才需要传递C类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### applyNormalAttribute

applyNormalAttribute?(instance: T): void

定义正常态更新属性函数，在AttributeUpdater后续更新属性时触发。不建议在同一组件上同时用属性直通更新和属性方法设置相同属性，否则易出现混淆。当与属性方法同时设置时，属性生效的原则为后设置的生效。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| instance | T | 是 | 组件的属性类实例，开发者通过调用该实例的属性方法来设置或更新组件的正常态属性，比如Button组件的ButtonAttribute，Text组件的TextAttribute等。 |

### initializeModifier

initializeModifier(instance: T): void

AttributeUpdater首次设置给组件时提供的样式。不建议在同一组件上同时用属性直通更新和属性方法设置相同属性，否则易出现混淆。当与属性方法同时设置时，属性生效的原则为后设置的生效。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| instance | T | 是 | 组件的属性类实例，开发者通过调用该实例的属性方法来初始化设置组件的样式属性，比如Button组件的ButtonAttribute，Text组件的TextAttribute等。 |

**示例：**

通过initializeModifier方法初始化设置属性值。

```ts
// xxx.ets
import { AttributeUpdater } from '@kit.ArkUI';

class MyButtonModifier extends AttributeUpdater<ButtonAttribute> {
  // 该AttributeUpdater对象第一次使用的时候触发的回调
  initializeModifier(instance: ButtonAttribute): void {
    instance.backgroundColor('#ffd5d5d5')
      .labelStyle({ maxLines: 3 })
      .width('80%');
  }

  // 该AttributeUpdater对象后续使用或者更新的时候触发的回调
  applyNormalAttribute(instance: ButtonAttribute): void {
    instance.borderWidth(1);
  }
}

@Entry
@Component
struct Index {
  modifier: MyButtonModifier = new MyButtonModifier();
  @State flushTheButton: string = 'Button';

  build() {
    Row() {
      Column() {
        Button(this.flushTheButton)
          .attributeModifier(this.modifier)
          .onClick(() => {
            // 通过AttributeUpdater的attribute对属性进行修改
            // 需要注意先通过组件的attributeModifier属性方法建立组件与AttributeUpdater绑定关系
            this.modifier.attribute?.backgroundColor('#ff2787d9').labelStyle({ maxLines: 5 });
          })
          .margin('10%')
        Button('Trigger Button Update')
          .width('80%')
          .labelStyle({ maxLines: 2 })
          .onClick(() => {
            this.flushTheButton = this.flushTheButton + ' Updated';
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/v5cLrh6GRkywP4Z0PObRoQ/zh-cn_image_0000002742124743.gif)

### attribute

get attribute(): T | undefined

获取AttributeUpdater中组件对应的属性类实例，通过该实例实现属性直通更新。需先通过组件的attributeModifier属性方法建立组件与AttributeUpdater的绑定关系，绑定后方可获取到属性类实例。不建议在同一组件上同时用属性直通更新和属性方法设置相同属性；当与属性方法同时设置时，属性生效的原则为后设置的生效。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | undefined | 如果AttributeUpdater中组件的属性类实例存在，则返回对应组件的属性类实例，否则返回undefined。 |

**示例：**

通过属性直通设置方式更新属性值。

```ts
// xxx.ets
import { AttributeUpdater } from '@kit.ArkUI';

class MyButtonModifier extends AttributeUpdater<ButtonAttribute> {
  initializeModifier(instance: ButtonAttribute): void {
    instance.backgroundColor('#ffd5d5d5')
      .width('50%')
      .height(30);
  }
}

@Entry
@Component
struct UpdaterDemo2 {
  modifier: MyButtonModifier = new MyButtonModifier();

  build() {
    Row() {
      Column() {
        Button('Button')
          .attributeModifier(this.modifier)
          .onClick(() => {
            this.modifier.attribute?.backgroundColor('#ff2787d9').width('30%');
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/BVAqMgs-R-e5SSQnz6Fzzg/zh-cn_image_0000002712245836.gif)

### 属性

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| updateConstructorParams | [C](js-apis-arkui-attributeupdater.md#attributeupdatert-c--initializert) | 否 | 否 | C代表组件的构造函数类型，比如Text组件的TextInterface，Image组件的ImageInterface等。用于更改组件的构造函数入参。需先通过组件的attributeModifier属性方法建立组件与AttributeUpdater的绑定关系，绑定后方可使用。当前仅支持Button、Image、Text、Span、SymbolSpan和ImageSpan组件，使用前需确保T和C类型匹配，否则可能导致功能异常。 |

**示例：**

使用updateConstructorParams更新组件的构造入参。

```ts
// xxx.ets
import { AttributeUpdater } from '@kit.ArkUI';

class MyTextModifier extends AttributeUpdater<TextAttribute, TextInterface> {
  initializeModifier(instance: TextAttribute): void {
  }
}

@Entry
@Component
struct AttributeDemo3 {
  private modifier: MyTextModifier = new MyTextModifier();

  build() {
    Row() {
      Column() {
        Text('Initialize')
          .attributeModifier(this.modifier)
          .fontSize(14).border({ width: 1 }).textAlign(TextAlign.Center).lineHeight(20)
          .width(200).height(50)
          .backgroundColor('#fff7f7f7')
          .onClick(() => {
            this.modifier.updateConstructorParams('Updated');
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/3eIrf9XUSMieEXDhEDVX4A/zh-cn_image_0000002742004785.gif)

### onComponentChanged

onComponentChanged(component: T): void

当多个组件绑定同一个自定义AttributeUpdater对象，且绑定的组件发生切换时，通过该接口通知应用。需注意一个AttributeUpdater对象只能同时关联一个组件，否则将出现设置的属性只在一个组件上生效的现象。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| component | T | 是 | 组件的属性类实例，开发者通过调用该实例的属性方法来设置切换后组件的属性，比如Button组件的ButtonAttribute，Text组件的TextAttribute等。 |

**示例：**

```ts
// xxx.ets
import { AttributeUpdater } from '@kit.ArkUI';

class MyButtonModifier extends AttributeUpdater<ButtonAttribute> {
  initializeModifier(instance: ButtonAttribute): void {
    instance.backgroundColor('#ff2787d9')
      .width('50%')
      .height(30);
  }

  onComponentChanged(component: ButtonAttribute): void {
    component.backgroundColor('#ff519db4')
      .width('50%')
      .height(30);
  }
}

@Entry
@Component
struct UpdaterDemo4 {
  @State btnState: boolean = false;
  modifier: MyButtonModifier = new MyButtonModifier();

  build() {
    Row() {
      Column() {
        Button('Test')
          .onClick(() => {
            this.btnState = !this.btnState;
          }).margin({ bottom: 20 })

        if (this.btnState) {
          Button('Button')
            .attributeModifier(this.modifier)
        } else {
          Button('Button')
            .attributeModifier(this.modifier)
        }
      }
      .width('100%')
    }
    .height('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/USno8z9gQquxgIhZpeIF_w/zh-cn_image_0000002712405796.gif)
