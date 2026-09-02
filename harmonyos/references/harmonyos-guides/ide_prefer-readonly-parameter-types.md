---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_prefer-readonly-parameter-types
title: "@typescript-eslint/prefer-readonly-parameter-types"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/prefer-readonly-parameter-types
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:51+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:45d5f0791fdf2d1dfdf37a813b714342c05d71056791642cfefab3af4b93063e
---

要求将函数参数解析为“只读”类型，以防止参数被修改而产生副作用，更多规则详情请参考[prefer-readonly-parameter-types](https://typescript-eslint.nodejs.cn/rules/prefer-readonly-parameter-types)。

该规则校验比较严格，由开发者自主判断是否需要修复告警。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/prefer-readonly-parameter-types": "warn"
  }
}
```

## 选项

详情请参考[@typescript-eslint/prefer-readonly-parameter-types选项](https://typescript-eslint.nodejs.cn/rules/prefer-readonly-parameter-types/#options)。

## 正例

```screen
const index = 0;
export function array1(arg: readonly string[]): void {
  console.info(`${arg[index]}`);
}

export function array2(arg: readonly (readonly string[])[]): void {
  console.info(`${arg[index][index]}`);
}
export function array3(arg: readonly [string, number]): void {
  console.info(`${arg[index][index]}`);
}

export function array4(arg: readonly [readonly string[], number]): void {
  console.info(`${arg[index][index]}`);
}

export function primitive1(arg: string): void {
  console.info(`${arg}`);
}

export function primitive2(arg: number): void {
  console.info(`${arg}`);
}

export function primitive3(arg: boolean): void {
  console.info(`${arg}`);
}

export function primitive5(arg: null): void {
  console.info(`${arg}`);
}

export function primitive6(arg: undefined): void {
  console.info(`${arg}`);
}
```

## 反例

```screen
const index = 0;
export function array1(arg: string[]): void {
  console.info(`${arg[index]}`);
}

export function array2(arg: (string[])[]): void {
  console.info(`${arg[index][index]}`);
}
export function array3(arg: [string, number]): void {
  console.info(`${arg[index][index]}`);
}

export function array4(arg: [string[], number]): void {
  console.info(`${arg[index][index]}`);
}
```

## 规则集

```screen
plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
