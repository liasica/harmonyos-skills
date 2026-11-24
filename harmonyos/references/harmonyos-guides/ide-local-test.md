---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-local-test
title: 本地测试（Local Test）
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 开发自测试 > 测试框架 > 代码测试 > 本地测试（Local Test）
category: harmonyos-guides
scraped_at: 2026-11-24T12:42:31+08:00
doc_updated_at: 2026-10-10
content_hash: sha256:516e844214dca7b3b202afd8b875f3913921c32c497aea9d6809cce1d6683d9c
---

**说明** 

当前不支持测试C/C++方法及系统API。

## 创建Local Test测试用例

1. 在工程目录下打开待测试模块（支持HAP、HAR、HSP模块）下的ets文件，将光标置于代码中任意位置，单击**右键 > Show Context Actions** **> Create Local Test**或快捷键**Alt+Enter****（macOS为Option+Enter） > Create Local Test**创建测试类。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/iXIv4I7GQLOGtmM0KkCqCw/zh-cn_image_0000002779567518.png?HW-CC-KV=V1&HW-CC-Date=20261124T044231Z&HW-CC-Expire=31536000000&HW-CC-Sign=49EA795B111E214FCF9E2F19E11E1D6F3617F835AF54FA28D3D590C348225D12)
2. 在弹出的Create Local Test窗口，输入或选择如下参数。
   * **Testing library**：测试类型，默认为DECC-ArkTSUnit。
   * **ArkTS name**：创建的测试文件名称，测试文件中包含了测试用例。测试文件名称要求在工程目录范围内具有唯一性，仅支持字母、数字、下划线（\_）和点（.）。
   * **Destination package**：测试文件存放的位置，建议存放在待测试模块的test目录下。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/MUe61XvfRISM9kjL9I9EkA/zh-cn_image_0000002808767097.png?HW-CC-KV=V1&HW-CC-Date=20261124T044231Z&HW-CC-Expire=31536000000&HW-CC-Sign=117AB9EDCF12A6139CF8B364143BAE15CB25250B03DD5527222F6AD2117256C0)
3. DevEco Studio在test目录下自动生成对应的测试类。在测试类中，DevEco Studio会生成对应方法的用例模板，具体测试代码需要开发者根据业务逻辑进行开发，具体请参考[单元测试框架](unittest-guidelines.md)。

   **说明** 

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/zwHiFVcoTUulQHk9WafCaA/zh-cn_image_0000002808887183.png?HW-CC-KV=V1&HW-CC-Date=20261124T044231Z&HW-CC-Expire=31536000000&HW-CC-Sign=6944EC345C1A3F6343E5B91CD99540A847496F8453B1BF059B7F6841924EAB0F)

也可以通过如下方式，执行Local Test：

* 在工具栏主菜单单击**Run > Run'测试名称'**。
* 在DevEco Studio的右上角，选择一项测试任务的配置，然后单击右侧的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/s8GbBglFQYqJvHNnbZHTTA/zh-cn_image_0000002779407544.png?HW-CC-KV=V1&HW-CC-Date=20261124T044231Z&HW-CC-Expire=31536000000&HW-CC-Sign=08995404C088FDA81771E89DE92E19D0886A5694F4FA787828FCAF5E0059DD20)按钮，执行Local Test。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/WhdAb6PWQHyJ8j1f2Y__EQ/zh-cn_image_0000002779407546.png?HW-CC-KV=V1&HW-CC-Date=20261124T044231Z&HW-CC-Expire=31536000000&HW-CC-Sign=4DB489694FDA8CA2C6A0F2F00864D2E21417938B82925B2B1D5BD0E30B5F73DD)

执行完测试任务后，查看测试结果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/wiERIucEQUG4ParmEbCbTQ/zh-cn_image_0000002779567516.png?HW-CC-KV=V1&HW-CC-Date=20261124T044231Z&HW-CC-Expire=31536000000&HW-CC-Sign=CCBA359BFD24353A162BD8217D2AA74AF7A58FB2C67B224214067E1E0DC57783)

### 调试模式

调试模式相比运行模式增加了断点管理功能。在断点命中时，可以选择单步执行、步入步出、进入下个断点等方式进行调试，另外可以使用线程堆栈可视化、变量和表达式可视化功能，快速定位问题。

以文件级别为例，在添加断点之后，在工程目录中，选中文件，单击**右键 > Debug'测试文件名称'**，以调试模式执行测试任务。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/GrQ9X1qAQdqnrPzNRWSqkg/zh-cn_image_0000002779407536.png?HW-CC-KV=V1&HW-CC-Date=20261124T044231Z&HW-CC-Expire=31536000000&HW-CC-Sign=EE37865978031A9A7ECB9902F3447D98A28AAA2C47A0E2607F2CACEE96C81E35)

在断点命中时，下方将出现Debug窗口。开发者可在该窗口中进行断点管理与基础调试能力的可视化操作，在断点命中时可查看当前线程的变量和堆栈信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/miOax2l2SR-gPgV6SghDmA/zh-cn_image_0000002779567522.png?HW-CC-KV=V1&HW-CC-Date=20261124T044231Z&HW-CC-Expire=31536000000&HW-CC-Sign=6C343B0A0114C36E44FBBE5E31E27E34679A8431F91E6877091E4B2C5997D453)

断点命中时，在代码编辑器窗口单击右键，在弹出的菜单中将出现调试模式特有功能，如计算表达式、添加变量监视等。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/4FdCSzSURYK1u96ck5qpaA/zh-cn_image_0000002808767101.png?HW-CC-KV=V1&HW-CC-Date=20261124T044231Z&HW-CC-Expire=31536000000&HW-CC-Sign=1FB69EA72276DFDB4020172336072DD13ADE03DB475B44CC27785C87C2BA3664)

在跳出所有断点后，测试结束，与运行模式相同，在测试窗口查看测试结果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/E4iQ23CQRmu0L-XvHZXX1g/zh-cn_image_0000002808767099.png?HW-CC-KV=V1&HW-CC-Date=20261124T044231Z&HW-CC-Expire=31536000000&HW-CC-Sign=4D9E12322947AACD79CCBE66AAFA7186EB6FDAFD9503137C19D45CEA2FBD5CA4)

### 覆盖率统计模式

在LocalTest运行的基础上支持代码覆盖率统计，当前仅支持ArkTS工程。

开发者可以自定义参与覆盖率测试的本地文件或远程源码har包，具体配置方法请参考[配置覆盖率过滤文件](ide-ui-test.md#section13756446154)。

如前所述，覆盖率统计模式也有多级别入口，以文件级别为例，有两种方式启动测试：

* 方式一：在工程目录中，选中文件，单击**右键 > Run '测试文件名称' with Coverage**，以覆盖率统计模式执行测试任务。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/fG52qDMJSnWEUq9hEmc3ww/zh-cn_image_0000002779407542.png?HW-CC-KV=V1&HW-CC-Date=20261124T044231Z&HW-CC-Expire=31536000000&HW-CC-Sign=65D6866BC28FCB22F15777919D0189B938C3622670DF27FDC7014B3628F5BA79)

* 方式二：在DevEco Studio的右上角，选择测试任务，然后单击右侧的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/_xM_KyQJQIW4spkU9W1Dxg/zh-cn_image_0000002779567514.png?HW-CC-KV=V1&HW-CC-Date=20261124T044231Z&HW-CC-Expire=31536000000&HW-CC-Sign=EC40BF9EBE409A290E84603780FCFBEEA0EAF0F318882E45E3698A15136D609F)按钮，执行测试。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/SpNs7bYUQXK_TlwH8hMIsg/zh-cn_image_0000002808887187.png?HW-CC-KV=V1&HW-CC-Date=20261124T044231Z&HW-CC-Expire=31536000000&HW-CC-Sign=045A0FDDA5DF459950082890BA3928B69B31EC23253C60A8825A4A55F5F3BE07)

启动测试后，进行编译构建，底部将出现Cover窗口，构建结束后自动拉起Cover窗口，测试任务结束后，窗口中会打印测试报告的路径。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/wf3K5ebvSIyrl84viUL-pA/zh-cn_image_0000002808767095.png?HW-CC-KV=V1&HW-CC-Date=20261124T044231Z&HW-CC-Expire=31536000000&HW-CC-Sign=596AA01EFBCFB3B1BD4AA367D2C30F81CDB7F90C3F07061BC19E9F2F42816D30)

点击链接可打开报告，查看代码覆盖率详情，关于覆盖率的计算方式请参考[查看覆盖率报告](ide-ui-test.md#section10394362109)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/zaICdg_ZR8qqGHAAt1cGhA/zh-cn_image_0000002779407538.png?HW-CC-KV=V1&HW-CC-Date=20261124T044231Z&HW-CC-Expire=31536000000&HW-CC-Sign=A0ECE580D1418705BF18015F14BE51CB19589B32C851B86A204B3A2AB9201E5D)

在Cover窗口中，单击rerun按钮可以按照之前的设置，重新执行覆盖率用例。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/-96LBX5KTIWHhMJhh7nUbg/zh-cn_image_0000002808887181.png?HW-CC-KV=V1&HW-CC-Date=20261124T044231Z&HW-CC-Expire=31536000000&HW-CC-Sign=04ACD145B73AD21E4821F4409F9EDB73B1B2ACFF10EFDA90C134A7048FD0D9A5)

## （可选）自定义测试用例运行任务

默认情况下，测试用例可直接运行。如果需要自定义测试用例运行任务，可通过如下方法进行设置。

1. 在工具栏主菜单单击**Run**>**Edit Configurations**，进入Run/Debug Configurations界面。
2. 在**Run/Debug Configurations**界面，单击**+**按钮，在弹出的下拉菜单中，单击**Local Test**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/giXDTUgqTBSqMRZCQGoUBQ/zh-cn_image_0000002779567512.png?HW-CC-KV=V1&HW-CC-Date=20261124T044231Z&HW-CC-Expire=31536000000&HW-CC-Sign=A7FA2F8EB81B2D449E86E1A47769C359FCD5868AE3C3C26B2A0AE510B97CF7FA)
3. 根据实际情况，配置Local Test的运行参数。 然后单击**OK**，完成配置。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/y2QLwMmcQAar9-XI6ClMlA/zh-cn_image_0000002779407534.png?HW-CC-KV=V1&HW-CC-Date=20261124T044231Z&HW-CC-Expire=31536000000&HW-CC-Sign=BB846FE81E3E70E3094FD5DAECFA07A2B266372F6E9128393F8C2171750B71D3)

## 使用命令行执行测试

通过命令行方式执行Local Test，在工程根目录下执行命令：

```bash
hvigorw test -p module={moduleName} -p coverage={true | false} -p scope={suiteName}#{methodName} -p patch={patchPath}
```

* module：执行测试的模块。缺省默认是执行所有模块的用例。
* coverage：是否生成覆盖率报告，缺省默认是true，在<module-path>/.test/default/outputs/test/reports路径下生成两份报告，一份是html格式（index.html），一份是json格式（coverageReport.json），具体参考[查看覆盖率报告](ide-ui-test.md#section10394362109)。
* scope：格式为{suiteName}#{methodName}或{suiteName}，分别表示测试用例级别或测试套件级别的测试，缺省默认是执行当前模块的所有用例。
* patch：可选参数，指定代码补丁文件路径，用于统计增量代码覆盖率。仅支持绝对路径，后缀必须为.patch或.diff，可以通过git diff等命令生成。从26.0.0版本开始支持。

**说明** 

* 多个module和scope之间用英文逗号隔开。
* 暂不支持在Linux上执行该命令。

测试结果文件：<module-path>/.test/default/intermediates/test/coverage\_data/test\_result.txt
