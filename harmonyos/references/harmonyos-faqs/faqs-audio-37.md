---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-audio-37
title: 如何控制音量条的位置或显隐
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 音频（Audio） > 如何控制音量条的位置或显隐
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:43+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:e78d04676c90c8a2b5558ea64479c785ae0b2da67fdc70c4117bed79bced7d45
---

## 问题现象

是否有控制系统音量进度条的位置或者显示隐藏的API？

## 效果预览

正常显示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/5pCW_QwuThWy6GTaQlPbCA/zh-cn_image_0000002658792009.png "点击放大")

使用Position属性隐藏后：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/czlwPfYDT72c19hvtNRMJQ/zh-cn_image_0000002628552632.png "点击放大")

## 背景知识

应用无法直接调节系统音量，可以通过[系统音量面板](../harmonyos-references/ohos-multimedia-avvolumepanel.md)，让用户通过界面操作来调节音量。当用户通过应用内音量面板调节音量时，系统会展示音量提示界面，显性地提示用户系统音量发生改变。

## 解决方案

目前没有控制系统音量进度条位置或显隐的API，可以给页面增加[音量面板组件](../harmonyos-references/ohos-multimedia-avvolumepanel.md)并使用[Position](../harmonyos-references/ts-types.md#position)属性将面板移出屏幕外，以实现系统音量进度条和音量面板的隐藏效果。

```screen
import { AVVolumePanel } from '@kit.AudioKit';

@Entry
@Component
struct AVVolumePanelPage {
  @State volume: number = 0;

  build() {
    Row() {
      Column() {
        AVVolumePanel({
          volumeLevel: this.volume,
          volumeParameter: {
            position: {
              x: -100,
              y: -200
            }
          }
        })
      }
    }.width('50%').height('50%')
  }
}
```
