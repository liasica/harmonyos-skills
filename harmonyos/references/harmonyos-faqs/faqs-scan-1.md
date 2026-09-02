---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-scan-1
title: 扫码时无法识别多个码图
breadcrumb: FAQ > 媒体开发 > 拍照和图片 > 扫码服务（Scan） > 扫码时无法识别多个码图
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:43+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:2e56f42228ed83e1bf13948e48a810a65ff5c295caf79fbe51e4afbc10da69d3
---

## 问题现象

使用扫码功能识别多个码图时，无法识别多个。

## 背景知识

[ScanOptions](../harmonyos-references/scan-scanbarcode-api.md#scanoptions)：扫码、识码参数。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| scanTypes | Array | 否 | 是 | 设置扫码类型，默认扫码ALL（全部码类型）。 |
| enableMultiMode | boolean | 否 | 是 | 是否开启多码识别，默认false。 |
| enableAlbum | boolean | 否 | 是 | 是否开启相册，默认true。 |

## 问题定位

查看代码，检查scanTypes扫码类型是否设置ALL，检查enableMultiMode多码识别是否开启。如下，如果ScanOptions未设置正确，会导致无法识别多个码图。

```ts
let options: scanBarcode.ScanOptions = { scanTypes: [scanCore.ScanType.ONE_D_CODE], enableMultiMode: false, enableAlbum: true };
```

## 分析结论

应用没有开启多码识别或扫码类型没有设置对应类型。

## 修改建议

参考以下示例，完善ScanOptions的参数配置，将ScanType设置为ALL，enableMultiMode设置为true：

```ts
import { scanBarcode, scanCore } from '@kit.ScanKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 定义扫码参数options，ScanType设置为ALL，enableMultiMode设置为true
let options: scanBarcode.ScanOptions = { scanTypes: [scanCore.ScanType.ALL], enableMultiMode: true, enableAlbum: true };

function loadPage(uiContext: UIContext) {
  try {
    scanBarcode.startScanForResult(uiContext.getHostContext(), options).then(() => {
      console.info('[Scan Sample]', `Succeeded in getting ScanResult by promise with options`);
    }).catch((error: BusinessError) => {
      console.error('[Scan Sample]',
        `Failed to get ScanResult by promise with options. Code: ${error.code}, message: ${error.message}`);
    });
  } catch (error) {
    console.error('[Scan Sample]', `Failed to startScanForResult. Code: ${error.code}, message: ${error.message}`);
  }
}

@Entry
@Component
struct Index {
  message: string = 'Hello World';

  build() {
    RelativeContainer() {
      Button(this.message)
        .fontSize($r('app.float.page_text_font_size'))
        .fontWeight(FontWeight.Bold)
        .alignRules({
          center: { anchor: '__container__', align: VerticalAlign.Center },
          middle: { anchor: '__container__', align: HorizontalAlign.Center }
        })
        .onClick(() => {
          loadPage(this.getUIContext());
        });
    }
    .height('100%')
    .width('100%');
  }
}
```
