---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_space-before-blocks
title: "@hw-stylistic/space-before-blocks"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > ArkTS代码风格规则@hw-stylistic > @hw-stylistic/space-before-blocks
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:53+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:a5d689aef7906bbc52b9bddcee004db6d4d715f835f9114f8bd05ccdc371613a
---

强制在“{”之前加空格。该规则仅检查.ets文件类型。

例外：

* 函数的第一个参数或者数组中的第一个元素是对象，对象的“{”之前不用加空格。
* 模板代码中的“{”之前不用加空格。
* 行首的“{”之前不用加空格。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@hw-stylistic/space-before-blocks": "error"
  }
}
```

## 选项

该规则无需配置选项。

## 正例

```screen
export function a() {
  // doSomething
}

@Entry
@Component
struct Index {
  build() {
    Row() {
      Column() {
        Text('Hello World')
      }
      .width('100%')
    }
    .height('100%')
  }
}
```

## 反例

```screen
// Missing space before opening brace.
export function a(){
  // doSomething
}

@Entry
@Component
// Missing space before opening brace.
struct Index{
  // Missing space before opening brace.
  build(){
    // Missing space before opening brace.
    Row(){
      // Missing space before opening brace.
      Column(){
        Text('Hello World')
      }
      .width('100%')
    }
    .height('100%')
  }
}
```

## 规则集

```screen
"plugin:@hw-stylistic/recommended"
"plugin:@hw-stylistic/all"
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
