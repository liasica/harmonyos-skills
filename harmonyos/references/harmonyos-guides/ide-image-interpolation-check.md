---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-image-interpolation-check
title: "@correctness/image-interpolation-check"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 正确性规则@correctness > @correctness/image-interpolation-check
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:53+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:04345a2f00297a4378593df45d44676d602c2ba217642c2195c4307a5e1368ad
---

在使用Image组件[interpolation](../harmonyos-references/ts-basic-components-image.md#interpolation)接口时，建议不要使用最邻近插值，避免出现明显锯齿问题。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@correctness/image-interpolation-check": "warn"
  }
}
```

## 选项

该规则无需配置选项。

## 正例

```screen
const ADAPTIVE_SCALE = 1.5;

@Component
export struct AppIcon {
  @State icon: string | PixelMap = '';
  @Prop iconSize: number = 1;
  private mInterpolation: ImageInterpolation = ImageInterpolation.None;

  aboutToAppear(): void {
    this.mInterpolation = ImageInterpolation.Medium;
  }

  @Builder
  overlayIcon() {
    Image(this.icon)
      .height(this.iconSize * ADAPTIVE_SCALE)
      .width(this.iconSize * ADAPTIVE_SCALE)
      .interpolation(ImageInterpolation.Medium)
  }

  @Builder
  overlayIcon1() {
    Image(this.icon)
      .height(this.iconSize * ADAPTIVE_SCALE)
      .width(this.iconSize * ADAPTIVE_SCALE)
      .interpolation(this.mInterpolation)
  }

  build() {
    Column() {
      this.overlayIcon();
      this.overlayIcon1();
      Image($r('app.media.pause'))
        .draggable(false)
        .interpolation(ImageInterpolation.Medium)
    }
  }
}
```

## 反例

```screen
const ADAPTIVE_SCALE = 1.5;

@Component
export struct AppIcon {
  @State icon: string | PixelMap = '';
  @Prop iconSize: number = 1;
  private mInterpolation: ImageInterpolation = ImageInterpolation.Medium;

  aboutToAppear(): void {
    this.mInterpolation = ImageInterpolation.None;
  }

  @Builder
  overlayIcon() {
    Image(this.icon)
      .height(this.iconSize * ADAPTIVE_SCALE)
      .width(this.iconSize * ADAPTIVE_SCALE)
      // warning
      .interpolation(ImageInterpolation.None)
  }

  @Builder
  overlayIcon1() {
    Image(this.icon)
      .height(this.iconSize * ADAPTIVE_SCALE)
      .width(this.iconSize * ADAPTIVE_SCALE)
      // warning
      .interpolation(this.mInterpolation)
  }

  build() {
    Column() {
      this.overlayIcon();
      this.overlayIcon1();
      Image($r('app.media.pause'))
        .draggable(false)
        // warning
        .interpolation(ImageInterpolation.None)
    }
  }
}
```

## 规则集

```screen
plugin:@correctness/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
