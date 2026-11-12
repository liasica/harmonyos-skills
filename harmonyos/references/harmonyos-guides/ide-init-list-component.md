---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-init-list-component
title: "@performance/init-list-component"
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 性能规则@performance > @performance/init-list-component
category: harmonyos-guides
scraped_at: 2026-11-12T09:52:58+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:f3894c9fe2fcce9a97bbe471ec38a176caaad409dd0cb3fa5935157b57c09028
---

List组件在使用时，建议同时定义width和height属性。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@performance/init-list-component": "warn",
  }
}
```

## 选项

该规则无需配置选项。

## 正例

```screen
@Component
struct Greeting {
  @Builder myBuilder() {
    List().width(10).height(10)
  }
  build() {
    List() {
    }.width(10).height(10);
  }
}

@Builder function globalBuilder() {
  List().width(10).height(10)
}
```

## 反例

```screen
@Component
struct Greeting {
  @Builder myBuilder() {
    // missing initialization of attribute 'height'
    List().width(10)
  }
  build() {
    // missing initialization of attribute 'width'
    List().height(10);
  }
}

@Builder function myBuilder() {
  // missing initialization of attribute 'height'
  List().width(10)
}
```

## 规则集

```screen
plugin:@performance/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查（ArkTS/TS）](ide-code-linter.md)。
