---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/arkweb-kit-troubleshooting-0003
title: ArkWeb网页视频全屏问题排查与解决
breadcrumb: FAQ > 应用框架开发 > Web框架 > Web开发（ArkWeb） > 故障排查 > ArkWeb网页视频全屏问题排查与解决
category: harmonyos-faqs
scraped_at: 2026-10-21T07:11:47+08:00
doc_updated_at: 2026-10-20
content_hash: sha256:fd27983c6844b58b7673552633ac966de6a8042f9f69268cc9a052d01e81a053
---

## 问题现象

通过Web组件加载H5页面，页面中视频的全屏按钮置灰，无法点击。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/ShzP1XsaTL2FuwyhpbgF9w/zh-cn_image_0000002768271488.png "点击放大")

## 定位过程

1. 查看浏览器访问H5页面时视频的全屏按钮是否是置灰状态；
2. Web组件加载时全屏按钮是否是置灰状态。

## 分析结论

直接打开HTML文件在浏览器中全屏按钮也是置灰的，由此怀疑是H5页面写法有问题，打开H5页面发现其加载了iframe，浏览器对iframe中的视频播放做了限制，根据其安全策略阻止视频全屏播放。

## 修改建议

需要添加iframe全屏权限属性allowfullscreen="true"，为了解决浏览器兼容问题，最好也加上mozallowfullscreen="true"、webkitallowfullscreen="true"这两个属性。

WebComponent.ets（下方Web组件引入的本地文件需要在rawfile文件夹中有相应的文件）:

```ts
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: $rawfile('test.html'), controller: this.controller })
        .domStorageAccess(true)
        .geolocationAccess(false)
        .fileAccess(false)
        .width('100%')
        .height('100%');
    }
    .width('100%')
    .height('100%');
  }
}
```

test.html（需要将下方iframe加载的src内容替换为实际的业务中的有视频播放的链接）:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta content="width=device-width, initial-scale=1.0" name="viewport">
    <title>Responsive iFrame</title>
</head>
<body>
<div style="width: 100%;height:100%;text-align:center;">
    <iframe allowfullscreen="true" data-v-558f754e="" mozallowfullscreen="true" src="xx.xx.xx"
            style="width:80%;height:100%;border:1px solid #000000;"
            webkitallowfullscreen="true"></iframe>
</div>
</body>
</html>
```
