---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-101
title: 视频只支持竖屏全屏播放，不支持横屏全屏播放
breadcrumb: FAQ > 应用框架开发 > Web框架 > Web开发（ArkWeb） > 视频只支持竖屏全屏播放，不支持横屏全屏播放
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:32+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:e0c326c15dacab4f5df8ff8f48d0ef94761e0eea4bb87d9ba649a83c7672c403
---

## 问题现象

H5页面视频点击全屏后，视频页面只能保持竖屏全屏显示，未能跟随屏幕横竖屏变化。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/x3r41dYrRuyIoUGF820O2w/zh-cn_image_0000002628899122.png "点击放大")

## 背景知识

* 调用应用窗口的[setPreferredOrientation](../harmonyos-references/arkts-apis-window-window.md#setpreferredorientation9)可以设置进入应用后修改窗口的显示方向属性。
* 可以通过Web组件的[onFullScreenEnter](../harmonyos-references/arkts-basic-components-web-events.md#onfullscreenenter9)和[onFullScreenExit](../harmonyos-references/arkts-basic-components-web-events.md#onfullscreenexit9)方法，监听Web组件进入和退出全屏模式事件。
* 横屏状态下需通过CSS媒体查询、动态调整元素宽高与旋转角度，确保视频填充满屏幕。

  Web页面适配全屏播放视频流程图：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/ZK_DV44GT9WDyiO7Zf2bOg/zh-cn_image_0000002659138391.png)

## 问题定位

1. 通过DevEco Testing查看视频页面所在组件，该组件为Web组件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/N8EUrheBQvqudVUofqnrqw/zh-cn_image_0000002629059040.png "点击放大")
2. 全局搜索setPreferredOrientation方法，查看应用是否设置了横竖屏切换。

   ```screen
   import { webview } from '@kit.ArkWeb';
   import { window } from '@kit.ArkUI';
   import { common } from '@kit.AbilityKit';

   @Entry
   @Component
   struct Index {
     controller: webview.WebviewController = new webview.WebviewController();
     context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;

     aboutToAppear(): void {
       window.getLastWindow(this.context).then((lastWindow) => {
         lastWindow.setWindowLayoutFullScreen(true);
       });
     }

     build() {
       Column() {
         // $rawfile('index_cn.html')需要替换为开发者需要的网页资源文件
         Web({ src: $rawfile('index_cn.html'), controller: this.controller })
           .height('100%')
           .width('100%')
           .fileAccess(true)
           .geolocationAccess(false)
           .onFullScreenEnter(() => {
             // 未使用setPreferredOrientation设置旋转屏幕
           })
           .onFullScreenExit(() => {
             // 未使用setPreferredOrientation设置旋转屏幕
           });
       }
       .height('100%')
       .width('100%');
     }
   }
   ```

## 分析结论

应用未使用setPreferredOrientation，Web组件全屏时未触发屏幕旋转功能，导致视频竖屏全屏播放，不能横屏全屏播放。

## 修改建议

使用setPreferredOrientation，在Web组件全屏时设置屏幕旋转功能。

```screen
import { webview } from '@kit.ArkWeb';
import { window } from '@kit.ArkUI';
import { common } from '@kit.AbilityKit';

@Entry
@Component
struct Index {
  controller: webview.WebviewController = new webview.WebviewController();
  context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;

  aboutToAppear(): void {
    window.getLastWindow(this.context).then((lastWindow) => {
      lastWindow.setWindowLayoutFullScreen(true);
    });
  }

  private changeOrientation(isLandscape: boolean) {
    window.getLastWindow(this.context).then((lastWindow) => {
      lastWindow.setPreferredOrientation(isLandscape ? window.Orientation.LANDSCAPE : window.Orientation.PORTRAIT); // 设置屏幕旋转
      lastWindow.setWindowSystemBarEnable(isLandscape ? [] : ['status', 'navigation']); // 设置沉浸式全屏
    });
  }

  build() {
    Column() {
      Web({ src: $rawfile('index_cn.html'), controller: this.controller })
        .height('100%')
        .width('100%')
        .fileAccess(true)
        .geolocationAccess(false)
        .onFullScreenEnter(() => {
          this.changeOrientation(true);
        })
        .onFullScreenExit(() => {
          this.changeOrientation(false);
        });
    }
    .height('100%')
    .width('100%');
  }
}
```

src/main/resources/rawfile：

```screen
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>测试页面</title>
    <style>
        * {
            padding: 0;
            margin: 0;
        }
        body {
            width: 100vw;
            height: 100vh;
            box-sizing: border-box;
        }
        .page {
            display: flex;
            flex-direction: column;
            justify-content: flex-start;
            align-items: flex-start;
            width: 100%;
            height: 100%;
            box-sizing: border-box;
        }
        .descriptions {
            width: 100%;
            height: 78px;
            padding: 8px 0;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            margin-bottom: 12px;
            box-sizing: border-box;
            margin-top: 96px;
            padding-left: 16px;
        }
        .title {
            color: rgba(0, 0, 0, 0.9);
            font-size: 30px;
            font-weight: 700;
            line-height: 40px;
            height: 40px;
        }
        .sub-title {
            color: rgba(0, 0, 0, 0.6);
            font-size: 14px;
            font-weight: 400;
            line-height: 19px;
        }
        .video-box {
            width: 100%;
            display: flex;
            flex-direction: column;
            justify-content: start;
            align-items: center;
            box-sizing: border-box;
            margin-top: 200px;
        }
        .img-subtitle {
            color: black;
            font-size: 16px;
            font-weight: 400;
            line-height: 21px;
            margin-top: 8px;
        }
        .myVideo {
            width: 100%;
            height: calc(100vw * 9 / 16);
            object-fit: contain;
            background-color: black;
        }
    </style>
</head>
<body>
<div class="page">
    <div class="video-box">
        <video autoplay muted loop class="myVideo" controls>
            <!-- www.example.mp4需要替换为开发者需要的视频资源 -->
            <source src="www.example.mp4" type="video/mp4">
        </video>
    </div>
</div>
</body>
</html>
```

效果图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/sjCrDVsSRTeCC4668EtIUg/zh-cn_image_0000002659258343.png "点击放大")
