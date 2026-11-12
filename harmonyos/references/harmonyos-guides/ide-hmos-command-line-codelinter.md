---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-command-line-codelinter
title: 代码检查工具（codelinter）
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 命令行工具 > 代码检查工具（codelinter）
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-10-10
content_hash: sha256:045f06cd1d03a0f4d5cef8493d1576f0048b3c9d8dc595c8c78f26a2d23c8779
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

        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/glGGoP9zRSmQY5G5iCDkmQ/zh-cn_image_0000002810750705.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=C77FBB1748CD4DEF81E3F1588213BB4FEAE44D2C85815F41BF219C5EDB4B08E3 "点击放大")
     2. 执行如下命令，指定codelinter检查所使用的code-linter.json5规则配置文件，并进行代码检查。

        ```screen
        codelinter -c filepath // 指定执行检查的规则配置文件位置
        ```

        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/vEgkuYHUQZSFGH5omy5FCA/zh-cn_image_0000002781311102.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=2F3F5E7D0AB0BB80863D42FCFFDE1D9D0CD343670E26E01C79EDA643DDFFE3D5 "点击放大")
     3. 执行如下命令，对指定工程将根据指定的规则配置文件执行codelinter检查，并对部分支持修复的告警信息进行自动修复。

        ```screen
        codelinter -c filepath --fix // 对工程中的告警进行修复
        ```

        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/XNyhNWQCRlqFS-Gzh2OClw/zh-cn_image_0000002810630589.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=BFFF56EC42544FD30B69612B11621D987FFB0B6D1F10BA963A529301DEAF89C7 "点击放大")
   * 在非工程根目录下使用命令行工具：
     1. 执行如下命令，指定需要进行检查的工程目录或文件路径。此时根据默认codelinter检查规则，对该工程中的TS/ArkTS文件进行代码检查。默认的规则清单可在检查完成后，根据命令行提示，查看相应位置的code-linter.json5文件。

        ```screen
        codelinter dir [filepath] [dir1] // 指定执行检查的工程目录或文件路径。支持同时配置多个文件/文件夹路径。 filepath为待检查的文件所在位置，dir、dir1指定待检查的工程目录
        ```

        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/84k6xEV4R9WsPEnlin7xDw/zh-cn_image_0000002781311104.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=FDB4AB506061997DB1F6F9B166EAC71DD41702EC7E67CEE0EB22AD178CE222B2 "点击放大")
     2. 在指定的工程目录下，根据指定的codelinter规则配置文件进行代码检查。

        ```screen
        codelinter -c filepath dir // filepath为指定的规则配置文件所在位置，dir指定执行检查的工程根目录
        ```

        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/Gs341YZkSI2y2HIGOzX41Q/zh-cn_image_0000002810750699.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=4521F5A9B042FD928B66B86136F469FC01959CA725749E49830E3B568AE8319F "点击放大")
     3. 执行如下命令，对指定工程重新执行codelinter检查，并对部分支持修复的告警进行自动修复。

        ```screen
        codelinter -c filepath dir --fix // 对指定工程中的告警进行修复。支持配置同时多个工程路径
        ```

        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/jAnPWvTySJGzyllaxZclNw/zh-cn_image_0000002810630595.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=065CFBE5683938ACB2C168D8C0E170426067E668051ACDF73672D3ED23714ACC "点击放大")
2. 如需指定检查结果输出格式（以json格式为例），执行如下指令。检查结果将在命令行窗口展示。

   ```screen
   codelinter [dir] -f json  //[dir]为待检查的工程根目录
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/wz5JQM9TTNaWMR-N6EbMFw/zh-cn_image_0000002781471040.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=4964BBB6F072D8DC5A90DA575D212EDE34CD35D581B081D13536599A2CBB4700 "点击放大")
3. 执行如下指令，指定代码检查输出格式及结果保存位置。检查结果不在命令行窗口打印，可在指定的文件存放路径下查看。

   ```screen
   codelinter [dir] -f json -o filepath2     // [dir]为待检查的工程根目录，filepath2为指定存放代码检查结果的文件路径
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/h7lvhlApTCWxvgcJXIVwwQ/zh-cn_image_0000002810630597.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=CF8E5767B58F8D31F9AF5957DA120DEE0AF914A8E830F7401D95D7AB0ADFE2FA "点击放大")
