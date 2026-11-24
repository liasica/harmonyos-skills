---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-code-linter
title: Code Linter代码检查
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查
category: harmonyos-guides
scraped_at: 2026-11-24T12:42:42+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:2ba156f6261b5f93f097a73e12fa0a826ce5f5578c9c6642a418f76f4f6c5ec1
---

Code Linter针对ArkTS/TS代码进行最佳实践、编程规范方面的检查。开发者可根据扫描结果中告警提示手动修复代码缺陷，或者执行一键式自动修复，在代码开发阶段，确保代码质量。

## 配置代码检查规则

在工程根目录下创建code-linter.json5配置文件，可对于代码检查的范围及对应生效的检查规则进行配置。

其中files和ignore配置项共同确定了代码检查范围，ruleSet和rules配置项共同确定了生效的规则范围。具体配置项功能如下：

**files**：配置待检查的文件名单，如未指定目录，将检查当前被选中的文件或文件夹中所有的.ets文件，例如：["\*\*/\*.ets"]。

**ignore**：配置无需检查的文件目录，其指定的目录或文件需使用相对路径格式，相对于code-linter.json5所在工程根目录，例如：build/\*\*/\*。

**ruleSet**：配置检查使用的规则集，规则集支持一次导入多条规则。目前仅支持all和recommended两种规则集，规则详情请参见[Code Linter代码检查规则](ide-hmos-codelinter-rule.md)。目前支持的规则集包括：

* 通用规则@typescript-eslint
* 安全规则@security
* 性能规则@performance
* 预览规则@previewer
* 一次开发多端部署规则@cross-device-app-dev
* ArkTS代码风格规则@hw-stylistic

  **说明** 

  + 以上规则集均分为all和recommended两种规则集。all规则集是规则全集，包含所有规则；recommended规则集是推荐使用的规则集合。all规则集包含recommended规则集。
  + 不在工程根目录新建code-linter.json5文件的情况下，Code Linter默认会检查@performance/recommended和@typescript-eslint/recommended规则集包含的规则。

**rules**：可以基于ruleSet配置的规则集，新增额外规则项，或修改ruleSet中规则默认配置，例如：将规则集中某条规则告警级别由warn改为error。

**overrides**：针对工程根目录下部分特定目录或文件，可配置定制化检查的规则。

```screen
{
  "files":   //用于表示配置适用的文件范围的 glob 模式数组。在没有指定的情况下，应用默认配置
  [
    "**/*.ets",   //字符串类型
    "**/*.js",
    "**/*.ts"
  ],
  "ignore":  //一个表示配置对象不应适用的文件的 glob 模式数组。如果没有指定，配置对象将适用于所有由 files 匹配的文件
  [
    "build/**/*",    //字符串类型
    "node_modules/**/*"
  ],
  "ruleSet":       //设置检查待应用的规则集, 当前仅支持DevEco Studio内置规则集all、recommended
  [
    "plugin:@typescript-eslint/recommended"    //快捷批量引入的规则集, 枚举类型：plugin:@typescript-eslint/all, plugin:@typescript-eslint/recommended
  ],
  "rules":         //可以对ruleSet配置的规则集中特定的某些规则进行修改、去使能, 或者新增规则集以外的规则；ruleSet和rules共同确定了代码检查所应用的规则
  {
    "@typescript-eslint/no-explicit-any":  // ruleId后面跟数组时, 第一个元素为告警级别, 后面的对象元素为规则特定开关配置
    [
      "error",              //告警级别: 枚举类型, 支持配置为error, warn, off
      {
        "ignoreRestArgs": true   //规则特定的开关配置, 为可选项, 不同规则其下层的配置项不同
      }
    ],
    "@typescript-eslint/explicit-function-return-type": 2,   // ruleId后面跟单独一个数字时, 表示仅设置告警级别, 枚举值为: 2(error), 1(warn), 0(off)
    "@typescript-eslint/no-unsafe-return": "warn"            // ruleId后面跟单独一个字符串时, 表示仅设置告警级别, 枚举值为: error, warn, off
  },
  "overrides":      //针对特定的目录或文件采用定制化的规则配置
  [
    {
      "files":   //指定需要定制化配置规则的文件或目录
      [
        "entry/**/*.ts"   //字符串类型
      ],
      "excluded":
      [
        "entry/**/*.test.js" //指定需要排除的目录或文件, 被排除的目录或文件不会被检查; 字符串类型
      ],
      "rules":   //支持对overrides外公共配置的规则进行修改、去使能, 或者新增公共配置以外的规则; 该配置将覆盖公共配置
      {
        "@typescript-eslint/explicit-function-return-type":  // ruleId: 枚举类型
        [
          "warn",     //告警级别: 枚举类型, 支持配置为error, warn, off; 覆盖公共配置, explicit-function-return-type告警级别为warn
          {
             allowExpressions: true    //规则特定的开关配置, 为可选项, 不同规则其下层的配置项不同
          }
        ],
        "@typescript-eslint/no-unsafe-return": "off"   // 覆盖公共配置, 不检查no-unsafe-return规则
      }
    }
  ]
}
```

## 进行代码检查

在已打开的代码编辑器窗口单击右键选择**代码静态检查**，或在工程管理窗口中鼠标选中单个或多个工程文件/目录，右键选择**代码静态检查** **> 全量检查**执行代码全量检查。如只需对Git工程中增量文件（包含新增/修改/重命名）进行检查，右键选择**代码静态检查** **>** **增量检查**。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/F3detIqmQQiEXmIZQaaCsw/zh-cn_image_0000002820721057.png?HW-CC-KV=V1&HW-CC-Date=20261124T044241Z&HW-CC-Expire=31536000000&HW-CC-Sign=8832D246A974E633071B9482C15FE7A00676A7FA396851B7C6A9B6B9C0A9CC88 "点击放大")

**说明** 

* 若未配置代码检查规则文件，直接执行代码静态检查，将按照默认的编程规范规则对.ets文件进行检查。
* 代码静态检查不对如下文件及目录进行检查：
  + src/ohosTest文件夹
  + /src/test文件夹
  + node\_modules文件夹
  + oh\_modules文件夹
  + build文件夹
  + hvigorfile.ts文件
  + BuildProfile.ets文件

## 查看/处理代码检查结果

**查看检查结果：**

扫描完成后，在底部工具面板查看检查结果，具体包括：

* 单击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/TNDPnwlBT5y5vC8ZeaBE5w/zh-cn_image_0000002820721059.png?HW-CC-KV=V1&HW-CC-Date=20261124T044241Z&HW-CC-Expire=31536000000&HW-CC-Sign=5C3F05E597D60765184FD64E076AA079857F0DAA178D6A87D42E0C48535B8597 "点击放大")图标，查看可修复的代码；点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/2xXLGF7GQWqlkWxRdy4pFA/zh-cn_image_0000002791841122.png?HW-CC-KV=V1&HW-CC-Date=20261124T044241Z&HW-CC-Expire=31536000000&HW-CC-Sign=A6CE12238A60A561901B8BB59EA1363F092C326FD304994F12FF81AE24D82EB7 "点击放大")图标，可以一键式批量修复，并刷新检查结果；点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/ervmDIZqTFyA_7FrVwuj4g/zh-cn_image_0000002820721065.png?HW-CC-KV=V1&HW-CC-Date=20261124T044241Z&HW-CC-Expire=31536000000&HW-CC-Sign=36FE51A584B8DBB6751C37DBF8AD64D6C6076AED4944ACC5E1445CBA81A71021 "点击放大")图标，可以重新进行检查；点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/xH7negjNR0uckAOAgKMBEw/zh-cn_image_0000002820721063.png?HW-CC-KV=V1&HW-CC-Date=20261124T044241Z&HW-CC-Expire=31536000000&HW-CC-Sign=CE4B3BB74891CC393A8CC0DFABDA5203B701AF22A6130A9D45578890CCC29858 "点击放大")图标，可以收起或者展开检查结果。
* 点击不同告警等级，可分别查看对应告警级别的信息，其中![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/bASK3LGJR3mBPgWSkNr9oA/zh-cn_image_0000002820681063.png?HW-CC-KV=V1&HW-CC-Date=20261124T044241Z&HW-CC-Expire=31536000000&HW-CC-Sign=2B31D6424F2F5B02110AFFCBCD050A1C364A35BAA9DFEC784CFE45269F0093FF "点击放大")表示错误、![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/SDX4-zehTHmWSKKOvzMjzQ/zh-cn_image_0000002791841132.png?HW-CC-KV=V1&HW-CC-Date=20261124T044241Z&HW-CC-Expire=31536000000&HW-CC-Sign=7263988A2C9DFD11894724EE984342DAD5F8D086CD35862EB1308374A624D01E "点击放大")表示警告、![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/eeKUI1VXTUeF67WLu_snYA/zh-cn_image_0000002791841130.png?HW-CC-KV=V1&HW-CC-Date=20261124T044241Z&HW-CC-Expire=31536000000&HW-CC-Sign=7BE041E00804C21FEACFBBC1F8642472CE972777FD1BFB314D52991662F457E8 "点击放大")表示建议。
* 点击**按场景筛选**下拉菜单，可以筛选不同规则的检查结果。
* 选中某条告警结果，可以在右侧**缺陷详情**查看告警对应的规则详细说明，其中包含正向和反向示例，并根据其中的建议修改代码。
* 双击某条告警结果，可以跳转到对应代码缺陷位置。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/m5FM7jOHQvGLEk3bB6O4qA/zh-cn_image_0000002792001104.png?HW-CC-KV=V1&HW-CC-Date=20261124T044241Z&HW-CC-Expire=31536000000&HW-CC-Sign=476EBD2607CBCD535CA3132E3824094B7AA0AFB05B1DCFCD59036D6AF6AD2C3B "点击放大")

**屏蔽告警信息：**

* 在某些特殊场景下，若扫描结果中出现误报，鼠标悬浮在该条告警结果后点击右侧![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/qPL2JmDFQWWcvRxdP2Qgjw/zh-cn_image_0000002820681055.png?HW-CC-KV=V1&HW-CC-Date=20261124T044241Z&HW-CC-Expire=31536000000&HW-CC-Sign=E73E6A77F5E08D6E10F61B63C5AF7E24E53C5A222BE85A13A75AE305E3EC1CA4 "点击放大")图标，可以忽略对告警所在行的code linter检查；或勾选多条待屏蔽的告警，点击工具面板![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/U3CCQtCFT4yBVjRPQ_hC8w/zh-cn_image_0000002820681061.png?HW-CC-KV=V1&HW-CC-Date=20261124T044241Z&HW-CC-Expire=31536000000&HW-CC-Sign=9FAC66FAA32E0C6E481DFA7133F550B4CC46C7902B806D6E1010A87D0EDCDE5D "点击放大")图标批量执行。
* 在文件顶部添加注释/\* eslint-disable \*/可以屏蔽整个文件执行code linter检查，在eslint-disable 后加入一个或多个以逗号分隔的规则Id，可以屏蔽具体检查规则。
* 在需要忽略检查的代码块前后分别添加/\* eslint-disable \*/和/\* eslint-enable \*/添加注释信息，再执行Code Linter，将不再显示该代码块扫描结果；在待屏蔽的代码行前一行添加/\* eslint-disable-next-line \*/，也可屏蔽对该代码行的codelinter检查。

**导出检查结果：**点击工具面板![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0e/v3/R4Nek5oFRXyFBIvxbYKfkQ/zh-cn_image_0000002792001096.png?HW-CC-KV=V1&HW-CC-Date=20261124T044241Z&HW-CC-Expire=31536000000&HW-CC-Sign=84736AFCAFE32B79D9F5C1CE2D1EECB8C92EC05A979FFD132837075DCFDB5053 "点击放大")图标，即可导出检查结果到csv文件，包含告警所在行，告警明细，告警级别等信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/GwkMwAwvQK6ZUwljGJeEjA/zh-cn_image_0000002792001094.png?HW-CC-KV=V1&HW-CC-Date=20261124T044241Z&HW-CC-Expire=31536000000&HW-CC-Sign=4BF28B2762063EC21D520EA425B33E4B0D7BE7BC22BEBAAC4F3EE04747856722 "点击放大")
