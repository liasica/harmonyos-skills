---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/compiling-and-building-faq-0022
title: DevEco Studio工程配置调试与安装报错问题排查
breadcrumb: FAQ > DevEco Studio > 编译构建 > 常见问题 > DevEco Studio工程配置调试与安装报错问题排查
category: harmonyos-faqs
scraped_at: 2026-10-28T07:48:51+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:4ee52f614ba5c7143b8f99b8cc5abb4922869499713c7a0e8b44018202f3852a
---

**Q：无法调试，DevEco Studio提示“ The target can not be empty. Check the build-profile.json5 file of the project root directory and make sure the targets of the modules in configuration is set to specified product: default in applyToProducts.”**

**A**：问题现象

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/sVzR_YSgR3SofdYDXPyJhQ/zh-cn_image_0000002802062937.png "点击放大")

问题分析

报该错误，可能是build-profile.json5文件中未添加“targets”配置，Module Target下为空，工程同步失败。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/mPBMP2WMSUGAABz-TW7A0A/zh-cn_image_0000002772863194.png)

解决措施

需要在模块级build-profile.json5文件中添加“targets”配置，点击“Sync Now”，待完成同步后，即可解决该问题（确保工程同步成功）。具体配置如图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/b3ho4zpIQGWS--Z7w2EJ4A/zh-cn_image_0000002772703212.png "点击放大")

**Q：在启动调试或运行应用/服务时，安装HAP出现错误，提示“compatibleSdkVersion和releaseType与设备上的apiVersion和releaseType不匹配。”如何解决？**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/EqTW-JgATFuRtdU0om2sDQ/zh-cn_image_0000002772703214.png "点击放大")

**A**：出现该问题是因为当前工程配置的最低兼容版本高于设备镜像版本。

使用命令hdc shell param get const.ohos.apiversion查询当前设备的 API 版本，并对比工程级build-profile.json5配置文件中的compatibleSdkVersion字段。如果版本不匹配，可以使用以下解决办法：

方法一：请升级设备镜像版本以匹配当前工程版本。在系统设置界面升级设备系统。

方法二：降低工程的API版本，点击DevEco Studio右上角的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/GBfqUMQPR8-R6JCocAhDdQ/zh-cn_image_0000002802143057.png)，Compatible SDK选择更低的版本号，以兼容设备的API版本。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/WitEDvKHTrKoVDvUd_3ZlQ/zh-cn_image_0000002802143061.png "点击放大")

**说明** 

* 如果执行命令后返回“Fail*F**ai**l*ExecuteCommand need connect-key? please confirm a device by help info”，可能是连接了多台调试设备，或者模拟器和真机同时使用。
  + 如果同时连接了模拟器和真机，请断开模拟器。
  + 如果连接了多台设备，每次执行命令时需要使用-t参数指定目标设备的标识符。您可先执行**hdc list targets命令**查询连接的设备，再通过**hdc -t *connect-key* shell param get const.ohos.apiversion**命令指定要连接的目标设备，其中connect-key为设备标识符，即**hdc list targets**返回的信息。
