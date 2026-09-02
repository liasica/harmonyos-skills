---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_hp-arkui-use-word-break-in-space
title: "@performance/hp-arkui-use-word-break-to-replace-zero-width-space"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 性能规则@performance > @performance/hp-arkui-use-word-break-to-replace-zero-width-space
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:52+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:7188e7a2b2cba73aaebc7fca590c171386410a16c6c79b195a4eade8c90a1310
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

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
