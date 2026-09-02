---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_brace-style
title: "@typescript-eslint/brace-style"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/brace-style
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:50+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:7884c9acbd6ac87583888a65f41a2f3d546b8380f51f25b410b731a8822d8739
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

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
