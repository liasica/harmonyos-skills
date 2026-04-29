---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-add-new-module
title: 添加/删除模块
breadcrumb: 指南 > 开发环境搭建 > 工程创建 > 模块管理 > 添加/删除模块
category: harmonyos-guides
scraped_at: 2026-04-29T13:44:34+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:84f4f38f6d14da809b6218a63d47ba1b1c387ee4142cda08820ac0b55389d7bb
---

模块（Module）是应用/元服务的基本功能单元，包含了源代码、资源文件、第三方库及应用/元服务配置文件。一个应用/元服务通常会包含一个或多个模块，因此，可以在工程中创建多个模块。模块支持entry、feature（仅应用工程支持创建）、har、shared四种类型，具体请参考[module.json5配置文件](module-configuration-file.md#配置文件标签)。

从DevEco Studio 6.0.1 Beta1开始，创建Native C++模块或Library模板时支持选择C++版本。

## 创建新的模块

1. 通过如下三种方法，在工程中添加新的模块。
   * 方法1：鼠标移到工程目录顶部，单击鼠标右键，选择**New > Module**...，开始创建新的Module，此时该模块将创建在工程根目录下。
   * 方法2：选中工程目录中任意文件，然后在菜单栏选择**File > New > Module**...，开始创建新的Module，此时该模块将创建在工程根目录下。
   * 方法3：在工程根目录下创建一个新的Directory，可在该目录下单击鼠标右键，选择**New > Module**...，创建新的模块，此时模块将创建在该文件目录下，方便开发者对模块进行分类管理。

     说明

     当前暂不支持在AppScope、hvigor、oh\_modules、build、以点开头的目录（如：.hvigor、.idea）下通过单击鼠标右键创建模块。
2. 在**New Project Module**界面中，选择需要创建的模板，单击**Next**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/rhoJcmL0RlmUwK-7u4oU5Q/zh-cn_image_0000002530752976.png?HW-CC-KV=V1&HW-CC-Date=20260429T054433Z&HW-CC-Expire=86400&HW-CC-Sign=D58F4AD4AA98E44010248E34ABFF3BCFAA001D2931C9301A0F6B31457A00D05F)
3. 在模块配置页面，设置新增模块的基本信息，然后单击**Next**。从DevEco Studio 6.0.1 Beta1开始，支持选择C++版本。
   * **Module name**：新增模块的名称，**Module name**不可与工程名称/工程中其他模块名称相同。
   * **Module type**：仅在Ability模板存在该字段，可以选择Feature和Entry类型。

     说明

     + 同一工程通过新增模块仅支持创建一个Entry模块。如需构建Entry类型模块，可在module.json5文件中修改相应module下的type字段。
     + 如果同一类型的设备已经存在Entry模块，出现新的Entry模块后，还需要[配置分发策略](module-configuration-file.md#distributionfilter标签)。
   * **Device type**：选择模块的设备类型，如果新建模块的Module type为feature，则只能选择该工程原有的设备类型；如果Module type为entry，可以选择该模块支持的其他设备类型。
   * **Enable native**：仅Library模板存在，将创建一个可以调用C/C++的共享包。
   * **C++ Standard：**C++标准库，取值包括：Toolchain Default、C++11、C++14。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/_av20zlmScKSmX_ds960mQ/zh-cn_image_0000002561832893.png?HW-CC-KV=V1&HW-CC-Date=20260429T054433Z&HW-CC-Expire=86400&HW-CC-Sign=D31372336BAC4383FFE1DAEFFFCA6D8DB1436848BBA0068ED6B8518906BE75A9)
4. 若该模块的模板类型为Ability，还需要设置新增Ability的**Ability name**和****E****xported****参数，**E****xported**参数表示该Ability是否可以被其它应用/元服务所调用（FA模型下为Visible参数)。
   * 勾选（true）：可以被其它应用/元服务调用。
   * 不勾选（false）：不能被其它应用/元服务调用。
5. 单击**Finish**，等待创建完成后，可以在工程目录中查看和编辑新增的模块。工程中所包含模块的信息可以在[build-profile.json5](ide-hvigor-build-profile-app.md)中modules字段进行配置。

## 导入/引用模块

DevEco Studio支持通过以下两种方式导入其他工程下的模块：

1. 通过[Import Module](ide-add-new-module.md#section13771399184)功能，将其它HarmonyOS模块的功能代码复制到当前工程中；当前仅支持FA模型的模块导入到FA模型，Stage模型的模块导入到Stage模型。不支持FA模型的模块导入到Stage模型，或Stage模型的模块导入到FA模型。
2. 通过在[srcPath字段下配置相对路径](ide-add-new-module.md#section12961144312265)的方式引用其他工程下的模块，该方式仅引用模块相关信息，不会将模块代码完全复制至本地。当前支持引用其他工程下的HAR和HSP模块。

### Import Module

1. 在菜单栏单击**File > New > Import... > Import Module。**

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/wWaU2fGhQ0yoqTFnUIqC1Q/zh-cn_image_0000002530912964.png?HW-CC-KV=V1&HW-CC-Date=20260429T054433Z&HW-CC-Expire=86400&HW-CC-Sign=16CB0AF8B2B2D0D7A96400854296EEFC75741B63DB860C33B5EB2033DEDE4B7E)
2. 选择导入的模块。

   在指定路径下，选择导入的模块，单击**OK**。导入的模块可以为文件夹，也可以为zip格式。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/xYlx0lGeQEqx_HDMCJQpqw/zh-cn_image_0000002530752972.png?HW-CC-KV=V1&HW-CC-Date=20260429T054433Z&HW-CC-Expire=86400&HW-CC-Sign=42CDDD52F0F02B1EFE8C390D3D4E99AB86222117A2541A4844457E358052A33D)

### srcPath方式引用模块

在工程级build-profile.json5文件中，如下图所示在modules > srcPath字段下配置工程外模块的相对路径，即可引用模块相关信息，不会将模块代码完全复制至本工程中。当前支持引用其他工程下的HAR和HSP模块。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/aDTtFHwPQxS1dqazxPOvJw/zh-cn_image_0000002530752974.png?HW-CC-KV=V1&HW-CC-Date=20260429T054433Z&HW-CC-Expire=86400&HW-CC-Sign=A02F96B2390123ECC867F84B2B03F8BD5A71E79298678E5B4164F5FF0D3953A9)

## 删除Module

在工程目录中选中要删除的模块，单击鼠标右键，选中**Delete**，并在弹出的对话框中单击**Delete**。
