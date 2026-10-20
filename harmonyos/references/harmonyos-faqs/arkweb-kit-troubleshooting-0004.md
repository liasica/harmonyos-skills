---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/arkweb-kit-troubleshooting-0004
title: ArkWeb视频横屏全屏播放问题定位
breadcrumb: FAQ > 应用框架开发 > Web框架 > Web开发（ArkWeb） > 故障排查 > ArkWeb视频横屏全屏播放问题定位
category: harmonyos-faqs
scraped_at: 2026-10-21T07:11:48+08:00
doc_updated_at: 2026-10-20
content_hash: sha256:fae067070437a878794029272c4c7edc25243923cebf88c7e29e52d80703e355
---

## 问题现象

H5页面视频点击全屏后，视频页面只能保持竖屏全屏显示，未能跟随屏幕横竖屏变化。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/fetYRUA4QWuhJr3XSRiDXA/zh-cn_image_0000002768114830.png "点击放大")

## 定位过程

1. 通过DevEco Testing查看视频页面所在组件，该组件为Web组件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/1eomVJmMSP6Up_H8dPT1kA/zh-cn_image_0000002797434787.png "点击放大")
2. 全局搜索setPreferredOrientation方法，查看应用是否设置了横竖屏切换。

   ```ts
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

```ts
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

```html
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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/nTqRP5fASmCtu1b8pvuibg/zh-cn_image_0000002797394765.png "点击放大")
