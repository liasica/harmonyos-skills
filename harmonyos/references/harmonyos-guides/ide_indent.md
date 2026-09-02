---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_indent
title: "@hw-stylistic/indent"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > ArkTS代码风格规则@hw-stylistic > @hw-stylistic/indent
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:53+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:3e911db83eb4bbdbc0ebf5175faeeb6784149a6b8a20874dd0d4c78acb6e28c9
---

强制switch语句中的case和default缩进一层。该规则仅检查.ets文件类型。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@hw-stylistic/indent": "error"
  }
}
```

## 选项

该规则无需配置选项。

## 正例

```screen
enum E {
  a = 'a',
  b = 'b',
  c = 'c'
}

export function test(e: E) {
  switch (e) {
    case E.a:
      console.info('doSomething');
      break;
    case E.b:
    case E.c:
      console.info('doSomething');
      break;
    default:
      console.info('doSomething');
  }
}
```

## 反例

```screen
enum E {
  a = 'a',
  b = 'b',
  c = 'c'
}

export function test(e: E) {
  switch (e) {
      // Expected indentation of 2 relative to switch.
      case E.a:
      // Expected indentation of 2 relative to case.
      console.info('hello');
      // Expected indentation of 2 relative to case.
      break;
    case E.b:
      console.info('hello');
      break;
    case E.c:
    // Expected indentation of 2 relative to case.
    console.info('hello');
      break;
    default:
    // Expected indentation of 2 relative to default.
    console.info('hello');
  }
}
```

## 规则集

```screen
"plugin:@hw-stylistic/recommended"
"plugin:@hw-stylistic/all"
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
