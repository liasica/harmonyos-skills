---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_hp-arkui-use-scale-to-replace-attr-animateto
title: "@performance/hp-arkui-use-scale-to-replace-attr-animateto"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 性能规则@performance > @performance/hp-arkui-use-scale-to-replace-attr-animateto
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:52+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:41be238caa5f1e95e1e82047d9d44a100efc9a1ddb6fd90d39f38b42c64e8a5d
---

建议组件布局改动时使用图形变换属性动画。

动效丢帧场景下，建议优先修改。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@performance/hp-arkui-use-scale-to-replace-attr-animateto": "warn",
  }
}
```

## 选项

该规则无需配置选项。

## 正例

```screen
@Entry
@Component
struct MyComponent {
  @State textScaleX: number = 1;
  @State textScaleY: number = 1;
  build() {
    Column() {
      Text()
        .backgroundColor(Color.Blue)
        .fontColor(Color.White)
        .fontSize(20)
        .width(10)
        .height(10)
        .scale({ x: this.textScaleX, y: this.textScaleY })
        .margin({ top: 100 })
      Button('图形变换属性')
        .backgroundColor(Color.Blue)
        .fontColor(Color.White)
        .fontSize(20)
        .margin({ top: 60 })
        .borderRadius(30)
        .padding(10)
        .onClick(() => {
          animateTo({ duration: 1000 }, () => {
            this.textScaleX = 10;
            this.textScaleY = 10;
          })
        })
    }
 }
}
```

## 反例

```screen
@Entry
@Component
struct MyComponent {
  @State textWidth: number = 10;
  @State textHeight: number = 10;
  build() {
    Column() {
      Text()
        .backgroundColor(Color.Blue)
        .fontColor(Color.White)
        .fontSize(20)
        .width(this.textWidth)
        .height(this.textHeight)
      Button('布局属性')
        .backgroundColor(Color.Blue)
        .fontColor(Color.White)
        .fontSize(20)
        .margin({ top: 30 })
        .borderRadius(30)
        .padding(10)
        .onClick(() => {
          animateTo({ duration: 1000 }, () => {
            this.textWidth = 100;
            this.textHeight = 100;
          })
        })
    }
 }
}
```

## 规则集

```screen
plugin:@performance/recommended
plugin:@performance/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
