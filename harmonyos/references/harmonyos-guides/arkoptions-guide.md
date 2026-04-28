---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkoptions-guide
title: 在build-profile.json5中配置arkOptions
breadcrumb: 指南 > 应用框架 > ArkTS（方舟编程语言） > ArkTS编译工具链 > 在build-profile.json5中配置arkOptions
category: harmonyos-guides
scraped_at: 2026-04-28T07:38:51+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:d96105a8fcf0e85e567ee7b0482c97e90181e2fc6160f850e3a92ff2c48c3f42
---

## 概述

arkOptions主要提供ArkTS编译相关配置，当前文档介绍arkOptions中types配置类型、maxFlowDepth配置控制流分析最大深度等，arkOptions中的其他配置项请参考[build-profile.json5](ide-hvigor-configuration-file-overview.md)。

## types

### types配置文件标签说明

arkOptions的types字段配置文件标签说明：

| 属性名称 | 含义 | 配置范围 | 数据类型 | 是否可缺省 |
| --- | --- | --- | --- | --- |
| types | 通过types字段将指定的类型声明文件作为全局引入，从而避免在每个源码文件中单独引入。 | 模块级 | 数组 | 该标签可缺省，缺省值为空。 |

### arkOptions中的types字段配置说明

arkOptions中types字段示例：

在模块build-profile.json5配置文件buildOption标签的arkOptions属性中添加types字段。

```
1. // 在/entry/build-profile.json5
2. "arkOptions": {
3. "types": ["pako", "./oh_modules/@types/mime", "./src/main/ets/pages/global"]
4. },
```

types字段支持填写包名、包所在位置的相对路径，以及声明文件所在位置的相对路径。类型的查找范围仅限于当前声明文件所在的模块内，若目录下存在同名文件（后缀不同），默认加载顺序为 .d.ets > .d.ts，即优先加载 .d.ets 后缀的文件。

1. 填写包名方式：通过包名到oh\_modules/@types/目录查找包名中定义的声明文件，如"pako"。
2. 填写包所在相对路径方式：支持在基于build-profile.json5的相对路径中查找定义的声明文件，如"./oh\_modules/@types/mime"。
3. 填写声明文件所在相对路径方式：支持查找相对路径下的声明文件，如"./src/main/ets/pages/global"。

### 注意事项

如果在types字段中填写包名或者包所在位置的相对路径，需要在工程文件/entry/oh-package.json5中dependencies作如下配置：

```
1. "dependencies": {
2. "@types/pako": "latest",
3. "@types/mime": "latest"
4. }
```

如果在types字段中填写声明文件所在相对路径，前提是在模块下存在相应的声明文件，比如模块下存在src/main/ets/pages/global.d.ts声明文件，声明文件内容如下所示：

```
1. declare namespace Global {
2. type ObjectType = string | number;
3. }
```

通过types全局引入后，对全局类型的使用示例如下：

```
1. // 在entry/src/main/ets/pages/Index.ets
2. let testPako: pako.constants = 0;
3. let testMime: mime.TypeMap = {};
4. let testGlobal: Global.ObjectType = 'test';
```

## maxFlowDepth

### maxFlowDepth配置文件标签说明

arkOptions下tscConfig中maxFlowDepth字段配置文件标签说明：

| 属性名称 | 含义 | 配置范围 | 数据类型 | 是否可缺省 |
| --- | --- | --- | --- | --- |
| maxFlowDepth | 开发者通过maxFlowDepth字段自定义配置tsc编译过程中的tsc控制流分析最大深度，避免固定最大深度导致编译报错问题。该配置项可配置的最小值为2000，可配置最大值为65535。 | 工程级 | 数字型 | 该标签可缺省，缺省值时使用tsc控制流分析最大深度默认值2000。 |

### arkOptions下的tscConfig中maxFlowDepth字段配置说明

arkOptions/tscConfig中maxFlowDepth字段展示。

在工程级目录下的build-profile.json5配置文件buildOption标签的arkOptions/tscConfig属性中添加maxFlowDepth字段。

```
1. // 在工程名/build-profile.json5文件中。
2. "arkOptions": {
3. "tscConfig": {
4. "maxFlowDepth": 2222
5. }
6. }
```

### 注意事项

* 仅可在工程级目录下build-profile.json5文件中配置maxFlowDepth字段。
* 若开发者未对maxFlowDepth字段进行配置时，则该字段默认为2000；若开发者对maxFlowDepth字段配置的值超过可配置范围，则会出现编译构建相关报错。

  ```
  1. hvigor ERROR: Schema validate failed.
  2. Detail: Please check the following fields.
  3. {
  4. instancePath: 'app.products[0].buildOption.arkOptions.tscConfig.maxFlowDepth',
  5. keyword: 'maximum',
  6. params: { comparison: '<=', limit: 65535 },
  7. message: 'must be <= 65535',
  8. location: 'D:/工程名/build-profile.json5:行号:列号'
  9. }
  ```
* 如果代码中函数或者模块过长导致控制流分析深度大于或者等于该字段所配置/默认的值，则会终止控制流分析并且报错：The containing function or module body is too large for control flow analysis.

## transformLib

### transformLib配置文件标签说明

arkOptions的transformLib字段配置文件标签说明：

| 属性名称 | 含义 | 配置范围 | 数据类型 | 是否可缺省 |
| --- | --- | --- | --- | --- |
| transformLib | 字节码插桩插件配置，允许开发者在编译时对字节码进行插桩修改。仅支持Stage模型，格式为相对路径，指向实现插桩功能的动态库。不同系统要求的动态库文件类型如下，动态库文件内容需要在对应平台生成，不能拷贝修改后缀名混用。 | 模块级 | 字符串型 | 该标签可缺省，缺省值时代表不使用该功能。 |

### arkOptions中的transformLib字段配置说明

arkOptions中transformLib字段示例：

在模块build-profile.json5配置文件buildOption标签的arkOptions属性中添加transformLib字段。

```
1. // 在/entry/build-profile.json5
2. {
3. "buildOption": {
4. "arkOptions": {
5. "transformLib": "./dll/example.dll"
6. }
7. }
8. }
```

修改方舟字节码能力可参考[编译期自定义修改方舟字节码](customize-bytecode-during-compilation.md)。

### 注意事项

* 若开发者未对字段进行配置时，则默认不使用该功能。
* HAP、HSP模块配置即生效，HAR模块仅字节码HAR配置生效，非字节码HAR配置不生效。
* 文件格式要求：Windows：.dll文件，Linux/Mac：.so文件。
