---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-local-test
title: Local Test
breadcrumb: 指南 > 编写与调试应用 > 开发自测试 > 测试框架 > 代码测试 > Local Test
category: harmonyos-guides
scraped_at: 2026-04-28T07:57:01+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:4f3c29bfd10c834045ffcca181821066735bd9b796a14608b3cb8183208875fc
---

说明

当前不支持测试C/C++方法及系统API。

## 创建Local Test测试用例

1. 在工程目录下打开待测试模块（支持HAP、HAR、HSP模块）下的ets文件，将光标置于代码中任意位置，单击**右键 > Show Context Actions** **> Create Local Test**或快捷键**Alt+Enter****（macOS为Option+Enter） > Create Local Test**创建测试类。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/XEgEY4QaSDmvsb2mx5F1Nw/zh-cn_image_0000002561833569.png?HW-CC-KV=V1&HW-CC-Date=20260427T235659Z&HW-CC-Expire=86400&HW-CC-Sign=183B740B6F7A7ACF0481C11898053586883D1F85F08774B7E22A43440E93B932)
2. 在弹出的Create Local Test窗口，输入或选择如下参数。
   * **Testing library**：测试类型，默认为DECC-ArkTSUnit。
   * **ArkTS name**：创建的测试文件名称，测试文件中包含了测试用例。测试文件名称要求在工程目录范围内具有唯一性，仅支持字母、数字、下划线（\_）和点（.）。
   * **Destination package**：测试文件存放的位置，建议存放在待测试模块的test目录下。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/mddRWpuRQMq1t9wxJVIqQQ/zh-cn_image_0000002561753591.png?HW-CC-KV=V1&HW-CC-Date=20260427T235659Z&HW-CC-Expire=86400&HW-CC-Sign=F3501C2EF4F041B753E0EAD6C2662EF8BEE645F5EE87754ED248CA532DCD0A2A)
3. DevEco Studio在test目录下自动生成对应的测试类。在测试类中，DevEco Studio会生成对应方法的用例模板，具体测试代码需要开发者根据业务逻辑进行开发，具体请参考[单元测试框架](unittest-guidelines.md)。

   说明

   您也可以手动在test文件夹下创建测试用例，手动创建后，需要在List.test.ets文件中添加创建的用例类。

## 运行Local Test测试用例

### 运行模式

可以采用运行工程目录（test）、测试文件（如Index.test.ets）、测试套件（describe）、测试方法（it）的方式来执行Local Test，各级别测试执行入口如下。

|  |  |
| --- | --- |
|  |  |
| 目录级 | 文件级 |
|  |  |
| 套件级 | 方法级 |

以文件级别为例，在工程目录中，选中文件，单击**右键 > Run'测试文件名称'**，执行测试。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/KEmLxT7XSxil-iuu8VCJGA/zh-cn_image_0000002530753656.png?HW-CC-KV=V1&HW-CC-Date=20260427T235659Z&HW-CC-Expire=86400&HW-CC-Sign=56A359EAB73C293C7F76D6CBE362CD21310F4495A8D852FC0AB88E7FFC909184)

也可以通过如下方式，执行Local Test：

* 在工具栏主菜单单击**Run > Run'测试名称'**。
* 在DevEco Studio的右上角，选择一项测试任务的配置，然后单击右侧的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/6z9-pSV_RkeTGNLWs-VRAA/zh-cn_image_0000002530913656.png?HW-CC-KV=V1&HW-CC-Date=20260427T235659Z&HW-CC-Expire=86400&HW-CC-Sign=1AB241C9CFD5FC797E88181A1EA470C9223773EA8166AC8507A5619C9F9621FE)按钮，执行Local Test。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/s5_23hySSHu8PN6-MmmkKw/zh-cn_image_0000002561753609.png?HW-CC-KV=V1&HW-CC-Date=20260427T235659Z&HW-CC-Expire=86400&HW-CC-Sign=B5ABE3D644FBA61AEBD2774C4826990EED231D2C443A14F9335E953C337BF759)

执行完测试任务后，查看测试结果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/4NM6lVvbQGa6I29JU8NOpg/zh-cn_image_0000002530753644.png?HW-CC-KV=V1&HW-CC-Date=20260427T235659Z&HW-CC-Expire=86400&HW-CC-Sign=258898F4CBF66D4B6A25F82BED0A711680129BC20A1B2754C877E848A5282EC9)

### 调试模式

调试模式相比运行模式增加了断点管理功能。在断点命中时，可以选择单步执行、步入步出、进入下个断点等方式进行调试，另外可以使用线程堆栈可视化、变量和表达式可视化功能，快速定位问题。

以文件级别为例，在添加断点之后，在工程目录中，选中文件，单击**右键 > Debug'测试文件名称'**，以调试模式执行测试任务。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/jlrZ-9MLSFau8ZihLQzf7w/zh-cn_image_0000002530753642.png?HW-CC-KV=V1&HW-CC-Date=20260427T235659Z&HW-CC-Expire=86400&HW-CC-Sign=9A66272E08C6E36A679F20FA5104B2CD16C0446D15442B6C46DA7625D1484733)

在断点命中时，下方将出现Debug窗口。开发者可在该窗口中进行断点管理与基础调试能力的可视化操作，在断点命中时可查看当前线程的变量和堆栈信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/oDrE4OSETDua1smc7nzBLA/zh-cn_image_0000002530753666.png?HW-CC-KV=V1&HW-CC-Date=20260427T235659Z&HW-CC-Expire=86400&HW-CC-Sign=A012A3D5B9BAC772423A8BCAE558F8166CB8269B44E694DA09D365D018ECFADE)

断点命中时，在代码编辑器窗口单击右键，在弹出的菜单中将出现调试模式特有功能，如计算表达式、添加变量监视等。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/07P-j6VjRD2i3P5TKzxrPQ/zh-cn_image_0000002561833587.png?HW-CC-KV=V1&HW-CC-Date=20260427T235659Z&HW-CC-Expire=86400&HW-CC-Sign=B383B4FD7161931227ACEAC5D12CB16B354A3CF9A79067266792CB7C9D4A30E4)

在跳出所有断点后，测试结束，与运行模式相同，在测试窗口查看测试结果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/Ru6-NemlSW6LCR5-fctpdQ/zh-cn_image_0000002561753599.png?HW-CC-KV=V1&HW-CC-Date=20260427T235659Z&HW-CC-Expire=86400&HW-CC-Sign=2B8394C7D850E2B425E7770479CA56C6E35414269BEAF3D34610AB762CE1FA7F)

### 覆盖率统计模式

在LocalTest运行的基础上支持代码覆盖率统计，当前仅支持ArkTS工程。

开发者可以自定义需要参与覆盖率测试的文件，具体配置方法请参考[配置覆盖率过滤文件](ide-ui-test.md#section13756446154)。

如前所述，覆盖率统计模式也有多级别入口，以文件级别为例，有两种方式启动测试：

* 方式一：在工程目录中，选中文件，单击**右键 > Run '测试文件名称' with Coverage**，以覆盖率统计模式执行测试任务。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/hQD-BiViR_GcIhjXLRx7UA/zh-cn_image_0000002530913648.png?HW-CC-KV=V1&HW-CC-Date=20260427T235659Z&HW-CC-Expire=86400&HW-CC-Sign=07B610AB1B6E3D7A956723420474084026618D48DAEDBF7423295ECC1B5D1747)

* 方式二：在DevEco Studio的右上角，选择测试任务，然后单击右侧的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/GW1ixM-UQTa4x5VXIxM_LA/zh-cn_image_0000002561753581.png?HW-CC-KV=V1&HW-CC-Date=20260427T235659Z&HW-CC-Expire=86400&HW-CC-Sign=548AC7500C675DE69799D4EAC4F66D3916AC2323BA7498CA002BFFAB04AC33E3)按钮，执行测试。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3/v3/ql-tnShXQd-QHpN8crQp2g/zh-cn_image_0000002530913666.png?HW-CC-KV=V1&HW-CC-Date=20260427T235659Z&HW-CC-Expire=86400&HW-CC-Sign=ADC1505D9B4C17A91E7CC729BF8EE3A2F240EC4907E07A608D6BA7355CAF6831)

启动测试后，进行编译构建，底部将出现Cover窗口，构建结束后自动拉起Cover窗口，测试任务结束后，窗口中会打印测试报告的路径。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/gfvasKBkQva4S4SkRe_1YQ/zh-cn_image_0000002530913638.png?HW-CC-KV=V1&HW-CC-Date=20260427T235659Z&HW-CC-Expire=86400&HW-CC-Sign=ACC1CE4644A9D5219A1F7DAFFA510C6E7FA76CC7C66B84EC1B949A9DA8D8CAB6)

点击链接可打开报告，查看代码覆盖率详情，关于覆盖率的计算方式请参考[查看覆盖率报告](ide-ui-test.md#section10394362109)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/vV-bzoK3SLCs8QnzNiI1YA/zh-cn_image_0000002561833561.png?HW-CC-KV=V1&HW-CC-Date=20260427T235659Z&HW-CC-Expire=86400&HW-CC-Sign=ADF2E3F9B719A3FD34B6E2CB47A91B503449FA456960565D7C156711C41025C2)

在Cover窗口中，单击rerun按钮可以按照之前的设置，重新执行覆盖率用例。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/95LfFWDwQB2n7lBd_SFQpQ/zh-cn_image_0000002530753648.png?HW-CC-KV=V1&HW-CC-Date=20260427T235659Z&HW-CC-Expire=86400&HW-CC-Sign=005F8787C11D88220800AB5F511F8811957E4854BB0E652CD2515C959BC0DD4E)

## （可选）自定义测试用例运行任务

默认情况下，测试用例可直接运行。如果需要自定义测试用例运行任务，可通过如下方法进行设置。

1. 在工具栏主菜单单击**Run**>**Edit Configurations**，进入Run/Debug Configurations界面。
2. 在**Run/Debug Configurations**界面，单击**+**按钮，在弹出的下拉菜单中，单击**Local Test**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/M50VBc1JQ1KTMSw1LeXZYQ/zh-cn_image_0000002530913632.png?HW-CC-KV=V1&HW-CC-Date=20260427T235659Z&HW-CC-Expire=86400&HW-CC-Sign=16D72074BB0D887253723E338FB03091EA4EE8065F8D9C175D9145B0FE22A1F0)
3. 根据实际情况，配置Local Test的运行参数。 然后单击**OK**，完成配置。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/slR2_WuPQjO4hluW5qJOxg/zh-cn_image_0000002561753575.png?HW-CC-KV=V1&HW-CC-Date=20260427T235659Z&HW-CC-Expire=86400&HW-CC-Sign=E63C484166004FEE0BA10BF91F28923B1ED5BAEF92EFF9AC5E5EF7EBE18E35F7)

## 使用命令行执行Local Test

通过命令行方式执行Local Test，在工程根目录下执行命令：

```
1. hvigorw test -p module={moduleName} -p coverage={true | false} -p scope={suiteName}#{methodName}
```

* module：执行测试的模块。缺省默认是执行所有模块的用例。
* coverage：是否生成覆盖率报告，缺省默认是true，在<module-path>/.test/default/outputs/test/reports路径下生成两份报告，一份是html格式（index.html），一份是json格式（coverageReport.json），具体参考[查看覆盖率报告](ide-ui-test.md#section10394362109)。
* scope：格式为{suiteName}#{methodName}或{suiteName}，分别表示测试用例级别或测试套件级别的测试，缺省默认是执行当前模块的所有用例。

说明

* 多个module和scope之间用英文逗号隔开。
* 暂不支持在Linux上执行该命令。

测试结果文件：<module-path>/.test/default/intermediates/test/coverage\_data/test\_result.txt
