---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-monitor-invisible-area-in-image-animation
title: "@performance/monitor-invisible-area-in-image-animation"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 性能规则@performance > @performance/monitor-invisible-area-in-image-animation
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:53+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:59162fadf5fdadc11ccc9546bc4b59a364e7e63895511d344b365a809a2c7e81
---

使用ImageAnimation实现帧动画时，建议显式调用monitorInvisibleArea接口。在动画组件不可见时，会停止动画播放，减少冗余动画带来的负载恶化。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@performance/monitor-invisible-area-in-image-animation": "warn",
  }
}
```

## 选项

该规则无需配置选项。

## 正例

```screen
@Entry
@Component
struct ImageAnimatorTest {
  @State message: string = 'hello world';
  build() {
    Column() {
      ImageAnimator()
        .images([])
        .borderRadius(10)
        .monitorInvisibleArea(true)
      test1()
    }
    .width('100%')
  }
}
@Builder
function test1() {
  ImageAnimator()
    .monitorInvisibleArea(true)
}
```

## 反例

```screen
@Entry
@Component
struct ImageAnimatorTest {
  @State message: string = 'hello world';
  build() {
    Column() {
      ImageAnimator()
        .images([])
        .borderRadius(10)
      test1()
    }
    .width('100%')
  }
}
@Builder
function test1() {
  ImageAnimator()
    .images([])
    .borderRadius(10)
}
```

## 规则集

```screen
plugin:@performance/recommended
plugin:@performance/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
