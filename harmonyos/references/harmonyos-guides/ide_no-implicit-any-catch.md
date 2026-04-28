---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-implicit-any-catch
title: @typescript-eslint/no-implicit-any-catch
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/no-implicit-any-catch
category: harmonyos-guides
scraped_at: 2026-04-28T07:55:34+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:290cc1d3b6908a125b88ca6a997d7a842148e295987d90ea056b5e03458a353e
---

禁止在 catch 表达式中使用隐式“any”类型。

该规则仅支持对.js/.ts文件进行检查。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@typescript-eslint/no-implicit-any-catch": "error"
5. }
6. }
```

## 选项

该规则默认不允许使用隐式any类型。但是可以接受{"allowExplicitAny": true}对象作为规则参数，以允许使用显式的any类型。

示例：

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@typescript-eslint/no-implicit-any-catch": ["error", {"allowExplicitAny": true}]
5. }
6. }
```

在配置{"allowExplicitAny": true}的条件下，以下代码不会产生告警：

```
1. try {
2. // ...
3. } catch (e: any) {
4. // ...
5. }
```

## 正例

```
1. try {
2. // ...
3. } catch (e: unknown) {
4. // ...
5. }
```

## 反例

```
1. try {
2. // ...
3. // 默认不允许使用隐式any类型
4. } catch (e) {
5. // ...
6. }
```

## 规则集

```
1. plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
