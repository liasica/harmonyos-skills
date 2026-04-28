---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_hp-arkui-use-word-break-in-space
title: @performance/hp-arkui-use-word-break-to-replace-zero-width-space
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 性能规则@performance > @performance/hp-arkui-use-word-break-to-replace-zero-width-space
category: harmonyos-guides
scraped_at: 2026-04-28T07:56:11+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:9092e6325744c6fc54ce5ef0d4556a3710495216024b3b84e1aa338a4daa3999
---

建议使用word-break替换零宽空格(\u200b)。

根据ArkUI编程规范，建议修改。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@performance/hp-arkui-use-word-break-to-replace-zero-width-space": "suggestion",
5. }
6. }
```

## 选项

该规则无需配置额外选项。

## 正例

```
1. @Component
2. export struct MyComponent {
3. private diskName: string = '';

5. build() {
6. Text(this.diskName)
7. .textAlign(TextAlign.Start)
8. .wordBreak(WordBreak.BREAK_ALL)
9. }
10. }
```

## 反例

```
1. @Component
2. export struct MyComponent {
3. private diskName: string = '';

5. build() {
6. Text(this.diskName.split("").join("\u200B"))
7. .textAlign(TextAlign.Start)
8. }
9. }
```

## 规则集

```
1. plugin:@performance/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
