---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/scan-generatebarcode
title: generateBarcode (码图生成)
breadcrumb: API参考 > 媒体 > Scan Kit（统一扫码服务） > ArkTS API > generateBarcode (码图生成)
category: harmonyos-references
scraped_at: 2026-09-02T15:02:39+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:91ff15490581869e30f8a3f5abeddacc0398dbf72413eb3a4e479333daa130d6
---

## 模块概述

generateBarcode模块支持通过文本或字节数组生成码图。目前已支持的码类型为EAN-8、EAN-13、UPC-A、UPC-E、Codabar、Code 39、Code 93、Code 128、ITF-14、QR Code、Data Matrix、PDF417、Aztec。暂不支持MULTIFUNCTIONAL CODE生成。

为便于开发者快速上手，建议参考官方提供的[示例工程](https://gitcode.com/HarmonyOS_Samples/scankit-samplecode-clientdemo-arkts)。

**起始版本：** 4.1.0(11)

## 导入模块

```typescript
import { generateBarcode } from '@kit.ScanKit';
```

## ErrorCorrectionLevel

纠错率枚举。纠错率越高，码图在物理损伤（如损坏、污损、遮挡等场景）下的可识别性越强，但相应会导致图案复杂度提升和尺寸增大；反之，低纠错率则呈现更简洁的码图但抗损能力较弱。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API版本5.0.2(14)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Scan.GenerateBarcode

**起始版本：** 4.1.0(11)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| LEVEL\_L | 0 | 7%纠错率。 |
| LEVEL\_M | 1 | 15%纠错率。 |
| LEVEL\_Q | 2 | 25%纠错率。 |
| LEVEL\_H | 3 | 30%纠错率。 |

## CreateOptions

生成码参数。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API版本5.0.2(14)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Scan.GenerateBarcode

**起始版本：** 4.1.0(11)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| scanType | scanCore.[ScanType](scan-scancore.md#scantype) | 否 | 否 | 指定要生成的码类型。 |
| width | number | 否 | 否 | 码图宽，单位：px。取值范围：[200, 4096]。 |
| height | number | 否 | 否 | 码图高，单位：px。取值范围：[200, 4096]。 |
| margin | number | 否 | 是 | 最小边距（生成码图的边距大于等于该值），单位：px，默认值为1，取值范围：[1, 10]。 |
| level | [ErrorCorrectionLevel](scan-generatebarcode.md#errorcorrectionlevel) | 否 | 是 | 纠错水平，默认值为LEVEL\_H。此参数只在生成QR码时有效。 |
| backgroundColor | number | 否 | 是 | 生成码图背景颜色，HEX格式颜色，默认为白色（0xFFFFFF）。 |
| pixelMapColor | number | 否 | 是 | 生成码图颜色，HEX格式颜色，默认为黑色（0x000000）。 |

**说明** 

生成码参数建议：

* 码图颜色和背景

  建议使用默认颜色和背景：黑色码图、白色背景。如果码图颜色和背景对比度较小会影响识别。
* 码图最小边距

  建议使用默认最小边距1，单位：px，取值范围：[1, 10]。
* 码图大小

  1. 生成QR Code、Data Matrix、Aztec类型的码图时，输入的width和height值相同且均大于等于200小于等于4096，单位：px，否则生成的码图过小会影响识别。
  2. 生成EAN-8、EAN-13、UPC-A、UPC-E、Codabar、Code 39、Code 93、Code 128、ITF-14、PDF417类型的码图时，建议输入的width和height值比例为2:1，并且width值需大于400，单位：px，否则生成的码图会过小影响识别。

**示例：**

```typescript
import { scanCore, generateBarcode } from '@kit.ScanKit';

// 以QR码为例
let options: generateBarcode.CreateOptions = {
  scanType: scanCore.ScanType.QR_CODE,
  width: 200,
  height: 200,
  margin: 1,
  level: generateBarcode.ErrorCorrectionLevel.LEVEL_H,
  backgroundColor: 0xFFFFFF,
  pixelMapColor: 0x000000
};
```

## createBarcode

createBarcode(content: string, options: CreateOptions): Promise<image.PixelMap>

通过文本生成并返回码图。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API版本5.0.2(14)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Scan.GenerateBarcode

**起始版本：** 4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| content | string | 是 | 码内容字符串，参数限制请参见下方表1-content参数限制条件。 |
| options | [CreateOptions](scan-generatebarcode.md#createoptions) | 是 | 码图生成的配置参数。 |

**返回值：**

| **类型** | **说明** |
| --- | --- |
| Promise<image.[PixelMap](arkts-apis-image-pixelmap.md)> | Promise对象，返回生成的码图对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ArkTS API错误码](errorcode-scan.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 1000500001 | Internal error. |

**示例：**

```typescript
import { image } from '@kit.ImageKit';
import { scanCore, generateBarcode } from '@kit.ScanKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

// 以QR码为例，码图生成的参数
const content: string = 'Huawei@HMSCore';
const options: generateBarcode.CreateOptions = {
  scanType: scanCore.ScanType.QR_CODE,
  width: 200,
  height: 200
};
generateBarcode.createBarcode(content, options).then((data: image.PixelMap) => {
  // 码图生成成功，返回生成码图的PixelMap对象
  hilog.info(0x0001, '[Scan Sample]',
    `Succeeded in getting PixelMap by promise with options, isResultAvailable: ${!!data}`);
}).catch((err: BusinessError) => {
  // 码图生成失败，返回错误信息
  hilog.error(0x0001, '[Scan Sample]',
    `Failed to get PixelMap by promise with options. Code: ${err.code}, message: ${err.message}`);
});
```

**表1** content参数限制条件

| 生成码类型 | 参数建议内容 |
| --- | --- |
| QR Code | 支持中文，不超过512字符长度，如果内容过长会导致码复杂，影响识别。 |
| Aztec | 支持中文，不超过512字符长度，如果内容过长会导致码复杂，影响识别。 |
| PDF417 | 支持中文，不超过512字符长度，如果内容过长会导致码复杂，影响识别。 |
| Data Matrix | 不支持中文，不超过512字符长度，如果内容过长会导致码复杂，影响识别。 |
| UPC-A | 支持11位数字输入，只支持数字，生成包含12位数字的码图，包含最后一位校验数字。 |
| UPC-E | 支持7位数字输入，只支持数字，首位需要是0或1，生成包含8位数字的码图，包含最后一位校验数字。 |
| ITF-14 | 支持80位以内数字输入，并且需要是偶数位，只支持数字，生成包含偶数位数字的码图，如果内容过长会导致码复杂，影响识别。 |
| EAN-8 | 支持7位数字输入，只支持数字，生成包含8位数字的码图，包含最后一位校验数字。 |
| EAN-13 | 支持12位数字输入，只支持数字，首位不可以是0，生成包含13位数字的码图，包含最后一位校验数字。 |
| Code 39 | 不超过80字节长度，如果内容过长会导致码复杂，影响识别。字符集可以是数字、大小写字母和- . $ / + % \* SPACE英文格式符号（请注意：一个小写字母占用2个字节）。 |
| Code 93 | 不超过80字节长度，如果内容过长会导致码复杂，影响识别。字符集可以是数字、大小写字母和- . $ / + % \* SPACE英文格式符号（请注意：一个小写字母占用2个字节）。 |
| Code 128 | 不超过80字节长度，如果内容过长会导致码复杂，影响识别。字符集可以是数字、大小写字母和- . $ / + % \* SPACE英文格式符号（请注意：一个小写字母占用1个字节）。 |
| Codabar | 不超过512字符长度，如果内容过长会导致码复杂，影响识别。起始/终止符可以是ABCD中的任一个（特殊情况下，TN\*E也会编码成ABCD，推荐使用ABCD）。其他字符可以是数字和- . $ / : +英文格式符号。 |

## createBarcode

createBarcode(content: string, options: CreateOptions, callback: AsyncCallback<image.PixelMap>): void

通过文本生成并返回码图。使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API版本5.0.2(14)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Scan.GenerateBarcode

**起始版本：** 4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| content | string | 是 | 码内容字符串。参数限制请参见[createBarcode](scan-generatebarcode.md#createbarcode)的表1-content参数限制条件。 |
| options | [CreateOptions](scan-generatebarcode.md#createoptions) | 是 | 码图生成的配置参数。 |
| callback | AsyncCallback<image.[PixelMap](arkts-apis-image-pixelmap.md)> | 是 | 回调函数。当码图生成成功，err为undefined，data为生成的码图对象image.PixelMap；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ArkTS API错误码](errorcode-scan.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 1000500001 | Internal error. |

**示例：**

```typescript
import { image } from '@kit.ImageKit';
import { scanCore, generateBarcode } from '@kit.ScanKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

// 以QR码为例，码图生成的参数
const content: string = 'Huawei@HMSCore';
const options: generateBarcode.CreateOptions = {
  scanType: scanCore.ScanType.QR_CODE,
  width: 200,
  height: 200
};
generateBarcode.createBarcode(content, options, (err: BusinessError, data: image.PixelMap) => {
  // 码图生成失败，返回错误信息
  if (err) {
    hilog.error(0x0001, '[Scan Sample]',
      `Failed to get PixelMap by callback with options. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  // 码图生成成功，返回生成码图的PixelMap对象
  hilog.info(0x0001, '[Scan Sample]',
    `Succeeded in getting PixelMap by callback with options, isResultAvailable : ${!!data}`);
});
```

## createBarcode

createBarcode(content: ArrayBuffer, options: CreateOptions): Promise<image.PixelMap>

通过字节数组生成并返回码图。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API版本5.0.2(14)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Scan.GenerateBarcode

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| content | ArrayBuffer | 是 | 码内容字节数组，参数限制请参见下方表2-content参数限制条件。 |
| options | [CreateOptions](scan-generatebarcode.md#createoptions) | 是 | 码图生成的配置参数，ScanType仅支持QR Code。 |

**返回值：**

| **类型** | **说明** |
| --- | --- |
| Promise<image.[PixelMap](arkts-apis-image-pixelmap.md)> | Promise对象，返回生成的码图对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ArkTS API错误码](errorcode-scan.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 1000500001 | Internal error. |

**示例：**

```typescript
import { image } from '@kit.ImageKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { scanCore, generateBarcode } from '@kit.ScanKit';
import { buffer } from '@kit.ArkTS';

@Entry
@Component
struct Index {
  @State pixelMap: image.PixelMap | undefined = undefined;

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Button('generateBarcode Promise').onClick(() => {
        this.pixelMap = undefined;
        const content: string =
          '0177C10DD10F7768600202312110000063458FD14112345678FFFFD381012610b746365409210201b66636540ad0200020000000000110e617003201000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000006645fbec664358ECF657CB40693c92da';
        const contentBuffer: ArrayBuffer = buffer.from(content, 'hex').buffer; // 将包含十六进制字符的字符串转换成ArrayBuffer
        const options: generateBarcode.CreateOptions = {
          scanType: scanCore.ScanType.QR_CODE,
          width: 400,
          height: 400
        }; // 码图生成的配置参数
        generateBarcode.createBarcode(contentBuffer, options).then((pixelMap: image.PixelMap) => {
          this.pixelMap = pixelMap; // 码图生成成功，返回生成码图的PixelMap对象
          hilog.info(0x0001, '[Scan Sample]', 'Succeeded in creating barCode.');
        }).catch((err: BusinessError) => {
          // 码图生成失败，返回错误信息
          hilog.error(0x0001, '[Scan Sample]',
            `Failed to create barCode. Code: ${err.code}, message: ${err.message}`);
        });
      })
      // 码图生成成功，显示码图
      if (this.pixelMap) {
        Image(this.pixelMap).width('400px').height('400px').objectFit(ImageFit.Contain)
      }
    }
    .width('100%')
    .height('100%')
  }
}
```

**表2** content参数限制条件：

| 纠错水平 | 参数内容限制 |
| --- | --- |
| LEVEL\_L | 字节数组长度限制建议不超过2048，如果内容过长会导致码复杂，影响识别。 |
| LEVEL\_M | 字节数组长度限制建议不超过2048，如果内容过长会导致码复杂，影响识别。 |
| LEVEL\_Q | 字节数组长度限制建议不超过1536， 如果内容过长会导致码复杂，影响识别。 |
| LEVEL\_H | 字节数组长度限制建议不超过1024， 如果内容过长会导致码复杂，影响识别。 |
