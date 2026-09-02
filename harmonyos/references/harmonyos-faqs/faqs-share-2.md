---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-share-2
title: 分享图片到应用显示“您选择的文件不支持分享”
breadcrumb: FAQ > 应用服务开发 > 内容分享服务（Share Kit） > 分享图片到应用显示“您选择的文件不支持分享”
category: harmonyos-faqs
scraped_at: 2026-09-02T15:04:26+08:00
doc_updated_at: 2026-08-12
content_hash: sha256:aa3eb1664d71a2510d512691187178ac2ece2a7e065944569666946c173dfa9d
---

## 问题现象

调用分享弹出应用选择，选择任一应用均提示“您选择的文件不支持分享”，请问是什么原因？

问题效果预览：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/kgnC2jH0QMCSmJgnL5wp4Q/zh-cn_image_0000002658913741.png "点击放大")

## 背景知识

* [Share Kit](../harmonyos-guides/share-introduction.md)：为应用提供文本、图片、视频等内容跨应用、跨端分享能力。
* [systemShare](../harmonyos-references/share-system-share.md)：提供分享数据创建及分享面板拉起的功能，提供多种系统标准分享服务，例如分享数据给其他应用、复制、打印等。
* [SharedRecord](../harmonyos-references/share-system-share.md#sharedrecord)：用于构造一条分享数据记录。包含数据类型、数据内容及描述等信息。

## 问题定位

构造分享数据，添加一条分享记录。

```ts
let uiContext: UIContext = this.getUIContext();
let context: common.UIAbilityContext = uiContext.getHostContext() as common.UIAbilityContext;
let thumbnail = await context.resourceManager.getRawFileContent('picture.png');
// 构造ShareData，需配置一条有效数据信息
let shareData: systemShare.SharedData = new systemShare.SharedData({
  utd: utd.UniformDataType.HYPERLINK,
  uri: 'xxx',
  title: '测试',
  thumbnail: thumbnail
});
```

此分享数据无法分享到应用，复现问题，复现场景。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/lNyPWQ2BSNaTjKrhn2ntqQ/zh-cn_image_0000002658793793.png "点击放大")

再将SharedData中参数uri换成content。

```ts
let uiContext: UIContext = this.getUIContext();
let context: common.UIAbilityContext = uiContext.getHostContext() as common.UIAbilityContext;
let thumbnail = await context.resourceManager.getRawFileContent('picture.png');
// 构造ShareData，需配置一条有效数据信息
let shareData: systemShare.SharedData = new systemShare.SharedData({
  utd: utd.UniformDataType.HYPERLINK,
  content: 'xxx',
  title: '测试',
  thumbnail: thumbnail
});
```

此时选择任一应用可以进行分享（此示例选择备忘录），分享成功如图。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/lnGyZSC1SSKadf3K97DiLQ/zh-cn_image_0000002628394526.png "点击放大")

## 分析结论

* SharedRecord中参数uri为数据记录的uri。支持的uri类型：
  + 应用文件uri，参见：[应用文件分享](../harmonyos-guides/share-app-file.md)。
  + 用户文件uri，参见：[用户文件uri介绍](../harmonyos-guides/user-file-uri-intro.md#媒体文件uri介绍)。
* SharedRecord中参数content为数据记录内容，链接（包含App Linking）、文本类型的内容通过该字段传递。
* 如果SharedRecord中路径参数想设置为uri，那么路径需要为固定格式：“file://<bundleName>/<path>”，否则会显示“您选择的文件不支持分享”。实际路径为https的超链接格式，那么路径参数应该设置为content，此时分享才不会显示异常。

**说明** 

content和uri二者至少有一个不为空。

## 修改建议

如果是链接（包含App Linking）、文本类型的内容，SharedRecord中参数可设置为content。

```ts
import { systemShare } from '@kit.ShareKit';
import { uniformTypeDescriptor as utd } from '@kit.ArkData';
import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct SharePage {
  private async share() {
    let uiContext: UIContext = this.getUIContext();
    let context: common.UIAbilityContext = uiContext.getHostContext() as common.UIAbilityContext;
    let thumbail = await context.resourceManager.getRawFileContent('img.png');
    // 构造ShareData，需配置一条有效数据信息
    let shareData: systemShare.SharedData = new systemShare.SharedData({
      utd: utd.UniformDataType.HYPERLINK,
      // 实际内容根据开发者自行配置
      content: 'xxx.xxx.com',
      title: '测试',
      thumbnail: thumbail
    });

    let controller: systemShare.ShareController = new systemShare.ShareController(shareData);
    controller.show(context, {
      selectionMode: systemShare.SelectionMode.SINGLE,
      previewMode: systemShare.SharePreviewMode.DETAIL,
    }).then(() => {
      console.info('ShareController show success.');
    }).catch((error: BusinessError) => {
      console.error(`ShareController show error. code: ${error.code}, message: ${error.message}`);
    });
  }

  build() {
    Row() {
      Text('分享')
      Button('分享')
        .onClick(() => {
          this.share();
        })
    }
    .width('100%')
    .margin({ top: 12 })
    .padding({ left: 20, right: 20 })
    .justifyContent(FlexAlign.SpaceBetween)
  }
}
```

## 常见FAQ

Q：系统分享是否支持分享在线图片？

A：系统分享不支持分享在线图片，可以先将在线图片保存到本地后再分享。

Q：缩略图thumbnail有什么限制，为什么设置无效？

A：[thumbnail](../harmonyos-references/share-system-share.md#sharedrecord)限制图片大小：32KB以下。过大的图片可能导致want数据超限无法拉起分享，可使用[ImagePacker.packing](../harmonyos-references/arkts-apis-image-imagepacker.md#packing13)压缩图片质量。另外，当前规格2in1设备不支持缩略图。

Q：使用systemShare.getSharedData(want)获取分享的数据，报错1003703001，如何解决？

A：数据记录数量超过限制，可以不通过getSharedData接口获取分享数据，直接从want.uri属性，即分享的链接中，解析出分享的数据。

Q：API17的SDK版本下，在App中添加隔空抓取分享的功能，按照[隔空传送API文档](../harmonyos-guides/gestures-share.md)进行开发提示报错：Argument of type '"gesturesShare"' is not assignable to parameter of type '"knockShare"。这是什么原因？

A：隔空传送能力为HarmonyOS6.0版本[新增特性](../harmonyos-releases/os-new-feature-600.md#section1911561445211)，三方应用接入该能力需升级至HarmonyOS6.0版本。

Q：content和uri已确认完成配置，仍然提示文件不支持分享，还有可能是什么原因？

A：确认分享文件存在，请排查分享文件的路径或者权限。
