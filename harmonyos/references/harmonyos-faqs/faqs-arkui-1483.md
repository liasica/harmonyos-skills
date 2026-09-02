---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1483
title: 如何解决CustomDialog内嵌套Navigation导致弹窗无法底部对齐的问题
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何解决CustomDialog内嵌套Navigation导致弹窗无法底部对齐的问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:27+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:02e9e20379a304cb6c31c8f61011fc271e068b8356bb68a7d5045e256c68cac9
---

## 问题现象

当CustomDialog内部嵌套Navigation容器时，弹窗设置底部显示alignment: DialogAlignment.Bottom时失效，问题代码如下：

```ts
@CustomDialog
export struct MyDialog {
  controller: CustomDialogController;

  build() {
    Navigation() {
      Column() {
        Text('我是弹窗')
          .margin({ top: 20 });
      }
      .width('100%')
      .height(200)
      .backgroundColor(Color.White);
    };
  }
}

@Entry
@Component
struct Dialog {
  myDiaController: CustomDialogController = new CustomDialogController({
    builder: MyDialog({}),
    customStyle: true, // 弹窗容器样式是否自定义
    autoCancel: false, // 是否允许点击遮障层退出
    alignment: DialogAlignment.Bottom, // 弹窗在竖直方向上的对齐，底部对齐失效
  });

  onPageShow(): void {
    this.myDiaController.open();
  }

  build() {
  }
}
```

问题现象如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/YRrTLS4DS5-d91dlPxK3Ig/zh-cn_image_0000002658845073.png "点击放大")

## 背景知识

[CustomDialog](../harmonyos-references/ts-methods-custom-dialog-box.md)：是一种常见的自定义弹窗方式，当其内部嵌套[Navigation](../harmonyos-references/ts-basic-components-navigation.md)容器时，Navigation容器在不设置高度的情况下会默认撑满屏幕，而Navigation内部默认至上而下显示，所以导致弹窗的底部显示命令在显示效果上没有生效。

## 解决方案

* 由于Navigation在不设置高度时，默认撑满整个手机屏幕，导致嵌套Navigation的弹窗也是全屏显示，从而导致DialogAlignment.Bottom从体验上未生效。实际逻辑是弹窗已经是全屏显示，弹窗底部对齐后依旧是全屏显示。
* 为Navigation容器设置高度限制（本示例设置300vp），并设置背景颜色为蓝色后，可以发现弹窗为底部对齐效果：

  ```ts
  @CustomDialog
  export struct MyDialog {
    controller: CustomDialogController;
    pathStack: NavPathStack = new NavPathStack();

    build() {
      // 弹窗内使用Navigation可实现弹窗内路由跳转，从而更换弹窗内显示的页面
      Navigation(this.pathStack) {
        Column() {
          Text('我是弹窗')
            .margin({ top: 20 });
        }
        .width('100%')
        .height(200)
        .backgroundColor(Color.White);
      }
      .height(300)
      .backgroundColor('#0a59f7');
    }
  }

  @Entry
  @Component
  struct DialogDemo {
    myDialogController: CustomDialogController = new CustomDialogController({
      builder: MyDialog({}),
      customStyle: true, // 弹窗容器样式是否自定义
      autoCancel: false, // 是否允许点击遮障层退出
      alignment: DialogAlignment.Bottom, // 弹窗在竖直方向上的对齐，底部对齐失效
    });

    onPageShow(): void {
      this.myDialogController.open();
    }

    build() {
    }
  }
  ```

实现效果如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/ILKGvnkxR1mSVz1AUFN56Q/zh-cn_image_0000002628765700.png "点击放大")

上图中弹窗为白色与蓝色部分（其中白色是弹窗中子组件背景色，蓝色是弹窗背景色），弹窗底部对齐。

## 总结

多数情况下，父容器的大小在未设置尺寸限制的情况下默认自适应子组件大小，所以，该思维惯性会陷入一个误区：默认Navigation容器未设置尺寸时会自适应其子组件Column的高度200vp，从而默认弹窗高度是200vp、底部对齐命令未生效。而实际上，部分容器在未设置尺寸限制时会默认全屏显示，例如Navigation、Tabs等。
