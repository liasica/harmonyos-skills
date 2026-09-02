---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_semi-spacing
title: "@hw-stylistic/semi-spacing"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > ArkTS代码风格规则@hw-stylistic > @hw-stylistic/semi-spacing
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:53+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:bda3e36ee3de7b3d01eaaf91135c675665e87ee53660e84c79ffaab1d06bfbaf
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

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
