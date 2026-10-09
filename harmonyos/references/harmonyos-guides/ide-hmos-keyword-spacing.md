---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-keyword-spacing
title: "@typescript-eslint/keyword-spacing"
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/keyword-spacing
category: harmonyos-guides
scraped_at: 2026-10-09T08:15:29+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:0fa720bf2732ebfcfa64c232efe5185c3d8107b3d66dcbf2c0e9654ff747b335
---

强制在关键字之前和关键字之后保持一致的空格风格。

## 规则配置

```json
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/keyword-spacing": "error"
  }
}
```

## 选项

详情请参考[@typescript-eslint/keyword-spacing选项](https://eslint.nodejs.cn/docs/rules/keyword-spacing#选项)。

## 正例

```ts
function isSatisfy1(): boolean {
  return true;
}

function isSatisfy2(): boolean {
  return false;
}
// 默认关键字前至少需要一个空格，关键字后至少需要一个空格
if (isSatisfy1()) {
  //...
} else if (isSatisfy2()) {
  //...
} else {
  //...
}
```

## 反例

```ts
function isSatisfy1(): boolean {
  return true;
}

function isSatisfy2(): boolean {
  return false;
}
// 默认关键字前至少需要一个空格，关键字后至少需要一个空格
if (isSatisfy1()) {
  //...
}else if(isSatisfy2()) {
  //...
}else{
  //...
}
```

## 规则集

```screen
plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-hmos-code-linter.md)。
