---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-add-new-module
title: 添加和删除模块
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 开发环境搭建 > 工程创建 > 模块管理 > 添加和删除模块
category: harmonyos-guides
scraped_at: 2026-10-11T07:23:15+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:5f0e7e2d115676f74a745347408bc8c9faaf61744576562c2492e2e88543d040
---

模块（Module）是应用/元服务的基本功能单元，包含了源代码、资源文件、第三方库及应用/元服务配置文件。每一个模块都可以独立进行编译和运行。一个应用/元服务通常会包含一个或多个模块。因此，可以在工程中创建多个模块。模块支持entry、feature、har、shared四种类型，具体请参考[module.json5配置文件](module-configuration-file.md#配置文件标签)。

## 创建新的模块

1. 通过如下三种方法，在工程中添加新的模块。
   * 方法一：在菜单栏点击**新建 > 模块**，开始创建新模块，此时该模块将创建在工程根目录下。
   * 方法二：鼠标移到工程目录顶部，单击鼠标右键，选择**新建 > 模块**，开始创建新模块，此时该模块将创建在工程根目录下。
   * 方法三：在工程根目录下创建一个新的文件夹，可在该目录下单击鼠标右键，选择**新建 > 模块**，开始创建新模块，此时模块将创建在该文件目录下，方便开发者对模块进行分类管理。

     **说明** 

     当前暂不支持在AppScope、hvigor、oh\_modules、build、以点开头的目录（如：.hvigor、.idea）下通过单击鼠标右键创建模块。
2. 在**新建模块**界面，选择需要创建的模板，设置新增模块的基本信息后，单击**确认**。
   * **模块名**：新增模块的名称，模块名不可与工程名称或工程中其他模块名称相同。
   * **模块类型**：仅Empty Ability模板存在，可以选择Feature和Entry类型。

     **说明** 

     同一工程通过新增模块仅支持创建一个Entry模块。如需构建Entry类型模块，可在module.json5文件中修改相应module下的type字段。
   * **设备类型**：选择模块的设备类型，如果新建模块的模块类型为Feature，则只能选择该工程原有的设备类型；如果模块类型为Entry，可以选择该模块支持的其他设备类型。
   * **Enable Native**：仅Shared Library和Static Library模板存在，创建一个可以调用C/C++的共享包。
   * **Ability信息：**若该模块的模板类型为Empty Ability，还需要设置新增的**Ability****名称**和**Exported**参数，**E****xported**参数表示该Ability是否可以被其它应用/元服务所调用。
     + 勾选（true）：可以被其它应用/元服务调用。
     + 不勾选（false）：不可以被其它应用/元服务调用。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/zXJHZK0nTk2cQILaZE2BFQ/zh-cn_image_0000002750169642.png "点击放大")
3. 单击**确认**，等待创建完成后，可以在工程目录中查看和编辑新增的模块。工程中所包含模块的信息可以在[build-profile.json5](ide-hvigor-build-profile-app.md)中modules字段进行配置。

## 删除模块

在工程目录中选中要删除的模块，单击鼠标右键，选中**删除**，并在弹出的对话框中单击**删除**。
