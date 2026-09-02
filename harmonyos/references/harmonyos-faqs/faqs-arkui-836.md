---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-836
title: 无法查看头像
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 无法查看头像
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:04+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:8f6d7ba442909b7e804c05efe6af1913c214f3b6c89438221c5f7650a47da470
---

## 问题现象

点击头像没有反应，无法进行大图预览。

## 背景知识

* [DevEco Testing](../harmonyos-guides/deveco-testing.md)：DevEco Testing是一款专项集成测试工具，提供了多项测试能力。DevEco Testing将测试能力以测试服务卡片的形式呈现给用户，无需复杂的配置，即可一键执行测试任务，同时提供了测试报告和分析，辅助开发者发现应用和产品问题，提升应用质量。
* [CustomDialog](../harmonyos-references/ts-methods-custom-dialog-box.md#customdialogcontrolleroptions对象说明)：通过CustomDialogController类显示自定义弹窗。使用弹窗组件时，优先考虑自定义弹窗，便于弹窗样式与内容的自定义。

## 问题定位

通过DevEco Testing工具的实用工具下的UIViewer，获取页面的DOM树，找到图片所在节点，排查clickable属性是否为true。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/si01SUm6TXO50mVx2dlUXw/zh-cn_image_0000002658917671.png "点击放大")

## 分析结论

通过页面DOM树，找到对应节点下的Image标签，查看clickable属性为false，表示没有添加点击事件无法进行大图预览。

## 修改建议

1. 创建一个自定义弹窗存放预览的大图。
2. 对自定义弹窗的控制器dialogController进行初始化设置宽高、圆角、背景色等参数。
3. 将显示自定义弹窗内容的open()方法添加到Image组件点击事件中。

```ts
@Entry
@Component
struct ShowLargeImage {
  dialogController: CustomDialogController | null = new CustomDialogController({
    builder: CustomImgDialogExample({}),
    autoCancel: true,
    alignment: DialogAlignment.Center,
    customStyle: false,
    cornerRadius:0,
    width: 300,
    height: 300,
    backgroundColor: Color.White,
    maskColor: '#ff050505'
  });

  // 在自定义组件即将析构销毁时将dialogController置空
  aboutToDisappear() {
    this.dialogController = null; // 将dialogController置空
  }

  build() {
    Column() {
      Image($r('app.media.startIcon'))
        .width(40)
        .height(40)
        .onClick(() => {
          if (this.dialogController != null) {
            this.dialogController.open();
          }
        })
    }
    .backgroundColor(Color.Pink)
    .height('100%')
    .width('100%')
  }
}

@CustomDialog
struct CustomImgDialogExample {
  controller?: CustomDialogController;
  build() {
    Column() {
      Image($r('app.media.startIcon'))
        .height('100%')
        .width('100%')
    }
    .height('100%')
    .width('100%')
    .alignItems(HorizontalAlign.Center)
    .justifyContent(FlexAlign.Center)
  }
}
```
