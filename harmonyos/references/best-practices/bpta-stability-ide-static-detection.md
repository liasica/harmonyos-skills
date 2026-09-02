---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-stability-ide-static-detection
title: 使用DevEco Studio静态检测编码规范
breadcrumb: 最佳实践 > 稳定性 > 稳定性优化 > 稳定性编码规范 > 使用DevEco Studio静态检测编码规范
category: best-practices
scraped_at: 2026-09-02T15:03:24+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:95181f0b45e95147ff576342410d4cfb4a1d5541943903e5990b998cbf3fcad5
---

## 使用Clang-Tidy检测

**自定义配置**

DevEco Studio集成了开源的Clang-Tidy。

1. 开发者可以在Setting -> Editor -> Inspections页面，选择CPP -> clang-tidy的配置页进行Clang-Tidy Checks配置，如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/7_L2jZ6ZSSeSPMgl4gJbLQ/zh-cn_image_0000002194009836.png)

2. 开发者可以在Setting -> Languages & Frameworks -> C/C++中进行Clang-Tidy Checks配置，勾选“Use clang-tidy via clangd to enable the following checks”，然后配置规则，如下图所示

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/-LWEeF6ETJ-Ag6eZiZHPdA/zh-cn_image_0000002229335633.png)

配置参考文档：

<https://clang.llvm.org/extra/clang-tidy/#using-clang-tidy>

**DevEco Studio默认检查规则**

1. 需触发按钮 Code -> Inspect Code -> Analyze

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/ZX5YWCWfQpGBviztBxPQXw/zh-cn_image_0000002229335613.png)

2. 实时触发的规则如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/ri7LR4JlQLKtURk28RJO8w/zh-cn_image_0000002229450133.png)

**DevEco Studio默认检查规则检查示例**

1. 手动检查代码，示例中不符合检查规则“clang-analyzer-huawei-InfiniteLoopChecker”

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/jAqhrRHYSGm0Lws3_oeUag/zh-cn_image_0000002193850236.png)

2. 实时检查，示例中不符合检查规则“misc-unused-local-variable”

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/CyKZOp2CTmO0HQA11fWwcw/zh-cn_image_0000002194009820.png)

**默认配置检查内容**

|  |  |
| --- | --- |
| **默认配置类型** | **检测问题** |
| clang-analyzer-unix.MismatchedDeallocator | 用于检测不匹配的内存释放问题。例如，如果使用malloc分配了内存，却错误地使用了delete或free来释放。 |
| clang-analyzer-huawei.InfiniteRecursiveChecker | 用于检测可能导致无限递归的问题。无限递归可能会导致栈溢出等问题。 |
| clang-analyzer-huawei.InfiniteGotoChecker | 用于检测可能导致无限循环的goto语句。无限循环可能会导致程序卡死或资源耗尽。 |
| clang-analyzer-huawei.InfiniteLoopChecker | 用于检测可能导致无限循环的循环结构。无限循环可能会导致程序卡死或资源耗尽。 |
| clang-analyzer-core.StackAddressEscape | 用于检测栈内存地址逃逸的问题。栈内存地址逃逸可能会导致安全问题，例如缓冲区溢出攻击。 |
| clang-analyzer-core.ArrayBoundV2 | 用于检测数组越界的问题。数组越界可能会导致未定义行为，包括程序崩溃或数据损坏。 |
| misc-missing-switch-cases | 确保switch语句覆盖所有枚举值，并且包含default分支。 |
| misc-napi-module-name | 用于检查Node.js N-API模块的命名是否符合规范。 |
| misc-replace-if-else-with-ternary-operator | 用于建议将简单的if-else语句替换为三元运算符（ternary operator），以提高代码的简洁性。 |
| misc-unused-local-variable | 用于检测并报告代码中未使用的局部变量。未使用的局部变量会导致代码冗余并降低可读性。 |
| misc-unused-parameters | 用于检测并报告函数中未使用的参数。未使用的参数会导致代码冗余并降低可读性。 |
| modernize-use-auto | 用于建议在适当的情况下使用auto关键字来简化代码。使用auto可以减少重复的类型声明，使代码更加简洁和易读。 |
| readability-system-capabilities | 用于检测代码中对系统功能或库的使用是否符合最佳实践。这个规则通常会检查代码是否正确使用了系统提供的功能，以及是否有更好的替代方案。 |

## 使用CodeLinter检测

**Code Linter代码检查**

DevEco Studio集成了Code Linter，用于针对ArkTS/TS代码进行最佳实践/编程规范方面的检查。检查规则支持配置，配置方式请参考[配置代码检查规则](../harmonyos-guides/ide-code-linter.md#section19310459444)。

根据扫描结果中的告警提示，开发者可以手工修复代码缺陷，也可以执行一键式自动修复。这有助于在代码开发阶段确保代码质量。

检查方法：

在已打开的代码编辑器窗口中，单击右键选择Code Linter，或在工程管理窗口中选中单个或多个文件/目录，右键选择Code Linter > Full Linter执行全量代码检查。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/VCDzUa4gSUioFF-8xCZkXA/zh-cn_image_0000002194009856.png)

如需对Git工程中的增量文件（新增、修改、重命名）进行检查，可在commit界面右下角点击齿轮图标，选择Incremental Linter执行增量检查。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/sfOe5p23TRO1fCNZWJRExw/zh-cn_image_0000002193850228.png)

**说明** 

* 若未配置代码检查规则文件，直接执行Code Linter，将按照默认的编程规范规则对.ets文件进行检查。
* Code Linter不对如下文件及目录进行检查：
  + src/ohosTest文件夹
  + src/test文件夹
  + node\_modules文件夹
  + oh\_modules文件夹
  + build文件夹
  + .preview文件夹
  + hvigorfile.ts文件
  + hvigorfile.js文件

**配置代码检查规则**

在工程根目录下创建code-linter.json5配置文件，可以配置代码检查的范围及生效的检查规则。其中，files和ignore配置项共同确定代码检查范围，ruleSet和rules配置项共同确定生效的规则范围。具体配置项功能如下：

files：配置待检查的文件名单，如未指定目录，将检查当前选中的所有.ets文件。

ignore：配置无需检查的文件目录，指定的目录或文件需使用相对于code-linter.json5所在工程根目录的相对路径，例如：build/\*\*/\*。

ruleSet：配置检查使用的规则集，规则集支持一次导入多条规则。规则详情请参见[Code Linter代码检查规则](../harmonyos-guides/ide-codelinter-rule.md)。目前支持的规则集包括：

* 通用规则@typescript-eslint
* 一次开发多端部署规则@cross-device-app-dev
* ArkTS代码风格规则@hw-stylistic
* 安全规则@security
* 性能规则@performance
* 预览规则@previewer

**说明** 

* 以上规则集均分为all和recommended两种规则集。all规则集是规则全集，包含所有规则；recommended规则集是推荐使用的规则集合。recommended规则集是all规则集的子集。
* 不在工程根目录新建code-linter.json5文件的情况下，Code Linter默认会检查@performance/recommended和@typescript-eslint/recommended规则集包含的规则。

rules：可以基于ruleSet配置的规则集，新增额外规则项，或修改ruleSet中规则默认配置，例如：将规则集中某条规则告警级别由warn改为error。

overrides：针对工程根目录下的部分特定目录或文件，可以配置定制化的检查规则。

```screen
{
  "files":   // 用于表示配置适用的文件范围的glob模式数组。在没有指定的情况下，应用默认配置
  [
    "**/*.js", // 字符串类型
    "**/*.ts"
  ],
  "ignore":  // 一个表示配置对象不应适用的文件的glob模式数组。如果没有指定，配置对象将适用于所有由files匹配的文件
  [
    "build/**/*",    // 字符串类型
    "node_modules/**/*"
  ],
  "ruleSet":       // 设置检查待应用的规则集
  [
    "plugin:@typescript-eslint/recommended"    // 快捷批量引入的规则集, 枚举类型：plugin:@typescript-eslint/all, plugin:@typescript-eslint/recommended, plugin:@cross-device-app-dev/all, plugin:@cross-device-app-dev/recommended等
  ],
  "rules":         // 可以对ruleSet配置的规则集中特定的某些规则进行修改、去使能, 或者新增规则集以外的规则；ruleSet和rules共同确定了代码检查所应用的规则
  {
    "@typescript-eslint/no-explicit-any":  // ruleId后面跟数组时, 第一个元素为告警级别, 后面的对象元素为规则特定开关配置
    [
      "error",              // 告警级别: 枚举类型, 支持配置为suggestion, error, warn, off
      {
        "ignoreRestArgs": true   // 规则特定的开关配置, 为可选项, 不同规则其下层的配置项不同
      }
    ],
    "@typescript-eslint/explicit-function-return-type": 2,   // ruleId后面跟单独一个数字时, 表示仅设置告警级别, 枚举值为: 3(suggestion), 2(error), 1(warn), 0(off)
    "@typescript-eslint/no-unsafe-return": "warn"            // ruleId后面跟单独一个字符串时, 表示仅设置告警级别, 枚举值为: suggestion, error, warn, off
  },
  "overrides":      // 针对特定的目录或文件采用定制化的规则配置
  [
    {
      "files":   // 指定需要定制化配置规则的文件或目录
      [
        "entry/**/*.ts"   // 字符串类型
      ],
      "excluded":
      [
       "entry/**/*.test.js" // 指定需要排除的目录或文件, 被排除的目录或文件不会按照定制化的规则配置被检查; 字符串类型
      ],
      "rules":   // 支持对overrides外公共配置的规则进行修改、去使能, 或者新增公共配置以外的规则; 该配置将覆盖公共配置
      {
        "@typescript-eslint/explicit-function-return-type":  // ruleId: 枚举类型
        [
          "warn",     // 告警级别: 枚举类型, 支持配置为error, warn, off; 覆盖公共配置, explicit-function-return-type告警级别为warn
          {
             allowExpressions: true    // 规则特定的开关配置, 为可选项, 不同规则其下层的配置项不同
          }
        ],
        "@typescript-eslint/no-unsafe-return": "off"   // 覆盖公共配置, 不检查no-unsafe-return规则
      }
    }
  ]
}
```

**查看/处理代码检查结果**

扫描完成后，在底部工具面板查看检查结果。勾选Defects中的告警等级，查看对应告警信息。双击告警结果，跳转到代码缺陷位置。选中告警结果时，右侧Defect Description窗口显示规则详细说明。搜索规则时，可设定全词匹配和大小写敏感。

单击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/TQeuDaN1R0qYWIFC_wh2_A/zh-cn_image_0000002194009816.png)图标，查看可修复的代码规则，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/VGzRJF9fTIipwVhnd1AJMw/zh-cn_image_0000002229335641.png)代码修复图标，可以一键式批量修复告警，并刷新检查结果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/suRyR5wSQji4prsMsddxCg/zh-cn_image_0000002194009860.png)屏蔽告警信息：

* 在某些特殊场景下，若扫描结果中出现误报，点击单条告警结果后的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/kNmCfKSLQWGmfwa8wy9f_Q/zh-cn_image_0000002193850240.png)Ignore图标，可以忽略对告警所在行的code linter检查；或勾选文件名称或多条待屏蔽的告警，点击左侧工具面板Ignore图标批量执行操作；
* 在文件顶部添加注释/\* eslint-disable \*/可以屏蔽整个文件执行code linter检查，在eslint-disable 后加入一个或多个以逗号分隔的规则Id，可以屏蔽具体检查规则；
* 在需要忽略检查的代码块前后分别添加/\* eslint-disable \*/和/\* eslint-enable \*/添加注释信息，再执行Code Linter，将不再显示该代码块扫描结果；在待屏蔽的代码行前一行添加/\* eslint-disable-next-line \*/，也可屏蔽对该代码行的codelinter检查。

如需恢复忽略的报错信息，删除该行上方的注释，然后重新执行Code Linter检查。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/TmnrN-0FSZ-Ayg_c5-jgXg/zh-cn_image_0000002194009844.png)

导出检查结果：点击工具面板左侧![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/NlfLXSpZTzyu0yxOKb29VA/zh-cn_image_0000002229450101.png)导出按钮，即可导出检查结果到excel文件，包含告警所在行，告警明细，告警级别等信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/s15D7IarTq2iYzwvLDhAKQ/zh-cn_image_0000002229450125.png)

**实践说明**

以@typescript-eslint/no-restricted-syntax（使用某类语法时，codelinter告警）、@typescript-eslint/naming-convention（命名风格校验）和@hw-stylistic/file-naming-convention（检查代码文件的命名风格）三个规则为例，介绍codelinter配置文件的使用方法。

**示例1：调用类Foo下bar方法时，Code Linter告警**

**在配置文件中定义规则**

在ArkTS工程的pages/Index.ets文件中增加以下用例：

```typescript
class Foo {
  static bar() {}
}

Foo.bar();
```

在工程根目录下新建code-linter.json5文件，新增以下配置：

```screen
{
  "rules": {
    "@typescript-eslint/no-restricted-syntax": [
      // 告警级别: 枚举类型, 支持配置为error, warn, off
      "error",
      {
        // selector属性必选，配置要禁用的语法
        // 可通过特定DSL筛选待限制的语句，CallExpression表示方法调用表达式，后面的中括号里面是筛选条件（根据语法树Node节点来确定）
        // 其中callee.object.name根据指定的名称筛选调用方法的对象（class，namespace或module），以上示例中为"Foo"
        // callee.property.name则根据指定的名称筛选被调用的方法，以上示例中为"bar"
        "selector": "CallExpression[callee.object.name='Foo'][callee.property.name='bar']",
        // message属性可选，配置要展示的报错信息
        "message": "Foo.bar() is not allowed"
      }
    ]
  },
}
```

**说明** 

如需在code-linter.json5文件中配置其他字段，请参见[配置代码检查规则](../harmonyos-guides/ide-code-linter.md#section19310459444)。

执行代码检查

对pages/Index.ets文件进行代码检查，结果如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/yxx81bGaQ3WVIrMHDcWVzA/zh-cn_image_0000002194009852.png)

**示例2：对类名Foo的命名风格校验**

在配置文件中定义规则

在ArkTS工程中，pages/Index.ets文件下增加以下用例：

```typescript
class foo {    //Here is an example of a naming style error, where foo is the incorrect class name used, and the correct class name should be Foo
  bar() {}
}
```

在工程根目录下创建code-linter.json5文件，并添加以下配置：

```screen
{
  "rules": {
    "@typescript-eslint/naming-convention": [
      "error",
      {
        // selector属性必选，配置要检查的语法，这里配置的class表示检查自定义组件名
        "selector": "class",
        // format属性必选，配置期望的命名风格，支持枚举值，这里配置的PascalCase表示大驼峰风格
        "format": ["PascalCase"],
        // custom属性可选，配置用户自定义的命名风格
        "custom": {
          // regex属性必选，配置具体的正则
          "regex": "^[a-zA-Z]+$",
          // match属性必选，配置为true表示正则未命中时报错；配置为false表示正则命中时报错
          "match": true
        }
      }
    ]
  },
}
```

**表1** 字段说明

| 字段名称 | 参数说明 | 是否必选 | 类型 | 支持配置的参数 |
| --- | --- | --- | --- | --- |
| selector | 配置要检查的语法 | 是 | 字符串、字符串数组 | * variable：变量 * function：函数 * parameter：参数 * parameterProperty：参数属性 * accessor：get/set方法 * enumMember：枚举成员 * classMethod：类方法 * structMethod：自定义组件中的方法 * objectLiteralMethod：对象方法 * typeMethod：接口方法 * classProperty：类属性 * structProperty：自定义组件中的属性 * objectLiteralProperty：对象属性 * typeProperty：接口属性 * class：类 * struct：自定义组件 * interface：接口 * typeAlias：类型别名 * enum：枚举 * typeParameter：泛型参数 * default：包含以上所有的类型 * variableLike：包含variable，function，parameter * memberLike：包含classProperty，structProperty，objectLiteralProperty，typeProperty，parameterProperty ，enumMember，classMethod，objectLiteralMethod，typeMethod，accessor * typeLike：包含class，struct，interface，typeAlias，enum，typeParameter * method：包含classMethod，structMethod，objectLiteralMethod，typeMethod * property：包含classProperty，objectLiteralProperty，typeProperty |
| format | 配置期望的命名风格 | 是 | 字符串数组 | * camelCase：小驼峰命名风格，比如getName，getID（支持连续大写字母），不支持下划线 * strictCamelCase：严格小驼峰命名风格，除了不支持连续大写字母（getID），其他的和camelCase相同 * PascalCase：大驼峰命名风格，比如Foo，CC，除了要求第一个字母大写，其他的和camelCase相同 * StrictPascalCase：大驼峰命名风格，除了不支持连续大写字母（CC），其他的和PascalCase相同 * snake\_case：小写字母+下划线+小写字母的命名风格，比如a\_a，不支持\_a，a\_a\_ * UPPER\_CASE：大写字母+下划线+大写字母的命名风格，比如A\_A，不支持\_A，A\_A\_ |
| custom | 配置用户自定义的命名风格 | 否 | 对象 | * regex：属性必选，配置具体的正则 * match：属性必选，配置为true表示正则未命中时报错，配置为false表示正则命中时报错 |
| leadingUnderscore/trailingUnderscore | 配置是否允许以下划线开头/以下划线结尾的命名风格 | 否 | 字符串 | * allow：允许以一个下划线开头/结尾的命名风格，比如\_name * allowDouble：允许以两个下划线开头/结尾的命名风格，比如\_\_name * allowSingleOrDouble：允许以一个或者两个下划线开头/结尾的命名风格（allow+allowDouble） * forbid：禁止以下划线开头/结尾的命名风格，比如\_name，\_\_name * require：必须是以下划线开头/结尾的命名风格，比如\_name，\_\_name * requireDouble：必须是以两个下划线开头/结尾的命名风格，比如\_\_name |
| prefix/suffix | 配置固定前缀/后缀的命名风格。如果前缀/后缀未匹配则报错 | 否 | 字符串数组 | 用户自定义前缀/后缀 |
| filter | 过滤特定的命名风格，检查或者不检查正则命中的命名 | 否 | 对象 | 配置格式与custom相似  match：设置为true表示只检查正则命中的名字，设置为false表示不检查正则命中的名字  regex：设置过滤的正则  说明  支持直接配置一个字符串，这个字符串配置的是regex，此时match相当于配置的是true。 |
| modifiers | 匹配修饰符，只有包含特定修饰符的命名才会检查 | 否 | 字符串数组 | * abstract：匹配abstract关键字 * override：匹配override关键字 * private：匹配private关键字 * protected：匹配protected关键字 * static：匹配static关键字 * async：匹配async关键字 * const：匹配const关键字 * destructured：匹配解构语法 * exported：匹配export关键字 * global：匹配全局声明 * #private：匹配私有符号# * public：匹配public级别的访问修饰符 * requiresQuotes：匹配字符串类型的命名，并且 字符串中包含特殊字符 * unused：匹配未使用的声明 |
| types | 匹配类型，只有特定类型的名字才会检查 | 否 | 字符串数组 | * array：数组类型 * boolean：布尔类型 * function：函数类型 * number：数字类型 * string：字符串类型 |

**说明** 

以上配置的参数校验优先级为：filter > types > modifiers > validate leading underscore > validate trailing underscore > validate prefix > validate suffix > validate custom > validate format。

**执行代码检查**

对pages/Index.ets文件执行代码检查，显示检查结果如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/aWhsecgKQTCZUU3G59q9TA/zh-cn_image_0000002229335649.png)

**示例3：检查代码文件的命名风格**

**在配置文件中定义规则**

在ArkTS工程中，pages目录下新建test.ets文件；

在工程根目录下新建code-linter.json5文件，并新增以下配置：

```screen
{
  "rules": {
    "@hw-stylistic/file-naming-convention": [
      // 告警级别：枚举类型，支持配置为error，warn，off
      "error",
      {
        // selector属性可选，支持配置为code或者resources
        // code表示检查代码文件的命名风格
        // resources表示检查资源文件的命名风格
        "selector": "code"
      }
    ]
  },
}
```

**说明** 

如果未配置selector属性，默认检查代码文件和资源文件的命名风格。

**执行代码检查**

对pages/test.ets文件执行代码检查，显示检查结果如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/pBtjIy41QQuPXvqvFZ2SaA/zh-cn_image_0000002229450117.png)
