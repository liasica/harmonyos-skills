---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-import-native-module
title: 静态方式加载Native模块
breadcrumb: 指南 > 应用框架 > ArkTS（方舟编程语言） > ArkTS运行时 > ArkTS模块化 > 静态方式加载Native模块
category: harmonyos-guides
scraped_at: 2026-04-28T07:38:45+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:9e3b065771f6e445558ee40ac46d9a3575c412afdac178165f2162a47750c3a4
---

在ES6(ECMAScript 6.0)模块设计中，使用import语法加载其他文件导出的内容是ECMA规范所定义的语法规则。为支持开发者使用该功能导入Native模块（so）导出的内容，ArkTS进行了相关适配，并提供了以下几种支持写法。

## 直接导入

在Native模块的index.d.ts文件中导出，并在文件内直接导入。

### 具名导入

```
1. // libentry.so对应的index.d.ts。
2. export const add: (a: number, b: number) => number;
```

```
1. // NameImport.ets
2. import { add } from 'libentry.so'
3. add(2, 3);
```

### 默认导入

```
1. // libentry.so对应的index.d.ts。
2. export const add: (a: number, b: number) => number;
```

```
1. // DefaultImport.ets
2. import entry from 'libentry.so'
3. entry.add(2, 3);
```

### 命名空间导入

```
1. // libentry.so对应的index.d.ts。
2. export const add: (a: number, b: number) => number;
```

```
1. // NamespaceImport.ets
2. import * as entry from 'libentry.so'
3. entry.add(2, 3);
```

## 间接导入

### 转为具名变量导出再导入

```
1. // libentry.so对应的index.d.ts。
2. export const add: (a: number, b: number) => number;
```

```
1. // NameExport.ets
2. // 将libentry.so的API封装后导出
3. import { add } from 'libentry.so';
4. export { add };
```

```
1. // NameImportFromExport.ets
2. // 从中间模块导入API
3. import { add } from './NameExport';
4. const result = add(2, 3);
```

### 转为命名空间导出再导入

```
1. // libentry.so对应的index.d.ts。
2. export const add: (a: number, b: number) => number;
```

```
1. // NamespaceExport.ets
2. export * from 'libentry.so'
```

```
1. // NamespaceImportFromExport.ets
2. import { add } from './NamespaceExport'
3. add(2, 3);
```

注意

不支持Native模块导出和导入同时使用命名空间。

**反例：**

```
1. // test1.ets
2. export * from 'libentry.so'
```

```
1. // test2.ets
2. import * as add from './test1'
3. // 无法获取add对象
```

## 动态导入

### 直接导入

```
1. // libentry.so对应的index.d.ts。
2. export const add: (a: number, b: number) => number;
```

```
1. // DynamicImport.ets
2. import('libentry.so').then((entry:ESObject) => {
3. entry.default.add(2, 3);
4. })
```

### 间接导入

```
1. // DynamicExport.ets
2. import entry from 'libentry.so'
3. export { entry }
```

```
1. // DynamicImportFromExport.ets
2. import('./DynamicExport').then((ns:ESObject) => {
3. ns.entry.add(2, 3);
4. })
```

注意

不支持动态加载时，导出文件使用命名空间。

**反例：**

```
1. // test1.ets
2. export * from 'libentry.so'
```

```
1. // test2.ets
2. import('./test1').then((ns:ESObject) => {
3. // 无法获取ns对象
4. })
```
