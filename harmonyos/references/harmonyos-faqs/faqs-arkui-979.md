---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-979
title: 如何实现输入框实时改变二维码并支持截图展示
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何实现输入框实时改变二维码并支持截图展示
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:05+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:e07902e03a93a4a6f901d6fc983110e5a8688fa18555784589621e23e9e9208c
---

## 问题现象

期望实现根据输入框内容，实时生成二维码，并且支持点击按钮进行截图展示。

## 背景知识

* [二维码生成](../design-guides/qrcode-0000001929816020.md)：将链接或文案转换生成为二维码的样式来展示。
* [双向绑定](../atomic-ascf/logical-layer-event-bidirectional-binding.md)：支持将用户输入实时同步给service层对应的字段值。状态管理V2可以使用[!!语法](../harmonyos-guides/arkts-new-binding.md)完成双向绑定。
* [组件截图](../harmonyos-guides/arkts-uicontext-component-snapshot.md)：将应用内一个组件节点树的渲染结果生成位图（[PixelMap](../harmonyos-references/arkts-apis-image-pixelmap.md)）的能力。

## 解决方案

* 实现思路：
  + 通过componentSnapshot.getSync()方法截取二维码组件图像。

    ```ts
    Button("点击生成截图")
      .onClick(() => {
        try {
          this.hideInputMethod();
          let pixelmap = componentSnapshot.getSync("qr_id", { scale: 0.5, waitUntilRenderFinished: true });
          this.pixmap = pixelmap;
        } catch (error) {
          console.error("getSync errorCode: " + error.code + " message: " + error.message);
        }
      }).margin(10);
    ```
  + 通过TextArea实现文本输入，并使用!!语法实现文本输入的实时双向绑定。
  + 通过QRCode组件实现二维码生成。

    ```ts
    TextArea({ text: this.normalQrTxt!! }).fontSize(9).width("50%").fontSize(15).height(140);
    QRCode(this.normalQrTxt).width(140).height(140);
    ```
* 完整代码如下：

  ```screen
  import { componentSnapshot } from "@kit.ArkUI";
  import { image } from "@kit.ImageKit";
  import { inputMethod } from "@kit.IMEKit";

  @Entry
  @ComponentV2
  struct Index {
    @Local pixmap: image.PixelMap | undefined = undefined;
    @Local normalQrTxt: string = "普通二维码文案";

    build() {
      Column() {
        Row() {
          Image(this.pixmap)
            .width("50%")
            .border({ color: Color.Black, width: 2 })
            .height(140)
            .objectFit(ImageFit.Contain);
        };

        Button("点击生成截图")
          .onClick(() => {
            try {
              this.hideInputMethod();
              let pixelmap = componentSnapshot.getSync("qr_id", { scale: 0.5, waitUntilRenderFinished: true });
              this.pixmap = pixelmap;
            } catch (error) {
              console.error("getSync errorCode: " + error.code + " message: " + error.message);
            }
          }).margin(10);

        Button("点击清空截图")
          .onClick(() => {
            this.hideInputMethod();
            this.pixmap = image.createPixelMapSync({ size: { width: 100, height: 100 } });
          });

        Column({ space: 25 }) {
          Row({ space: 15 }) {
            TextArea({ text: this.normalQrTxt!! }).fontSize(9).width("50%").fontSize(15).height(140);
            QRCode(this.normalQrTxt).width(140).height(140);
          };
        }.width("100%").margin({ top: 25 }).id("qr_id");
      }
      .onClick(() => {
        this.hideInputMethod();
      })
      .width("100%")
      .height("70%")
      .justifyContent(FlexAlign.Center)
      .alignItems(HorizontalAlign.Center);
    }

    private hideInputMethod() {
      try {
        inputMethod.getController().hideTextInput().catch(() => {
          console.error("hideTextInput occur error");
        });
      } catch (error) {
        console.error("get inputMethod controller occur error");
      }
    }
  }
  ```
