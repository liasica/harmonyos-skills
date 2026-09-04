---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/scenario-button-annotation
title: 按钮标注
breadcrumb: 指南 > 应用框架 > Accessibility Kit（无障碍服务） > 提升应用的无障碍体验 > 提升屏幕朗读无障碍体验 > 按钮标注
category: harmonyos-guides
scraped_at: 2026-09-05T06:13:48+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:7a48f18afe894d9ba30a586d28380d827a5acbced42fcdbd5cb358f7b2db22ec
---

## 设计场景

对于用户可点击等操作的任何按钮，如果不是文本类控件，则须通过给出标注信息，包括用户自定义的控件中的虚拟按钮区域，否则可能会导致屏幕朗读用户无法完成对应的功能。此类控件在进行标注时，标注文本不要包含控件类型、“单指双击即可打开”之类的字符串，此部分指引由屏幕朗读根据控件类型、控件状态，并结合用户是否开启了“新手指引”自动追加朗读。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2/v3/j0K-l9yPTBKYrJtdutwR9Q/zh-cn_image_0000002742002251.png)

## 开发流程

在下面的代码片段中，您可以看到[Image](../harmonyos-references/ts-basic-components-image.md)组件（它实际上是一个播放/暂停按钮），通过设置[accessibilityText](../harmonyos-references/ts-universal-attributes-accessibility.md#accessibilitytext12)属性提供标注信息：

```typescript
const RESOURCE_STR_PLAY: Resource = $r('sys.media.ohos_ic_public_play');
const RESOURCE_STR_PAUSE: Resource = $r('sys.media.ohos_ic_public_pause');

@Entry
@Component
export struct Rule_2_1_5 {
  title: string = 'Rule 2.1.5';
  @State isPlaying: boolean = false;
  play() {
    console.info('play audio file');
  }

  pause() {
    console.info('pause playing of audio file');
  }

  build() {
    NavDestination() {
      Column() {
        Flex({
          direction: FlexDirection.Column,
          alignItems: ItemAlign.Center,
          justifyContent: FlexAlign.Center,
        }) {
          Row() {
            Image(this.isPlaying ? RESOURCE_STR_PAUSE : RESOURCE_STR_PLAY)
              .width(50)
              .height(50)
              .onClick(() => {
                this.isPlaying = !this.isPlaying;
                if (this.isPlaying) {
                  this.play();
                } else {
                  this.pause();
                }
              })
              .accessibilityRole(AccessibilityRoleType.BUTTON)
              .accessibilityText(this.isPlaying ? 'Pause' : 'Play') // 设置注释信息。
            Text('Good_morning.mp3')
              .margin({
                left: 10
              })
          }
        }
        .width('100%')
        .height('100%')
        .backgroundColor(Color.White)
      }
    }
    .title(this.title)
  }
}
```
