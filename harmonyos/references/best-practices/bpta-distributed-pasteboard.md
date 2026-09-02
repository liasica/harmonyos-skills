---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-distributed-pasteboard
title: 跨设备剪贴板常见场景
breadcrumb: 最佳实践 > 自由流转 > 多端协同 > 跨设备剪贴板常见场景
category: best-practices
scraped_at: 2026-09-02T15:13:22+08:00
doc_updated_at: 2026-08-26
content_hash: sha256:61bdf26a188a3e7ee116855d11d7d5fcce89dea544658514a720fc24e348f9b2
---

## 概述

剪贴板分为本地剪贴板和跨设备剪贴板，本地剪贴板提供设备内的内容复制粘贴，跨设备剪贴板提供跨设备的内容复制粘贴。跨设备剪贴板通过全场景协同能力同步剪贴板内容，实现手机、PC/2in1、平板等设备间的无缝数据互通。

当用户拥有多台设备时，可以通过跨设备剪贴板的功能，在A设备的应用上复制一段内容，粘贴到B设备的应用中，高效地完成多设备间的内容共享，其核心价值在于提升多设备协作效率。

## 实现原理

**场景分析**

1. 用户在设备A复制数据，写入到系统剪贴板服务。

2. 系统剪贴板服务将处理相关数据，并完成数据同步，此过程开发者不感知。

3. 用户在设备B读取系统剪贴板内容，粘贴来自设备A的数据。

详细的使用限制可参考跨设备剪贴板[约束与限制](bpta-distributed-pasteboard-cast.md#section42331744172619)。

**关键技术**

在开发跨设备剪贴板的功能时，系统将自动完成跨设备的数据传递，应用可根据实际需求，接入跨设备剪贴板，完成跨设备剪贴板的开发，具体运作机制可参考：跨设备剪贴板[运作机制](bpta-distributed-pasteboard-cast.md#section111721843182510)。

## 开发流程

跨设备剪贴板的开发流程主要包括以下两个步骤：

1. 设备A复制数据，写入剪贴板服务：将需要存入系统剪贴板的数据转换为系统剪贴板可接受的通用格式，调用SystemPasteboard.[setData()](../harmonyos-references/js-apis-pasteboard.md#setdata9)方法，将数据写入系统剪贴板。
2. 设备B粘贴数据，读取剪贴板内容：可以[使用粘贴控件](../harmonyos-guides/pastebutton.md)获得临时授权直接读取剪贴板数据。或申请系统剪贴板权限[ohos.permission.READ\_PASTEBOARD](../harmonyos-guides/restricted-permissions.md#ohospermissionread_pasteboard)后，使用[@ohos.pasteboard (剪贴板)](../harmonyos-references/js-apis-pasteboard.md#systempasteboard)接口读取剪贴板数据。具体开发步骤请参考[访问剪贴板内容](../harmonyos-guides/get-pastedata-permission-guidelines.md#访问剪贴板内容)。

下文将通过[分享直达](bpta-distributed-pasteboard.md#section1146419501282)场景、[多样式复制粘贴](bpta-distributed-pasteboard.md#section91711442235)场景、[进度条接入](bpta-distributed-pasteboard.md#section58295561239)场景，详细介绍跨设备剪贴板开发过程中常见场景的开发实现流程。

## 分享直达

用户在任意应用（如短信、浏览器等）中复制包含特定标识的文本（如活动口令、订单号或链接等），随后打开目标应用（如商城应用、服务应用），应用能自动识别复制文本中预设的关键字或编码。应用在校验关键字格式、时效性或用户权限通过后，弹窗或直接跳转至关联的活动页面、订单详情页或其他特定功能模块。例如用户复制短信中的活动链接，打开商城应用后自动跳转至促销活动页，无需手动搜索或点击多级菜单。

[视频](https://contentcenter-videovali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_300_3/4/v3/Wu9jlU2QRDmCA852v4Q7Zg/zh-cn_media_0000002429043485.mp4)

**构建****数据存入剪贴板**

使用createData()创建一个包含单URI类型的pasteData数据。使用[setData()](../harmonyos-references/js-apis-pasteboard.md#setdata9)方法将pasteData数据写入系统剪贴板。

```typescript
let pasteData: pasteboard.PasteData = pasteboard.createData(pasteboard.MIMETYPE_TEXT_URI, 'PageABuilder');
let systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
await systemPasteboard.setData(pasteData);
```

**读取剪贴板数据实现跳转**

由于应用读取系统剪贴板的权限[ohos.permission.READ\_PASTEBOARD](../harmonyos-guides/restricted-permissions.md#ohospermissionread_pasteboard)是受限访问的，因此需要先通过AGC平台申请此权限，才能获取系统剪贴板内的数据。具体申请权限的流程可参考[申请调试Profile文件和添加权限信息](../harmonyos-guides/ide-signing.md#section89479413571)。

首先，应用在启动时或从后台进入前台时，在[onPageShow()](../harmonyos-references/ts-custom-component-lifecycle.md#onpageshow)生命周期中检查系统剪贴板中是否包含URI类型数据。URI类型数据存在时检查权限ohos.permission.READ\_PASTEBOARD是否已授权。确认权限授权后，使用[getData()](../harmonyos-references/js-apis-pasteboard.md#getdata9)方法获取系统剪贴板内的数据，并使用[getPrimaryUri()](../harmonyos-references/js-apis-pasteboard.md#getprimaryuri7)方法获取单URI类型的数据。校验数据格式正确后，拉起弹窗询问用户是否需要执行跳转。

```typescript
onPageShow(): void {
  let systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
  try {
    let result: boolean = systemPasteboard.hasDataType(pasteboard.MIMETYPE_TEXT_URI);
    if (result) {
      this.checkPermissionGrant();
    }
  } catch (error) {
    const err: BusinessError = error as BusinessError;
    hilog.error(0x0000, '[Home]',
      `Check data type failed. Code is ${err.code}, message is ${err.message}`);
  }
}

checkPermissionGrant(): void {
  let hasPermission = false;
  let tokenId: number = 0;
  try {
    let bundleInfo: bundleManager.BundleInfo =
      bundleManager.getBundleInfoForSelfSync(bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_APPLICATION);
    let appInfo: bundleManager.ApplicationInfo = bundleInfo.appInfo;
    tokenId = appInfo.accessTokenId;
  } catch (error) {
    const err: BusinessError = error as BusinessError;
    hilog.error(0x0000, '[Home]',
      `Failed to get bundle info for self. Code is ${err.code}, message is ${err.message}`);
  }

  try {
    let atManager = abilityAccessCtrl.createAtManager();
    let approximatelyLocation = atManager.checkAccessTokenSync(tokenId, 'ohos.permission.READ_PASTEBOARD');
    hasPermission = approximatelyLocation === abilityAccessCtrl.GrantStatus.PERMISSION_GRANTED;
  } catch (error) {
    const err: BusinessError = error as BusinessError;
    hilog.error(0x0000, '[Home]', `Failed to check access token. Code is ${err.code}, message is ${err.message}`);
  }
  if (hasPermission) {
    let systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
    systemPasteboard.getData().then((pasteData: pasteboard.PasteData) => {
      this.uri = pasteData.getPrimaryUri();
      if (this.uri === 'PageABuilder' || this.uri === 'PageBBuilder') {
        this.dialogControllerImage.open();
      }
    }).catch((err: BusinessError) => {
      hilog.error(0x0000, '[Home]', 'Failed to get PasteData. Cause: ' + err.message);
    })
  } else {
    hilog.error(0x0000, '[Home]', 'The app is not authorized.');
    this.requestPermissionsFn();
  }
}
```

## 多样式复制粘贴

随着富文本数据接入不同设备，为了使复制的数据能够被更多的设备B识别，设备A需要将同一份数据的多种样式存入剪贴板中。如设备A图文混排的富文本数据可以按[纯文本类型（'text/plain'）](../harmonyos-references/js-apis-pasteboard.md#常量)、包含文字样式及图片的[HTML类型（'text/html'）](../harmonyos-references/js-apis-pasteboard.md#常量)、[纯图片类型（'pixelMap'）](../harmonyos-references/js-apis-pasteboard.md#常量)等多种类型存入剪贴板。设备B选择需要的类型读取对应类型的数据，然后实现粘贴操作。剪贴板支持的数据类型请参考[@ohos.pasteboard (剪贴板)](../harmonyos-references/js-apis-pasteboard.md#常量)。

[视频](https://contentcenter-videovali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_300_3/8f/v3/oOvDY6d-SF6m2eL263QshA/zh-cn_media_0000002429163385.mp4)

**构建数据存入剪贴板**

创建[PasteData](../harmonyos-references/js-apis-pasteboard.md#pastedata)类型对象pasteData，通过PasteData.[getRecord()](../harmonyos-references/js-apis-pasteboard.md#getrecord9)方法获取数据条目[PasteDataRecord](../harmonyos-references/js-apis-pasteboard.md#pastedatarecord7)。本示例中使用[RichEditor](../harmonyos-references/ts-basic-components-richeditor.md)组件实现富文本数据的初始化，开发者可以选择其他富文本实现方案读取粘贴富文本数据。使用初始化RichEditor组件[RichEditorStyledStringController](../harmonyos-references/ts-basic-components-richeditor.md#richeditorstyledstringcontroller12)控制器的[getStyledString()](../harmonyos-references/ts-basic-components-richeditor.md#getstyledstring12)方法获取富文本框内的数据。根据需要的数据类型，使用PasteDataRecord.[addEntry()](../harmonyos-references/js-apis-pasteboard.md#addentry14)方法向条目中添加多种类型的数据。最后，调用[setData()](../harmonyos-references/js-apis-pasteboard.md#setdata9)方法将包含多样式数据的对象pasteData存入系统剪贴板。需要注意，PasteDataRecord 仅支持单个PixelMap数据传输，如需传输多个PixelMap，需要向PasteData中存入多个PasteDataRecord分别保存PixelMap。

```typescript
let pasteData: pasteboard.PasteData = pasteboard.createData(pasteboard.MIMETYPE_TEXT_PLAIN, '');
let record: pasteboard.PasteDataRecord = pasteData.getRecord(0);

let styledString: StyledString = this.editController.getStyledString();
let html: string = StyledString.toHtml(styledString);

record.addEntry(pasteboard.MIMETYPE_TEXT_HTML, html);
record.addEntry(pasteboard.MIMETYPE_TEXT_PLAIN, styledString.getString());
const htmlSpans = this.pastePixelMapController.fromStyledString(styledString);
if (!htmlSpans || htmlSpans.length < 1) {
  return;
}
for (let i = 0; i < htmlSpans.length; i++) {
  const span = htmlSpans[i];
  if (!!(span as RichEditorImageSpanResult)?.valuePixelMap) {
    const pixelMap = (span as RichEditorImageSpanResult)?.valuePixelMap;
    record.addEntry(pasteboard.MIMETYPE_PIXELMAP, pixelMap);
    break;
  }
}

let systemPasteBoard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
await systemPasteBoard.setData(pasteData).catch((err: BusinessError) => {
  hilog.error(0x0000, '[PasteBoard]',
    `Failed to set pastedata. Code: ${err.code}, message: ${err.message}`);
});
```

**实现多样式数据读取**

1. 数据写入系统剪贴板后，[使用粘贴控件](../harmonyos-guides/pastebutton.md)获得临时授权读取剪贴板数据。直接点击粘贴按钮，使用[getData()](../harmonyos-references/js-apis-pasteboard.md#getdata9)方法，即可直接读取系统剪贴板的内容。

   ```typescript
   PasteButton()
   // ...
     .onClick(async (_event: ClickEvent, result: PasteButtonOnClickResult) => {
       if (result === PasteButtonOnClickResult.SUCCESS) {
         try {
           // ...
           let systemPasteBoard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
           let gettedData = await systemPasteBoard.getData();
           // ...
         } catch {
           (err: BusinessError) => {
             hilog.error(0x0000, '[PasteBoard]', `getData error.code: ${err.code}, message: ${err.message}`);
           }
         }
       }
     })
   ```
2. 对于存储在系统剪贴板中的多样式数据，使用PasteDataRecord.[getValidTypes()](../harmonyos-references/js-apis-pasteboard.md#getvalidtypes14)方法获取剪贴板中数据类型与传入参数类型的交集的数据类型数组，交集结果表示请求的类型在剪贴板中存在。遍历数据类型数组，使用PasteDataRecord.[getData()](../harmonyos-references/js-apis-pasteboard.md#getdata14)方法获取对应类型的数据，通过不同RichEditor组件的控制器，实现不同类型数据的粘贴。请注意若剪贴板中不存在请求的数据类型，则对应类型的粘贴操作无法执行，对应RichEditor组件中内容不做更新。

   ```typescript
   PasteButton()
   // ...
     .onClick(async (_event: ClickEvent, result: PasteButtonOnClickResult) => {
       if (result === PasteButtonOnClickResult.SUCCESS) {
         try {
           // ...
           let systemPasteBoard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
           let gettedData = await systemPasteBoard.getData();
           if (gettedData.getRecordCount() <= 0) {
             return;
           }

           let isPastedSuccess: boolean = false;
           for (let i = 0; i < gettedData.getRecordCount(); i++) {
             let record = gettedData.getRecord(i);
             let targetTypes: string[] = [
               pasteboard.MIMETYPE_TEXT_HTML,
               pasteboard.MIMETYPE_TEXT_PLAIN,
               pasteboard.MIMETYPE_PIXELMAP
             ];
             let tmpTypes: string[] = record.getValidTypes(targetTypes);
             for (let j = 0; j < tmpTypes.length; j++) {
               switch (tmpTypes[j]) {
                 case pasteboard.MIMETYPE_TEXT_HTML: {
                   let htmlRecord = await record.getData(pasteboard.MIMETYPE_TEXT_HTML);
                   htmlRecord = htmlRecord as string;
                   this.handlerPasteHtmlData(htmlRecord);
                   isPastedSuccess = true;
                   break;
                 }
                 case pasteboard.MIMETYPE_TEXT_PLAIN: {
                   let textRecord = await record.getData(pasteboard.MIMETYPE_TEXT_PLAIN);
                   textRecord = textRecord as string;
                   let styledString = new StyledString(textRecord);
                   this.pasteTextController.setStyledString(styledString);
                   isPastedSuccess = true;
                   break;
                 }
                 case pasteboard.MIMETYPE_PIXELMAP: {
                   let pixelMapRecord = await record.getData(pasteboard.MIMETYPE_PIXELMAP);
                   pixelMapRecord = pixelMapRecord as PixelMap;
                   this.pastePixelMapController.deleteSpans();
                   this.pastePixelMapController.addImageSpan(pixelMapRecord, {
                     imageStyle: {
                       size: ['57px', '57px']
                     }
                   });
                   isPastedSuccess = true;
                   break;
                 }
                 default:
                   break;
               }
             }
           }
           // ...
         } catch {
           (err: BusinessError) => {
             hilog.error(0x0000, '[PasteBoard]', `getData error.code: ${err.code}, message: ${err.message}`);
           }
         }
       }
     })
   ```

## 进度条接入

允许文件粘贴时，通常需要使用进度条将抽象进程转化为可视化的动态变化，帮助用户快速了解当前进展。

[视频](https://contentcenter-videovali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_300_3/ce/v3/C6OJdINhQXy4ls--tkUpQw/zh-cn_media_0000002395443772.mp4)

**构建****数据存入剪贴板**

创建一个包含单样式的pasteData数据。创建一个文本文件存入剪贴板。

```screen
let filesDir = uiContext?.getHostContext()!.filesDir;
let fileFullName = filesDir + '/test1.txt';
hilog.info(0x0000, '[ProgressBar]', 'The fileFullName of str is:' + fileFullName);
let file = fileIo.openSync(fileFullName, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
let writeLen = fileIo.writeSync(file.fd, VALUE_TEST_STRING_ELEMENT);
hilog.info(0x0000, '[ProgressBar]', 'The size of str is: ' + writeLen);
fileIo.closeSync(file);
let pasteData =
  pasteboard.createData(pasteboard.MIMETYPE_TEXT_URI, fileUri.getUriFromPath(fileFullName));

let systemPasteBoard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
await systemPasteBoard.setData(pasteData).catch((err: BusinessError) => {
  hilog.error(0x0000, '[ProgressBar]',
    `Failed to set pastedata. Code: ${err.code}, message: ${err.message}`);
});
```

**获取剪贴板的内容和进度**

[使用粘贴控件](../harmonyos-guides/pastebutton.md)获取临时授权后，调用[getDataWithProgress()](../harmonyos-references/js-apis-pasteboard.md#getdatawithprogress15)方法获取剪贴板的内容及进度。params参数用于在应用使用剪贴板提供的文件拷贝功能时提供必要的信息，包括目标路径、文件冲突处理选项、进度条类型等。[ProgressListener](../harmonyos-references/js-apis-pasteboard.md#progresslistener15)是用于订阅进度数据变化的函数，可以当前获取数据的进度信息。进度数据状态变量更新后，刷新进度条Progress组件显示。

```screen
PasteButton()
// ...
  .onClick(async (event: ClickEvent, result: PasteButtonOnClickResult) => {
    if (result === PasteButtonOnClickResult.SUCCESS) {
      let systemPasteboard = pasteboard.getSystemPasteboard();
      let ProgressListener = (progress: pasteboard.ProgressInfo) => {
        this.progressInfo = progress.progress;
        hilog.info(0x0000, '[ProgressBar]', 'progressListener success, progress:' + progress.progress);
        // ...
      }
      let dstUri: string = fileUri.getUriFromPath(dstDir);
      hilog.info(0x0000, '[ProgressBar]', 'progressBar' + 'dstUri: ' + dstUri + ' length: ' + dstUri.length);
      let params: pasteboard.GetDataParams = {
        destUri: dstUri,
        progressIndicator: pasteboard.ProgressIndicator.NONE,
        progressListener: ProgressListener
      };
      try {
        await systemPasteboard.getDataWithProgress(params).then((data) => {
          hilog.info(0x0000, '[ProgressBar]', 'getDataWithProgress success');
          fileIo.unlink(dstUri);
        }).catch((error: BusinessError) => {
          hilog.error(0x0000, '[ProgressBar]', 'getDataWithProgress failed,error: ' + JSON.stringify(error));
        })
      } catch (err) {
        hilog.error(0x0000, '[ProgressBar]',
          'getDataWithProgress fail,err：' + err.code + ',message: ' + err.message);
      }
    }
  })
```

## 示例代码

* [实现剪贴板复制粘贴的功能](https://gitcode.com/harmonyos_samples/pasteboard)
