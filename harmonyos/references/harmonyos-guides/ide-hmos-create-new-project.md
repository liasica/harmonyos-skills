---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-create-new-project
title: 创建一个新的工程
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 开发环境搭建 > 工程创建 > 创建一个新的工程
category: harmonyos-guides
scraped_at: 2026-10-11T07:23:15+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:16bf618868fcc1ff4e54f765ccc5d26935745f5964c01d3a2a1c85d730f12872
---

当开发者开始开发一个应用/元服务时，首先需要根据工程创建向导，创建一个新的工程。工具会自动生成对应的代码和资源模板。

**说明** 

在运行DevEco Studio工程时，建议每一个运行窗口有2GB以上的可用内存空间。

## 创建应用工程

1. 通过如下两种方式，打开工程创建向导界面。
   * 如果当前未打开任何工程，可以在鸿蒙电脑DevEco Studio的欢迎页，选择**新建工程**。
   * 如果已经打开了工程，可以在菜单栏选择**新建 > 工程**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/FZvUG6rwRLS46UnV76SPdQ/zh-cn_image_0000002779608767.png "点击放大")
2. 根据工程创建向导，在应用下所需的Ability工程模板，填写工程的基本信息。
   * **工程名**：工程的名称，可以自定义，由大小写字母、数字和下划线组成，必须由大小写字母开头，长度为1~200个字符。
   * **包名**：标识应用的包名，用于标识应用的唯一性。

     **说明** 

     应用包名要求：

     + 必须为以点号（.）分隔的字符串，且至少包含三段，每段中仅允许使用英文字母、数字、下划线（\_），如“com.example.myapplication ”。
     + 首段以英文字母开头，非首段以数字或英文字母开头，每一段以数字或者英文字母结尾，如“com.01example.myapplication”。
     + 不允许多个点号（.）连续出现，如“com.example..myapplication ”。
     + 长度为7~128个字符。
   * **保存位置**：工程文件本地存储路径，由大小写字母、数字和下划线等组成，不能包含中文字符。
   * **兼容SDK**：兼容的最低API Version。
   * **模块名**： 模块的名称。
   * **设备类型：**该工程模板支持的设备类型。设备类型说明请参考[deviceTypes标签](module-configuration-file.md#devicetypes标签)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a/v3/SPaagGswSgCXa-0jzFtTiw/zh-cn_image_0000002779608765.png)
3. 单击**确认**，工具会自动生成示例代码和相关资源。

## 创建元服务工程

1. 若首次打开DevEco Studio，请选择**新建工程**。若已经打开了一个工程，请在菜单栏选择**新建** > **工程**。![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/H-iV5-HmS3K1CooUUWa1Uw/zh-cn_image_0000002750009850.png "点击放大")
2. 在元服务下选择所需的模板。

   选择**华为账号**后点击**登录**，登录华为开发者账号进行开发，或选择**访客模式**后点击**确认**。

   **说明** 

   访客模式无需登录华为账号。

   访客模式仅用于体验元服务开发功能。如需将访客模式下开发的元服务工程或历史元服务工程在真机上运行并安装，需在**AppScope > app.json5**文件中补充当前开发者账号下已在AppGallery注册且真实存在的包名。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/-sB6h_0iTWygXtAMGQ-RYg/zh-cn_image_0000002750009852.png "点击放大")
3. 选择登录华为账号下已经在AppGallery中注册的应用ID。如您未在AppGallery中注册元服务应用，或者需要使用新应用ID时，请点击**注册应用ID**进行注册。

   **说明** 

   仅元服务应用的应用ID在界面展示。

   在AppGallery注册应用ID时应用分类请选择“元服务”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/N53lhue0Qi2eEefvXNrH6A/zh-cn_image_0000002779608763.png "点击放大")
4. 点击**注册应用ID**，在弹窗中填写元服务的基本信息后，点击**确认**。
   * **项目**：项目名称。可以输入一个新项目名称，或在下拉框中选择已有项目。
   * **应用类型**：应用类型为元服务。此处不支持修改。
   * **应用名称：**元服务在华为应用市场详情页展示的名称。关于元服务名称要求请参考[为元服务创建APP ID](../app/agc-help-create-atomic-service-0000002247795706.md#section16423184171915)。
   * **应用分类：**应用和游戏。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7/v3/X3lImCLnQJ2FjUmmy0WxZA/zh-cn_image_0000002779728915.png "点击放大")
5. 完成注册后，返回DevEco Studio界面刷新，选择所需的应用ID。填写**工程名**，其他参数保持默认设置即可。点击**确认**，工具会自动生成示例代码和相关资源，等待工程创建完成。

   **说明** 

   元服务的包名自动生成，采用固定前缀和应用ID组合方式命名（com.atomicservice.应用ID），开发者无法手动修改。
