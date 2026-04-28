---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-125
title: 如何解决第三方包require语句报错
breadcrumb: FAQ > DevEco Studio > 编译构建 > 如何解决第三方包require语句报错
category: harmonyos-faqs
scraped_at: 2026-04-28T08:29:34+08:00
doc_updated_at: 2026-03-17
content_hash: sha256:1d32073da1d3bfd4fc722fa599d4603ef425fb38312a8c721d2809696501b40c
---

**问题现象**

引入第三方包时，编译出现错误。

**报错原因**

部分第三方包由npm迁移而来，其开发环境为Node。其中的require语法ArkCompiler不完全支持，导致运行时出现错误。

**场景1**：

```
1. // Module/src/test.json
2. {a: 1, b: 2}
3. //use.js
4. let test = require("Module/src/test.json")
```

**需修改为：**

// Module/src/test.json

```
1. module.exports = {a: 1, b: 2}
```

[test.js](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/CompilingAndBuilding/entry/src/test.js#L18-L18)

//use.js

```
1. let test = require("Module/src/test")
```

[use.js](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/CompilingAndBuilding/entry/src/use.js#L18-L18)

**场景2：**

```
1. // Module/package.json
2. ...
3. main: "./src"
4. ...
5. // use.js
6. let module = require("Module")
```

**需修改为：**

// Module/package.json

```
1. "main": "./src/index.js",
```

[oh-package.json5](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/CompilingAndBuilding/entry/oh-package.json5#L7-L7)

// use.js

```
1. let module = require("Module")
```

[use.js](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/CompilingAndBuilding/entry/src/use.js#L22-L22)

**场景3：**

编译时出现警告信息：

```
1. Plugin node-resolve: preferring built-in module 'util' over local alternative at '/Users/~/Documents/fe-module/demo/node_modules/util/util.js', pass 'preferBuiltins: false' to disable this behavior or 'preferBuiltins: true' to disable this warning
```

**解决方案**

修改rollup.config.js中的preferBuiltins字段。

```
1. plugins: [
2. resolve({
3. preferBuiltins: false,    // true or false
4. mainFields: ['module', 'main'],
5. extensions
6. })
7. ];
```

[rollup.config.js](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/CompilingAndBuilding/entry/src/rollup.config.js#L18-L24)

**场景4：**

```
1. import {Buffer} from 'buffer'
```

**需修改为：**

```
1. import {Buffer} from 'buffer/'
```

[use.js](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/CompilingAndBuilding/entry/src/use.js#L26-L26)
