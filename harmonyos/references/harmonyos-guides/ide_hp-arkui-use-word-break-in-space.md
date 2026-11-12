---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_hp-arkui-use-word-break-in-space
title: "@performance/hp-arkui-use-word-break-to-replace-zero-width-space"
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 性能规则@performance > @performance/hp-arkui-use-word-break-to-replace-zero-width-space
category: harmonyos-guides
scraped_at: 2026-11-12T09:52:58+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:950c3afeb644e7737791b9a6f5ddae1e48fb04f418214ba1febca6ac13daae26
---

建议使用word-break替换零宽空格(\u200b)。

根据ArkUI编程规范，建议修改。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@performance/hp-arkui-use-word-break-to-replace-zero-width-space": "suggestion",
  }
}
```

## 选项

该规则无需配置选项。

## 正例

```screen
@Component
export struct MyComponent {
  private diskName: string = '';

  build() {
    Text(this.diskName)
      .textAlign(TextAlign.Start)
      .wordBreak(WordBreak.BREAK_ALL)
  }
}
```

## 反例

```screen
@Component
export struct MyComponent {
  private diskName: string = '';

  build() {
    Text(this.diskName.split("").join("\u200B"))
      .textAlign(TextAlign.Start)
  }
}
```

## 规则集

```screen
plugin:@performance/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查（ArkTS/TS）](ide-code-linter.md)。
