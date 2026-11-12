---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-unallowed-decorator-on-root-component
title: "@previewer/no-unallowed-decorator-on-root-component"
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 预览规则@previewer > @previewer/no-unallowed-decorator-on-root-component
category: harmonyos-guides
scraped_at: 2026-11-12T09:52:59+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:ccfd81de509b072892011042570d3db5bbf1773fe98e2d51db818891d0983b2e
---

不允许直接预览包含@Consume、@Link、@ObjectLink、@Prop等装饰器的子组件；建议使用一个定义了完整的、合法的、不依赖运行时的默认值的父组件，并查看此父组件中子组件的预览效果。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@previewer/no-unallowed-decorator-on-root-component": "warn"
  }
}
```

## 选项

该规则无需配置选项。

## 正例

```screen
@Entry
@Component
struct LinkSampleContainer {
  @State message: string = 'Hello World';
  build() {
    Row() {
      LinkSample({message: this.message})
    }
  }
}
@Component
struct LinkSample {
  @Link message: string;
  build() {
    Row() {
      Text(this.message)
    }
  }
}
```

## 反例

```screen
@Preview
@Component
struct LinkSample {
  @Link message: string;
  build() {
    Row() {
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

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查（ArkTS/TS）](ide-code-linter.md)。
