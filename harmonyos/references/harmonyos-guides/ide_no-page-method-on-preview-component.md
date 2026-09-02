---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-page-method-on-preview-component
title: "@previewer/no-page-method-on-preview-component"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 预览规则@previewer > @previewer/no-page-method-on-preview-component
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:53+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:0705dfd0dd1d8cade4771420fa2b53b439e0125e03ac3d489a23ac0e1d3f59ff
---

禁止在非路由组件上实例化onPageShow、onPageHide、onBackPress等页面级方法。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@previewer/no-page-method-on-preview-component": "warn"
  }
}
```

## 选项

该规则无需配置选项。

## 正例

```screen
@Entry
@Component
struct Index {
  @State message: string = 'Hello World';
  onPageShow(): void {}
  onPageHide(): void {}
  onBackPress(): void {}
  build() {
    Row() {
      Column() {
        Text(this.message)
      }
    }
  }
}
```

## 反例

```screen
@Preview
@Component
struct Index {
  @State message: string = 'Hello World';
  onPageShow(): void {}
  onPageHide(): void {}
  onBackPress(): void {}
  build() {
    Column() {
      Text(this.message)
    }
  }
}
```

## 规则集

```screen
plugin:@previewer/recommended
plugin:@previewer/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
