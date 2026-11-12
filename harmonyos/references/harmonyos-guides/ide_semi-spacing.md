---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_semi-spacing
title: "@hw-stylistic/semi-spacing"
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > ArkTS代码风格规则@hw-stylistic > @hw-stylistic/semi-spacing
category: harmonyos-guides
scraped_at: 2026-11-12T09:52:59+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:a36c6ab76f8e03c102202aff53e3908105134ba4f028f72550da153baa5be8f4
---

强制分号之前不加空格。该规则仅检查.ets文件类型。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@hw-stylistic/semi-spacing": "error"
  }
}
```

## 选项

该规则无需配置选项。

## 正例

```screen
export {x, test, C};

const x = 10;

function test(size: number): number {
  let sum = 0;
  for (let a = 0; a < size; a++) {
    sum += a;
  }
  return sum;
}

class C {
  public name: string = 'hello';
}
```

## 反例

```screen
// Unexpected whitespace before semicolon.
export {x, test, C} ;

// Unexpected whitespace before semicolon.
const x = 10 ;

function test(size: number): number {
  let sum = 0;
  // Unexpected whitespace before semicolon.
  // Unexpected whitespace before semicolon.
  for (let a = 0 ; a < size ; a++) {
    sum += a;
  }
  // Unexpected whitespace before semicolon.
  return sum ;
}

class C {
  // Unexpected whitespace before semicolon.
  public name: string = 'hello' ;
}
```

## 规则集

```screen
"plugin:@hw-stylistic/recommended"
"plugin:@hw-stylistic/all"
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查（ArkTS/TS）](ide-code-linter.md)。
