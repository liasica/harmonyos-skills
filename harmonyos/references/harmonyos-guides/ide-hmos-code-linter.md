---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-code-linter
title: Code Linter代码检查
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:f151fb8c676dcdaaab9cf47f67583281be9a8c656d6305915da99eff9ae13634
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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0a/v3/y45f1pTrQ2S8hczMJbv6LA/zh-cn_image_0000002781311108.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=3D46D7CBA6C962981326589F0FE070D1EF869DC11F4AC802858434DD939CB7D1 "点击放大")

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

* 单击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/06/v3/AtpdDWFeREqfbeNvzFvbeg/zh-cn_image_0000002781311112.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=FD990D50605408D4FCD415B22D7EC969C6D4AEFE49489FED6618007E7BB4043D "点击放大")图标，查看可修复的代码；点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/gEXZ19kBSxGQhI0oWsqJGg/zh-cn_image_0000002781311106.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=3B61A19A1DE8B4AA1DB17D9AAAB29C141501C9F7921FEEE8902A97E247CE383F "点击放大")图标，可以一键式批量修复，并刷新检查结果；点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/fjarFeNbQsS4k_dB9LTjyA/zh-cn_image_0000002810750709.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=55663547D94682A4D966CCBA729E5B202152D89DC301E39D152D7D5D630BCD65 "点击放大")图标，可以重新进行检查；点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/a-Bc6C3IQ-ijvCIoyju9KA/zh-cn_image_0000002781311110.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=1C73DD327556867848EE93FF1CE2B3D7EB6C3C659ED26BE828B88A19C123BA30 "点击放大")图标，可以收起或者展开检查结果。
* 点击不同告警等级，可分别查看对应告警级别的信息，其中![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/uH7aodR4TK6eEiKitAqJRQ/zh-cn_image_0000002781471048.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=E850AE8E5686FCD8F81F97C9C4412769DA2D670E31C2819455F6B6A94C68D91F "点击放大")表示错误、![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/Non8Hg4pSBW4mRwuSv9aVw/zh-cn_image_0000002781471050.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=FAE09B2512228DB650AD420511B97850C5E4BD227C4999109D3A5009948B777C "点击放大")表示警告、![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/iOgrQqOGReGhAYW5VIe8Ww/zh-cn_image_0000002781471046.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=FCF4740D1112971E339FBC2CE7DB4408414314D326B69A1532E6A6FD6943957A "点击放大")表示建议。
* 点击**按场景筛选**下拉菜单，可以筛选不同规则的检查结果。
* 选中某条告警结果，可以在右侧**缺陷详情**查看告警对应的规则详细说明，其中包含正向和反向示例，并根据其中的建议修改代码。
* 双击某条告警结果，可以跳转到对应代码缺陷位置。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4/v3/BHcqJDN9Sn6wJ7YJH1nOZA/zh-cn_image_0000002781471042.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=D4BE51508F343DC5070B21491E0403C45A7C61553D791BEF020BDD29038B4E08 "点击放大")

**屏蔽告警信息：**

* 在某些特殊场景下，若扫描结果中出现误报，鼠标悬浮在该条告警结果后点击右侧![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/w4RoqdnURnC5ejoR2V4Q7A/zh-cn_image_0000002781311114.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=463EA50250ADDF906CF343F3B1280CE115A9C0E87D63EBAA44514A472E86355D "点击放大")图标，可以忽略对告警所在行的code linter检查；或勾选多条待屏蔽的告警，点击工具面板![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/UFSS7ZwHQe6S0X_EDNR5nQ/zh-cn_image_0000002810630599.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=4F9D0A4587C77DB842AEB63F0EA4411E3686CE64CA234111F7A23F11463B568D "点击放大")图标批量执行。
* 在文件顶部添加注释/\* eslint-disable \*/可以屏蔽整个文件执行code linter检查，在eslint-disable 后加入一个或多个以逗号分隔的规则Id，可以屏蔽具体检查规则。
* 在需要忽略检查的代码块前后分别添加/\* eslint-disable \*/和/\* eslint-enable \*/添加注释信息，再执行Code Linter，将不再显示该代码块扫描结果；在待屏蔽的代码行前一行添加/\* eslint-disable-next-line \*/，也可屏蔽对该代码行的codelinter检查。

**导出检查结果：**点击工具面板![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/Gn4uWftdTZaIChWb3l6Nlg/zh-cn_image_0000002810750707.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=2DDD6C5BED157E624D1D61A4F4ADF36BC17F9E02509BD6EC172B95AFB99EA37E "点击放大")图标，即可导出检查结果到csv文件，包含告警所在行，告警明细，告警级别等信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/hHrumiMRTTGRAUzoii8PfQ/zh-cn_image_0000002810750701.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=B2DC8450E17ADB76E114BAA919E0A8ADF6BD85FFA6B7E0C4F63FB9090CBAD05F "点击放大")
