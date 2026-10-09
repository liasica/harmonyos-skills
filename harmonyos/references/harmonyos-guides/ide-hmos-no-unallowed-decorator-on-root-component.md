---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-no-unallowed-decorator-on-root-component
title: "@previewer/no-unallowed-decorator-on-root-component"
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 预览规则@previewer > @previewer/no-unallowed-decorator-on-root-component
category: harmonyos-guides
scraped_at: 2026-10-09T08:15:32+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:7ed145818274051035cd75280e9dda45f457b5db6ad6037529f4d99ce1c3cbae
---

对于@Entry组件，不允许使用@Consume、@Link、@ObjectLink、@Prop注解；对于@Preview组件，建议使用一个定义了完整的、合法的、不依赖运行时的默认值的父组件作为预览该组件的容器。

## 规则配置

```json
// code-linter.json5
{
  "rules": {
    "@previewer/no-unallowed-decorator-on-root-component": "warn"
  }
}
```

## 选项

该规则无需配置额外选项。

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

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-hmos-code-linter.md)。
