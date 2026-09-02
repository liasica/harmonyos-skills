---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-104
title: 页面顶部会显示一个网址链接信息
breadcrumb: FAQ > 应用框架开发 > Web框架 > Web开发（ArkWeb） > 页面顶部会显示一个网址链接信息
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:32+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:f81e3add6fb40412ba71b789c11d376d584fbae864d2bd6794cdb86cad13e6fb
---

## 问题现象

页面标题处显示链接内容。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/SFcQ-Eu3R5mB2XpTJ0rawQ/zh-cn_image_0000002659138393.png "点击放大")

## 背景知识

* [Text](../harmonyos-references/ts-basic-components-text.md)为显示一段文本的组件。

* [Web](../harmonyos-references/arkts-basic-components-web.md)组件提供网页显示能力。
* H5页面使用title可设置页面标题，未设置时以链接地址作为标题。
* 使用[onTitleReceive](../harmonyos-references/arkts-basic-components-web-events.md#ontitlereceive)可通知应用程序页面document标题已更改，如果加载的页面未设置title元素指定的标题，Web组件将基于URL生成标题并返回给应用程序。

## 问题定位

1. 使用DevEco Testing-实用工具-UIViewer查看页面布局，标题为Text组件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/_zXXIcBtSAuasjSP6fX_RA/zh-cn_image_0000002629059042.png "点击放大")
2. 查看该Web组件的设置，该Web组件使用onTitleReceive获取H5页面的标题，并通过Text组件显示标题。

   ```ts
   Column() {
     Text(this.pageTitle)
       .width('100%')
       .height('10%')
       .textAlign(TextAlign.Center);

     Web({ src: $rawfile('video.html'), controller: this.controller })
       .height('90%')
       .width('100%')
       .fileAccess(true)
       .geolocationAccess(false)
       .onTitleReceive((event) => {
         if (event) {
           this.pageTitle = event.title;
         }
       });
   }
   ```
3. 使用Devtools或开发者工具查看该H5页面的设置，该H5页面未使用title设置页面标题。

   ```html
   <!DOCTYPE html>
   <html lang="zh">
   <head>
       <meta charset="UTF-8" />
       <meta name="viewport" content="width=device-width, initial-scale=1.0" />
       <!-- 未使用title设置页面标题 -->
   </head>
   </html>
   ```

## 分析结论

H5页面的标题内容未设置，导致页面标题处显示链接内容。

## 修改建议

合理设置H5页面的<title>标签中的标题内容。

```ts
import { webview } from '@kit.ArkWeb';
import { window } from '@kit.ArkUI';
import { common } from '@kit.AbilityKit';

@Entry
@Component
struct WebVideo {
  controller: webview.WebviewController = new webview.WebviewController();
  @State pageTitle: string = '';

  aboutToAppear(): void {
    let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
    window.getLastWindow(context).then((lastWindow) => {
      lastWindow.setWindowLayoutFullScreen(true);
    });
  }

  build() {
    Column() {
      Text(this.pageTitle)
        .width('100%')
        .height('10%')
        .textAlign(TextAlign.Center);

      Web({ src: $rawfile('video.html'), controller: this.controller })
        .height('90%')
        .width('100%')
        .fileAccess(true)
        .geolocationAccess(false)
        .onTitleReceive((event) => {
          if (event) {
            this.pageTitle = event.title;
          }
        });
    }
    .height('100%')
    .width('100%')
    .padding({ top: '123px', bottom: '91px' })
    .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM]); // 扩展页面区域到导航栏和状态栏
  }
}
```

```html
<!DOCTYPE html>
<html lang="zh">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>视频页面</title>
    <style>
        * {
            padding: 0;
            margin: 0;
        }

        body {
            width: 100%;
            height: 100%;
            box-sizing: border-box;
            background-color: #ffffff;
        }

        .page {
            display: flex;
            justify-content: center;  /* 水平居中 */
            align-items: center;      /* 垂直居中 */
            align-items: flex-start;
            width: 100%;
            height: 100%;
            box-sizing: border-box;
        }

        .video-box {
            width: 100%;
            height: calc(100vw * 9 / 16);
            display: flex;
            justify-content: center;  /* 水平居中 */
            align-items: center;      /* 垂直居中 */
            align-items: center;
            box-sizing: border-box;
            margin-top: 200px;
        }

        .myVideo {
            width: 100%;
            height: 100%;
            object-fit: contain;
            background-color: black;
        }
    </style>
</head>
<body>

<div class="page" >
    <div class="video-box" >
        <video autoplay muted loop class="myVideo" controls>
            <!-- "www.example.mp4"需要替换为开发者需要的视频资源文件 -->
            <source src="www.example.mp4" type="video/mp4">
        </video>
    </div>
</div>
</body>
</html>
```

效果图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/HzNmogmIR1KvN0V-MWjh8g/zh-cn_image_0000002659258345.png "点击放大")
