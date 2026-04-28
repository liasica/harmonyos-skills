---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-build-obfuscation
title: 混淆加固
breadcrumb: 指南 > 构建应用 > 混淆加固
category: harmonyos-guides
scraped_at: 2026-04-28T07:57:24+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:e09eb5db7d07b5164a763bb0b3176b592887b69e0ccd0c0055200858e08e85eb
---

DevEco Studio原先默认开启源码混淆功能，会对API 10及以上的Stage工程，且编译模式是release时，自动进行简单的源码混淆，仅对参数名和局部变量名进行混淆。

从DevEco Studio NEXT Developer Beta3（5.0.3.600）版本开始，新建工程及模块默认关闭源码混淆功能，如果在模块级build-profile.json5配置文件中开启源码混淆，则混淆规则配置文件obfuscation-rules.txt中默认开启推荐的混淆规则，包含-enable-property-obfuscation、-enable-toplevel-obfuscation、-enable-filename-obfuscation、-enable-export-obfuscation四项混淆项，开发者可进一步在obfuscation-rules.txt文件中选择开启的混淆项，关于混淆项的介绍请查看[混淆规则](source-obfuscation.md#混淆选项)。

## 使用约束

* 仅支持Stage工程。
* 在[构建模式](ide-hvigor-compilation-options-customizing-guide.md#section192461528194916)为release模式时生效。
* 模块及模块依赖的HAR和HSP均未关闭混淆。

## 字段说明

可在模块级build-profile.json5文件中进行源码混淆相关配置。obfuscation字段说明如下：

| 配置项 | | 类型 | 是否必填 | 说明 |
| --- | --- | --- | --- | --- |
| ruleOptions | | 对象 | 否 | 混淆规则配置。 |
|  | enable | 布尔值 | 是 | 是否启用源码混淆：   * true：启用。 * false（默认值）：不启用。   说明  从DevEco Studio NEXT Developer Beta3（5.0.3.600）版本开始，默认值由true改为false。 |
| files | 字符串数组 | 否 | 配置混淆规则文件的相对路径，默认使用obfuscation-rules.txt文件。文件中配置的混淆规则仅在本模块编译时生效（包含依赖代码）。  说明  * 规则文件中支持配置所有[混淆规则](source-obfuscation.md)。 * 支持配置多个文件，文件名称支持自定义，当存在多个混淆规则文件时，规则合并以及合并后的作用范围可参考[混淆规则合并策略](source-obfuscation.md#混淆规则合并策略)。 |
| consumerFiles | | 字符串/字符串数组 | 否 | 仅HAR/HSP模块可配置，配置传递给集成方的混淆规则文件的相对路径，支持配置多个文件，文件名称支持自定义。  说明  * 为保证HAR/HSP模块可被正确集成使用，若有不希望被集成方混淆的内容，建议在规则文件中配置对应的[保留选项](source-obfuscation.md#保留选项)，例如HAR/HSP模块中导出的变量或函数。  * 规则文件中配置的[混淆选项](source-obfuscation.md#混淆选项)会与集成方的混淆规则进行合并，进而影响集成方的编译混淆，因此，建议仅配置[保留选项](source-obfuscation.md#保留选项)。 * 从DevEco Studio 5.1.0 Release版本开始支持在HSP模块中配置该字段。 |

## 使能混淆

为保护代码资产，建议开启混淆，您可以在模块级的build-profile.json5配置文件中开启源码混淆功能：

```
1. "arkOptions": {
2. "obfuscation": {
3. "ruleOptions": {
4. "enable": true  // 配置true，即可开启源码混淆功能
5. }
6. }
7. }
```

从DevEco Studio NEXT Developer Beta3（5.0.3.600）版本开始，开启混淆后，混淆规则配置文件obfuscation-rules.txt中默认开启推荐的混淆规则，包含-enable-property-obfuscation、-enable-toplevel-obfuscation、-enable-filename-obfuscation、-enable-export-obfuscation四项混淆项。

说明

使用[release模式](ide-hvigor-compilation-options-customizing-guide.md#section192461528194916)编译发布时，建议开启混淆，需要正确配置混淆规则，否则可能会有[运行时问题](source-obfuscation-questions.md)。

## 使能高阶混淆

在[开启混淆](ide-build-obfuscation.md#section18326541833)后，若您需要更高阶的混淆能力，可以通过以下操作配置高阶混淆规则。

### 配置所有混淆规则

1. 打开模块级build-profile.json5文件，在"files"字段下配置混淆规则文件的相对路径，支持配置多个文件，默认为./obfuscation-rules.txt。

   ```
   1. {
   2. "apiType": "stageMode",
   3. ...
   4. "buildOptionSet": [
   5. {
   6. "name": "release",
   7. "arkOptions": {
   8. "obfuscation": {
   9. "ruleOptions": {
   10. "enable": true,
   11. "files": [
   12. "./obfuscation-rules.txt"  // 混淆规则文件
   13. ]
   14. }
   15. }
   16. }
   17. },
   18. ],
   19. ...
   20. }
   ```
2. 打开模块目录内的obfuscation-rules.txt文件配置混淆规则，具体的配置规则请参见[配置混淆规则](source-obfuscation.md)，对于不需要混淆的内容，请配置[保留选项](source-obfuscation.md#保留选项)。

   当存在多个混淆规则文件时，规则合并以及合并后的作用范围可参考[混淆规则合并策略](source-obfuscation.md#混淆规则合并策略)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/mv2Npm4kQEWWBLJAcYu6Ww/zh-cn_image_0000002530913828.png?HW-CC-KV=V1&HW-CC-Date=20260427T235722Z&HW-CC-Expire=86400&HW-CC-Sign=F921B6AD7D08ADF8B9813A4B10E8401529598D3CD874ED0D3960F0E88F1618D4)

### HAR/HSP配置保留选项

为保证HAR/HSP模块可被正确集成使用，若有不希望被集成方混淆的内容，建议在规则文件中配置对应的[保留选项](source-obfuscation.md#保留选项)，例如HAR/HSP模块中导出的变量或函数。

1. 打开模块级build-profile.json5文件，在"consumerFiles"字段下配置传递给集成方的混淆规则文件的相对路径，支持配置多个文件，默认为./consumer-rules.txt，对应编译后HAR包中的obfuscation.txt文件。

   ```
   1. {
   2. "apiType": "stageMode",
   3. ...
   4. "buildOptionSet": [
   5. {
   6. "name": "release",
   7. "arkOptions": {
   8. "obfuscation": {
   9. "ruleOptions": {
   10. "enable": true,
   11. "files": [
   12. "./obfuscation-rules.txt"
   13. ]
   14. },
   15. "consumerFiles": [              // 该模块被依赖时的混淆规则
   16. "./consumer-rules.txt"
   17. ]
   18. }
   19. }
   20. },
   21. ],
   22. ...
   23. }
   ```
2. 打开模块目录内的consumer-rules.txt文件配置[保留选项](source-obfuscation.md#保留选项)。

   当存在多个混淆规则文件时，规则合并以及合并后的作用范围可参考[混淆规则合并策略](source-obfuscation.md#混淆规则合并策略)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2/v3/T4iMfHvRQyiTtax3WM3P5g/zh-cn_image_0000002561833723.png?HW-CC-KV=V1&HW-CC-Date=20260427T235722Z&HW-CC-Expire=86400&HW-CC-Sign=5FA80BE8766DD84E91348358E0C614F58FB39BE4C605E12970574077AF053B64)

## 通过混淆助手配置保留选项

开启混淆后，代码中的方法、属性或路径被混淆，但运行的时候访问的是未混淆的方法、属性或路径，可能导致功能不可用，因此需要将对应的字段配置保留选项。关于保留选项的排查场景及配置方式请参考[保留选项](source-obfuscation.md#保留选项)。

需要排查的场景和配置的字段有很多，因此DevEco Studio提供了混淆助手工具（ObfuscationHelper），可以根据模块和场景对源码进行扫描，快速[识别需要配置的保留选项和白名单字段](ide-build-obfuscation.md#section3989185975217)，开发者可以一键生成白名单混淆规则文件。由于某些场景是动态访问名称、属性，需要在运行的时候才能确定的字段，ObfuscationHelper会识别该类场景，开发者需要根据业务进一步[排查识别白名单后进行配置](ide-build-obfuscation.md#section42331014105310)。

### 扫描代码

1. 通过以下任意一种方式打开ObfuscationHelper：
   * 点击菜单栏**Tools >** **ObfuscationHelper**。
   * 在模块目录上点击鼠标右键，在弹出的菜单中选择**ObfuscationHelper**。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/QCViwRw8Qsu8irjvIn256A/zh-cn_image_0000002530913810.png?HW-CC-KV=V1&HW-CC-Date=20260427T235722Z&HW-CC-Expire=86400&HW-CC-Sign=9099F4EB2FB670E1890712F438CA292FAB316F2F11C8D9BEDC129BE1EB9FE4BC)
2. 点击模块下拉选择框，选择待扫描的模块。
3. 如果模块之前被扫描过，并且生成了排查白名单，则会生成相应的历史记录。选择对应的历史记录，在本次扫描完成后，会自动关联历史的排查记录，历史已经排查过的白名单字段无需再重复排查。

   从DevEco Studio 6.0.0 Beta1开始支持关联历史记录。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/r_UGV4M5QZu-iddiWfY8sw/zh-cn_image_0000002530913790.png?HW-CC-KV=V1&HW-CC-Date=20260427T235722Z&HW-CC-Expire=86400&HW-CC-Sign=5971F82A97820E7497FA6DABA1F47FE6564B70A9EED7EBBAB3BDD68744D6DCBC)
4. 根据涉及的混淆场景，选择一个或多个扫描任务，点击**开始扫描**。关于扫描任务的介绍请参考[扫描任务](ide-build-obfuscation.md#section18125192133818)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/4JM4j8GJTOyjoqWl5Zm1dg/zh-cn_image_0000002530913836.png?HW-CC-KV=V1&HW-CC-Date=20260427T235722Z&HW-CC-Expire=86400&HW-CC-Sign=01E7107B9769F910218E94927D9E360CAE2CA44E36ACE68B8C1F5DB871800F48)
5. 等待扫描成功后，进入[推荐白名单](ide-build-obfuscation.md#section3989185975217)和[待排查白名单](ide-build-obfuscation.md#section42331014105310)配置页面。在扫描的过程中，也可以点击**停止扫描**按钮，结束扫描。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/AwZqM1I4T5WPdjV95QZc0g/zh-cn_image_0000002530913824.png?HW-CC-KV=V1&HW-CC-Date=20260427T235722Z&HW-CC-Expire=86400&HW-CC-Sign=1435C325FAF7CEFCB1D6895458F70D7F9938726494E7CA16AB4249D4AA4C73AA)

### 配置推荐白名单

在推荐白名单配置页面，可以查看扫描出来的推荐配置的保留选项和白名单字段，并一键生成白名单混淆规则文件。

* **使用DevEco Studio 6.0.0 Beta1及以上版本，按以下步骤操作：**
  1. 在页面上方，按照以下的树状结构呈现扫描结果。

     ```
     1. 模块名
     2. ----混淆选项
     3. --------扫描任务：扫描出来推荐配置白名单字段的数量
     ```

     选中一个扫描任务，在页面下方会按照以下的树状结构，显示推荐的保留选项和白名单字段。

     ```
     1. 保留选项
     2. ----关键代码
     3. --------白名单字段 --> 字段所在文件:代码行
     ```

     + **关键代码**：点击关键代码，可以跳转到代码所在的文件和代码行。

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/lElKleR7QPK3Guc7HzWJZw/zh-cn_image_0000002561833717.png?HW-CC-KV=V1&HW-CC-Date=20260427T235722Z&HW-CC-Expire=86400&HW-CC-Sign=F4299F908F19AFEC10AA88717D1E07DC2F45F9C364530096FDAC5024170A5A35)
     + **白名单字段**：点击白名单字段，可以跳转到字段所在的文件和代码行。

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/LGQiPaNjQzadr7cJTT28qw/zh-cn_image_0000002561833741.png?HW-CC-KV=V1&HW-CC-Date=20260427T235722Z&HW-CC-Expire=86400&HW-CC-Sign=8E4F6DDD341F67B014CEFD36CE866975F905A670F51B5EB07070CF67867122ED)
  2. 如果需要将白名单文件生成到工程中，可以点击**生成推荐白名单**按钮，ObfuscationHelper会在对应模块下生成推荐白名单文件Hm-recommend-keep-list.txt/Hm-recommend-consumer-keep-list.txt，并提示对应的文件路径。同时在工程根目录下生成对应的白名单Excel表格obfuscation-helper-xxx.xlsx。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/FYUHe39jT2aenqhB_OibLQ/zh-cn_image_0000002561753757.png?HW-CC-KV=V1&HW-CC-Date=20260427T235722Z&HW-CC-Expire=86400&HW-CC-Sign=FE9422855C54CA09B38BABC26E0CD9A77973AFB86B1B6330FC9D1DC5A3E1D5CE)

     + 点击**OK**，会关闭提示框，停留在推荐白名单场景。
     + 点击**跳转待排查**，会关闭提示框，进入到待排查白名单场景。

     如果勾选**合并白名单文件**，点击**OK**或者**跳转待排查**时，会在工程根目录下生成合并后的白名单文件Hm-merge-recommend-keep-list.txt，该文件会合并entry模块的Hm-recommend-keep-list.txt和所有模块的Hm-recommend-consumer-keep-list.txt。

     如以下模块下生成推荐白名单文件：

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/iluLFEw7SyuRy5csR0kWbg/zh-cn_image_0000002561833713.png?HW-CC-KV=V1&HW-CC-Date=20260427T235722Z&HW-CC-Expire=86400&HW-CC-Sign=BE7284DC8B160925D9003B59611A41A69E7B303E2C39A887DE0E4104A4BAA640)
  3. 在混淆配置中添加白名单文件，有两种方式。
     + 在各模块的build-profile.json5中，将Hm-recommend-keep-list.txt加入到混淆配置files字段下，将Hm-recommend-consumer-keep-list.txt加入到consumerFiles字段下。关于字段的介绍请参考[字段说明](ide-build-obfuscation.md#section88021016154414)。
     + 将合并后的文件Hm-merge-recommend-keep-list.txt配置在entry模块build-profile.json5的files字段下。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/7sHHaKGoSamsZKQ7Z2BrwA/zh-cn_image_0000002530913816.png?HW-CC-KV=V1&HW-CC-Date=20260427T235722Z&HW-CC-Expire=86400&HW-CC-Sign=6A81F851DA367046A42C6C865FD47F63CE9B37C2C5DAF6F2D99EA8745A3F734B)
* **使用DevEco Studio 6.0.0 Beta1以下版本，按以下步骤操作：**
  1. 在页面上方，按照以下的树状结构呈现扫描结果。

     ```
     1. 模块名
     2. ----混淆选项
     3. --------扫描任务：扫描出来推荐配置白名单字段的数量
     ```

     选中一个扫描任务，在页面下方会按照以下的树状结构，显示推荐的保留选项和白名单字段。

     ```
     1. 保留选项
     2. ----关键代码
     3. --------白名单字段 --> 字段所在文件:代码行
     ```

     + **关键代码**：点击关键代码，可以跳转到代码所在的文件和代码行。

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/2P9Evks5SgG7jHnJaKeV2w/zh-cn_image_0000002561833729.png?HW-CC-KV=V1&HW-CC-Date=20260427T235722Z&HW-CC-Expire=86400&HW-CC-Sign=B10CB45915741ED5A4C0E88970FE860D577A244116D53EAD6A51BA590CE3628F)
     + **白名单字段**：点击白名单字段，可以跳转到字段所在的文件和代码行。

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/_9XgGKhWTu2pw8gCh38nSw/zh-cn_image_0000002530753812.png?HW-CC-KV=V1&HW-CC-Date=20260427T235722Z&HW-CC-Expire=86400&HW-CC-Sign=102F49B41D12A02064ACCE6AF4455D818F1D333503E3874479A0A8FC65549F67)
  2. 如果需要将白名单文件生成到工程中，可以点击**生成推荐白名单**按钮，ObfuscationHelper会在对应模块下生成Hm-recommend-keep-list.txt文件，并提示对应的文件路径。同时在工程根目录下生成对应的白名单Excel表格obfuscation-helper-xxx.xlsx。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/c-6QglZgTf-axfLWSt7NJQ/zh-cn_image_0000002530753838.png?HW-CC-KV=V1&HW-CC-Date=20260427T235722Z&HW-CC-Expire=86400&HW-CC-Sign=47C4D49C2E1459D1EA8D406FC7818663305C66306511067E2B6F045620018C67)

     + 点击OK，会关闭提示框，停留在推荐白名单场景。
     + 点击跳转待排查，会关闭提示框，进入到待排查白名单场景。

     如以下模块下生成推荐白名单文件：

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/NhdNlabcSNOHfE63C9N-Bg/zh-cn_image_0000002530753828.png?HW-CC-KV=V1&HW-CC-Date=20260427T235722Z&HW-CC-Expire=86400&HW-CC-Sign=4B02C5CA276F020DAF69927551D1E4CFCD71A198B874B96418A4AAAD3EED6352)
  3. 在模块下的build-profile.json5中，将模块下生成的推荐白名单文件Hm-recommend-keep-list.txt加入到混淆配置files或consumerFiles字段下。关于字段的介绍请参考[字段说明](ide-build-obfuscation.md#section88021016154414)。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/c_GWQlnyTZS9m0wT5xIm8A/zh-cn_image_0000002530913796.png?HW-CC-KV=V1&HW-CC-Date=20260427T235722Z&HW-CC-Expire=86400&HW-CC-Sign=0854973A54F59E07F128D14BC9EDE07EF3E6D3A82A44532FEE61B693098B0914)

### 配置待排查白名单

在待排查白名单配置页面，可以查看扫描出来的关键代码，需要开发者根据业务进一步排查，识别白名单字段并配置到文件中。

* **使用DevEco Studio 6.0.0 Beta1及以上版本，按以下步骤操作：**
  1. 在页面上方，按照以下的树状结构呈现扫描结果。

     ```
     1. 模块名
     2. ----混淆选项
     3. --------扫描任务：扫描出来待排查的关键代码的数量
     ```

     选中一个扫描任务，在页面下方会显示待排查的代码。点击关键代码，可以跳转到代码所在的文件和代码行。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/uXNdmNElQ62bF8cP8ItgMA/zh-cn_image_0000002561833733.png?HW-CC-KV=V1&HW-CC-Date=20260427T235722Z&HW-CC-Expire=86400&HW-CC-Sign=7E9B08552BBDBE15E5476E19EB9D02248FCBBFEB3E244980AA9FA62496AFC72C)
  2. 跳转到关键代码后，根据具体场景识别是否需要配置白名单字段，排查方式请参考[扫描任务](ide-build-obfuscation.md#section18125192133818)。
     + 如果排查后不需要配置白名单，点击**待排查**，选择**已排查**，标记该项已经排查。
     + 如果排查后需要配置白名单，点击**添加白名单**，在输入框中输入保留选项和白名单字段，点击**保存白名单**。保存后该排查项会被标记为已排查。

     被标记为已排查的排查项，后续再次扫描该模块和场景时，如果关联本次的排查记录，将不再需要重复排查。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/83OiAQx4RHewuEAjsjlXOg/zh-cn_image_0000002561753765.png?HW-CC-KV=V1&HW-CC-Date=20260427T235722Z&HW-CC-Expire=86400&HW-CC-Sign=EF37FB0DC86F7866248DC1B060A927333A925B9CA79F9CFDF1BE868C4C6FD883)
  3. 排查完成后，点击**生成排查白名单**按钮，ObfuscationHelper会在对应模块下生成排查白名单文件Hm-manual-keep-list.txt/Hm-manual-consumer-keep-list.txt，并提示对应的文件路径。同时在工程根目录下生成对应的白名单Excel表格obfuscation-helper-xxx.xlsx。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c/v3/L-_1NvjlSQeMB4SFG3GlTg/zh-cn_image_0000002561753775.png?HW-CC-KV=V1&HW-CC-Date=20260427T235722Z&HW-CC-Expire=86400&HW-CC-Sign=3A0AEFF009A04D955F74824D33EFBEB4B43EBF7785B7C480B8BD306BFC9E93E8)

     如果勾选**合并白名单文件**，点击**OK**，会在工程根目录下生成合并后的白名单文件Hm-merge-manual-keep-list.txt，该文件会合并entry模块的Hm-manual-keep-list.txt和所有模块的Hm-manual-consumer-keep-list.txt。

     如以下模块下生成排查白名单文件：

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/sApHCHvbTge7TcoboEuLYg/zh-cn_image_0000002530913800.png?HW-CC-KV=V1&HW-CC-Date=20260427T235722Z&HW-CC-Expire=86400&HW-CC-Sign=7FC6755936D2C7EC67C00B76CDF70C22F927FB20A03F6D101CE14D99FE626EC6)
  4. 在混淆配置中添加白名单文件，有两种方式。
     + 在各模块的build-profile.json5中，将Hm-manual-keep-list.txt加入到混淆配置files字段下，将Hm-manual-consumer-keep-list.txt加入到consumerFiles字段下。关于字段的介绍请参考[字段说明](ide-build-obfuscation.md#section88021016154414)。
     + 将合并后的文件Hm-merge-manual-keep-list.txt配置在entry模块build-profile.json5的files字段下。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/3gSCLT3WQD-SJvmJ2X5ekg/zh-cn_image_0000002561753771.png?HW-CC-KV=V1&HW-CC-Date=20260427T235722Z&HW-CC-Expire=86400&HW-CC-Sign=7F52623251E392FEBAEC360ADB72674A6588053BD60E8494D5FA18A0AB494FE7)
* **使用DevEco Studio 6.0.0 Beta1以下版本，按以下步骤操作：**
  1. 在页面上方，按照以下的树状结构呈现扫描结果。

     ```
     1. 模块名
     2. ----混淆选项
     3. --------扫描任务：扫描出来待排查的关键代码的数量
     ```

     选中一个扫描任务，在页面下方会按照“关键代码 --> 代码所在文件: 代码行”的结构，显示待排查的代码。点击关键代码，可以跳转到代码所在的文件和代码行。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/wMlilElWTo6XiX7dY0Gmpw/zh-cn_image_0000002561833759.png?HW-CC-KV=V1&HW-CC-Date=20260427T235722Z&HW-CC-Expire=86400&HW-CC-Sign=20C315BC8D15C1075C72103E88BAC4F518CBB7F890EBE9EB54C8D9E238610A99)
  2. 跳转到关键代码后，根据具体场景识别是否需要配置白名单字段，排查方式请参考[扫描任务](ide-build-obfuscation.md#section18125192133818)。如果存在需要配置的字段，在上方的输入框中，输入保留选项和对应的白名单字段。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/Urfb9o3sT92Eo6k7brgrKw/zh-cn_image_0000002530753820.png?HW-CC-KV=V1&HW-CC-Date=20260427T235722Z&HW-CC-Expire=86400&HW-CC-Sign=0136E68C616E42EF02617635E2ACAE26DCAE5DA245E8B1429E7F94BB6560090C)
  3. 排查完成后，点击**生成排查白名单**按钮，ObfuscationHelper会在对应模块下生成Hm-manual-keep-list.txt文件，并提示对应的文件路径。同时在工程根目录下生成对应的白名单Excel表格obfuscation-helper-xxx.xlsx。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/jZ4IR0AAR0eQP5pH8Xio2w/zh-cn_image_0000002530913832.png?HW-CC-KV=V1&HW-CC-Date=20260427T235722Z&HW-CC-Expire=86400&HW-CC-Sign=F18D48D389DD1C13586D987375104B4792446DB4063D6F0BD67759FFD28B32E7)

     如以下模块下生成排查白名单文件：

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/eLpWhn38T7KRGpqnqQhJaw/zh-cn_image_0000002561753779.png?HW-CC-KV=V1&HW-CC-Date=20260427T235722Z&HW-CC-Expire=86400&HW-CC-Sign=DC48FB01A08B00B7E53843DFCF40F30501639A1A20ACCA599396A8D5BB6691FE)
  4. 在模块下的build-profile.json5中，将模块下生成的排查白名单文件Hm-manual-keep-list.txt加入到混淆配置files或consumerFiles字段下。关于字段的介绍请参考[字段说明](ide-build-obfuscation.md#section88021016154414)。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/BHeKkD1PRBOnDtqerkdfCQ/zh-cn_image_0000002530913806.png?HW-CC-KV=V1&HW-CC-Date=20260427T235722Z&HW-CC-Expire=86400&HW-CC-Sign=6AB1E5030D8F8CA0C1F65459363386310D0170E5B4A6D459C9E21DA56B86D339)

### 查看历史记录

点击生成推荐白名单或者待排查白名单后，会生成一条历史记录，方便开发者后续查看和继续排查白名单。

在ObfuscationHelper的首页，点击底部的**历史记录**按钮，可查看所有的历史记录。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/D1-29xcWSCG6Jwdzz6uQBA/zh-cn_image_0000002530753816.png?HW-CC-KV=V1&HW-CC-Date=20260427T235722Z&HW-CC-Expire=86400&HW-CC-Sign=D0EC754449E01E719741E419767E67214E423B3EA83AA6E9DAA97D0BCC293188)

* 保存路径是历史记录的缓存文件，鼠标悬停在保存路径上，可以查看白名单文件和Excel表格保存的路径。
* 点击查看详情图标![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/X6xJbhNATKmJR15efdSMew/zh-cn_image_0000002530913818.png?HW-CC-KV=V1&HW-CC-Date=20260427T235722Z&HW-CC-Expire=86400&HW-CC-Sign=B75C2CE3E79E1B640FC2AD8DDB0CAA1EBDE921E2235760BED80E9016ABA07CFB)，可以跳转到对应的白名单场景配置页面。
* 点击删除图标，可以删除指定的历史记录，以及对应的缓存文件和Excel表格，但是不会删除白名单文件。

### 扫描任务

以下是ObfuscationHelper的扫描任务，关于保留选项的原理介绍和排查场景请参考[混淆规则](source-obfuscation.md)。

**属性混淆**

* **JSON数据解析及对象序列化**

  在使用JSON/ArkTSUtils.ASON进行转换时，对象类型中的属性需要被保留。

  ```
  1. // JSON.parse
  2. class JSONTest {
  3. prop1: string = ""
  4. prop2: number = 0
  5. }
  6. // 示例JSON文件test.json
  7. /*
  8. {
  9. "prop1": "value",
  10. "prop2": 10
  11. }
  12. */
  13. const jsonData = buffer.from(this.context.resourceManager.getRawFileContentSync("test.json")).toString();
  14. let demo: JSONTest = JSON.parse(jsonData)       // JSONTest加入keep-property-name
  15. let demo = JSON.parse(jsonData) as JSONTest     // JSONTest加入keep-property-name
  16. let demo = JSON.parse(jsonData) as ESObject as JSONTest      // JSONTest加入keep-property-name
  17. let demo: ESObject = JSON.parse(jsonData)       // 没有明确类型的，包括(ESObject、Object、object)加入待排查白名单中，需要将jsonData中所有的key，如prop1/prop2加入keep-property-name

  19. // ArkTSUtils.ASON.parse
  20. let demo: JSONTest = ArkTSUtils.ASON.parse(jsonData)      // JSONTest加入keep-property-name
  21. let demo = ArkTSUtils.ASON.parse(jsonData) as JSONTest    // JSONTest加入keep-property-name
  22. let demo = ArkTSUtils.ASON.parse(jsonData) as ESObject as ESObject as JSONTest    // JSONTest加入keep-property-name
  23. let demo: ESObject = ArkTSUtils.ASON.parse(jsonData)      // 没有明确类型的，包括(ESObject、Object、object)加入待排查白名单中，需要将jsonData中所有的key，如prop1/prop2加入keep-property-name

  25. // JSON.stringify
  26. let type = new JSONTest()
  27. let str = JSON.stringify(type)    // JSON.stringify加入待排查白名单，需要将JSONTest中的所有属性加入-keep-property-name

  29. // ArkTSUtils.ASON.stringify
  30. let type = new JSONTest()
  31. let str = ArkTSUtils.ASON.stringify(type)  // ArkTSUtils.ASON.stringify加入待排查白名单，需要将JSONTest中的所有属性加入-keep-property-name
  ```
* **通过字符串访问的对象属性**

  通过中括号形式访问的对象属性，以及Object.defineProperty/Object.defineProperties/Object.getOwnPropertyDescriptor接口中的属性需要被保留。

  ```
  1. // 通过中括号形式访问的属性如obj['name']，如果name是变量，加入待排查白名单，需要将name对应的内容加入-keep-property-name
  2. Object.defineProperty(obj, 'y', {})   // 如果y是变量，加入待排查白名单，需要将y对应的内容加入-keep-property-name
  3. Object.defineProperties(obj, {        // 属性prop1/prop2加入推荐白名单-keep-property-name
  4. prop1: {
  5. value: 'Hello',
  6. writable: true,
  7. enumerable: true,
  8. configurable: true
  9. },
  10. prop2: {
  11. value: 'Hello',
  12. writable: true,
  13. enumerable: true,
  14. configurable: true
  15. }
  16. });
  17. Object.getOwnPropertyDescriptor(obj, 'bbb');    // 如果bbb是变量，加入待排查白名单，需要将bbb对应的内容加入-keep-property-name
  18. obj.s=0; let key='s'; obj[key]    // key是变量，加入待排查白名单，需要将key对应的内容s加入keep-property-name
  ```
* **C++侧访问/操作ArkTS对象属性**

  开发者需要根据C++接口来排查与其相关的ArkTS中的属性字符串，并手动加入白名单中，涉及的C++接口参考[使用Node-API接口设置ArkTS对象的属性](use-napi-about-property.md)。

  ```
  1. //index.ets
  2. func() {
  3. let obj: NapiTestClassObj = { napiTestClassObjData: 0, napiTestClassObjMessage: "hello world" };
  4. let result: ESObject = testNapi.setProperty(obj, "napiTestClassObjMessage", "100");    // 根据napi_set_property接口排查到ArkTS中的属性napiTestClassObjMessage被修改，需要将napiTestClassObjMessage加入-keep-property-name白名单
  5. if (obj.napiTestClassObjMessage === "100") {
  6. console.log("setProperty success");
  7. return true;
  8. }
  9. return false;
  10. }
  11. //napi_init.cpp
  12. static napi_value SetProperty(napi_env env, napi_callback_info info) {
  13. size_t argc = 3;
  14. napi_value args[3];
  15. napi_status status = napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);
  16. if (status != napi_ok) {
  17. napi_throw_error(env, nullptr, "Node-API napi_get_cb_info fail");
  18. }
  19. status = napi_set_property(env, args[0], args[1], args[2]);    // 扫描napi_set_property关键API
  20. if (status != napi_ok) {
  21. napi_throw_error(env, nullptr, "Node-API napi_set_property fail");
  22. return nullptr;
  23. }
  24. return args[0];
  25. }
  ```
* **数据库键值对类型（ValuesBucket）中的属性**

  数据库键值对类型（ValuesBucket）中的属性需要被保留。

  ```
  1. const valueBucket: ValuesBucket = {
  2. 'ID1': ID1,    // ID1、NAME1、AGE1、SALARY1加入到-keep-property-name
  3. 'NAME1': name,
  4. 'AGE1': age,
  5. 'SALARY1': salary
  6. };
  ```
* **自定义装饰器修饰的成员变量、方法、参数**

  自定义装饰器修饰的成员变量、方法、参数，需要排查是否加入白名单。

  ```
  1. function logClass(target: any) {
  2. console.log('类被创建：', target);    // MyClass未参与混淆，因此被@logClass修饰的类名不需要加入白名单
  3. return target;
  4. }
  5. export function logMethod(target: any, methodName: string, descriptor: PropertyDescriptor) {
  6. const originalMethod = descriptor.value;
  7. descriptor.value = function (...args: any[]) {
  8. if(methodName === 'myMethod'){    // methodName会被混淆，与'myMethod'作比较不符合预期，因此被@logMethod修饰的方法名myMethod需要加入白名单
  9. console.log('调用myMethod方法')
  10. }
  11. console.log(`方法 ${methodName} 即将被调用，参数为：`, args);
  12. const result = originalMethod.apply(this, args);
  13. console.log(`方法 ${methodName} 调用完毕，结果为：`, result);
  14. return result;
  15. };
  16. return descriptor;
  17. }
  18. function logProperty(target: any, propertyName: string) {
  19. let value;
  20. const getter = function () {
  21. console.log(`正在获取属性 ${propertyName}`);   // propertyName会被混淆，但不影响运行结果，不需要加入白名单
  22. return value;
  23. };
  24. const setter = function (newValue: any) {
  25. console.log(`正在设置属性 ${propertyName}，新值为：${newValue}`);
  26. value = newValue;
  27. };
  28. Object.defineProperty(target, propertyName, {
  29. get: getter,
  30. set: setter,
  31. enumerable: true,
  32. configurable: true
  33. });
  34. return;
  35. }
  36. @logClass
  37. class MyClass {    // 自定义装饰器修饰的类名，需要排查MyClass是否加入白名单
  38. @logProperty
  39. myProperty: number;    // 自定义装饰器修饰的属性，需要排查myProperty是否加入白名单
  40. constructor() {
  41. this.myProperty = 10;
  42. }
  43. @abcd
  44. @logMethod
  45. myMethod(arg1: number, arg2: number) {    // 自定义装饰器修饰的方法，需要排查myMethod是否加入白名单
  46. return arg1 + arg2;
  47. }
  48. }
  ```
* **Record类型对象的属性**

  Record类型对象的属性需要被保留。该场景从DevEco Studio 6.0.1 Beta1版本开始支持。

  ```
  1. // 支持扫描的场景
  2. export function hello() {
  3. const person: Record<string, Object> = {
  4. ddName: 'zhangsan',    // Record类型对象person的属性ddName、ggAge、isWfStudent，加入到-keep-property-name
  5. ggAge: 25,
  6. isWfStudent: true
  7. }
  8. person.wwArea = '112';     // 通过点语法新增的属性wwArea，加入到-keep-property-name
  9. return person;
  10. }
  11. // 不支持扫描的场景
  12. // 1、调用该方法获取Record类型对象，通过点语法添加sssd属性不支持扫描，该属性会被混淆
  13. let ret = hello();
  14. ret.sssd = '1111';
  15. // 2、隐式Record类型的对象parameters的属性a123、b123不支持扫描，会被混淆
  16. export function sendPost3() {
  17. const want: Want = {
  18. action: 'ohos.want.action.viewData',
  19. entities: ['entity.system.browsable'],
  20. uri: '123',
  21. parameters: {
  22. a123: 1,
  23. b123: 2
  24. }
  25. };
  26. }
  ```

**顶层作用域名称混淆**

* **namespace中导出的名称**

  namespace中导出的名称、嵌套namespace中导出的名称都需要被保留。

  ```
  1. export namespace namespace1 {
  2. export class namespace1Class1 {      // namespace1Class1加入推荐白名单-keep-global-name
  3. }
  4. export namespace namespace1_1 {      // namespace1_1加入推荐白名单-keep-global-name
  5. export let namespace1Property1_1: string = '111';      // namespace1Property1_1加入推荐白名单-keep-global-name
  6. export function namespace1Func1_1() {      // namespace1Func1_1加入推荐白名单-keep-global-name
  7. console.log('namespace1Func1_1 execute success');
  8. }
  9. export class namespaceClass1_1{      // namespaceClass1_1加入推荐白名单-keep-global-name
  10. func(){
  11. console.log(""namespaceClass1_1 success"")
  12. }
  13. }
  14. }
  15. }
  ```
* **动态导入的名称**

  动态导入的接口名、属性名和类名，需要被保留。该场景从DevEco Studio 6.0.0 Beta2版本开始支持。

  ```
  1. // 导入模块后，使用的类名TestClass加入推荐白名单keep-global-name
  2. try {
  3. let test = (await import('../model/TestClass')).TestClass
  4. console.warn(TAG, 'test = ', test);
  5. // console.warn(TAG, 'test TestClass = ', test.);
  6. console.warn(TAG, 'test staticGlsAdd = ', test.staticGlsAdd(5, 6));
  7. } catch (e) {
  8. console.warn(TAG, `error = ${e}`);
  9. }
  10. // 导入模块后，使用的方法名componentClass加入推荐白名单keep-global-name
  11. let util = await import('harlibrary/src/main/ets/utils/Util');
  12. try {
  13. console.warn(TAG, 'util = ', util);
  14. console.warn(TAG, 'call util function = ', await util.componentClass());
  15. } catch (e) {
  16. console.warn(TAG, `error = ${e}`);
  17. }
  18. // 导入模块后，使用default后调用的方法warn加入推荐白名单keep-global-name
  19. import('hsplibrary/src/main/ets/utils/Logger').then(logger => {
  20. try {
  21. console.warn(TAG, 'import Logger success.');
  22. logger.default.warn('this is logger warn')
  23. } catch (e) {
  24. console.warn(TAG, `error = ${e}`);
  25. }
  26. })
  27. // 将动态导入封装为方法，导出的类实例如果是变量，加入待排查白名单，需要排查后将变量对应的值加入keep-global-name
  28. public static importFile<T>(modulePath: string, resultClassName: string) {
  29. return import(modulePath).then((ns: ESObject) => {
  30. let res: T = new ns[resultClassName]();   // 该行加入待排查白名单，排查后将resultClassName对应的值TestClass加入keep-global-name
  31. return res;
  32. }).catch((err: Error) => {
  33. console.warn('chisj debug: importFile error = ', err);
  34. return undefined;
  35. });
  36. }
  37. // Index.ets
  38. let modulePath = '../model/TestClass';
  39. let className = 'TestClass';
  40. ImportUtil.importFile<ESObject>(modulePath, className).then((ns:ESObject) => {
  41. try {
  42. console.warn(TAG, 'import importFile success')
  43. console.warn(TAG, 'ns = ', ns)
  44. console.warn(TAG, 'calcAdd = ', ns?.calcAdd(1, 2));
  45. } catch (e) {
  46. console.warn(TAG, `error = ${e}`);
  47. }
  48. })
  49. // 将动态导入封装为方法，导出的模块myModule调用的方法Calc加入推荐白名单
  50. // ImportUtil.ts
  51. export function dynamicImport<T>(modulePath: string): Promise<T> {
  52. return import(modulePath).then(module => {
  53. // 有些模块可能有默认导出，这里处理一下
  54. return module.default || module as T;
  55. });
  56. }
  57. // Index.ets
  58. const myModule = await dynamicImport<typeof import('harlibrary')>('harlibrary');
  59. console.warn(TAG, '1 calc = ', myModule.Calc(1, 2))
  ```

**文件名名称混淆**

* **动态导入的路径名**

  模块下build-profile.json5文件中，sources字段对应的路径名需要被保留。

  ```
  1. // 模块级build-profile.json5
  2. {
  3. "apiType": "stageMode",
  4. "buildOption": {
  5. "arkOptions": {"runtimeOnly": {"sources": ["./aaa/bbb", "./ccc/dddd"]}}  //./aaa/bbb和./ccc/dddd加入keep-file-name
  6. },
  7. "buildOptionSet": [
  8. {
  9. "name": "release",
  10. "arkOptions": {
  11. "runtimeOnly": {"sources": ["./e/f", "./g/h"]},  // ./e/f和./g/h加入keep-file-name
  12. "obfuscation": {
  13. "ruleOptions": {
  14. "enable": true,
  15. "files": [
  16. "./obfuscation-rules.txt"
  17. ]
  18. }
  19. }
  20. },
  21. },
  22. ],
  23. ......
  24. }
  ```
* **传递给动态路由的路径名**

  模块下resources/base/profile/route\_map.json中，pageSourceFile字段对应的路径名需要被保留。

  ```
  1. // 模块下resources/base/profile/route_map.json文件
  2. {
  3. "routerMap": [
  4. {
  5. "name": "PageOne",
  6. "pageSourceFile": "src/main/ets/pages/directory/PageOne.ets",  // src/main/ets/pages/directory/PageOne.ets加入keep-file-name
  7. "buildFunction": "PageOneBuilder",
  8. "data": {
  9. "description" : "this is PageOne"
  10. }
  11. }
  12. ]
  13. }
  ```

**导入/导出名称混淆**

* **从so库导入的接口**

  从so库中导入的接口及其点式调用的属性，需要被保留。

  ```
  1. import testNapi from "xxxx.so"    // testNapi加入keep-global-name
  2. import {testNapi} from "xxxx.so"  // testNapi加入keep-global-name
  3. import {testNapi as napi} from "xxxx.so"    // testNapi加入keep-global-name
  4. testNapi.add()    // add加入-keep-property-name
  ```
* **hsp对外暴露的接口**

  hsp的入口文件(一般为index.ets)中导出的接口名及其属性名，需要被保留。

  ```
  1. // 导出的常量
  2. export const LOCAL_NUM = 100  // LOCAL_NUM加入keep-global-name
  3. // 导出的方法
  4. export function harFun() {    // harFun加入keep-global-name
  5. }
  6. // 导出的类名及其属性(包括该类的父类和属性)，如果属性也是一个类，该类也需要以同样的方式保留。
  7. class FatherClass {
  8. prop4: string = "bbb"
  9. }
  10. class SubClass {
  11. prop3: string = "bbb"
  12. }
  13. export class HSPClass extends FatherClass{    // 类名称HSPClass加入到-keep-global-name
  14. prop1: string = "aaa"
  15. prop2: SubClass = new SubClass()    // 属性prop1,prop2,prop3,prop4加入到-keep-property-name
  16. }

  18. // 导出的namespace，包括其中的方法、常量、类(保留方式同上)、子namespace
  19. export namespace NmSpace {
  20. export const NUM_NAME_SPACE = 100   // 常量NUM_NAME_SPACE加入-keep-global-name
  21. export class classNameSpace {       // 类名称classNameSpace加入-keep-global-name
  22. prop: string = "bbb"             // 类属性prop加入-keep-property-name
  23. }
  24. export function funNameSpace() {    // 方法funNameSpace加入-keep-global-name
  25. }
  26. }
  27. // 将入口文件相对路径,如 ./index.ets加入keep保留选项。
  28. // 将入口文件名如index.ets加入keep-file-name保留选项。
  ```
* **从hsp导入的接口**

  从hsp中导入的接口及其点式调用的属性，需要被保留。

  ```
  1. import MyClass1 from "xxxx"     // MyClass1加入keep-global-name
  2. import {MyClass2} from "xxxx"   // MyClass2加入keep-global-name
  3. import {MyClass3 as MyClass} from "xxxx"    // MyClass3加入keep-global-name
  4. MyClass1.add()    // add加入keep-property-name
  ```
* **har对外暴露的接口**

  参考[hsp对外暴露的接口](ide-build-obfuscation.md#li15198347161014)。

  仅当hap->hsp->har，同时hap->har时，该har会被扫描，其中->表示依赖关系。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/uM1GnTitRLWRvCDDmr-xRQ/zh-cn_image_0000002561833755.png?HW-CC-KV=V1&HW-CC-Date=20260427T235722Z&HW-CC-Expire=86400&HW-CC-Sign=CE4ACD64F214183CAB7D6BF525EA550ED984E0ED07D3A626D5B1C446444CAB24)
