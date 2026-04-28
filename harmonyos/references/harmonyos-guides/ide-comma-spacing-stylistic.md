---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-comma-spacing-stylistic
title: @hw-stylistic/comma-spacing
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > ArkTS代码风格规则@hw-stylistic > @hw-stylistic/comma-spacing
category: harmonyos-guides
scraped_at: 2026-04-28T07:56:25+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:ebd5af4fe98ed73d7475c24bb8ae449de35fa212e786f85367dbc75bdef91c1d
---

强制数组元素和函数中多个参数之间的逗号后面加空格，逗号前不加空格。该规则仅检查.ets文件类型。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@hw-stylistic/comma-spacing": "error"
5. }
6. }
```

## 选项

该规则无需配置额外选项。

## 正例

```
1. export {bar, arr};

3. function bar(param1: string, param2: string) {
4. return [param1, param2];
5. }
6. const arr = ['s1', 's2', 's3', 's4'];
```

## 反例

```
1. export {arr};
2. // A space is required after ','.
3. // There should be no space before ','.
4. const arr = ['s1' ,'s2' ,'s3'];
```

## 规则集

```
1. "plugin:@hw-stylistic/recommended"
2. "plugin:@hw-stylistic/all"
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
