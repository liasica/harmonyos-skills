---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-brace-style-stylistic
title: @hw-stylistic/brace-style
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > ArkTS代码风格规则@hw-stylistic > @hw-stylistic/brace-style
category: harmonyos-guides
scraped_at: 2026-04-28T07:56:25+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:7955798c341f42891705223396ff2ee06e69f81ca8b035c8e88e5e05b0ffbe73
---

强制大括号和语句位于同一行。该规则仅检查.ets文件类型。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@hw-stylistic/brace-style": "error"
5. }
6. }
```

## 选项

该规则无需配置额外选项。

## 正例

```
1. try {
2. // doSomething
3. } catch (e) {
4. // doSomething
5. } finally {
6. // doSomething
7. }
```

## 反例

```
1. try
2. // Opening curly brace does not appear on the same line as statement before.
3. {

5. // Closing curly brace does not appear on the same line as statement after.
6. }
7. catch (e)
8. // Opening curly brace does not appear on the same line as statement before.
9. {

11. // Closing curly brace does not appear on the same line as statement after.
12. }
13. finally
14. // Opening curly brace does not appear on the same line as statement before.
15. {

17. }
```

## 规则集

```
1. "plugin:@hw-stylistic/recommended"
2. "plugin:@hw-stylistic/all"
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
