---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1299
title: screenshot.capture截图获取的图片无法展示
breadcrumb: FAQ > 应用框架开发 > UI框架 > 屏幕管理 > screenshot.capture截图获取的图片无法展示
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:13+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:1547e98529f325f9dab7cbccbf09a7891574723d873f87d1a597a446ce972ddd
---

## 问题现象

使用[screenshot.capture官方文档](../harmonyos-references/js-apis-screenshot.md#screenshotcapture14)中提供的示例代码进行截图，获取的PixelMap在Image组件上无法正常显示。

问题代码示例参考如下：

```ts
@Component
struct PixelMapToAlbumComponent {
  @State showPixelMap: image.PixelMap | undefined = undefined;

  build() {
    Column() {
      Image(this.showPixelMap).width(200).height(200).border({ color: Color.Black, width: 2 }).margin(5)
      Button('screenshot.capture').onClick(async () => {
        try {
          let captureOption: screenshot.CaptureOption = {
            "displayId": 0
          };
          let promise = screenshot.capture(captureOption);
          promise.then((pixelMap: image.PixelMap) => {
            getPixelBytesNumber();
            this.showPixelMap = pixelMap;
            pixelMap.release(); // PixelMap使用完后及时释放内存
          }).catch((err: BusinessError) => {
            console.error(`Failed to save screenshot. Code: ${err.code}`);
          });
        } catch (exception) {
          const err: BusinessError = exception as BusinessError;
          console.error(`Failed to save screenshot. Code: ${err.code}`);
        }
      })
    }
    .width('100%')
    .height('100%')
    .alignItems(HorizontalAlign.Center)
  }
}
```

运行日志示例参考如下：

```txt
04-02 11:31:26.826   42438-42438   C04200/com.exa...erCommonLayer  com.examp...stmodule  I     (294)Resolve: screen shot default.
04-02 11:31:26.826   42438-42438   C04200/com.exa...erCommonLayer  com.examp...stmodule  I     (297)Resolve: screen shot ret=0.
04-02 11:31:26.826   42438-42438   C04200/com.exa...erCommonLayer  com.examp...stmodule  I     [nodict]Resolve:311 Screenshot image Width 1600, Height 2560
04-02 11:31:26.827   42438-42438   C04200/com.exa...erCommonLayer  com.examp...stmodule  I     [nodict]ProcessPromise:110 AsyncProcess: Promise
04-02 11:31:26.827   42438-42438   C04200/com.exa...erCommonLayer  com.examp...stmodule  I     [nodict]ProcessPromise:112 AsyncProcess: Promise resolve
04-02 11:31:26.827   42438-42438   A03D00/com.exa...tmodule/JSAPP  com.examp...stmodule  I     Succeeded in saving screenshot. Pixel bytes number: 16384000
04-02 11:31:26.835   42438-42438   C0391F/com.exa...dule/AceImage  com.examp...stmodule  W     [(100000:100000:scope)] pixmap pointer is nullptr when CreatePixelMap.
04-02 11:31:26.853   42438-42599   C01406/com.exa...dule/OHOS::RS  com.examp...stmodule  I     RSUIDirector::ProcessMessages messageId:12, cmdCount:1, instanceId:100000
```

## 背景知识

* [screenshot.capture](../harmonyos-references/js-apis-screenshot.md#screenshotcapture14)：获取屏幕全屏截图，此接口仅支持在平板和2in1设备上使用，会返回一个PixelMap对象。
* [PixelMap](../harmonyos-references/arkts-apis-image-pixelmap.md)：图像像素类，用于读取或写入图像数据以及获取图像信息。
* [Image](../harmonyos-references/ts-basic-components-image.md)：图片组件，支持加载PixelMap类型的数据源。

## 问题定位

1. 排查screenshot.capture是否正确调用，并返回PixelMap类型Promise对象：由日志Succeeded in saving screenshot. Pixel bytes number: 16384000可以推断，Promise的then回调方法已完成调用且返回了PixelMap。
2. 排查Image中不显示相应PixelMap图片的原因：根据日志pixmap pointer is nullptr when CreatePixelMap排查到Image当前引用的PixelMap指向为空。
3. 根据日志排查代码：调用screenshot.capture方法，获取到相应PixelMap并赋值给Image组件绑定的全局变量后（this.showPixelMap = pixelMap），立即调用了pixelMap.release()方法，PixelMap对象已被释放。

## 分析结论

screenshot.capture获取的PixelMap在赋值给全局变量showPixelMap后立即调用[release()](../harmonyos-references/arkts-apis-image-pixelmap.md#release7)方法，导致showPixelMap指向的PixelMap已经被释放，无法在Image组件中显示。

## 修改建议

在screenshot.capture获取到PixelMap并赋值给全局变量showPixelMap后，不要调用pixelMap.release()方法，Image组件便可正常展示PixelMap图片。
