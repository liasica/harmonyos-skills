---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1122
title: 评论栏显隐不正确
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 评论栏显隐不正确
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:15+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:db85f4f87d90bd35440707c5ac43f880ca9ec90f27283d09f1736a9e7648544f
---

## 问题现象

进入H5页面，点击播放视频，全屏后再退出全屏，底部出现评论栏，且无法关闭。

问题现象：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/ytn3kaFxRQ-DQkLVEpjs-g/zh-cn_image_0000002658808781.png "点击放大")

## 背景知识

在HarmonyOS中，通过[visibility](../harmonyos-references/ts-universal-attributes-visibility.md#visibility)属性可以控制组件的显隐。

## 问题定位

第一次进入视频播放页底部没有评论栏，全屏后退出，评论栏出现，且返回列表页不会消失，判断是评论栏的显隐控制有问题。排查代码中触发visibility属性值改变的位置是否正确，错误示范如下：

```ts
Image(this.fullVideoImg)
  .onClick(() => {
    // ...
    this.controller.requestFullscreen(true); // 点击全屏
    this.isCommentShow = true; // 设置显示评论栏
  })

Row() {
  // ...
}
.visibility(this.isCommentShow ? Visibility.Visible : Visibility.None) // 控制评论栏显隐
```

## 分析结论

点击全屏后设置显示评论栏，之后没有再将评论栏隐藏，导致退出视频播放后评论栏仍然存在。

## 修改建议

将评论栏的显示操作放在Web组件的[onFullScreenEnter](../harmonyos-references/arkts-basic-components-web-events.md#onfullscreenenter9)方法内，并在[onFullScreenExit](../harmonyos-references/arkts-basic-components-web-events.md#onfullscreenexit9)中设置隐藏，确保评论栏只在视频全屏播放时出现，其他页面状态下隐藏，示例代码如下：

```ts
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebVideoPlay {
  webSrc: string = 'XXX.XXX.com'; // 使用前可以替换为正式页面，如：https://developer.huawei.com/consumer/cn/design/devstart/
  controller: webview.WebviewController = new webview.WebviewController();
  @State isComment: boolean = false;

  build() {
    Column() {
      Web({ src: this.webSrc, controller: this.controller })
        .fileAccess(false)
        .geolocationAccess(false)
        .height(this.isComment ? '90%' : '100%')
        .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.BOTTOM])
        .onFullScreenEnter(() => {
          this.isComment = true;
        })
        .onFullScreenExit(() => {
          this.isComment = false;
        })

      Row() {
        Text('评论')
        TextInput()
          .width('70%')
      }
      .width('100%')
      .height('10%')
      .justifyContent(FlexAlign.SpaceEvenly)
      .visibility(this.isComment ? Visibility.Visible : Visibility.None)
      .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.BOTTOM])
    }
    .width('100%')
    .height('100%')
    .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.BOTTOM])
  }
}
```

运行效果：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/hpkuw72xT0ibTjG7emBPAA/zh-cn_image_0000002628569418.png "点击放大")
