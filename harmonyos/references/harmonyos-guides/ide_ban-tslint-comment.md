---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_ban-tslint-comment
title: @typescript-eslint/ban-tslint-comment
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/ban-tslint-comment
category: harmonyos-guides
scraped_at: 2026-04-28T07:55:23+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:16c1b0da3ab8d2abf3be742b3e77a2cf2889f148e6d7c1330ac3e12af906a731
---

不允许使用`//tslint:<rule-flag>`格式的注释。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@typescript-eslint/ban-tslint-comment": "error"
5. }
6. }
```

## 选项

该规则无需配置额外选项。

## 正例

```
1. // This is a comment that just happens to mention tslint
2. /* This is a multiline comment that just happens to mention tslint */
3. console.log('hello'); // This is a comment that just happens to mention tslint
```

## 反例

```
1. /* tslint:disable */
2. /* tslint:enable */
3. /* tslint:disable:rule1 rule2 rule3... */
4. /* tslint:enable:rule1 rule2 rule3... */
5. // tslint:disable-next-line
6. console.log('hello'); // tslint:disable-line
7. // tslint:disable-next-line:rule1 rule2 rule3...
```

## 规则集

```
1. plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
