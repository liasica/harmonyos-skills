---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-code-linter
title: Code Linter代码检查
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查
category: harmonyos-guides
scraped_at: 2026-10-11T07:23:16+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:95846b6d21e326edf0a7304bfc183c7be7ee0ea3c2eeadcd8747a67296db415a
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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/10T2alRDQmaOyX8-zRZQ2w/zh-cn_image_0000002750169574.png "点击放大")

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

* 单击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/XufrIiv7RzCxTgOi6YoU0g/zh-cn_image_0000002779728755.png "点击放大")图标，查看可修复的代码；点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/hc5RCmS9SAqd5ayeQMxxpQ/zh-cn_image_0000002750169572.png "点击放大")图标，可以一键式批量修复，并刷新检查结果；点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/FJTlFi1mTQWV6KSEvcIUyw/zh-cn_image_0000002750169580.png "点击放大")图标，可以重新进行检查；点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/LAYUfCf-SvGN4EB7RDZleQ/zh-cn_image_0000002779728753.png "点击放大")图标，可以收起或者展开检查结果。
* 点击不同告警等级，可分别查看对应告警级别的信息，其中![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/esLXWqhCR5efIGDUZWz9Fw/zh-cn_image_0000002750009694.png "点击放大")表示错误、![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/5Wpm_54ER8ax1XYzcThRmQ/zh-cn_image_0000002779608607.png "点击放大")表示警告、![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/YhQILi0oSo6pH_XUNCULzw/zh-cn_image_0000002779728751.png "点击放大")表示建议。
* 点击**按场景筛选**下拉菜单，可以筛选不同规则的检查结果。
* 选中某条告警结果，可以在右侧**缺陷详情**查看告警对应的规则详细说明，其中包含正向和反向示例，并根据其中的建议修改代码。
* 双击某条告警结果，可以跳转到对应代码缺陷位置。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0e/v3/-QQvIp6KSeutblZ_-4MtvQ/zh-cn_image_0000002750009684.png "点击放大")

**屏蔽告警信息：**

* 在某些特殊场景下，若扫描结果中出现误报，鼠标悬浮在该条告警结果后点击右侧![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/hp9MQZS0Sf-J73rk0Vzbcg/zh-cn_image_0000002750169582.png "点击放大")图标，可以忽略对告警所在行的code linter检查；或勾选多条待屏蔽的告警，点击工具面板![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/oFvcPUpURG2qtaoeqs3YYg/zh-cn_image_0000002750169578.png "点击放大")图标批量执行。
* 在文件顶部添加注释/\* eslint-disable \*/可以屏蔽整个文件执行code linter检查，在eslint-disable 后加入一个或多个以逗号分隔的规则Id，可以屏蔽具体检查规则。
* 在需要忽略检查的代码块前后分别添加/\* eslint-disable \*/和/\* eslint-enable \*/添加注释信息，再执行Code Linter，将不再显示该代码块扫描结果；在待屏蔽的代码行前一行添加/\* eslint-disable-next-line \*/，也可屏蔽对该代码行的codelinter检查。

**导出检查结果：**点击工具面板![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/EFX8JAY5T3-tuc3I3cjBHg/zh-cn_image_0000002779608601.png "点击放大")图标，即可导出检查结果到csv文件，包含告警所在行，告警明细，告警级别等信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/gMonARE-RYipd5Ye_9wBiA/zh-cn_image_0000002779728743.png "点击放大")
