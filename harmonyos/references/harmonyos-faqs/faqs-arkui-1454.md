---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1454
title: CustomDialog设置透明背景
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > CustomDialog设置透明背景
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:22+08:00
doc_updated_at: 2026-07-31
content_hash: sha256:f6719618b89555d1c305a4b01c8126d26ea0beff05a76284f71ab9fb8ec62b5e
---

## 问题现象

如何将自定义弹窗的背景设置为透明？

预览效果：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/pp0qFLilT7yFkH1qfAlXGg/zh-cn_image_0000002654196478.png "点击放大")

## 背景知识

自定义弹窗组件[CustomDialog](../harmonyos-references/ts-methods-custom-dialog-box.md)类能够显示弹窗，并且可以自定义弹窗的样式与内容，允许用户灵活地设置弹窗的样式，布局和交互行为。

## 解决方案

CustomDialog设置透明背景的解决方案如下：

* 方案一：将CustomDialog的backgroundColor设置为Color.Transparent，同时将backgroundBlurStyle设置为BlurStyle.NONE（若此项不设置则自定义弹窗的背景色为白色），两种属性配合使用实现透明背景效果。

  ```ts
  @CustomDialog
  struct CustomDialogContent {
    controller: CustomDialogController;

    build() {
      Column() {
        Button('关闭').onClick(() => {
          this.controller.close();
        })
          .backgroundColor('#0a59f7');
      }
      .justifyContent(FlexAlign.Center)
      .height('100%')
      .width('100%');
    }
  }

  @Entry
  @Component
  struct Index {
    dialogController: CustomDialogController = new CustomDialogController({
      builder: CustomDialogContent(),
      // 设置弹窗背景色为透明
      backgroundColor: Color.Transparent,
      backgroundBlurStyle: BlurStyle.NONE
    });

    build() {
      Row() {
        Button('弹窗').onClick(() => {
          this.dialogController.open();
        })
          .backgroundColor('#0a59f7')
          .margin({ top: 100 });
      }
      .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM])
      .alignItems(VerticalAlign.Center)
      .justifyContent(FlexAlign.Center)
      .height('100%')
      .width('100%')
      .backgroundColor(0xF1F3F5);
    }
  }
  ```
* 方案二：通过将CustomDialog的属性customStyle设置为true，就可以将弹窗容器样式的可自定义性关闭，此时的弹窗圆角为0，背景色为透明色，示例代码如下：

  ```ts
  @CustomDialog
  struct CustomDialogContent1 {
    controller: CustomDialogController;

    build() {
      Column() {
        Button('关闭').onClick(() => {
          this.controller.close();
        })
          .backgroundColor('#0a59f7');
      };
    }
  }

  @Entry
  @Component
  struct Index1 {
    dialogController: CustomDialogController = new CustomDialogController({
      builder: CustomDialogContent1(),
      customStyle: true, // 设置弹窗背景色为透明
    });

    build() {
      Row() {
        Button('弹窗').onClick(() => {
          this.dialogController.open();
        })
          .backgroundColor('#0a59f7') // 按钮颜色
          .margin({ top: 100 });
      }
      .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM])
      .alignItems(VerticalAlign.Center)
      .justifyContent(FlexAlign.Center)
      .height('100%')
      .width('100%')
      .backgroundColor(0xF1F3F5); // 主页面背景色
    }
  }
  ```
* 方案三：在方案二的基础上，通过将isModal设置为false，将弹窗设置为非模态弹窗，而非模态窗口无蒙层，即可实现完全透明弹窗。示例代码如下：

  ```ts
  @CustomDialog
  struct CustomDialogContent2 {
    controller: CustomDialogController;

    build() {
      Column() {
        Button('关闭').onClick(() => {
          this.controller.close();
        })
          .backgroundColor('#0a59f7');
      };
    }
  }

  @Entry
  @Component
  struct Index2 {
    dialogController: CustomDialogController = new CustomDialogController({
      builder: CustomDialogContent2(),
      customStyle: true, // 设置弹窗背景色为透明
      isModal: false
    });

    build() {
      Row() {
        Button('弹窗').onClick(() => {
          this.dialogController.open();
        })
          .backgroundColor('#0a59f7')
          .margin({ top: 100 });
      }
      .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM])
      .alignItems(VerticalAlign.Center)
      .justifyContent(FlexAlign.Center)
      .height('100%')
      .width('100%')
      .backgroundColor(0xF1F3F5);
    }
  }
  ```

## 常见FAQ

Q：如何修改自定义弹窗的背景色？同时怎么设定弹窗不点击遮罩就能消除？

A：可以使用自定义弹窗[CustomDialogControllerOptions对象说明](../harmonyos-references/ts-methods-custom-dialog-box.md#customdialogcontrolleroptions对象说明)下的蒙层颜色属性maskColor修改弹窗背景色，是否允许点击遮障层退出属性autoCancel设定弹窗不点击遮罩就能消除。

Q：为什么使用maskColor:"0xB0000000"设置maskColor无效？

A：该写法不符合规范，因此失效，可通过maskColor:0xB0000000或maskColor:'#B0000000'这样的规范写法设置maskColor。

Q：为maskColor设置resource类型不生效。

A：maskColor当前只支持字符串颜色值，不支持$r()资源引用。

Q：CustomDialog设置透明背景失效的可能原因有哪些？

A：设置透明背景失效的可能原因如下：1.customStyle未设置为true（即未开启自定义样式）；2.maskColor（自定义蒙层颜色）、backgroundColor（弹窗背板填充颜色）未设置透明；3.自定义弹窗内容构造器builder内容器背景未设置透明。相关属性配置可参考[CustomDialogControllerOptions对象说明](../harmonyos-references/ts-methods-custom-dialog-box.md#customdialogcontrolleroptions对象说明)。

## 总结

方案一、二、三都是通过自定义[CustomDialogController](../harmonyos-references/ts-methods-custom-dialog-box.md#customdialogcontroller)类方法实现透明背景，但实现方法略有不同，因此应用场景也不同，常见场景如下表格：

| 方案 | 特点 | 适用场景 |
| --- | --- | --- |
| 方案一 | 弹窗背板填充和模糊材质固定 | 消息提示、操作确认、图片预览 |
| 方案二 | 不能自定义弹窗容器样式 | 系统消息提示、应用权限请求、软件错误提示 |
| 方案三 | 背景完全透明 | 悬浮窗效果、评论弹窗 |
