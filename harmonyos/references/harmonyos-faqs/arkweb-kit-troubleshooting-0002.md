---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/arkweb-kit-troubleshooting-0002
title: ArkWeb页面顶部显示链接信息问题定位
breadcrumb: FAQ > 应用框架开发 > Web框架 > Web开发（ArkWeb） > 故障排查 > ArkWeb页面顶部显示链接信息问题定位
category: harmonyos-faqs
scraped_at: 2026-10-28T07:48:04+08:00
doc_updated_at: 2026-10-20
content_hash: sha256:f694069d9f223da53cb6a62fffbe0daafc78eb45f0b04e919ffa81736a5a43c5
---

## 问题现象

页面标题处显示链接内容。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/xav1I8UDQ2mxY6KVN8O5iw/zh-cn_image_0000002795303511.png "点击放大")

## 定位过程

1. 使用DevEco Testing-实用工具-UIViewer查看页面布局，标题为Text组件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/oEAny4wFQE-J2UbPg6CJ5Q/zh-cn_image_0000002795463357.png "点击放大")
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
<!-- Start solution1 -->
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>视频页面</title>
    <!-- End solution1 -->
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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/DbNocH2eSyGgaM8Fefjt7A/zh-cn_image_0000002766065434.png "点击放大")
