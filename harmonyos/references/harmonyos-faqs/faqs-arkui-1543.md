---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1543
title: web组件隐藏时，回调事件不触发
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > web组件隐藏时，回调事件不触发
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:11+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:dfad6bfa893bdf56253f7c5fbdd11ee21b596221bf5373bee9c403b0b9ccc405
---

## 问题现象

当web组件需要隐藏时，回调事件不触发，比如onPageBegin未触发。

问题代码示例参考如下：

```ts
Web({})
  .onPageBegin(() => {
    console.info(`into onPageBegin`)
  })
  .visibility(Visibility.None)
```

## 背景知识

[visibility](../harmonyos-references/ts-universal-attributes-visibility.md)是控制组件显隐控制的一个基础属性。其值类型说明参考文档：[Visibility枚举说明](../harmonyos-references/ts-appendix-enums.md#visibility)。

## 问题定位

通过ArkUI Inspector工具，可以看到出问题的组件并没有被渲染出来。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/_gzHfCtTRE2BiJzcRj985w/zh-cn_image_0000002658968439.png "点击放大")

## 分析结论

visibility属性设置Visibility.None后，是不会渲染组件的，所以组件相关的生命周期也不会触发。

## 修改建议

把visibility属性的值改成Visibility.Hidden即可。

```ts
import webview from '@ohos.web.webview';

@Entry
@Component
struct Index {
  // 开发者需根据自身需求填写网址
  @State webSrc: string = 'xxx';
  @State webController: WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: this.webSrc, controller: this.webController })
        .size({ width: '100%', height: '100%' })
        .onPageBegin(() => {
          console.info(`into onPageBegin (web Hidden)`);
        })
        // 按照示例代码，开发者需要隐藏，因此设置为Visibility.Hidden
        .visibility(Visibility.Hidden)
        .geolocationAccess(false)
        .fileAccess(false);
    }
    .height('100%')
    .width('100%')
  }
}
```

日志中onPageBegin()触发，打印了into onPageBegin (web Hidden)。
