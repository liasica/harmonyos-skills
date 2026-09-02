---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_hp-arkui-use-local-var-to-replace-state-var
title: "@performance/hp-arkui-use-local-var-to-replace-state-var"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 性能规则@performance > @performance/hp-arkui-use-local-var-to-replace-state-var
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:52+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:836016bd30b375033a3a79e9a0ce62eb4dda3af5d2ba78c936ae64c253f38ad4
---

建议使用临时变量替换状态变量。

通用丢帧场景下，建议优先修改。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@performance/hp-arkui-use-local-var-to-replace-state-var": "warn",
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
  @State message: string = '';
  appendMsg(newMsg: string) {
      let message = this.message;
      message += newMsg;
      message += ";";
      message += "<br/>";
      this.message = message;
  }
  build() {
    // 业务代码...
  }
}
```

## 反例

```screen
@Entry
@Component
struct MyComponent {
  @State message: string = '';
  appendMsg(newMsg: string) {
      this.message += newMsg;
      this.message += ";";
      this.message += "<br/>";
  }
  build() {
    // 业务代码...
  }
}
```

## 规则集

```screen
plugin:@performance/recommended
plugin:@performance/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
