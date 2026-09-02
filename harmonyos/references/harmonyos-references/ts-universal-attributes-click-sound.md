---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-click-sound
title: 点击音效
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 通用属性 > 交互属性 > 点击音效
category: harmonyos-references
scraped_at: 2026-09-02T15:00:56+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:60b98c870d21aba131a88a30b0203886f901b6cb78243a7bbd419801671702f4
---

设置组件是否启用默认点击音效，适用于需要控制组件点击反馈音效或自定义播放点击音效的场景。

**说明** 

* 从API version 24开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本模块接口仅可在Stage模型下使用。

## enableClickSoundEffect

enableClickSoundEffect(enabled: boolean | undefined): T

设置组件是否启用默认点击音效，适用于需要控制组件点击反馈音效或自定义点击发音的场景。是否能够发音还依赖设备声音相关的设置，如静音模式下不会播放音效。禁用默认点击音效后，开发者可以在onClick回调中调用音频相关接口自定义发音。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API version 24开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在TV中可正常调用，在其他设备中无效果。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enabled | boolean | undefined | 是 | 设置此组件是否启用默认点击音效。  true表示启用默认点击音效；false表示禁用默认点击音效。  值为undefined时，启用默认点击音效。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件，用于链式调用。 |

## 示例

### 示例1（禁用默认点击音效）

该示例通过配置enableClickSoundEffect属性，实现组件禁用默认点击音效，开发者可以在onClick回调中调用音频相关接口自定义发音。自定义发音可参考[SoundPool播放短音频指南](../harmonyos-guides/using-soundpool-for-playback.md)。

从API version 24开始，新增[enableClickSoundEffect](ts-universal-attributes-click-sound.md#enableclicksoundeffect)属性。

```ts
@Entry
@Component
struct Index {
  build() {
    Column() {
      Button('点击')
        .fontSize('20dp')
        .height('60')
        .width('200')
        .enableClickSoundEffect(false)
        .onClick(() => {
          // 此处自定义发音，参考SoundPool播放短音频指南。
        })
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center)
    .alignItems(HorizontalAlign.Center)
  }
}
```
