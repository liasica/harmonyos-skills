---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-command-line-codelinter
title: 代码检查工具（codelinter）
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 命令行工具 > 代码检查工具（codelinter）
category: harmonyos-guides
scraped_at: 2026-10-11T07:23:25+08:00
doc_updated_at: 2026-10-10
content_hash: sha256:c6c61abbd6b5d254f79d076e572cd565659efe69cfaec41c13437a89e8ae28dd
---

codelinter同时支持使用命令行执行代码检查与修复，可将codelinter工具集成到门禁或持续集成环境中。

执行命令前，需要先[配置环境变量](ide-hmos-commandline-get.md#section14891106103319)。

codelinter命令行格式为：

```screen
codelinter [options] [dir]
```

options：可选配置，请参考[codelinter命令行配置](ide-hmos-command-line-codelinter.md#table25697717185)。

dir：待检查的工程根目录；为可选参数，如不指定，默认为当前上下文目录。

**表1** codelinter命令行配置

| 指令 | 说明 |
| --- | --- |
| --config/-c *<configPath>* | 指定执行codelinter检查的规则配置文件，*<configPath>*指定执行检查的规则配置文件位置。 |
| --fix | 设置codelinter检查同时执行QuickFix。 |
| --format/-f <outputFormat> | 设置检查结果的输出格式。<outputFormat>：必须参数，指定输出格式，支持值：default（文本，默认）、json、xml、html。 |
| --output/-o *<reportFile>* | 指定检查结果保存位置，且命令行窗口不展示检查结果。*<reportFile>*指定存放代码检查结果的文件路径，支持使用相对/绝对路径。不使用--output指令时，检查结果默认会保存在命令行工具的result文件夹下。 |
| --version/-v | 查看codelinter版本。 |
| --product/-p *<productName>* | 当项目中存在多个product时，使用-p指定当前生效的product。 <productName> 为生效的product名称。 |
| --help/-h | 查询codelinter命令行帮助。 |

1. 进行codelinter代码检查与修复。若您的工程存在多个product，请使用--product/-p指令，指定生效的product和执行检查的工程根目录。
   * 在工程根目录下使用命令行工具：
     1. 直接执行 **codelinter** 指令。此时根据默认codelinter检查规则，对该工程中的TS/ArkTS文件进行代码检查。默认的规则清单可在检查完成后，根据命令行提示，查看相应位置的code-linter.json5文件。

        ```screen
        codelinter // 进行codelinter检查
        ```

        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/kqiAfoJ4RpSKBKZ3idv9ZQ/zh-cn_image_0000002750009688.png "点击放大")
     2. 执行如下命令，指定codelinter检查所使用的code-linter.json5规则配置文件，并进行代码检查。

        ```screen
        codelinter -c filepath // 指定执行检查的规则配置文件位置
        ```

        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/BxlGKwfbSH2RG3tJuhkong/zh-cn_image_0000002779608595.png "点击放大")
     3. 执行如下命令，对指定工程将根据指定的规则配置文件执行codelinter检查，并对部分支持修复的告警信息进行自动修复。

        ```screen
        codelinter -c filepath --fix // 对工程中的告警进行修复
        ```

        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/hwZeE6iRRj2582v6QJAiuQ/zh-cn_image_0000002779728741.png "点击放大")
   * 在非工程根目录下使用命令行工具：
     1. 执行如下命令，指定需要进行检查的工程目录或文件路径。此时根据默认codelinter检查规则，对该工程中的TS/ArkTS文件进行代码检查。默认的规则清单可在检查完成后，根据命令行提示，查看相应位置的code-linter.json5文件。

        ```screen
        codelinter dir [filepath] [dir1] // 指定执行检查的工程目录或文件路径。支持同时配置多个文件/文件夹路径。 filepath为待检查的文件所在位置，dir、dir1指定待检查的工程目录
        ```

        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/_0NV148pR4ifFdOILC1JOA/zh-cn_image_0000002750009686.png "点击放大")
     2. 在指定的工程目录下，根据指定的codelinter规则配置文件进行代码检查。

        ```screen
        codelinter -c filepath dir // filepath为指定的规则配置文件所在位置，dir指定执行检查的工程根目录
        ```

        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/cUr_O17gT5-wMwU-7zAdOw/zh-cn_image_0000002750169568.png "点击放大")
     3. 执行如下命令，对指定工程重新执行codelinter检查，并对部分支持修复的告警进行自动修复。

        ```screen
        codelinter -c filepath dir --fix // 对指定工程中的告警进行修复。支持配置同时多个工程路径
        ```

        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/8un4DhjGQ1y98ySGdabxaw/zh-cn_image_0000002779608599.png "点击放大")
2. 如需指定检查结果输出格式（以json格式为例），执行如下指令。检查结果将在命令行窗口展示。

   ```screen
   codelinter [dir] -f json  //[dir]为待检查的工程根目录
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/qK2u3GdMTnWcGo5NR8kRRg/zh-cn_image_0000002779728745.png "点击放大")
3. 执行如下指令，指定代码检查输出格式及结果保存位置。检查结果不在命令行窗口打印，可在指定的文件存放路径下查看。

   ```screen
   codelinter [dir] -f json -o filepath2     // [dir]为待检查的工程根目录，filepath2为指定存放代码检查结果的文件路径
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/JPOKFp4RRN-2w3Pik3s29g/zh-cn_image_0000002750009690.png "点击放大")
