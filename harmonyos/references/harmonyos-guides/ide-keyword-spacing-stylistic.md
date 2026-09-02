---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-keyword-spacing-stylistic
title: "@hw-stylistic/keyword-spacing"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > ArkTS代码风格规则@hw-stylistic > @hw-stylistic/keyword-spacing
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:53+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:4d9d6b17ffa74ea8bdf3491f4242b4edc29dbc8f9d52e5d1bf567ad312308e7c
---

在关键字前后强制加空格。该规则仅检查.ets文件类型。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@hw-stylistic/keyword-spacing": "error"
  }
}
```

## 选项

该规则无需配置选项。

## 正例

```screen
export function test(a: number, b: number) {
  if (a > b) {
    console.info('doSomething');
  } else if (a === b) {
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

```screen
export function test(a: number, b: number) {
  // Expected space after 'if'.
  if(a > b) {
    console.info('doSomething');
  // Expected space before 'else'.
  // Expected space after 'if'.
  }else if(a === b) {
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

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
