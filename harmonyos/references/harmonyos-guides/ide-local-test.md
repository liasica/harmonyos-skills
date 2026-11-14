---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-local-test
title: 本地测试（Local Test）
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 开发自测试 > 测试框架 > 代码测试 > 本地测试（Local Test）
category: harmonyos-guides
scraped_at: 2026-11-14T08:49:01+08:00
doc_updated_at: 2026-10-10
content_hash: sha256:1f49439645c2ab832cd3dbd6819c366088de82756dc441774b8304e2bf269621
---

**说明** 

当前不支持测试C/C++方法及系统API。

## 创建Local Test测试用例

1. 在工程目录下打开待测试模块（支持HAP、HAR、HSP模块）下的ets文件，将光标置于代码中任意位置，单击**右键 > Show Context Actions** **> Create Local Test**或快捷键**Alt+Enter****（macOS为Option+Enter） > Create Local Test**创建测试类。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/2woYNdsjRwCpgyvabLE-7A/zh-cn_image_0000002779567518.png?HW-CC-KV=V1&HW-CC-Date=20261114T004900Z&HW-CC-Expire=31536000000&HW-CC-Sign=262D224389AFE24900B0936884C44598579D1F1DE3798B0A6CF379D6F2D626AD)
2. 在弹出的Create Local Test窗口，输入或选择如下参数。
   * **Testing library**：测试类型，默认为DECC-ArkTSUnit。
   * **ArkTS name**：创建的测试文件名称，测试文件中包含了测试用例。测试文件名称要求在工程目录范围内具有唯一性，仅支持字母、数字、下划线（\_）和点（.）。
   * **Destination package**：测试文件存放的位置，建议存放在待测试模块的test目录下。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/EQdQy89iQUaR4t6caaQl3A/zh-cn_image_0000002808767097.png?HW-CC-KV=V1&HW-CC-Date=20261114T004900Z&HW-CC-Expire=31536000000&HW-CC-Sign=040AFDACC67E3563EF38F17E934DD1F33D42BCE86D8C4323B738AE83B410C06B)
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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f/v3/tmHtChrgSim_AfWK03WdbA/zh-cn_image_0000002808887183.png?HW-CC-KV=V1&HW-CC-Date=20261114T004900Z&HW-CC-Expire=31536000000&HW-CC-Sign=CB0B3D371F19928C8FB0525487669C61FC989A8154256113AFD79887B1E04253)

也可以通过如下方式，执行Local Test：

* 在工具栏主菜单单击**Run > Run'测试名称'**。
* 在DevEco Studio的右上角，选择一项测试任务的配置，然后单击右侧的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/ifoclDn1R2K6VbeNU8xEvA/zh-cn_image_0000002779407544.png?HW-CC-KV=V1&HW-CC-Date=20261114T004900Z&HW-CC-Expire=31536000000&HW-CC-Sign=1D9AB42E558BC0EDCAD605AFD1E890BBDD0089685A1B0AC98D87FF9A0C10ABBC)按钮，执行Local Test。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/1RtvH_ddSvimOdSOva5xKA/zh-cn_image_0000002779407546.png?HW-CC-KV=V1&HW-CC-Date=20261114T004900Z&HW-CC-Expire=31536000000&HW-CC-Sign=C003820C540254BB5DBD2BBD9B63E474FED301FC31357B2E0BC03BF9D874B7A4)

执行完测试任务后，查看测试结果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/LwcB8ZQJTvGtf5aViC9aFA/zh-cn_image_0000002779567516.png?HW-CC-KV=V1&HW-CC-Date=20261114T004900Z&HW-CC-Expire=31536000000&HW-CC-Sign=81925F322AE8127F85D3AFAB2DD1403CB47A202B3D45E3D2A64875167B81572C)

### 调试模式

调试模式相比运行模式增加了断点管理功能。在断点命中时，可以选择单步执行、步入步出、进入下个断点等方式进行调试，另外可以使用线程堆栈可视化、变量和表达式可视化功能，快速定位问题。

以文件级别为例，在添加断点之后，在工程目录中，选中文件，单击**右键 > Debug'测试文件名称'**，以调试模式执行测试任务。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/4SrN1kxBQfKol7f64lthkQ/zh-cn_image_0000002779407536.png?HW-CC-KV=V1&HW-CC-Date=20261114T004900Z&HW-CC-Expire=31536000000&HW-CC-Sign=AB97913108A1FCE603CA430F45AEECFE7FD05EF393FEF12CB07B66C472E242E9)

在断点命中时，下方将出现Debug窗口。开发者可在该窗口中进行断点管理与基础调试能力的可视化操作，在断点命中时可查看当前线程的变量和堆栈信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/v4qR05-3Q4W07I2fxu3qYw/zh-cn_image_0000002779567522.png?HW-CC-KV=V1&HW-CC-Date=20261114T004900Z&HW-CC-Expire=31536000000&HW-CC-Sign=D1EC68B7FE8953A193556661CD93215267E64F8AC0319B3CFC0D2503E82975F4)

断点命中时，在代码编辑器窗口单击右键，在弹出的菜单中将出现调试模式特有功能，如计算表达式、添加变量监视等。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/y9r0zH1kQLiFlTNUADhwdA/zh-cn_image_0000002808767101.png?HW-CC-KV=V1&HW-CC-Date=20261114T004900Z&HW-CC-Expire=31536000000&HW-CC-Sign=02078A99DA6CE7F2AA6D143BC00871A8728CAD41F110D1609ECD8E019AAF1D52)

在跳出所有断点后，测试结束，与运行模式相同，在测试窗口查看测试结果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/woofpithSxqfjrLmM_lkzA/zh-cn_image_0000002808767099.png?HW-CC-KV=V1&HW-CC-Date=20261114T004900Z&HW-CC-Expire=31536000000&HW-CC-Sign=A053AC4F2171D1BDADD939E02CC56C7B53FA38A1BAED3CB21EF5775876BD9763)

### 覆盖率统计模式

在LocalTest运行的基础上支持代码覆盖率统计，当前仅支持ArkTS工程。

开发者可以自定义参与覆盖率测试的本地文件或远程源码har包，具体配置方法请参考[配置覆盖率过滤文件](ide-ui-test.md#section13756446154)。

如前所述，覆盖率统计模式也有多级别入口，以文件级别为例，有两种方式启动测试：

* 方式一：在工程目录中，选中文件，单击**右键 > Run '测试文件名称' with Coverage**，以覆盖率统计模式执行测试任务。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ca/v3/pJ1SlZ-8QL-HxVnPuFbx_w/zh-cn_image_0000002779407542.png?HW-CC-KV=V1&HW-CC-Date=20261114T004900Z&HW-CC-Expire=31536000000&HW-CC-Sign=4AE4F45C40A319D3299F2746CABE909343B55BCDF26B465424CA8E84A1BF942D)

* 方式二：在DevEco Studio的右上角，选择测试任务，然后单击右侧的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/07/v3/pjE_C6VsTjGYWTuf2ubM8w/zh-cn_image_0000002779567514.png?HW-CC-KV=V1&HW-CC-Date=20261114T004900Z&HW-CC-Expire=31536000000&HW-CC-Sign=81AB607D7A75481BD6A108225B06064AE61F88503E75EEAED4B33DF599DDD31B)按钮，执行测试。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/q6qQQFduQhW99gTYwjqYBA/zh-cn_image_0000002808887187.png?HW-CC-KV=V1&HW-CC-Date=20261114T004900Z&HW-CC-Expire=31536000000&HW-CC-Sign=E65B04EA0316BBD346ADAFCFA92FB7AE6E3CD713893FDD3636645A73D20DD6E3)

启动测试后，进行编译构建，底部将出现Cover窗口，构建结束后自动拉起Cover窗口，测试任务结束后，窗口中会打印测试报告的路径。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/4SF-EB5LT1eLlfz-nhyrrA/zh-cn_image_0000002808767095.png?HW-CC-KV=V1&HW-CC-Date=20261114T004900Z&HW-CC-Expire=31536000000&HW-CC-Sign=4581A9E3C7BEE6A5F1A23D0D139849207042F6BF8BEA055F494ADED454CEA284)

点击链接可打开报告，查看代码覆盖率详情，关于覆盖率的计算方式请参考[查看覆盖率报告](ide-ui-test.md#section10394362109)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/RoBng4yTREq3afhplbO4jg/zh-cn_image_0000002779407538.png?HW-CC-KV=V1&HW-CC-Date=20261114T004900Z&HW-CC-Expire=31536000000&HW-CC-Sign=8BC6C27E87B2E3C58065C47677350A5D360C72B66E3C1BE3A33F8936DFD00E75)

在Cover窗口中，单击rerun按钮可以按照之前的设置，重新执行覆盖率用例。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/Wh8ZfhRiQ3-4hA1JsUS0SA/zh-cn_image_0000002808887181.png?HW-CC-KV=V1&HW-CC-Date=20261114T004900Z&HW-CC-Expire=31536000000&HW-CC-Sign=FC6AA286D597BFA4ED49F5D0A62AB594975050F45BC790B0E91F234713880BE7)

## （可选）自定义测试用例运行任务

默认情况下，测试用例可直接运行。如果需要自定义测试用例运行任务，可通过如下方法进行设置。

1. 在工具栏主菜单单击**Run**>**Edit Configurations**，进入Run/Debug Configurations界面。
2. 在**Run/Debug Configurations**界面，单击**+**按钮，在弹出的下拉菜单中，单击**Local Test**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/erpB0brISeCmmodyq6Fxkw/zh-cn_image_0000002779567512.png?HW-CC-KV=V1&HW-CC-Date=20261114T004900Z&HW-CC-Expire=31536000000&HW-CC-Sign=D93419AEC3ECA26AF6129710D7B488768758F03B50588B9E6A6E6C8E31F7AB32)
3. 根据实际情况，配置Local Test的运行参数。 然后单击**OK**，完成配置。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/EO_MwR8dTfW4UNaG_-7GEg/zh-cn_image_0000002779407534.png?HW-CC-KV=V1&HW-CC-Date=20261114T004900Z&HW-CC-Expire=31536000000&HW-CC-Sign=9813EE2E7734677E01EC465E1CF59429DBA62581717ADFEBBF2BFE678DEDC528)

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
