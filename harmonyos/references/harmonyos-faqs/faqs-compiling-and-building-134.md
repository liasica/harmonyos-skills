---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-134
title: 文件没有默认导出，但可以默认导入的场景说明
breadcrumb: FAQ > DevEco Studio > 编译构建 > 文件没有默认导出，但可以默认导入的场景说明
category: harmonyos-faqs
scraped_at: 2026-04-28T08:29:36+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:30584115bfc25fcf1747b35ecc61fe9a890deea771490fc39037de9d1120a8a8
---

**问题现象**

当声明文件没有默认导出时，使用 import xxx from 'module' 导入不会导致编译不会报错。

```
1. // test.d.ts file
2. export const addFunction: {
3. add: (a: number, b: number) => number
4. }
```

[test.d.ts](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/CompilingAndBuilding/library3/src/main/ets/components/test.d.ts#L21-L24)

```
1. // index.ets file
2. import test from './test'

5. test.addFunction.add(1,2)
```

[index.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/CompilingAndBuilding/library3/src/main/ets/components/index.ets#L21-L25)

**原因说明**

此场景编译时不报错，因为配置文件中开启了allowSyntheticDefaultImports选项。该选项不仅允许没有默认导出的声明文件默认导入，还兼容从使用 CommonJS（require）导出模块的库中导入默认导出（default exports），例如可以默认导入像 React 这样的第三方库。

**React 示例：安装 `@types/react` 包，使用默认导入的方式，编译不报错。**

```
1. import  React  from "react";
2. React.useId()
```

[test.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/CompilingAndBuilding/entry/src/main/ets/pages/test.ets#L20-L21)

**CommonJS 示例：用默认导入方式导入 CommonJS 模块**。

```
1. // 编译文件
2. import allFunction from 'library'

4. allFunction.sub(1,2)
```

[allFunction.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/CompilingAndBuilding/entry/src/main/ets/pages/allFunction.ets#L21-L24)

```
1. // 依赖包的实现文件 index.js
2. function sub(a, b) {
3. return a - b
4. }

6. var allFunction = { sub }
7. module.exports = allFunction
```

[index.js](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/CompilingAndBuilding/library/src/main/ets/components/index.js#L21-L27)

**解决方案**

如果源码文件没有默认导出，可以尝试使用import \* as xx from 'xxx'导入。
