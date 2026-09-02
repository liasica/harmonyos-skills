---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-145
title: Web组件加载H5，页面中视频全屏按钮置灰
breadcrumb: FAQ > 应用框架开发 > Web框架 > Web开发（ArkWeb） > Web组件加载H5，页面中视频全屏按钮置灰
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:33+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:a387541eb6067ccd52eb9a8c220a893eb999dc82b39bb0a0761f54035be941dd
---

## 问题现象

通过Web组件加载H5页面，页面中视频的全屏按钮置灰，无法点击。

问题效果预览：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/03/v3/9cmkUE5MRgSvZGJTmLBc3w/zh-cn_image_0000002628899138.png "点击放大")

## 背景知识

[使用Web组件加载页面](../harmonyos-guides/web-page-loading-with-web-components.md)：页面加载是Web组件的基本功能。根据页面加载数据来源可以分为三种常用场景，包括加载网络页面、加载本地页面、加载HTML格式的富文本数据。

## 问题定位

1. 查看浏览器访问H5页面时视频的全屏按钮是否是置灰状态。
2. Web组件加载时全屏按钮是否是置灰状态。

## 分析结论

直接打开HTML文件在浏览器中全屏按钮也是置灰的，由此怀疑是H5页面写法有问题，打开H5页面发现其加载了iframe，浏览器对iframe中的视频播放做了限制，根据其安全策略阻止视频全屏播放。

## 修改建议

需要添加iframe全屏权限属性allowfullscreen="true"，为了解决浏览器兼容问题，最好也加上mozallowfullscreen="true"、webkitallowfullscreen="true"这两个属性。

WebComponent.ets（下方Web组件引入的本地文件需要在rawfile文件夹中有相应的文件）：

```screen
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

test.html（需要将下方iframe加载的src内容替换为实际的业务中的有视频播放的链接）：

```screen
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
