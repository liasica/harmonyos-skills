---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-bad-deep-clone-check
title: "@performance/bad-deep-clone-check"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 性能规则@performance > @performance/bad-deep-clone-check
category: harmonyos-guides
scraped_at: 2026-09-02T15:00:22+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:1a2d79f0cd161d2b0502542cf49c679f9c9d99af8de5fb25e5610f2b00ac29c2
---

避免使用不合理深拷贝，如JSON.parse(JSON.stringify(foo))和\_.cloneDeep(foo)。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@performance/bad-deep-clone-check": "warn",
  }
}
```

## 选项

```screen
"@performance/bad-deep-clone-check": [
      1,
      {
        "functions": [
          "utils.clone"
        ]
      }
    ]
```

## 正例

**说明** 

正例的深拷贝实现仅作为示例，开发者需根据业务实际情况确认是否使用该实现。

* 该示例实现不支持函数和文档对象模型（Document Object Model）元素的拷贝。函数通常不需要深拷贝。
* 对于复杂的对象结构，使用该示例性能可能受到影响。
* 对于大型的自定义对象结构，可以使用结构化克隆算法（Structured Clone）或Web Worker。

```screen
// deepClone.ts
type Cloneable = object | Array<any> | Map<any, any> | Set<any> | Date | RegExp;

export function deepClone<T extends Cloneable>(source: T, weakMap = new WeakMap()): T {
  // 处理原始类型和函数
  if (typeof source !== 'object' || source === null) {
    return source;
  }
  // 处理循环引用
  if (weakMap.has(source)) {
    return weakMap.get(source);
  }
  // 处理特殊对象类型
  if (source instanceof Date) {
    return new Date(source) as T;
  }
  if (source instanceof RegExp) {
    return new RegExp(source.source, source.flags) as T;
  }
  // 处理数组
  if (Array.isArray(source)) {
    const cloneArr: any[] = [];
    weakMap.set(source, cloneArr);
    for (const item of source) {
      cloneArr.push(deepClone(item, weakMap));
    }
    return cloneArr as T;
  }
  // 处理Map
  if (source instanceof Map) {
    const cloneMap = new Map();
    weakMap.set(source, cloneMap);
    for (const [key, value] of source) {
      cloneMap.set(deepClone(key, weakMap), deepClone(value, weakMap));
    }
    return cloneMap as T;
  }
  // 处理Set
  if (source instanceof Set) {
    const cloneSet = new Set();
    weakMap.set(source, cloneSet);
    for (const value of source) {
      cloneSet.add(deepClone(value, weakMap));
    }
    return cloneSet as T;
  }
  // 处理普通对象
  const cloneObj = Object.create(Object.getPrototypeOf(source));
  weakMap.set(source, cloneObj);
  // 使用Object.getOwnPropertyDescriptors获取所有属性描述符
  const descriptors = Object.getOwnPropertyDescriptors(source);

  for (const [key, descriptor] of Object.entries(descriptors)) {
    if (descriptor.value !== undefined) {
      descriptor.value = deepClone(descriptor.value, weakMap);
    }
    Object.defineProperty(cloneObj, key, descriptor);
  }
  // 处理Symbol属性
  const symbolKeys = Object.getOwnPropertySymbols(source);
  for (const key of symbolKeys) {
    cloneObj[key] = deepClone(source[key as any], weakMap);
  }
  return cloneObj;
}
```

```screen
//example.ts
import { deepClone } from './deepClone';

// 使用示例
const obj = {
  a: 1,
  b: [2, 3],
  c: { d: 4 },
  e: new Date(),
  f: new Map([['key', 'value']]),
  g: new Set([1, 2, 3]),
  h: /regexp/gim
};
const cloned = deepClone(obj);
```

## 反例

```screen
import _ from 'lodash';
/**
* 下载lodash依赖：
* 1、ohpm install lodash
* 2、ohpm install @types/lodash --save-dev
*/
interface Foo {
id: number;
name: string;
}
const foo:Foo = {
id:1,
name:"aa"
}
const clone1:Foo = JSON.parse(JSON.stringify(foo)) as Foo;
const clone2:Foo = _.cloneDeep(foo);
```

## 规则集

```screen
plugin:@performance/recommended
plugin:@performance/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
