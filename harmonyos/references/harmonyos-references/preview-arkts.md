---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/preview-arkts
title: filePreview（文件预览）
breadcrumb: API参考 > 应用服务 > Preview Kit（文件预览服务） > ArkTS API > filePreview（文件预览）
category: harmonyos-references
scraped_at: 2026-09-02T14:53:29+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:b8c06e5f6e7f474b137ab8796cb7abe82c086eda6619aa005a15ade41d8c547f
---

本模块为应用提供便捷的文件快速预览能力。应用可以通过文件预览提供的系统级预览API，可快速启动预览界面，实现对各类文件的预览。通过预览服务，用户可以对文件（包括图片，视频，音频，文本、html等）进行操作。

本模块提供接入文件快速预览的能力，可通过传递文件信息快速打开预览窗口。

支持的预览文件类型如下：

| 类型 | 文件后缀 | mimeType类型 |
| --- | --- | --- |
| 文本 | txt、cpp、c、h、java、xhtml、xml | text/plain、text/x-c++src、text/x-csrc、text/x-chdr、text/x-java、application/xhtml+xml、text/xml |
| 网页 | html、htm | text/html |
| 图片 | jpg、png、gif、webp、bmp、svg | image/jpeg、image/png、image/gif、image/webp、image/bmp、image/svg+xml |
| 音频 | m4a、aac、mp3、ogg、wav | audio/mp4a-latm、audio/aac、audio/mpeg、audio/ogg、audio/x-wav |
| 视频 | mp4、mkv、ts | video/mp4、video/x-matroska、video/mp2ts |
| 文件夹 | 无 | 无 |
| 文档 | pdf | application/pdf  **起始版本：** 5.0.0(12) |
| Office文档 | doc、docx、xls、xlsx、ppt、pptx、csv、ofd | application/msword、application/vnd.openxmlformats-officedocument.wordprocessingml.document、application/vnd.ms-excel、application/vnd.openxmlformats-officedocument.spreadsheetml.sheet、application/vnd.ms-powerpoint、application/vnd.openxmlformats-officedocument.presentationml.presentation、text/csv、general.ofd  **起始版本：** 5.0.0(12) |

**起始版本：** 4.1.0(11)

## 导入模块

```typescript
import { filePreview } from '@kit.PreviewKit';
```

## PreviewInfo

文件预览信息，包含了文件标题名、uri以及文件类型（mimeType）。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.FileManagement.FilePreview.Core

**起始版本：** 4.1.0(11)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| title | string | 否 | 是 | 文件的标题名称 |
| uri | string | 否 | 否 | 文件的[uri](../harmonyos-guides/user-file-uri-intro.md) |
| mimeType | string | 否 | 否 | 文件的媒体资源类型，如text/plain。  **说明：**  若无法确定文件格式，该项可直接赋值空字符串（""），系统会通过uri后缀进行文件格式判断。 |

## DisplayInfo

悬浮窗口的属性值，包含了悬浮窗大小以及位置信息。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.FileManagement.FilePreview.Core

**起始版本：** 4.1.0(11)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| x | number | 否 | 否 | 预览窗口的起始X轴，单位px |
| y | number | 否 | 否 | 预览窗口的起始Y轴，单位px |
| width | number | 否 | 是 | 预览窗口的宽度，单位px |
| height | number | 否 | 是 | 预览窗口的高度，单位px |

## openPreview

openPreview(context: Context, file: PreviewInfo, info?: DisplayInfo): Promise<void>

通过传入文件预览信息以及悬浮窗口属性信息，打开预览窗口。1秒内重复调用无效。使用Promise方式异步回调。

该接口需要调用方确认传入的uri可进行转授权。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.FileManagement.FilePreview.Core

**起始版本：** 4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [Context](js-apis-inner-application-context.md) | 是 | 上下文[common.UIAbilityContext](js-apis-inner-application-uiabilitycontext.md)。  **注意：**  当前context仅支持传入UIAbilityContext。 |
| file | [PreviewInfo](preview-arkts.md#previewinfo) | 是 | 文件的预览信息，title为可选，不填会通过uri解析，无法解析则显示未知文件。 |
| info | [DisplayInfo](preview-arkts.md#displayinfo) | 否 | 模态窗口的窗口展示信息，PC/2in1端不填写则展示默认大小窗口，Phone、Tablet填写无效。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：** 以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid input parameter. |

**示例：**

```typescript
import { BusinessError } from '@kit.BasicServicesKit';
import { filePreview } from '@kit.PreviewKit';

let uiContext = this.getUIContext().getHostContext() as Context;
// 设置窗口展示信息
let displayInfo: filePreview.DisplayInfo = {
  x: 100,
  y: 100,
  width: 800,
  height: 800
};
// 设置文件预览信息
let fileInfo: filePreview.PreviewInfo = {
  title: '1.txt',
  uri: 'file://docs/storage/Users/currentUser/Documents/1.txt',
  mimeType: 'text/plain'
};
filePreview.openPreview(uiContext, fileInfo, displayInfo).then(() => {
  console.info('Succeeded in opening preview');
}).catch((err: BusinessError) => {
  console.error(`Failed to open preview, err.code = ${err.code}, err.message = ${err.message}`);
});
```

## openPreview

openPreview(context: Context, file: PreviewInfo, info: DisplayInfo, callback: AsyncCallback<void>): void

通过传入文件预览信息以及悬浮窗口属性信息，打开预览窗口。1秒内重复调用无效。使用Callback回调异步返回结果。

该接口需要调用方确认传入的uri可进行转授权。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.FileManagement.FilePreview.Core

**起始版本：** 4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [Context](js-apis-inner-application-context.md) | 是 | 上下文[common.UIAbilityContext](js-apis-inner-application-uiabilitycontext.md)。  **注意：**  当前context仅支持传入UIAbilityContext。 |
| file | [PreviewInfo](preview-arkts.md#previewinfo) | 是 | 文件的预览信息，title为可选，不填写时会通过uri解析，无法解析则显示未知文件。 |
| info | [DisplayInfo](preview-arkts.md#displayinfo) | 是 | 模态窗口的窗口展示信息，手机和平板设备填写无效。 |
| callback | [AsyncCallback](js-apis-base.md#asynccallback)<void> | 是 | 回调函数。当预览窗口成功打开时，err为undefined或err.code为0，否则为错误对象。 |

**错误码：** 以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid input parameter. |

**示例：**

```typescript
import { filePreview } from '@kit.PreviewKit';

let uiContext = this.getUIContext().getHostContext() as Context;
// 设置窗口展示信息
let displayInfo: filePreview.DisplayInfo = {
  x: 100,
  y: 100,
  width: 800,
  height: 800
};
// 设置文件预览信息
let fileInfo: filePreview.PreviewInfo = {
  title: '1.txt',
  uri: 'file://docs/storage/Users/currentUser/Documents/1.txt',
  mimeType: 'text/plain'
};
filePreview.openPreview(uiContext, fileInfo, displayInfo, (err) => {
  if (err && err.code) {
    console.error(`Failed to open preview, err.code = ${err.code}, err.message = ${err.message}`);
    return;
  }
  console.info('Succeeded in opening preview');
});
```

## openPreview

openPreview(context: Context, files: Array<PreviewInfo>, index?: number): Promise<void>

通过传入多个文件预览信息以及选择展示的文件信息下标，打开预览窗口。1秒内重复调用无效。使用Promise方式异步回调。

该接口需要调用方确认传入的uri可进行转授权。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.FileManagement.FilePreview.Core

**设备行为差异：** 此接口在PC/2in1中调用返回801错误码，在其他设备类型中可正常调用。

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [Context](js-apis-inner-application-context.md) | 是 | 上下文[common.UIAbilityContext](js-apis-inner-application-uiabilitycontext.md)。  **注意：**  当前context仅支持传入UIAbilityContext。 |
| files | Array<[PreviewInfo](preview-arkts.md#previewinfo)> | 是 | 文件预览信息列表。 |
| index | number | 否 | 预览窗口打开时展示的文件预览信息下标，不填默认为0。取值范围大于等于0，小于files长度。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：** 以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid input parameter. |
| 801 | Capability not supported. |

**示例：**

```typescript
import { BusinessError } from '@kit.BasicServicesKit';
import { filePreview } from '@kit.PreviewKit';

let uiContext = this.getUIContext().getHostContext() as Context;
// 创建单个文件的预览信息
let fileInfo: filePreview.PreviewInfo = {
  title: '1.txt',
  uri: 'file://docs/storage/Users/currentUser/Documents/1.txt',
  mimeType: 'text/plain'
};
// 创建多文件查看数组
let files: Array<filePreview.PreviewInfo> = new Array();
files.push(fileInfo);
filePreview.openPreview(uiContext, files, 0).then(() => {
  console.info('Succeeded in opening preview');
}).catch((err: BusinessError) => {
  console.error(`Failed to open preview, err.code = ${err.code}, err.message = ${err.message}`);
});
```

## canPreview

canPreview(context: Context, uri: string): Promise<boolean>

根据文件的uri判断文件是否可预览，当传入支持的文件uri时，会返回true；传入不可预览的文件uri时，返回false。使用Promise方式异步回调。

当前接口仅针对文件是否存在以及文件格式是否为支持的文件类型进行检验，后续[openPreview](preview-arkts.md#openpreview)进行文件查看时需要调用方保证文件可以被转授权。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.FileManagement.FilePreview.Core

**起始版本：** 4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [Context](js-apis-inner-application-context.md) | 是 | 上下文[common.UIAbilityContext](js-apis-inner-application-uiabilitycontext.md)。  **注意：**  当前context仅支持传入UIAbilityContext。 |
| uri | string | 是 | 文件[uri](../harmonyos-guides/user-file-uri-intro.md) |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象，当传入支持的文件uri时，会返回true；传入不可预览的文件uri时，返回false。 |

**错误码：** 以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid input parameter. |

**示例：**

```typescript
import { BusinessError } from '@kit.BasicServicesKit';
import { filePreview } from '@kit.PreviewKit';

 // e.g 文件存在且类型符合时
let uri = 'file://docs/storage/Users/currentUser/Documents/1.txt';
let uiContext = this.getUIContext().getHostContext() as Context;
filePreview.canPreview(uiContext, uri).then((result) => { // 此处返回true
  console.info(`Succeeded in obtaining the result of whether it can be previewed. result = ${result}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to obtain the result of whether it can be previewed, err.code = ${err.code}, err.message = ${err.message}`);
})
```

```typescript
import { BusinessError } from '@kit.BasicServicesKit';
import { filePreview } from '@kit.PreviewKit';

// e.g 文件不存在或文件类型不符合时
let uri = 'file://docs/storage/Users/currentUser/Documents/1.txt';
let uiContext = this.getUIContext().getHostContext() as Context;
filePreview.canPreview(uiContext, uri).then((result) => { // 此处返回false
  console.info(`Succeeded in obtaining the result of whether it can be previewed. result = ${result}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to obtain the result of whether it can be previewed, err.code = ${err.code}, err.message = ${err.message}`);
});
```

## canPreview

canPreview(context: Context, uri: string, callback: AsyncCallback<boolean>): void

根据文件的uri判断文件是否可预览，当传入支持的文件uri时，会返回true；传入不可预览的文件uri时，返回false。使用Callback回调异步返回结果。

当前接口仅针对文件是否存在以及文件格式是否为支持的文件类型进行检验，后续[openPreview](preview-arkts.md#openpreview)进行文件查看时需要调用方保证文件可以被转授权。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.FileManagement.FilePreview.Core

**起始版本：** 4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [Context](js-apis-inner-application-context.md) | 是 | 上下文[common.UIAbilityContext](js-apis-inner-application-uiabilitycontext.md)。  **注意：**  当前context仅支持传入UIAbilityContext。 |
| uri | string | 是 | 文件[uri](../harmonyos-guides/user-file-uri-intro.md) |
| callback | [AsyncCallback](js-apis-base.md#asynccallback)<boolean> | 是 | 回调函数。当传入支持的文件uri时，会返回true；传入不可预览的文件uri时，返回false。 |

**错误码：** 以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid input parameter. |

**示例：**

```typescript
import { filePreview } from '@kit.PreviewKit';

// e.g 文件存在且类型符合时
let uri = 'file://docs/storage/Users/currentUser/Documents/1.txt';
let uiContext = this.getUIContext().getHostContext() as Context;
filePreview.canPreview(uiContext, uri, (err, result) => {
  if (err && err.code) {
    console.error(`Failed to obtain the result of whether it can be previewed, err.code = ${err.code}, err.message = ${err.message}`);
    return;
  }
  console.info(`Succeeded in obtaining the result of whether it can be previewed. result = ${result}`); // 此处返回true
});
```

```typescript
import { filePreview } from '@kit.PreviewKit';

// e.g 文件不存在或文件类型不符合时
let uri = 'file://docs/storage/Users/currentUser/Documents/9.txt';
let uiContext = this.getUIContext().getHostContext() as Context;
filePreview.canPreview(uiContext, uri, (err, result) => {
  if (err && err.code) {
    console.error(`Failed to obtain the result of whether it can be previewed, err.code = ${err.code}, err.message = ${err.message}`);
    return;
  }
  console.info(`Succeeded in obtaining the result of whether it can be previewed. result = ${result}`); // 此处返回false
});
```

## hasDisplayed

hasDisplayed(context: Context): Promise<boolean>

判断预览窗口是否已经存在。预览窗口是单例的形式，如果预览窗口已经打开过并且没关闭，那会返回true。如果没打开或者打开后已关闭，那将返回false。使用Promise方式异步回调。判断是否已打开预览需要等待窗口创建完成才能产生效果，窗口还没创建完成就调用hasDisplayed接口会导致结果返回false。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.FileManagement.FilePreview.Core

**起始版本：** 4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [Context](js-apis-inner-application-context.md) | 是 | 上下文[common.UIAbilityContext](js-apis-inner-application-uiabilitycontext.md)。  **注意：**  当前context仅支持传入UIAbilityContext。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象，预览窗口是单例的形式，当预览窗口已经打开过并且没关闭，那会返回true。如果没打开或者打开后已关闭，那将返回false。 |

**错误码：** 以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid input parameter. |

**示例：**

```typescript
import { BusinessError } from '@kit.BasicServicesKit';
import { filePreview } from '@kit.PreviewKit';

// e.g 预览窗口已存在
let uiContext = this.getUIContext().getHostContext() as Context;
filePreview.hasDisplayed(uiContext).then((result) => { // 此处返回true
  console.info(`Succeeded in obtaining the result of whether the preview has displayed. result = ${result}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to obtain the result of whether the preview has displayed, err.code = ${err.code}, err.message = ${err.message}`);
});
```

```typescript
import { BusinessError } from '@kit.BasicServicesKit';
import { filePreview } from '@kit.PreviewKit';

 // e.g 预览窗口不存在
let uiContext = this.getUIContext().getHostContext() as Context;
filePreview.hasDisplayed(uiContext).then((result) => { // 此处返回false
  console.info(`Succeeded in obtaining the result of whether the preview has displayed. result = ${result}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to obtain the result of whether the preview has displayed, err.code = ${err.code}, err.message = ${err.message}`);
});
```

## hasDisplayed

hasDisplayed(context: Context, callback: AsyncCallback<boolean>): void

判断预览窗口是否已经存在。预览窗口是单例的形式，如果预览窗口已经打开过并且没关闭，那会返回true。如果没打开或者打开后已关闭，那将返回false。使用Callback回调异步返回结果。判断是否已打开预览需要等待窗口创建完成才能产生效果，窗口还没创建完成就调用hasDisplayed接口会导致结果返回false。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.FileManagement.FilePreview.Core

**起始版本：** 4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [Context](js-apis-inner-application-context.md) | 是 | 上下文[common.UIAbilityContext](js-apis-inner-application-uiabilitycontext.md)。  **注意：**  当前context仅支持传入UIAbilityContext。 |
| callback | [AsyncCallback](js-apis-base.md#asynccallback)<boolean> | 是 | 回调函数。预览窗口是单例的形式，当预览窗口已经打开过并且没关闭，那会返回true。如果没打开或者打开后已关闭，那将返回false。 |

**错误码：** 以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid input parameter. |

**示例：**

```typescript
import { filePreview } from '@kit.PreviewKit';

// e.g 预览窗口已存在
let uiContext = this.getUIContext().getHostContext() as Context;
filePreview.hasDisplayed(uiContext, (err, result) => {
  if (err && err.code) {
    console.error(`Failed to obtain the result of whether the preview has displayed, err.code = ${err.code}, err.message = ${err.message}`);
    return;
  }
  console.info(`Succeeded in obtaining the result of whether the preview has displayed. result = ${result}`); // 此处返回true
});
```

```typescript
import { filePreview } from '@kit.PreviewKit';

// e.g 预览窗口不存在
let uiContext = this.getUIContext().getHostContext() as Context;
filePreview.hasDisplayed(uiContext, (err, result) => {
  if (err && err.code) {
    console.error(`Failed to obtain the result of whether the preview has displayed, err.code = ${err.code}, err.message = ${err.message}`);
    return;
  }
  console.info(`Succeeded in obtaining the result of whether the preview has displayed. result = ${result}`); // 此处返回false
});
```

## closePreview

closePreview(context: Context): Promise<void>

关闭预览窗口，仅当预览窗口存在时起效。使用Promise方式异步回调。关闭预览窗口需要等待窗口创建完成才能产生效果，窗口还没创建完成就调用closePreview接口会无效。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.FileManagement.FilePreview.Core

**起始版本：** 4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [Context](js-apis-inner-application-context.md) | 是 | 上下文[common.UIAbilityContext](js-apis-inner-application-uiabilitycontext.md)。  **注意：**  当前context仅支持传入UIAbilityContext。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：** 以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid input parameter. |

**示例：**

```typescript
import { BusinessError } from '@kit.BasicServicesKit';
import { filePreview } from '@kit.PreviewKit';

let uiContext = this.getUIContext().getHostContext() as Context;
filePreview.closePreview(uiContext).then(() => { // 仅当预览窗口存在时起效
  console.info('Succeeded in closing preview');
}).catch((err: BusinessError) => {
  console.error(`Failed to close preview, err.code = ${err.code}, err.message = ${err.message}`);
});
```

## closePreview

closePreview(context: Context, callback: AsyncCallback<void>): void

关闭预览窗口，仅当预览窗口存在时起效。使用Callback回调异步返回结果。关闭预览窗口需要等待窗口创建完成才能产生效果，窗口还没创建完成就调用closePreview接口会无效。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.FileManagement.FilePreview.Core

**起始版本：** 4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [Context](js-apis-inner-application-context.md) | 是 | 上下文[common.UIAbilityContext](js-apis-inner-application-uiabilitycontext.md)。  **注意：**  当前context仅支持传入UIAbilityContext。 |
| callback | [AsyncCallback](js-apis-base.md#asynccallback)<void> | 是 | 回调函数。当预览窗口成功关闭时，err为undefined或err.code为0，否则为错误对象。 |

**错误码：** 以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid input parameter. |

**示例：**

```typescript
import { filePreview } from '@kit.PreviewKit';

let uiContext = this.getUIContext().getHostContext() as Context;
filePreview.closePreview(uiContext, (err) => { // 仅当预览窗口存在时起效
  if (err && err.code) {
    console.error(`Failed to close preview, err.code = ${err.code}, err.message = ${err.message}`);
    return;
  }
  console.info('Succeeded in closing preview');
});
```

## loadData

loadData(context: Context, file: PreviewInfo): Promise<void>

加载预览文件信息。仅当预览窗口存在时起效。传入可预览文件时展示对应预览界面，传入不可预览文件显示不支持预览界面。100毫秒内重复调用无效。使用Promise方式异步回调。加载预览文件需要等待窗口创建完成才能产生效果，窗口还没创建完成就调用loadData接口会无效。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.FileManagement.FilePreview.Core

**起始版本：** 4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [Context](js-apis-inner-application-context.md) | 是 | 上下文[common.UIAbilityContext](js-apis-inner-application-uiabilitycontext.md)。  **注意：**  当前context仅支持传入UIAbilityContext。 |
| file | [PreviewInfo](preview-arkts.md#previewinfo) | 是 | 文件的预览信息，title为可选，不填会通过uri解析，无法解析则显示未知文件。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：** 以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid input parameter. |

**示例：**

```typescript
import { BusinessError } from '@kit.BasicServicesKit';
import { filePreview } from '@kit.PreviewKit';

let uiContext = this.getUIContext().getHostContext() as Context;
let fileInfo: filePreview.PreviewInfo = {
  title: '1.txt',
  uri: 'file://docs/storage/Users/currentUser/Documents/1.txt',
  mimeType: 'text/plain'
};
filePreview.loadData(uiContext, fileInfo).then(() => { // 仅当预览窗口存在时起效
  console.info('Succeeded in loading data.');
}).catch((err: BusinessError) => {
  console.error(`Failed to load data, err.code = ${err.code}, err.message = ${err.message}`);
});
```

## loadData

loadData(context: Context, file: PreviewInfo, callback: AsyncCallback<void>): void

加载预览文件信息。仅当预览窗口存在时起效。传入可预览文件时展示对应预览界面，传入不可预览文件显示不支持预览界面。100毫秒内重复调用无效。使用Callback回调异步返回结果。加载预览文件需要等待窗口创建完成才能产生效果，窗口还没创建完成就调用loadData接口会无效。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.FileManagement.FilePreview.Core

**起始版本：** 4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [Context](js-apis-inner-application-context.md) | 是 | 上下文[common.UIAbilityContext](js-apis-inner-application-uiabilitycontext.md)。  **注意：**  当前context仅支持传入UIAbilityContext。 |
| file | [PreviewInfo](preview-arkts.md#previewinfo) | 是 | 文件的预览信息，title为可选，不填会通过uri解析，无法解析则显示未知文件。 |
| callback | [AsyncCallback](js-apis-base.md#asynccallback)<void> | 是 | 回调函数。当预览文件加载成功时，err为undefined或err.code为0，否则为错误对象。 |

**错误码：** 以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid input parameter. |

**示例：**

```typescript
import { filePreview } from '@kit.PreviewKit';

let uiContext = this.getUIContext().getHostContext() as Context;
let fileInfo: filePreview.PreviewInfo = {
  title: '1.txt',
  uri: 'file://docs/storage/Users/currentUser/Documents/1.txt',
  mimeType: 'text/plain'
};
filePreview.loadData(uiContext, fileInfo, (err) => { // 仅当预览窗口存在时起效
  if (err && err.code) {
    console.error(`Failed to load data, err.code = ${err.code}, err.message = ${err.message}`);
    return;
  }
  console.info('Succeeded in loading data.');
});
```

## loadData

loadData(context: Context, files: Array<PreviewInfo>, index?: number): Promise<void>

加载预览文件信息。仅当预览窗口存在时起效。可传入多个文件预览信息以及对应展示的列表下标进行选择预览。使用Promise方式异步回调。

加载预览文件需要等待窗口创建完成才能产生效果，窗口还没创建完成就调用loadData接口会无效。该接口在PC/2in1端无效。100毫秒内重复调用无效。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.FileManagement.FilePreview.Core

**设备行为差异：** 此接口在PC/2in1中调用返回801错误码，在其他设备类型中可正常调用。

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [Context](js-apis-inner-application-context.md) | 是 | 上下文[common.UIAbilityContext](js-apis-inner-application-uiabilitycontext.md)。  **注意：**  当前context仅支持传入UIAbilityContext。 |
| files | Array<[PreviewInfo](preview-arkts.md#previewinfo)> | 是 | 文件预览信息列表。 |
| index | number | 否 | 预览窗口打开时展示的文件预览信息下标，不填默认为0。取值范围大于等于0，小于files长度。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：** 以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid input parameter. |
| 801 | Capability not supported. |

**示例：**

```typescript
import { BusinessError } from '@kit.BasicServicesKit';
import { filePreview } from '@kit.PreviewKit';

let uiContext = this.getUIContext().getHostContext() as Context;
let fileInfo: filePreview.PreviewInfo = {
  title: '1.txt',
  uri: 'file://docs/storage/Users/currentUser/Documents/1.txt',
  mimeType: 'text/plain'
};
let files: Array<filePreview.PreviewInfo> = new Array();
files.push(fileInfo);
filePreview.loadData(uiContext, files, 0).then(() => { // 仅当预览窗口存在时起效
  console.info('Succeeded in loading data.');
}).catch((err: BusinessError) => {
  console.error(`Failed to load data, err.code = ${err.code}, err.message = ${err.message}`);
});
```
