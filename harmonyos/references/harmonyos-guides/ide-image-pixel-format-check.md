---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-image-pixel-format-check
title: "@correctness/image-pixel-format-check"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 正确性规则@correctness > @correctness/image-pixel-format-check
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:53+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:451f4d0dc2dadea5909f3149b56dcf60d34aae8d394b164feaeabcb1718ea4fa
---

在使用Image组件[createPixelMap](../harmonyos-references/arkts-apis-image-f.md#imagecreatepixelmap8)接口时，建议不要选择RGB\_565档位，避免出现色阶问题。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@correctness/image-pixel-format-check": "warn"
  }
}
```

## 选项

该规则无需配置选项。

## 正例

```screen
import image from '@ohos.multimedia.image';
const DEFAULT_IMAGE_WIDTH_HEIGHT: number = 600;
const DEFAULT_IMAGE_BUFFER_SIZE: number = DEFAULT_IMAGE_WIDTH_HEIGHT * DEFAULT_IMAGE_WIDTH_HEIGHT * 4;
export class AodFailTask {
  private async setImage(): Promise<void> {
    const color = new ArrayBuffer(DEFAULT_IMAGE_BUFFER_SIZE);
    let opts: image.InitializationOptions = {
      editable: true,
      pixelFormat: image.PixelMapFormat.RGBA_8888,
      size: { height: DEFAULT_IMAGE_WIDTH_HEIGHT, width: DEFAULT_IMAGE_WIDTH_HEIGHT }
    }
    const imageSrc = await image.createPixelMap(color, opts);
  }
  private async setImage1(): Promise<void> {
    const color = new ArrayBuffer(DEFAULT_IMAGE_BUFFER_SIZE);
    let opts: image.InitializationOptions = {
      editable: true,
      pixelFormat: image.PixelMapFormat.RGBA_8888,
      size: { height: DEFAULT_IMAGE_WIDTH_HEIGHT, width: DEFAULT_IMAGE_WIDTH_HEIGHT }
    }
    const imageSrc = await image.createPixelMap(color, opts);
  }
  
  private setImage2() {
    // Original image size
    let width: number = 100;
    let height: number = 100;
    let buffer: ArrayBuffer = new ArrayBuffer(width * height * 4);
    image.createPixelMap(buffer, {
      editable: false,
      pixelFormat: image.PixelMapFormat.RGBA_8888,
      size: { height: height, width: width }
    })
  }
  
}
```

## 反例

```screen
import image from '@ohos.multimedia.image';
const DEFAULT_IMAGE_WIDTH_HEIGHT: number = 600;
const DEFAULT_IMAGE_BUFFER_SIZE: number = DEFAULT_IMAGE_WIDTH_HEIGHT * DEFAULT_IMAGE_WIDTH_HEIGHT * 4;
export class AodFailTask {
  private async setImage(): Promise<void> {
    const color = new ArrayBuffer(DEFAULT_IMAGE_BUFFER_SIZE);
    let opts: image.InitializationOptions = {
      editable: true,
      pixelFormat: image.PixelMapFormat.RGB_565,
      size: { height: DEFAULT_IMAGE_WIDTH_HEIGHT, width: DEFAULT_IMAGE_WIDTH_HEIGHT }
    }
    // warning
    const imageSrc = await image.createPixelMap(color, opts);
  }
  private async setImage1(): Promise<void> {
    const color = new ArrayBuffer(DEFAULT_IMAGE_BUFFER_SIZE);
    let opts: image.InitializationOptions = {
      editable: true,
      pixelFormat: image.PixelMapFormat.RGB_565,
      size: { height: DEFAULT_IMAGE_WIDTH_HEIGHT, width: DEFAULT_IMAGE_WIDTH_HEIGHT }
    }
    // warning
    const imageSrc = await image.createPixelMap(color, opts);
  }
  private setImage2() {
    // Original image size
    let width: number = 100;
    let height: number = 100;
    let buffer: ArrayBuffer = new ArrayBuffer(width * height * 4);
    // warning
    image.createPixelMap(buffer, {
      editable: false,
      pixelFormat: image.PixelMapFormat.RGB_565,
      size: { height: height, width: width }
    })
  }
}
```

## 规则集

```screen
plugin:@correctness/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
