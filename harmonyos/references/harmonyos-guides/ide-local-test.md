---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-local-test
title: Local Test
breadcrumb: 指南 > 编写与调试应用 > 开发自测试 > 测试框架 > 代码测试 > Local Test
category: harmonyos-guides
scraped_at: 2026-04-29T13:46:59+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:ca9d4d3096c5a2ef67165275c1d78ae1978b43054918d66b8fd7488d3eaab7bb
---

说明

当前不支持测试C/C++方法及系统API。

## 创建Local Test测试用例

1. 在工程目录下打开待测试模块（支持HAP、HAR、HSP模块）下的ets文件，将光标置于代码中任意位置，单击**右键 > Show Context Actions** **> Create Local Test**或快捷键**Alt+Enter****（macOS为Option+Enter） > Create Local Test**创建测试类。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/hfCTfnL8SA64uPxCdycxmw/zh-cn_image_0000002561833569.png?HW-CC-KV=V1&HW-CC-Date=20260429T054657Z&HW-CC-Expire=86400&HW-CC-Sign=998277FAC36E4D4E7A9B78F1CA19B53D326F8F133E55CD4EEAEC2410333673B5)
2. 在弹出的Create Local Test窗口，输入或选择如下参数。
   * **Testing library**：测试类型，默认为DECC-ArkTSUnit。
   * **ArkTS name**：创建的测试文件名称，测试文件中包含了测试用例。测试文件名称要求在工程目录范围内具有唯一性，仅支持字母、数字、下划线（\_）和点（.）。
   * **Destination package**：测试文件存放的位置，建议存放在待测试模块的test目录下。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0e/v3/yzHJub7JTsmk7GsW9a9AWA/zh-cn_image_0000002561753591.png?HW-CC-KV=V1&HW-CC-Date=20260429T054657Z&HW-CC-Expire=86400&HW-CC-Sign=B2A5CBF948B81ADF22DEA82A4406243E10B8E2956F04B3B53C7D02A2F8CC1D14)
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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/xkjvR168RJirWJheFiAKlw/zh-cn_image_0000002530753656.png?HW-CC-KV=V1&HW-CC-Date=20260429T054657Z&HW-CC-Expire=86400&HW-CC-Sign=A7BC684E7D45E9B18E05920E4E0F2123F467060F3827211542B632B66A99CEEC)

也可以通过如下方式，执行Local Test：

* 在工具栏主菜单单击**Run > Run'测试名称'**。
* 在DevEco Studio的右上角，选择一项测试任务的配置，然后单击右侧的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/F4DlrwPeSLajlUdvtKC1ug/zh-cn_image_0000002530913656.png?HW-CC-KV=V1&HW-CC-Date=20260429T054657Z&HW-CC-Expire=86400&HW-CC-Sign=0EF524CB659EE5099B9D8F8CD272FDF3B1488C3FADA8F239363968A1A22BBBCC)按钮，执行Local Test。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/9PguAvtiS4WBACuiBKKxFg/zh-cn_image_0000002561753609.png?HW-CC-KV=V1&HW-CC-Date=20260429T054657Z&HW-CC-Expire=86400&HW-CC-Sign=DEFF21FB531E1097BFD5FE780560528B1BDFBFE8A33DB5AECAD7CBDEE40518BF)

执行完测试任务后，查看测试结果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/g5xkXvzdQFGjF4EUZcTsIg/zh-cn_image_0000002530753644.png?HW-CC-KV=V1&HW-CC-Date=20260429T054657Z&HW-CC-Expire=86400&HW-CC-Sign=438AC02D941A8D86F5DB2C6AF9C55A1B5B737169A3A28232D4394A77614EF1EA)

### 调试模式

调试模式相比运行模式增加了断点管理功能。在断点命中时，可以选择单步执行、步入步出、进入下个断点等方式进行调试，另外可以使用线程堆栈可视化、变量和表达式可视化功能，快速定位问题。

以文件级别为例，在添加断点之后，在工程目录中，选中文件，单击**右键 > Debug'测试文件名称'**，以调试模式执行测试任务。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/hrydCAXLSNyqVY0ExZS0MQ/zh-cn_image_0000002530753642.png?HW-CC-KV=V1&HW-CC-Date=20260429T054657Z&HW-CC-Expire=86400&HW-CC-Sign=6A5EF098AEC719F1D5783950DD0A72659187D3F28E8A486623AE8570847FF9F8)

在断点命中时，下方将出现Debug窗口。开发者可在该窗口中进行断点管理与基础调试能力的可视化操作，在断点命中时可查看当前线程的变量和堆栈信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/zKuHMS9uSnGUsnn3kRk96w/zh-cn_image_0000002530753666.png?HW-CC-KV=V1&HW-CC-Date=20260429T054657Z&HW-CC-Expire=86400&HW-CC-Sign=1C1787DA5A3C20FA4E2905936A63CA38DB92A0F19FB090D5C001CD970BBF3491)

断点命中时，在代码编辑器窗口单击右键，在弹出的菜单中将出现调试模式特有功能，如计算表达式、添加变量监视等。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/NAJvOvCyT5yWZs54I5abpg/zh-cn_image_0000002561833587.png?HW-CC-KV=V1&HW-CC-Date=20260429T054657Z&HW-CC-Expire=86400&HW-CC-Sign=DDBFF58B8F78C5A639060DD1B547EBB23E88F13E06DEEDC3B956319132BEE58E)

在跳出所有断点后，测试结束，与运行模式相同，在测试窗口查看测试结果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/TdU3OQ7aQGuk6bFbfpkVVQ/zh-cn_image_0000002561753599.png?HW-CC-KV=V1&HW-CC-Date=20260429T054657Z&HW-CC-Expire=86400&HW-CC-Sign=8BEE03DD5A1EC62CA1CFA7F4BA62648E00849D86F60B4369AD5D4E9F3A57488D)

### 覆盖率统计模式

在LocalTest运行的基础上支持代码覆盖率统计，当前仅支持ArkTS工程。

开发者可以自定义需要参与覆盖率测试的文件，具体配置方法请参考[配置覆盖率过滤文件](ide-ui-test.md#section13756446154)。

如前所述，覆盖率统计模式也有多级别入口，以文件级别为例，有两种方式启动测试：

* 方式一：在工程目录中，选中文件，单击**右键 > Run '测试文件名称' with Coverage**，以覆盖率统计模式执行测试任务。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/E9WpQAQETFqPi8jwcqqJaw/zh-cn_image_0000002530913648.png?HW-CC-KV=V1&HW-CC-Date=20260429T054657Z&HW-CC-Expire=86400&HW-CC-Sign=12B4D743780E14BA5BEBAF39D85E0DDA9F5FBA08A26043429799FBE9840521ED)

* 方式二：在DevEco Studio的右上角，选择测试任务，然后单击右侧的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/niQ3tzS9TMSks4fh6i0O6g/zh-cn_image_0000002561753581.png?HW-CC-KV=V1&HW-CC-Date=20260429T054657Z&HW-CC-Expire=86400&HW-CC-Sign=B501120A19F9FE7E616377B1407986C8E04DE09E073F5F6AFAF22B51441EA885)按钮，执行测试。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/T3qs5l8DQYq8JaIBr61whw/zh-cn_image_0000002530913666.png?HW-CC-KV=V1&HW-CC-Date=20260429T054657Z&HW-CC-Expire=86400&HW-CC-Sign=9B73FF77F10F07E385EBE8B684E5095247CC34F6C2343CBF59F381156A5EE54B)

启动测试后，进行编译构建，底部将出现Cover窗口，构建结束后自动拉起Cover窗口，测试任务结束后，窗口中会打印测试报告的路径。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/rg8VPVM0TeyadqFK0xm1MA/zh-cn_image_0000002530913638.png?HW-CC-KV=V1&HW-CC-Date=20260429T054657Z&HW-CC-Expire=86400&HW-CC-Sign=662E13F433A17CA3E6299C794E6BA978277000C80BF37716170CBFCA98716EEB)

点击链接可打开报告，查看代码覆盖率详情，关于覆盖率的计算方式请参考[查看覆盖率报告](ide-ui-test.md#section10394362109)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/HIovrxZmQTak0x6C6ojcDg/zh-cn_image_0000002561833561.png?HW-CC-KV=V1&HW-CC-Date=20260429T054657Z&HW-CC-Expire=86400&HW-CC-Sign=5DF2F624D0463B840E4844F01D57B0C2392EE899E23BF45290C088941EED5F4B)

在Cover窗口中，单击rerun按钮可以按照之前的设置，重新执行覆盖率用例。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/oWw_ecYqSp2XxeZD3CeeLA/zh-cn_image_0000002530753648.png?HW-CC-KV=V1&HW-CC-Date=20260429T054657Z&HW-CC-Expire=86400&HW-CC-Sign=EA6541639151A577C9748EC4A36E87ED24482FA39BF96D22CC550090DE855E3F)

## （可选）自定义测试用例运行任务

默认情况下，测试用例可直接运行。如果需要自定义测试用例运行任务，可通过如下方法进行设置。

1. 在工具栏主菜单单击**Run**>**Edit Configurations**，进入Run/Debug Configurations界面。
2. 在**Run/Debug Configurations**界面，单击**+**按钮，在弹出的下拉菜单中，单击**Local Test**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ca/v3/8LqjE63VTxC2lBGfbwXeHg/zh-cn_image_0000002530913632.png?HW-CC-KV=V1&HW-CC-Date=20260429T054657Z&HW-CC-Expire=86400&HW-CC-Sign=2E2582A4C1FD220A9908215D339CF8B34D64D8B91E565219A30734FDA8BA35A1)
3. 根据实际情况，配置Local Test的运行参数。 然后单击**OK**，完成配置。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/DfheIL-3T5yIanZywKWznA/zh-cn_image_0000002561753575.png?HW-CC-KV=V1&HW-CC-Date=20260429T054657Z&HW-CC-Expire=86400&HW-CC-Sign=E9A147EAB114CEF0309A1F72BDA63C40F171365641A096308688EF5AE1929931)

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
