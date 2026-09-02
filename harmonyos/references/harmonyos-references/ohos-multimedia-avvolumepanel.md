---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-multimedia-avvolumepanel
title: "@ohos.multimedia.avVolumePanel (音量面板)"
breadcrumb: API参考 > 媒体 > Audio Kit（音频服务） > ArkTS组件 > @ohos.multimedia.avVolumePanel (音量面板)
category: harmonyos-references
scraped_at: 2026-09-02T15:02:20+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:c4e977d0129d538e681d560ca7e68d9d4accc4f15e16d76311a939b33b1acdf6
---

本模块提供创建音量面板AVVolumePanel的功能，提供展示和调节系统音量的统一面板。

应用无法直接调节系统音量，可以通过系统音量面板，让用户通过界面操作来调节音量。当用户通过应用内音量面板调节音量时，系统会展示音量提示界面，显性地提示用户系统音量发生改变。

**说明** 

* 本模块首批接口从API version 12开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 示例效果请以真机为准，当前DevEco Studio预览器无真实音量展示和调节功能。
* **设备限制：**
  + 在穿戴设备上，可用于调节系统音量，但不显示界面，需开发者自行设计界面。
  + 本模块接口暂不支持TV设备使用。
* 系统音量条：以手机为例，通过侧边按键触发的系统音量条。
* 系统音量面板：使用[AVVolumePanel](ohos-multimedia-avvolumepanel.md#avvolumepanel)组件的默认样式。
* 自定义的音量面板：使用[AVVolumePanel](ohos-multimedia-avvolumepanel.md#avvolumepanel)组件，将系统音量面板隐藏后，应用自行设计并展示的音量调节界面。

## 导入模块

```js
import { AVVolumePanel } from '@kit.AudioKit';
```

## 属性

支持[通用属性](ts-component-general-attributes.md)。

## AVVolumePanel

AVVolumePanel({volumeLevel?: number, volumeParameter?: AVVolumePanelParameter})

音量面板，可用于在当前应用内展示音量调节面板。

**装饰器类型：** [@Component](../harmonyos-guides/arkts-create-custom-components.md#component)

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

| 名称 | 类型 | 必填 | 装饰器类型 | 说明 |
| --- | --- | --- | --- | --- |
| volumeLevel | number | 否 | @Prop | 通过音量面板设置的音量值。  如果不设置该参数，则使用当前设备音量值。  该值应介于当前设备音量的最小值和最大值之间。  如果该值大于当前设备音量的最大值，则视为设置最大音量值。  如果该值小于当前设备音量的最小值，则视为设置最小音量值。  获取设备的最大值、最小值和当前值，可参考[AudioVolumeGroupManager](arkts-apis-audio-audiovolumegroupmanager.md)。 |
| volumeParameter | [AVVolumePanelParameter](ohos-multimedia-avvolumepanel.md#avvolumepanelparameter) | 否 | @Prop | 设置音量面板的自定义参数。  如果不设置该参数，则使用系统音量条。 |

## AVVolumePanelParameter

音量面板参数设置。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| position | [Position](ts-types.md#position) | 否 | 是 | 设置音量面板的位置，坐标单位：vp。  如果不设置该参数，则使用系统默认的音量面板位置。  如果设置该参数且参数对应屏幕内有效范围的位置，则显示应用设置的位置；超出屏幕范围的位置视为屏幕外位置。  如果设置该参数且参数对应屏幕外位置，例如（-1, -1），则隐藏系统默认音量面板。  **注意：** 若应用需隐藏系统默认音量面板，必须提供自定义音量面板，以确保用户仍可调节音量。 |

## 事件

支持[通用事件](ts-component-general-events.md)。

## 使用建议

1. 应用在实现自定义音量面板的过程中，建议使用音频框架的音量变化监听接口，通过接口回调的音量类型volumeEvent.volumeType，音量等级volumeEvent.volume以及是否显示音量面板volumeEvent.updateUi等信息，应用可以判断是否需要处理当前数据和显示自定义的音量面板，具体可参考[on('streamVolumeChange')](arkts-apis-audio-audiovolumemanager.md#onstreamvolumechange20)介绍。
2. 为确保用户能感知音量变化，不允许应用后台调节音量，系统会做出对应的控制措施。
3. 系统提供音量面板的目的是，由用户在应用界面主动操作来调节系统音量，而非应用主动调节。因此，若应用通过设置音量面板位置参数隐藏了系统默认音量面板，必须提供应用自定义的音量面板，以确保用户正常进行音量调节。

## 示例

音量面板功能的示例说明参考如下。需要实际修改volume值或者按压音量按键体验调节音量效果。

```ts
import { AVVolumePanel } from '@kit.AudioKit';

@Entry
@Component
struct Index {

  @State volume: number = 0;

  build() {
    Row() {
      Column() {
        AVVolumePanel({
          volumeLevel: this.volume,
          volumeParameter: {
            position: {
              x: 100,
              y: 200
            }
          }
        })
      }
    }.width('50%').height('50%')
  }
}
```
