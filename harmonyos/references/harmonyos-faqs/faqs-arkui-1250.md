---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1250
title: 应用启动时出现黑屏
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 应用启动时出现黑屏
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:15+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:742edd873421cb3d5cb82b1735b0ae1b1ccd3e162aff2b53b0c5cd09d79dd912
---

## 问题现象

应用启动后，在页面内容出现前显示黑屏。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/6t908K0RT3GZoKdIEftigw/zh-cn_image_0000002628755348.png "点击放大")

## 背景知识

[setTimeout](../harmonyos-references/js-apis-timer.md#settimeout)可用来设定一个定时器，在定时到期以后执行注册的回调函数。

## 问题定位

查看启动页在资源加载完成前，是否使用过渡动效或页面。若没有使用过渡动效或页面，启动页资源加载完成前无显示内容，导致黑屏。

## 分析结论

启动页未设置资源加载完成前的替代显示内容，导致加载好内容前无显示内容，出现黑屏，影响用户体验。

## 修改建议

启动页设置资源加载完成前的替代显示内容。

```screen
import { window } from '@kit.ArkUI';
import { common } from '@kit.AbilityKit';

@Entry
@Component
struct StartDemo {
  @State loading: boolean = true;
  @State isShow: boolean = false;

  aboutToAppear() {
    let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
    window.getLastWindow(context).then((windowClass) => {
      windowClass.setWindowLayoutFullScreen(true);
    });
    // 加载好内容后到时才显示，避免闪屏
    setTimeout(() => {
      this.isShow = true;
    }, 2000);

    // 模拟页面内容加载
    setTimeout(() => {
      this.loading = false;
    }, 3000);
  }

  build() {
    Column() {
      if (!this.loading && this.isShow) {
        // 加载好的页面内容
        Stack() {
          Text('Hello World')
            .fontSize(20);
        }
        .width('100%')
        .height('100%')
        .backgroundColor(Color.White);
      } else {
        // 未加载好页面内容时使用图片替代
        Stack() {
          Image($r('app.media.beauty')) // $r('app.media.beauty')需要替换为开发者需要的图片资源文件
            .width('100%')
            .height('100%')
            .objectFit(ImageFit.Fill);
        }
        .width('100%')
        .height('100%');
      }
    }
    .backgroundColor(Color.Black)
    .width('100%')
    .height('100%');
  }
}
```

效果图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/GyRUb1cBRPOu0q9cL2kKog/zh-cn_image_0000002658954669.png "点击放大")
