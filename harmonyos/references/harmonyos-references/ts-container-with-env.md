---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-with-env
title: WithEnv：环境变量容器
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 响应式环境变量 > WithEnv：环境变量容器
category: harmonyos-references
scraped_at: 2026-09-02T15:01:10+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:c417bdc8facae324d99961d7cfa4047b73de5197d94c505ac326e128d5e68ba3
---

WithEnv组件用于为子组件树设置局部环境变量作用域。开发者可以通过该组件为后代组件提供自定义环境变量，或设置系统环境变量。

**起始版本：** 26.0.0

**说明** 

* 此接口仅可在Stage模型下使用。
* 可通过[customEnv](ts-container-with-env.md#customenv)设置自定义环境变量。
* 支持通过[env](ts-container-with-env.md#env)设置的系统环境变量键，系统环境变量键存于[WritableEnvKey](ts-env-system-property.md#writableenvkey)。
* WithEnv嵌套时，同名环境变量按最近作用域生效。

## 子组件

支持单个子组件。

## 接口

WithEnv()

设置局部环境变量作用域容器。

**起始版本：** 26.0.0

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**模型约束**：此接口仅可在Stage模型下使用。

## 属性

支持以下WithEnv专有属性。

### env

env<T>(key: WritableSystemEnvKey<T>, value: T)

设置作用域内的系统环境变量。当前正式支持的系统环境变量键为WritableEnvKey.FONT\_SCALE、WritableEnvKey.DIRECTION。

**说明** 

* WithEnv.env(WritableEnvKey.FONT\_SCALE, value)用于为尾随闭包里的作用域内组件提供局部字体缩放比例，value为number类型，表示字体缩放倍数。设置的value小于0时按0处理。
* WithEnv尾随闭包里的作用域内组件实际生效的字体缩放值同时受env属性通过键WritableEnvKey.FONT\_SCALE设置的值与组件自身的字体缩放限制共同作用。该限制可通过组件的minFontScale和maxFontScale属性设置，也可通过应用配置中的[fontSizeMaxScale](../harmonyos-guides/app-configuration-file.md)等全局配置生效。最终生效值为WritableEnvKey.FONT\_SCALE设置值在各限制范围内的取值。

**起始版本：** 26.0.0

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**模型约束**：此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | [WritableSystemEnvKey<T>](ts-env-system-property.md#writablesystemenvkeyt) | 是 | 系统环境变量键。当前正式支持WritableEnvKey.FONT\_SCALE和WritableEnvKey.DIRECTION。 |
| value | T | 是 | 系统环境变量值。value的类型T对应WritableSystemEnvKey<T>中的类型T。当key为WritableEnvKey.FONT\_SCALE时，value类型为number。当key为WritableEnvKey.DIRECTION时，value类型为Direction。 |

### customEnv

customEnv<T>(key: CustomEnvKey<T>, value: T)

设置作用域内可被后代自定义组件读取的自定义环境变量。

**起始版本：** 26.0.0

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**模型约束**：此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | [CustomEnvKey](ts-custom-env-property.md#customenvkeys)<T> | 是 | 自定义环境变量的键。 |
| value | T | 是 | 自定义环境变量的值。value的类型T对应CustomEnvKey<T>的类型T。 |

## 事件

不支持[通用事件](ts-component-general-events.md)。

## 示例

### 示例1（设置局部字体缩放）

该示例通过env(WritableEnvKey.FONT\_SCALE, value)为作用域内组件设置局部字体缩放比例。

从API版本26.0.0开始，新增env属性和键值WritableEnvKey.FONT\_SCALE。

```ts
// xxx.ets
import { WithEnv } from '@kit.ArkUI';
@Entry
@Component
struct WithEnvExample1 {
  @State fontScale: number = 1.0;

  build() {
    Column({ space: 12 }) {
      Row({ space: 8 }) {
        Button('缩小 0.5x')
          .onClick(() => {
            this.fontScale = 0.5;
          })
        Button('正常 1.0x')
          .onClick(() => {
            this.fontScale = 1.0;
          })
        Button('放大 1.5x')
          .onClick(() => {
            this.fontScale = 1.5;
          })
      }

      WithEnv() {
        Column({ space: 8 }) {
          Text('当前字体缩放作用域内的文本')
            .fontSize(16)
          Text('该文本同样受 WithEnv 字体缩放影响')
            .fontSize(14)
            .fontColor('#99182431')
        }
        .width('100%')
        .alignItems(HorizontalAlign.Start)
      }
      .env(WritableEnvKey.FONT_SCALE, this.fontScale) // 设置局部字体缩放比例
    }
    .padding(12)
    .width('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/0GRS_5gNSsuOzsluBMOMUg/zh-cn_image_0000002706836332.png)

### 示例2（设置局部布局方向）

该示例通过env(WritableEnvKey.DIRECTION, value)为作用域内组件设置局部布局方向。

从API版本26.0.0开始，新增env属性和键值WritableEnvKey.DIRECTION。

```ts
// xxx.ets
import { WithEnv } from '@kit.ArkUI';

@Entry
@Component
struct WithEnvExample2 {
  @State directionValue: Direction = Direction.Ltr;

  build() {
    Column({ space: 12 }) {
      Row({ space: 10 }) {
        Column().backgroundColor('#F0FAFF').width(60).height('100%')
        Column().backgroundColor('#2787D9').width(60).height('100%')
        Column().backgroundColor('#004AAF').width(60).height('100%')

      }.backgroundColor('#D5D5D5').width(200).height(50)

      WithEnv() {
        Row({ space: 10 }) {
          Column().backgroundColor('#F0FAFF').width(60).height('100%')
          Column().backgroundColor('#2787D9').width(60).height('100%')
          Column().backgroundColor('#004AAF').width(60).height('100%')

        }.backgroundColor('#D5D5D5').width(200).height(50)
      }
      .env(WritableEnvKey.DIRECTION, this.directionValue) // 设置局部布局方向

      Button('change direction').onClick(() => {
        if (this.directionValue === Direction.Ltr) {
          this.directionValue = Direction.Rtl;
        } else {
          this.directionValue = Direction.Ltr;
        }
      })
    }
    .width('80%')
    .height('30%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/5CDI00hvQ7qNh9bYwml8yQ/zh-cn_image_0000002736315437.gif)
