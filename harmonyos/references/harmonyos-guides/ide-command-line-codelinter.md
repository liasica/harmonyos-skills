---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-command-line-codelinter
title: 代码检查工具（codelinter）
breadcrumb: 指南 > 命令行工具 > 代码检查工具（codelinter）
category: harmonyos-guides
scraped_at: 2026-04-28T07:57:38+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:a93d172fef68cf4122ac10b6b87908d8a93186f5b7c02d29982d8332c926b99b
---

codelinter同时支持使用命令行执行代码检查与修复，可将codelinter工具集成到门禁或持续集成环境中。

codelinter命令行格式为：

```
1. codelinter [options] [dir]
```

options：可选配置，请参考[表1](ide-command-line-codelinter.md#table25697717185)。

dir：待检查的工程根目录；为可选参数，如不指定，默认为当前上下文目录。

**表1** codelinter命令行配置

| 指令 | 说明 |
| --- | --- |
| --config/-c *<filepath>* | 指定执行codelinter检查的规则配置文件，*<filepath>*指定执行检查的规则配置文件位置。 |
| --fix | 设置codelinter检查同时执行QuickFix。 |
| --format/-f | 设置检查结果的输出格式。目前支持default/json/xml/html四种格式；不指定时，默认是default格式（文本格式）。 |
| --output/-o *<filepath>* | 指定检查结果保存位置，且命令行窗口不展示检查结果。*<filepath>*指定存放代码检查结果的文件路径，支持使用相对/绝对路径。不使用--output指令时，检查结果默认会显示在命令行窗口中。 |
| --version/-v | 查看codelinter版本。 |
| --product/-p *<productName>* | 指定当前生效的product。 <productName> 为生效的product名称。 |
| --incremental/-i | 对Git工程中的增量文件（包含新增/修改/重命名的文件）执行Code Linter检查。 |
| --help/-h | 查询codelinter命令行帮助。 |
| --exit-on/-e <levels> | 指定哪些告警级别需要返回非零退出码，告警级别包括：error、warn和suggestion。若需要指定多个告警级别，级别间需要用英文逗号分开。  退出码的计算方式为：用一个3位的二进制数从高到低分别表示error、warn、suggestion告警级别。若在命令行中配置告警级别，并且代码检查结果中也包含该告警级别，则该二进制值为1，否则均为0。将二进制数转换为十进制数，则是退出码。  例如：   * 命令配置为--exit-on error，代码检查结果包括error、warn、suggestion三类告警，则退出码的二进制数为100，十进制数为4。 * 命令配置为--exit-on error，代码检查结果包括warn、suggestion两类告警，则退出码的二进制数为000，十进制数为0。 |

1. 进行codelinter代码检查与修复。若您的工程存在多个product，请使用--product/-p指令，指定生效的product和执行检查的工程根目录。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/cbycqU5uQpaIKj41S4uSmA/zh-cn_image_0000002561753715.png?HW-CC-KV=V1&HW-CC-Date=20260427T235737Z&HW-CC-Expire=86400&HW-CC-Sign=8EEF7AED14C9587C0C312BB63A125D1DDAD3C51494FD9A414F2E6B36408BBD30)
   * 在工程根目录下使用命令行工具：
     1. 直接执行 **codelinter** 指令。此时根据默认codelinter检查规则，对该工程中的TS/ArkTS文件进行代码检查。默认的规则清单可在检查完成后，根据命令行提示，查看相应位置的code-linter.json5文件。

        ```
        1. codelinter // 进行codelinter检查
        ```

        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/rDU0A3U3SYyaFbHZorO33A/zh-cn_image_0000002561833691.png?HW-CC-KV=V1&HW-CC-Date=20260427T235737Z&HW-CC-Expire=86400&HW-CC-Sign=8D56C2701AC55588399F858AA15E0C91D379A33BDB9DEDA85680A4036D46EBC8 "点击放大")
     2. 执行如下命令，指定codelinter检查所使用的code-linter.json5规则配置文件，并进行代码检查。

        ```
        1. codelinter -c filepath // 指定执行检查的规则配置文件位置
        ```

        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/fJ4J4iLrR1CtHUoFJNKcvg/zh-cn_image_0000002561833695.png?HW-CC-KV=V1&HW-CC-Date=20260427T235737Z&HW-CC-Expire=86400&HW-CC-Sign=B60049773928720F9BCDE47730F2C5FBA2CE81A3F7181D86B8701469EF4D1DB8 "点击放大")
     3. 执行如下命令，对指定工程将根据指定的规则配置文件执行codelinter检查，并对部分支持修复的告警信息进行自动修复。

        ```
        1. codelinter -c filepath --fix // 对工程中的告警进行修复
        ```

        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/jrcYuEV7StKnUwvEvup5MA/zh-cn_image_0000002561753719.png?HW-CC-KV=V1&HW-CC-Date=20260427T235737Z&HW-CC-Expire=86400&HW-CC-Sign=4E76C1BD2EFEA20E453EAD4ED30782772131F5C1CB65433E09129ED56BD5BDF8)
   * 在非工程根目录下使用命令行工具：
     1. 执行如下命令，指定需要进行检查的工程目录或文件路径。此时根据默认codelinter检查规则，对该工程中的TS/ArkTS文件进行代码检查。默认的规则清单可在检查完成后，根据命令行提示，查看相应位置的code-linter.json5文件。

        ```
        1. codelinter dir [filepath] [dir1] // 指定执行检查的工程目录或文件路径。支持同时配置多个文件/文件夹路径。 filepath为待检查的文件所在位置，dir、dir1指定待检查的工程目录
        ```

        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/gNVUc6DkQbqafJAUc0-UwQ/zh-cn_image_0000002530753780.png?HW-CC-KV=V1&HW-CC-Date=20260427T235737Z&HW-CC-Expire=86400&HW-CC-Sign=2A750A871208A94D3F1AF91B7D47E7EB52E7970D74C7697843AABDEFE93E456D "点击放大")
     2. 在指定的工程目录下，根据指定的codelinter规则配置文件进行代码检查。

        ```
        1. codelinter -c filepath dir // filepath为指定的规则配置文件所在位置，dir指定执行检查的工程根目录
        ```
     3. 执行如下命令，对指定工程重新执行codelinter检查，并对部分支持修复的告警进行自动修复。

        ```
        1. codelinter -c filepath dir --fix // 对指定工程中的告警进行修复。支持配置同时多个工程路径
        ```

        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/LETrJbCTT7C3_HTIvFG9tg/zh-cn_image_0000002530753774.png?HW-CC-KV=V1&HW-CC-Date=20260427T235737Z&HW-CC-Expire=86400&HW-CC-Sign=C4B11FF82C79D6667DE695E860DF4AEB00C54CB145DACEF7B3B75628567D7FCD "点击放大")
2. 如需指定检查结果输出格式（以json格式为例），执行如下指令。检查结果将在命令行窗口展示。

   ```
   1. codelinter [dir] -f json  //[dir]为待检查的工程根目录
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/NUO174cYQOubxxGapYefwg/zh-cn_image_0000002530753778.png?HW-CC-KV=V1&HW-CC-Date=20260427T235737Z&HW-CC-Expire=86400&HW-CC-Sign=4DF05B3D250008BB1A7474758B4E50069636136ED0F793CD2DBB7D1BCF0D37DB)
3. 执行如下指令，指定代码检查输出格式及结果保存位置。此时将不在命令行窗口中打印检查结果，可在指定的文件存放路径下查看。

   ```
   1. codelinter [dir] -f json -o filepath2     // [dir]为待检查的工程根目录，filepath2为指定存放代码检查结果的文件路径
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/5waGsmRTRxe8ZrvJz9X8LQ/zh-cn_image_0000002530913768.png?HW-CC-KV=V1&HW-CC-Date=20260427T235737Z&HW-CC-Expire=86400&HW-CC-Sign=E560C1BFF5A7F1A936BEE6512CEBA887FC8FA347222C793E2859BA8AD795D501)
