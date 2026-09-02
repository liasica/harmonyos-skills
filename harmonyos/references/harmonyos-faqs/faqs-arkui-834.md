---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-834
title: 点击图片，图片异常上下跳动
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 点击图片，图片异常上下跳动
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:15+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:d8efa583fe85c73385a38c561aa1d8c30db25db092d4e20e2217f5b07d1cc48f
---

## 问题现象

点击图片，图片放大跳动并显示弹窗，关闭弹窗时图片缩小跳动，放大缩小时无动画，显示异常。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/99/v3/jkBT23PcRA-_zhMiO4PbAQ/zh-cn_image_0000002628558358.png "点击放大")

## 背景知识

* [Image](../harmonyos-references/ts-basic-components-image.md)为图片组件，常用于在应用中显示图片。
* [scaleY](../harmonyos-references/js-components-common-animation.md)：Y轴方向缩放动画属性。
* [animateTo](../harmonyos-references/arkts-apis-uicontext-uicontext.md#animateto)：提供animateTo接口来指定由于闭包代码导致的状态变化插入过渡动效。

## 问题定位

1. 使用DevEco Testing查看问题组件，该组件为Image组件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/3CZeEVe2Tc2KyOGgIWYp1w/zh-cn_image_0000002658917669.png "点击放大")
2. 查看该Image组件的设置，该组件设置点击显示弹窗和关闭弹窗时改变图片组件的尺寸，且未对尺寸变化通过animateTo设置动画，而是直接改变尺寸。

   ```screen
   @Entry
   @Component
   struct AlertDialogExample {
     @State scaleX: number = 1;
     @State scaleY: number = 1;

     build() {
       Column({ space: 50 }) {
         Image($r('app.media.box'))
           .width(120)
           .height(120)
           .scale({ x: this.scaleX, y: this.scaleY }) // 图片缩放
           .onClick(() => {
             // 直接缩放
             this.scaleX = 1.5;
             this.scaleY = 1.5;
             this.getUIContext().showAlertDialog(
               {
                 message: "已开奖",
                 autoCancel: true,
                 alignment: DialogAlignment.Center,
                 primaryButton: {
                   value: "确认",
                   action: () => {
                     // 直接缩放
                     this.scaleY = 1;
                     this.scaleX = 1;
                   }
                 },
                 cornerRadius: 12, // 弹窗边框弧度
                 width: '80%' // 弹窗宽度
               }
             );
           })
           .margin({ top: 200 });
         Row() {
           Text('点击图片显示弹窗')
             .fontWeight(FontWeight.Bold)
             .fontSize(30)
             .margin({ top: 50 });
         };
       }
       .width('100%')
       .height('100%');
     }
   }
   ```

## 分析结论

Image组件未对尺寸变化通过animateTo设置动画，而是直接改变尺寸，导致图片异常上下跳动。

## 修改建议

打开和关闭弹窗时使用animateTo改变图片组件的尺寸。

```screen
@Entry
@Component
struct AlertDialogExample {
  @State scaleX: number = 1;
  @State scaleY: number = 1;

  build() {
    Column({ space: 50 }) {
      Image($r('app.media.box')) // $r('app.media.box')需要替换为开发者需要的图片资源文件
        .width(120)
        .height(120)
        .scale({ x: this.scaleX, y: this.scaleY }) // 图片缩放
        .onClick(() => {
          // 使用animateTo动画平滑缩放
          this.getUIContext()?.animateTo({
            duration: 500,
            curve: Curve.EaseOut,
            playMode: PlayMode.Normal,
            onFinish: () => {
              this.getUIContext().showAlertDialog(
                {
                  message: "已开奖",
                  autoCancel: true,
                  alignment: DialogAlignment.Center,
                  primaryButton: {
                    value: "确认",
                    fontColor: '#0A59F7',
                    action: () => {
                      // animateTo确保动画同步
                      this.getUIContext()?.animateTo({
                        duration: 500,
                        curve: Curve.EaseOut,
                        playMode: PlayMode.Normal
                      }, () => {
                        this.scaleY = 1;
                        this.scaleX = 1;
                      });
                    }
                  },
                  cornerRadius: 12, // 弹窗边框弧度
                  width: '80%' // 弹窗宽度
                }
              );
            }
          }, () => {
            this.scaleX = 1.5;
            this.scaleY = 1.5;
          });
        })
        .margin({ top: 200 });
      Row() {
        Text('点击图片显示弹窗')
          .fontWeight(FontWeight.Bold)
          .fontSize(30)
          .margin({ top: 50 });
      };
    }
    .width('100%')
    .height('100%');
  }
}
```
