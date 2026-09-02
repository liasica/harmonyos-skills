---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-119
title: 页面标题内容快速变化
breadcrumb: FAQ > 应用框架开发 > Web框架 > Web开发（ArkWeb） > 页面标题内容快速变化
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:32+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:cf8d9679cdde3c87a6d90bb4d5f77168ad1545a62d4c6f30c3664aaa31632953
---

## 问题现象

进入Web页面时，页面顶部的标题内容快速变化。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/tnzMoK_BQHy7qmngIXt-zg/zh-cn_image_0000002628899130.png "点击放大")

## 背景知识

* [Web](../harmonyos-references/arkts-basic-components-web.md)：提供具有网页显示能力的Web组件。
* [onTitleReceive](../harmonyos-references/arkts-basic-components-web-events.md#ontitlereceive)：当页面文档标题<title>元素发生变更时，触发回调。若当前页面未显示设置标题，ArkWeb将在加载完成前基于页面的URL生成标题并返回给应用。
* [onPageEnd](../harmonyos-references/arkts-basic-components-web-events.md#onpageend)：网页加载完成时触发该回调，且只在主frame触发，iframe或者frameset的内容加载时不会触发此回调。
* [onLoadIntercept](../harmonyos-references/arkts-basic-components-web-events.md#onloadintercept10)：当Web组件加载URL之前触发该回调，用于判断是否阻止此次访问。

## 问题定位

查看Web组件相关设置，发现使用了onTitleReceive方法动态获取页面标题并实时展示，且没有使用onPageEnd在页面加载完成后再显示标题。

```ts
Web({ src: this.url, controller: this.controller })
  .onTitleReceive(()=>{
    // 获取页面标题
  })
  // 未使用onPageEnd
```

## 分析结论

应用使用了onTitleReceive方法动态获取页面标题并实时展示，页面跳转到目的页面的过程中需要跳转到其他的页面，页面标题实时显示从而发生闪变。

## 修改建议

页面加载过程中不显示标题，通过onLoadIntercept判断是否跳转到目的网页，并通过onPageEnd在页面加载完成后再显示标题。

```ts
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct Index {
  controller: webview.WebviewController = new webview.WebviewController();
  @State title: string = '';
  @State lastTitle: string = '';
  @State url: string = '';

  build() {
    Scroll() {
      Column() {
        Text(this.lastTitle)
          .height('5%')
          .width('100%')
          .textAlign(TextAlign.Center)
          .fontSize(20);
        Web({ src: $rawfile('transitions.html'), controller: this.controller })
          .height('95%')
          .width('100%')
          .fileAccess(true)
          .geolocationAccess(false)
          .initialScale(85)
          .onTitleReceive((event) => {
            if (event) {
              this.title = event.title;
            }
          })
          .onLoadIntercept((event) => {
            this.url = event.data.getRequestUrl(); // 获取当前页面的URL
            return false;
          })
          .onPageEnd(() => {
            // 跳转到目的页面并加载完成后才显示标题
            if (this.url === 'resource://rawfile/title.html') {
              this.lastTitle = this.title;
            }
          });
      }
      .height('100%')
      .width('100%');
    }
    .width('100%')
    .height('100%');
  }
}
```

resource://rawfile/transitions.html：

```html
<!DOCTYPE html>
<html lang="zh">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
    <title>过渡页面</title>
</head>
<body>

<script>
    setTimeout(() => {
        // "./text.html"需替换为开发者需要的网页资源文件
        window.location.href = "./title.html";
    }, 300);
</script>

</body>
</html>
```

resource://rawfile/title.html：

```html
<!DOCTYPE html>
<html lang="en" data-dpr="1">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>古文展示</title>
    <style>
        body {
          font-size: 20px;
          height: 100%;
          width: 100%;
          padding: 20px;
        }
    </style>
</head>

<body>
<div>
    六王毕，四海一，蜀山兀，阿房出。覆压三百余里，隔离天日。骊山北构而西折，直走咸阳。二川溶溶，流入宫墙。五步一楼，十步一阁；廊腰缦回，檐牙高啄；各抱地势，钩心斗角。盘盘焉，囷囷焉，蜂房水涡，矗不知其几千万落。长桥卧波，未云何龙？复道行空，不霁何虹？高低冥迷，不知西东。歌台暖响，春光融融；舞殿冷袖，风雨凄凄。一日之内，一宫之间，而气候不齐。(不知其 一作：不知乎；西东 一作：东西)

    　　妃嫔媵嫱，王子皇孙，辞楼下殿，辇来于秦。朝歌夜弦，为秦宫人。明星荧荧，开妆镜也；绿云扰扰，梳晓鬟也；渭流涨腻，弃脂水也；烟斜雾横，焚椒兰也。雷霆乍惊，宫车过也；辘辘远听，杳不知其所之也。一肌一容，尽态极妍，缦立远视，而望幸焉。有不见者，三十六年。燕赵之收藏，韩魏之经营，齐楚之精英，几世几年，剽掠其人，倚叠如山。一旦不能有，输来其间。鼎铛玉石，金块珠砾，弃掷逦迤，秦人视之，亦不甚惜。(有不见者 一作：有不得见者)
</div>

</body>

</html>
```

访问在线网页时需添加网络权限：ohos.permission.INTERNET，具体申请方式请参考[声明权限](../harmonyos-guides/declare-permissions.md)。

效果图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/6aY29U-MSS2_bCJtsgktOw/zh-cn_image_0000002659138399.png "点击放大")
