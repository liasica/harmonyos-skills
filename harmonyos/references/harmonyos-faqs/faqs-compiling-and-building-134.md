---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-134
title: 文件没有默认导出，但可以默认导入的场景说明
breadcrumb: FAQ > DevEco Studio > 编译构建 > 文件没有默认导出，但可以默认导入的场景说明
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:55+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:b5d5b5860d8f4cdbd7ba2c561be0881792372418705b834811f43e8d62f0458e
---

**问题现象**

当声明文件没有默认导出时，使用 import xxx from 'module' 导入不会导致编译报错。

```typescript
// test.d.ts file
export const addFunction: {
  add: (a: number, b: number) => number
}
```

```typescript
// index.ets file
import test from './test'

test.addFunction.add(1,2)
```

**原因说明**

此场景编译时不报错，因为配置文件中开启了allowSyntheticDefaultImports选项。该选项不仅允许没有默认导出的声明文件默认导入，还兼容从使用 CommonJS（require）导出模块的库中导入默认导出（default exports），例如可以默认导入像 React 这样的第三方库。

**React 示例：安装 `@types/react` 包，使用默认导入的方式，编译不报错。**

```typescript
import  React  from "react";
React.useId()
```

**CommonJS 示例：用默认导入方式导入 CommonJS 模块**。

```typescript
// 编译文件
import allFunction from 'library'

allFunction.sub(1,2)
```

```js
// 依赖包的实现文件 index.js
function sub(a, b) {
    return a - b
}

var allFunction = { sub }
module.exports = allFunction
```

**解决方案**

如果源码文件没有默认导出，可以尝试使用import \* as xx from 'xxx'导入。
