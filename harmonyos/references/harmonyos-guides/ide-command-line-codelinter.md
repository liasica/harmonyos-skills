---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-command-line-codelinter
title: ArkTS/TS代码检查工具（codelinter）
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 命令行工具 > ArkTS/TS代码检查工具（codelinter）
category: harmonyos-guides
scraped_at: 2026-11-24T12:42:37+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:dea3e391df0ce3a65edc5e1303f3b9fa2dde48c3f07f2f42e3288f23515f2ad6
---

codelinter同时支持使用命令行执行代码检查与修复，可将codelinter工具集成到门禁或持续集成环境中。

codelinter命令行格式为：

```bash
codelinter [options] [dir]
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
| --incremental/-i | 对Git工程中的增量文件（包含新增/修改/重命名的文件）执行codelinter检查。 |
| --language/-l <language> | 设置codelinter语言为cn或en。默认为en。 |
| --help/-h | 查询codelinter命令行帮助。 |
| --exit-on/-e <levels> | 指定哪些告警级别需要返回非零退出码，告警级别包括：error、warn和suggestion。若需要指定多个告警级别，级别间需要用英文逗号分开。  退出码的计算方式为：用一个3位的二进制数从高到低分别表示error、warn、suggestion告警级别。若在命令行中配置告警级别，并且代码检查结果中也包含该告警级别，则该二进制值为1，否则均为0。将二进制数转换为十进制数，则是退出码。  例如：   * 命令配置为--exit-on error，代码检查结果包括error、warn、suggestion三类告警，则退出码的二进制数为100，十进制数为4。 * 命令配置为--exit-on error，代码检查结果包括warn、suggestion两类告警，则退出码的二进制数为000，十进制数为0。 |

1. 进行codelinter代码检查与修复。若您的工程存在多个product，请使用--product/-p指令，指定生效的product和执行检查的工程根目录。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/REUK01ZWQMOZttkeEqHi0g/zh-cn_image_0000002779567292.png?HW-CC-KV=V1&HW-CC-Date=20261124T044237Z&HW-CC-Expire=31536000000&HW-CC-Sign=EBFDE3195413D873AE781A740E217708F7DAEA8266F6E3F13DA5012D893E791D)
   * 在工程根目录下使用命令行工具：
     1. 直接执行 **codelinter** 指令。此时根据默认codelinter检查规则，对该工程中的TS/ArkTS文件进行代码检查。默认的规则清单可在检查完成后，根据命令行提示，查看相应位置的code-linter.json5文件。

        ```bash
        codelinter // 进行codelinter检查
        ```

        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/Ifg9QjQkTleR8e5S4FewUA/zh-cn_image_0000002779407310.png?HW-CC-KV=V1&HW-CC-Date=20261124T044237Z&HW-CC-Expire=31536000000&HW-CC-Sign=2419E832E82EC61B16B21C7827423B0F8A9FF82BD80C4DE7C7728416532A6BBD "点击放大")
     2. 执行如下命令，指定codelinter检查所使用的code-linter.json5规则配置文件，并进行代码检查。

        ```bash
        codelinter -c filepath // 指定执行检查的规则配置文件位置
        ```

        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/Cq0kr3gaS4eHK4rMRGDDrg/zh-cn_image_0000002779407314.png?HW-CC-KV=V1&HW-CC-Date=20261124T044237Z&HW-CC-Expire=31536000000&HW-CC-Sign=7C06D29EBE19474DFF2E6B1B7E8350076FB5ED063A659DD1DAFFBE997EC363E1 "点击放大")
     3. 执行如下命令，对指定工程将根据指定的规则配置文件执行codelinter检查，并对部分支持修复的告警信息进行自动修复。

        ```bash
        codelinter -c filepath --fix // 对工程中的告警进行修复
        ```

        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/HA5tfPhNTweUMtLKEiCrJg/zh-cn_image_0000002779567294.png?HW-CC-KV=V1&HW-CC-Date=20261124T044237Z&HW-CC-Expire=31536000000&HW-CC-Sign=F2E0DD362EEB517A6F2469A0B728AB72BD8BBEC932D177F958B69104100D02A5)
   * 在非工程根目录下使用命令行工具：
     1. 执行如下命令，指定需要进行检查的工程目录或文件路径。此时根据默认codelinter检查规则，对该工程中的TS/ArkTS文件进行代码检查。默认的规则清单可在检查完成后，根据命令行提示，查看相应位置的code-linter.json5文件。

        ```bash
        codelinter dir [filepath] [dir1] // 指定执行检查的工程目录或文件路径。支持同时配置多个文件/文件夹路径。 filepath为待检查的文件所在位置，dir、dir1指定待检查的工程目录
        ```

        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/J9JGOZV0ScCwSrAJG1ejSA/zh-cn_image_0000002808766875.png?HW-CC-KV=V1&HW-CC-Date=20261124T044237Z&HW-CC-Expire=31536000000&HW-CC-Sign=00D44D7D2F45B3B0DBE1B713C88E2204A280BFBBD0A8232BDF0EF19A093138EF "点击放大")
     2. 在指定的工程目录下，根据指定的codelinter规则配置文件进行代码检查。

        ```bash
        codelinter -c filepath dir // filepath为指定的规则配置文件所在位置，dir指定执行检查的工程根目录
        ```
     3. 执行如下命令，对指定工程重新执行codelinter检查，并对部分支持修复的告警进行自动修复。

        ```bash
        codelinter -c filepath dir --fix // 对指定工程中的告警进行修复。支持配置同时多个工程路径
        ```

        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/lnLyLmJ7Rk20nPVs5Kf-WQ/zh-cn_image_0000002779567290.png?HW-CC-KV=V1&HW-CC-Date=20261124T044237Z&HW-CC-Expire=31536000000&HW-CC-Sign=6B2EA7F559E8D23DE9C839135C2753B97188A341E0C177FB008100E331947675 "点击放大")
2. 如需指定检查结果输出格式（以json格式为例），执行如下指令。检查结果将在命令行窗口展示。

   ```bash
   codelinter [dir] -f json  //[dir]为待检查的工程根目录
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/Fvy_5gfCSbqU6lHhbJ3lBg/zh-cn_image_0000002808886955.png?HW-CC-KV=V1&HW-CC-Date=20261124T044237Z&HW-CC-Expire=31536000000&HW-CC-Sign=26952BC8EE0408CBEFB97F154A4EA3AA839B22CFF1ACA1B5092F0799B7770A03)
3. 执行如下指令，指定代码检查输出格式及结果保存位置。此时将不在命令行窗口中打印检查结果，可在指定的文件存放路径下查看。

   ```bash
   codelinter [dir] -f json -o filepath2     // [dir]为待检查的工程根目录，filepath2为指定存放代码检查结果的文件路径
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/RKpN_OxUSi-iK1kkb_poIA/zh-cn_image_0000002779407312.png?HW-CC-KV=V1&HW-CC-Date=20261124T044237Z&HW-CC-Expire=31536000000&HW-CC-Sign=5FEA6F91E8191E97C929F0D97FA53EDBEEEE045E764F96CD8045E7D945F13AA9)
