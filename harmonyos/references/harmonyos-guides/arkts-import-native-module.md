---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-import-native-module
title: 静态方式加载Native模块
breadcrumb: 指南 > 应用框架 > ArkTS（方舟编程语言） > ArkTS运行时 > ArkTS模块化 > 静态方式加载Native模块
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:13+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:b5c3ef1fea6480fc3a87f925e163a95696f8b9ca32a6fffad02deda653212ca1
---

在ES6(ECMAScript 6.0)模块设计中，使用import语法加载其他文件导出的内容是ECMA规范所定义的语法规则。为支持开发者使用该功能导入Native模块（so）导出的内容，ArkTS进行了相关适配，并提供了以下三类支持写法：直接导入、间接导入和动态导入。

## 直接导入

在Native模块的Index.d.ts文件中导出，并在文件内直接导入。

### 具名导入

```typescript
// libentry.so对应的Index.d.ts
export const add: (a: number, b: number) => number;
```

```typescript
// NameImport.ets
import { add } from 'libentry.so';
add(2, 3);
```

### 默认导入

```typescript
// libentry.so对应的Index.d.ts
export const add: (a: number, b: number) => number;
```

```typescript
// DefaultImport.ets
import entry from 'libentry.so';
entry.add(2, 3);
```

### 命名空间导入

```typescript
// libentry.so对应的Index.d.ts
export const add: (a: number, b: number) => number;
```

```typescript
// NamespaceImport.ets
import * as entry from 'libentry.so';
entry.add(2, 3);
```

## 间接导入

### 转为具名变量导出再导入

```typescript
// libentry.so对应的Index.d.ts
export const add: (a: number, b: number) => number;
```

```typescript
// NameExport.ets
// 将libentry.so的API封装后导出
import { add } from 'libentry.so';
export { add };
```

```typescript
// NameImportFromExport.ets
// 从中间模块导入API
import { add } from './NameExport';
const result = add(2, 3);
```

### 转为命名空间导出再导入

```typescript
// libentry.so对应的Index.d.ts
export const add: (a: number, b: number) => number;
```

```typescript
// NamespaceExport.ets
export * from 'libentry.so';
```

```typescript
// NamespaceImportFromExport.ets
import { add } from './NamespaceExport';
add(2, 3);
```

**注意** 

不支持在导出端使用命名空间导出（export \*）的同时在导入端使用命名空间导入（import \* as）。

**反例：**

```typescript
// test1.ets
export * from 'libentry.so';
```

```typescript
// test2.ets
import * as lib from './test1'
// 无法获取lib对象
```

## 动态导入

### 直接导入

```typescript
// libentry.so对应的Index.d.ts
export const add: (a: number, b: number) => number;
```

```typescript
// DynamicImport.ets
import('libentry.so').then((entry:ESObject) => {
  entry.default.add(2, 3);
})
```

### 间接导入

```typescript
// DynamicExport.ets
import entry from 'libentry.so';
export { entry }
```

```typescript
// DynamicImportFromExport.ets
import('./DynamicExport').then((ns:ESObject) => {
  ns.entry.add(2, 3);
})
```

**注意** 

不支持动态加载时，导出文件使用命名空间。

**反例：**

```typescript
// test1.ets
export * from 'libentry.so';
```

```typescript
// test2.ets
import('./test1').then((ns:ESObject) => {
    // 无法获取ns对象
})
```
