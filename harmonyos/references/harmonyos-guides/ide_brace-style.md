---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_brace-style
title: "@typescript-eslint/brace-style"
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/brace-style
category: harmonyos-guides
scraped_at: 2026-11-12T09:52:54+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:c5cd51392fd841335b7428ed2ae7af64a8df5d86f93e904298721134c56ea0c4
---

对代码块强制执行一致的括号样式。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/brace-style": "error"
  }
}
```

## 选项

详情请参考[@typescript-eslint/brace-style选项](https://eslint.nodejs.cn/docs/rules/brace-style#选项)。

## 正例

```screen
function foo(): boolean {
  return true;
}

class C {
  static {
    foo();
  }

  public meth() {
    foo();
  }
}

export { C };
```

## 反例

```screen
function foo(): boolean 
{
  return true;
}

class C {
  static 
  {
    foo();
  }

  public meth() 
  {
    foo();
  }
}

export { C };
```

## 规则集

```screen
plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查（ArkTS/TS）](ide-code-linter.md)。
