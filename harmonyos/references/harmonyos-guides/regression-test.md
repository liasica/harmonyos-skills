---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/regression-test
title: 回归测试
breadcrumb: 指南 > 应用测试 > 专项测试 > DevEco Testing > 回归测试
category: harmonyos-guides
scraped_at: 2026-04-29T13:48:11+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:dfaca188d9806572c759cdea12cfb49aa5191d90229e1bcc8c138a8d25c11f4a
---

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/W5TTh-tgRYakIlHteTleOw/zh-cn_image_0000002492343756.png?HW-CC-KV=V1&HW-CC-Date=20260429T054805Z&HW-CC-Expire=86400&HW-CC-Sign=85D088C7AFA236C1C0101DD59B4F96C51C83FBED46CF839FDCAEAA3B4FB0585D "点击放大")

## 回归测试

**回归测试：**针对待测试应用的指定场景，支持通过构建自定义测试包，无需搭建环境即可执行测试用例。用例执行过程中提供实时投屏、步骤截图、步骤结果和测试用例执行日志展示，辅助开发者快速定位问题；此外，测试报告支持指标上报，辅助开发者了解应用的执行性能，助力开发者更高效地打造出高质量应用。

**测试包构建**

回归测试的测试对象为应用的核心功能，用户可将应用核心功能的测试用例构建成多个可执行测试包，每个测试包中仅包含单个测试用例，便于观察到核心功能的每个小功能点的质量。

测试执行前需先构建测试包，用户利用python的setuptools工具在工程（测试工程构建参考[应用UI测试（基于Python）](hypium-python-guidelines.md)）根目录下构建setup-regression.py、MANIFEST.in文件，setup-regression.py文件中声明用例，MANIFEST.in文件中声明脚本执行过程中需要用到的aw包、config文件夹下的配置文件及其他的资源文件。

为方便用户构建测试包，DevEco Testing Hypium（PyCharm插件）已发布，用户可利用插件快速生成可执行测试包。具体操作步骤如下：

**步骤一：**PyCharm中本地安装 DevEco Testing Hypium 插件，安装成功后重启IDE，导航栏中出现相关字样，即为安装成功。

**步骤二：**新建hypium工程，编写用例。以下为示例工程目录：

```
1. HypiumTest
2. |     |----aw                                       // 工程中自定义模块文件夹
3. |     |     |----Utils.py                         // 示例模块文件
4. |     |----config                                  // 测试工程配置文件夹
5. |     |     |----user_config.xml             // 测试工程配置文件，主要是测试框架的任务配置
6. |     |----resource                              // 测试资源文件夹，测试过程中用到的资源文件默认会优先从当前文件夹进行查找
7. |     |    |----images            // 资源文件子目录
8. |     |    |    |----icon_mms.png   // 资源文件，以png图片为例
9. |     |----testcases                             // 测试用例文件夹，测试过程中的测试用例文件优先会从当前文件夹进行查找
10. |     |    |----Example.json                  // Example测试用例配置文件，配置用例设备信息等
11. |     |    |----Example.py                     // Example测试用例文件，实际的测试逻辑代码
```

注意

在用例脚本中，请导入并使用hypium.advance.deveco\_testing.step中的Step方法标记步骤(from hypium.advance.deveco\_testing.step import Step)，否则回归测试过程中无法正确读取到测试步骤，并导致指标监控为空。

**步骤三：**在工程根目录下创建setup-regression.py文件和MANIFEST.in文件（用户本地环境需预先安装setuptools模块），参考python的setuptools用法编写setup-regression.py，示例如下：

```
1. from setuptools import setup

3. setup(
4. name='hypiumTest',
5. version='1.0.0.0',
6. author='xxx',
7. # py_modules指定需要打包的hypium用例py文件
8. py_modules=['testcases.Example'],
9. include_package_data=True
10. )
```

注意

回归测试生成的可执行测试包中仅支持单用例（即单个json文件和json中指定的用例文件），编写setup-regression.py时需注意写法，否则会打包失败。

通过MANIFEST.in文件指定需要一起打包的文件，示例如下：

```
1. # 与打包用例对应的json文件
2. include testcases/Example.json
3. # 用例依赖的aw
4. include aw/*.py
5. # 用例中用到的各类配置文件
6. include config/*.xml
7. include config/*.json
8. include config/*.txt
9. # 用例中用到的resource
10. include resource/*
11. include resource/images/*
```

注意

一定要确保用例所需要的 aw 和配置文件及其他资源全部都写到 MANIFEST.in 中，否则用例包无法正常执行。

**步骤四：**在根目录下右键选择“DevEco Testing Hypium”-“生成测试服务包”，出现下图弹窗，选择“回归测试”，用户需填写待测试应用的名称及测试场景，信息填写完毕后点击“OK”即可在指定目录下查看测试包。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/3VO3n43XSJOw4bRa_zp1ag/zh-cn_image_0000002524503447.png?HW-CC-KV=V1&HW-CC-Date=20260429T054805Z&HW-CC-Expire=86400&HW-CC-Sign=7E5CCC4B61FF8A9CF3A8F89BD7237811F2F6D05C4D73A082266BF4C15795968C)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/uy1G_mN9S4aThGblOrEcdA/zh-cn_image_0000002492343754.png?HW-CC-KV=V1&HW-CC-Date=20260429T054805Z&HW-CC-Expire=86400&HW-CC-Sign=0A8C119CA9445BE39C42565F89BBA74998B08CE442994BCEE0A1B60941FFFAA5 "点击放大")

生成回归测试测试包，打包好的测试包支持在回归测试服务中本地执行。

**创建任务**

进入DevEco Testing客户端，在左侧菜单栏选择“回归测试”，点击“回归测试”服务卡片，即进入任务创建界面。按需配置任务参数，点击创建任务即开始测试。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/IMtENkGHTgKMTyesx3pE4Q/zh-cn_image_0000002492343752.png?HW-CC-KV=V1&HW-CC-Date=20260429T054805Z&HW-CC-Expire=86400&HW-CC-Sign=71A1EDABF2CC9661682602F7A6F7D6DD272A246EC315BCBF1854B2F4D0BF7CDF "点击放大")

配置服务参数：

任务名称：用于标识任务，系统会根据时间生成默认任务名，支持自定义修改。

备注信息：按需填写任务备注信息，便于快速筛选报告。

测试设备：选择一个待测设备。系统版本支持 HarmonyOS 5.0及以上版本。

测试包路径：选择待测测试包，服务将对测试包中指定应用进行解析，并执行测试包中测试用例。

**测试包详情：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/tj4O3I_MQCOEIQp1DTaPIw/zh-cn_image_0000002538035122.png?HW-CC-KV=V1&HW-CC-Date=20260429T054805Z&HW-CC-Expire=86400&HW-CC-Sign=E9C17C0E84E04E80540D1E7703140004031DBE12AE7CB14B067B7301D18467A6 "点击放大")

点击查看测试包详情，即可查看测试包基本信息。

参数配置完成后，点击“创建任务”即开始测试。

**测试执行**

任务创建后即进入测试执行页面，测试过程中，在测试页面可以看到设备实时投屏、设备截图、测试步骤结果上报以及指标数据上报。执行过程中如果脚本执行失败，任务会立刻停止，生成的报告中仅包含任务失败前的数据信息。手动停止查看报告时，报告中仅包含报告停止前的数据信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/VLjr82mhTKeuPwqVagz_fw/zh-cn_image_0000002492343750.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T054805Z&HW-CC-Expire=86400&HW-CC-Sign=80F1307444DAD6560C43ADCF7E9528001215CC68DC10FA4FB8C85A096F0D5A59 "点击放大")

**查看报告**

测试完成后，将自动跳转到报告界面。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/2sMDw4qDTpG-Jez0j_VXhg/zh-cn_image_0000002492343758.png?HW-CC-KV=V1&HW-CC-Date=20260429T054805Z&HW-CC-Expire=86400&HW-CC-Sign=72420843854A6788843399E317DB87DB02E17AD08C96CF39AD2C749A683BD5D2 "点击放大")

任务信息：在报告的最上方可查看本次任务的应用信息，运行时间，环境参数和执行日志，点击“打开目录”按钮，可以导出html格式的报告文件。

应用信息：基于测试包中指定的待测试应用获取设备上该应用的包名、版本、API版本。

环境参数：展示测试设备信息和参数配置。

测试结论：本次测试任务的执行结果。

上报指标：本次任务执行过程中CPU平均使用率、内存平均使用率以及用户在脚本中自定义指标上报，目前不支持自定义指标更新操作，若多次上报同一个指标，仅展示最后一次的指标上报结果。

测试截图&CPU使用率：该部分展示了任务执行过程中CPU使用率、内存使用的变化情况，同时移动指针可查看当前时间对应的截图（并非每一秒均存在截图）。

执行步骤&执行日志：该部分展示了测试用例执行的所有测试步骤、每一步的执行结果以及用例的执行日志，若某一步执行失败，则后续步骤不再执行。点击每一步，CPU使用率统计图中将会展示出该步骤执行过程中的CPU使用情况，同时该步骤对应的执行日志将会高亮显示。

说明

更多测试服务详情，请前往DevEco Testing客户端 -> 回归测试 -> 回归测试 -> 任务创建页 -> 测试指南中查询。
