---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-keyword-spacing-stylistic
title: "@hw-stylistic/keyword-spacing"
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > ArkTS代码风格规则@hw-stylistic > @hw-stylistic/keyword-spacing
category: harmonyos-guides
scraped_at: 2026-10-09T08:15:33+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:46067b10f9c94020fb4d74b6fa131a4146b073f9ca7c89e80657e3654b198a28
---

在关键字前后强制加空格。该规则仅检查.ets文件类型。

## 规则配置

```json
// code-linter.json5
{
  "rules": {
    "@hw-stylistic/keyword-spacing": "error"
  }
}
```

## 选项

该规则无需配置额外选项。

## 正例

```ts
export function test(a: number, b: number) {
  if (a > b) {
    console.info('doSomething');
  } else if (a = b) {
    console.info('doSomething');
  } else {
    console.info('doSomething');
  }

  for (const item of [a, b]) {
    console.info(`${item}`);
  }
}
```

## 反例

```ts
export function test(a: number, b: number) {
  // Expected space after 'if'.
  if(a > b) {
    console.info('doSomething');
  // Expected space before 'else'.
  // Expected space after 'if'.
  }else if(a = b) {
    console.info('doSomething');
  // Expected space before 'else'.
  // Expected space after 'else'.
  }else{
    console.info('doSomething');
  }

  // Expected space after 'for'.
  for(const item of [a, b]) {
    console.info(`${item}`);
  }
}
```

## 规则集

```screen
"plugin:@hw-stylistic/recommended"
"plugin:@hw-stylistic/all"
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-hmos-code-linter.md)。
