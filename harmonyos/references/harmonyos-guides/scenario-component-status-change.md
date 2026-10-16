---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/scenario-component-status-change
title: 控件状态变化
breadcrumb: 指南 > 应用框架 > Accessibility Kit（无障碍服务） > 提升应用的无障碍体验 > 提升屏幕朗读无障碍体验 > 控件状态变化
category: harmonyos-guides
scraped_at: 2026-10-17T06:40:59+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:0fea09c57ba67c0eab1924446e8c67c7ba645c7e1c76011d5819e6bf7fd1d6f2
---

## 开发流程

例如下图，播放暂停按钮对应着两种状态，在状态切换时需要实时变化对应的标注信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/0WBzYp0xRme9j5Q5JOd80g/zh-cn_image_0000002794409541.png)

```typescript
import { PromptAction } from "@kit.ArkUI"

const RESOURCE_STR_PLAY: Resource = $r('sys.media.ohos_ic_public_play');
const RESOURCE_STR_PAUSE: Resource = $r('sys.media.ohos_ic_public_pause');

@Entry
@Component
export struct Rule_2_1_8 {
  title: string = 'Rule 2.1.8';
  @State isPlaying: boolean = true;
  uiContext: UIContext = this.getUIContext();
  promptAction: PromptAction = this.uiContext.getPromptAction();
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
                this.promptAction.showToast({
                  message :this.isPlaying ? 'Play' : 'Pause'
                })
                this.isPlaying = !this.isPlaying;
                if (this.isPlaying) {
                  this.play();
                } else {
                  this.pause();
                }
              })
              .accessibilityText(this.isPlaying ? 'Pause' : 'Play') // 设置可访问性框架的注释信息。
          }
        }
        .width('100%')
        .height('100%')
        .backgroundColor(Color.White)
      }
    }.title(this.title)
  }
}
```
