---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1410
title: 使用组件截图后得到的图片如何传递给其他组件
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 使用组件截图后得到的图片如何传递给其他组件
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:18+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:0829dbbaaf22f38c1fb6a12420fa48524a2e36cc4e29dfb1e3f703ea82cd6f8c
---

## 问题现象

组件截图后如何传递到其他组件进行显示？

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/LbFoTubXQb-CB-iK--orxg/zh-cn_image_0000002628763166.gif "点击放大")

## 背景知识

Class (ComponentSnapshot)中[get()](../harmonyos-references/arkts-apis-uicontext-componentsnapshot.md#get12-1)方法可以通过组件标识找到对应组件进行截图，并返回[PixelMap](../harmonyos-references/arkts-apis-image-pixelmap.md)格式的图片。

## 解决方案

以自定义弹窗组件为示例：

1. 给需要截图的组件Scroll添加组件标识。
2. 调用componentSnapshot.get根据组件标识进行截图。
3. 得到的PixelMap图片传递弹窗组件。

使用componentSnapshot.get进行截图的页面代码：

```ts
import { image } from '@kit.ImageKit';

@Entry
@Component
struct SnapShotExample {
  @State items: string[] =
    ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20',
      '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32'];
  @State pixMap: image.PixelMap | undefined = undefined;
  @State mText: string = '我是内容';
  // dialogController只可以传入pixMap，options与buffer无效果
  dialogController: CustomDialogController =
    new CustomDialogController({ builder: CustomDialogComponent({ pixelMap: this.pixMap, text: this.mText }) });

  build() {
    Column() {
      Text('我是标题')
        .width('100%')
        .height(100)
        .textAlign(TextAlign.Center)
        .fontColor(Color.Black)
        .backgroundColor('#f1f3f5');
      Scroll() {
        Column() {
          ForEach(this.items, (item: string) => {
            Text('我是内容' + item).width('100%').height(50).fontColor('#0a59f7');
          });
        }.width('100%').padding(24);
      }.width('100%').layoutWeight(1).id('mainScroll');

      Blank().width('100%').height(1).backgroundColor(Color.Black);
      // 展示截屏图片
      Image(this.pixMap).width('100%').layoutWeight(0.5).objectFit(ImageFit.Contain);

      Button('点击截图').width(100).height(45).onClick(() => {
        // 核心方法，获取已加载的组件的截图
        let snapShot = this.getUIContext().getComponentSnapshot();
        snapShot.get('mainScroll', { scale: 0.8, waitUntilRenderFinished: true })
          .then((pixMap: image.PixelMap) => {
            // 用pixMap方式，同时可以对比测试
            this.pixMap = pixMap;
            // 打开弹窗
            this.dialogController.open();

            this.mText = '截图成功';
          })
          .catch((err: Error) => {
            console.error(`截图失败：${err}`);
          });
      });
    }.width('100%').height('100%');
  }
}
```

弹窗组件代码：

```screen
// 自定义弹窗组件，用于展示截屏图片
@CustomDialog
struct CustomDialogComponent {
  controller?: CustomDialogController;
  pixelMap: image.PixelMap | undefined; /*= undefined*/
  @Prop text: string | undefined;

  build() {
    Column() {
      Text(this.text).width('100%').height(50).textAlign(TextAlign.Center).fontColor('#0a59f7');
      // 展示截屏图片
      Image(this.pixelMap).width(200).height(500).objectFit(ImageFit.Contain);

      Button('关闭')
        .width(100)
        .height(45)
        .backgroundColor('#0a59f7')
        .onClick(() => {
          // 关闭弹窗
          this.controller?.close();
        })
        .margin({ top: 10 });
    };
  }
}
```

## 常见FAQ

Q：调用this.getUIContext().getComponentSnapshot().get()接口是否需要申请权限？

A：不需要，接口说明中无权限要求。

Q：调用this.getUIContext().getComponentSnapshot().get()接口失败，错误码100001，原因是什么？

A：错误码100001标识无效的ID，接口参数ID，不支持未挂树组件，当传入的组件标识是离屏或缓存未挂树的节点时，系统不会对其进行截图。确认ID对应的组件是否存在。
