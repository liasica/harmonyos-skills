---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-create-new-project
title: 创建一个新的工程
breadcrumb: 指南 > 开发环境搭建 > 工程创建 > 创建一个新的工程
category: harmonyos-guides
scraped_at: 2026-04-28T07:54:35+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:54a2255cf501e2f579cbf274dde808592f65223cddbb107ab7d910b7441b8c22
---

当您开始开发一个应用/元服务时，首先需要根据工程创建向导，创建一个新的工程，工具会自动生成对应的代码和资源模板。

说明

在运行DevEco Studio工程时，建议每一个运行窗口有2GB以上的可用内存空间。

## 创建和配置新工程

DevEco Studio提供了基础的工程模板资源，不同模板支持的设备类型、API Version可能不同，在创建新工程前，请提前了解各模板的相关信息，具体请参考[工程模板介绍](ide-template.md)。

从DevEco Studio 6.0.1 Beta1开始，创建Native C++工程时支持选择C++版本。

### 创建HarmonyOS工程

1. 通过如下两种方式，打开工程创建向导界面。
   * 如果当前未打开任何工程，可以在DevEco Studio的欢迎页，选择**Create Project**开始创建一个新工程。
   * 如果已经打开了工程，可以在菜单栏选择**File > New > Create Project**来创建一个新工程。
2. 根据工程创建向导，选择创建Application或[Atomic Service](../atomic-guides/atomic-service-create-project.md)。再选择需要的Ability工程模板，然后单击**Next**。

   说明

   * 从API 11版本开始支持Atomic Service元服务工程开发。
   * Atomic Service元服务工程暂不支持Native开发。
   * [CloudDev]Empty Ability模板：该功能仅支持中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/ezJsHz6ESheog97UWFognA/zh-cn_image_0000002561753153.png?HW-CC-KV=V1&HW-CC-Date=20260427T235434Z&HW-CC-Expire=86400&HW-CC-Sign=AE76BB5514866D09193ACD10C8D0CBBAABE5D59A7B9B2E85985D33F806196807)
3. 在工程配置页面，需要根据向导配置工程的基本信息。
   * **Project name**：工程的名称，可以自定义，由大小写字母、数字和下划线组成，必须由大小写字母开头，长度为1~200个字符。
   * **Bundle name**：标识应用的包名，用于标识应用的唯一性。

     说明

     应用包名要求：

     + 必须为以点号（.）分隔的字符串，且至少包含三段，每段中仅允许使用英文字母、数字、下划线（\_），如“com.example.myapplication ”。
     + 首段以英文字母开头，非首段以数字或英文字母开头，每一段以数字或者英文字母结尾，如“com.01example.myapplication”。
     + 不允许多个点号（.）连续出现，如“com.example..myapplication ”。
     + 长度为7~128个字符。
   * **Save location**：工程文件本地存储路径，由大小写字母、数字和下划线等组成，不能包含中文字符。
   * **Compatible SDK**：兼容的最低API Version。
   * **Module name**： 模块的名称。
   * **Device type：**该工程模板支持的设备类型。设备类型说明请参考[deviceTypes标签](module-configuration-file.md#devicetypes标签)。
   * **C++ Standard：**C++标准库，取值包括：Toolchain Default、C++11、C++14。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/vGnzVDLxRWKqo0PXVOSlFg/zh-cn_image_0000002530913214.png?HW-CC-KV=V1&HW-CC-Date=20260427T235434Z&HW-CC-Expire=86400&HW-CC-Sign=ADB3AD8A10A1DD8F88C7A3B28F0CF4C429A86C6B1C0AFCF0EDCAD274FDFE88FC)
4. 单击**Finish**，工具会自动生成示例代码和相关资源，等待工程创建完成。

### （可选）创建OpenHarmony工程

如需创建OpenHarmony工程进行应用开发，请按照以下步骤操作。

1. 在完成[创建HarmonyOS工程](ide-create-new-project.md#section11644183711342)后，根据如下操作修改工程级build-profile.json5文件中相关字段：
   1. 在工程级build-profile.json5文件添加**compileSdkVersion**字段。
   2. 将**compatibleSdkVersion**、**compileSdkVersion**、**targetSdkVersion**（若有）字段赋值为数值类型。
   3. 将runtimeOS从"HarmonyOS"修改为**"OpenHarmony"**。

   ```
   1. "app": {
   2. "signingConfigs": [],
   3. "products": [
   4. {
   5. "name": "default",
   6. "signingConfig": "default",
   7. "compileSdkVersion": 23,    //指定OpenHarmony应用编译时的版本，当前以API 23为例
   8. "targetSdkVersion": 23,     //指定OpenHarmony应用运行所需的目标SDK版本，当前以API 23为例
   9. "compatibleSdkVersion": 23, //指定OpenHarmony应用兼容的最低版本，当前以API 23为例
   10. "runtimeOS": "OpenHarmony",
   11. "buildOption": {
   12. "strictMode": {
   13. "caseSensitiveCheck": true,
   14. "useNormalizedOHMUrl": true
   15. }
   16. }
   17. }
   18. ],
   ```
2. 单击Sync Now进行同步。在Sync Check弹窗中点击**Yes**，同意将module.json5/config.json文件中的phone切换为OpenHarmony支持的default类型，并删除在OpenHarmony不适用的其他设备类型，同步成功无其他报错则工程创建完成。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/pr9dN0uET0-ho3--TL52kg/zh-cn_image_0000002561753155.png?HW-CC-KV=V1&HW-CC-Date=20260427T235434Z&HW-CC-Expire=86400&HW-CC-Sign=08B905F46EAB1E64CCFEBE9E3FEBFC1688F1FEA2E0AE133AAFD6589DC3B9DDAD)

说明

若选择Native C++模板创建OpenHarmony应用，且应用需要在RK开发板上运行，则需在对应Native模块的build-profile.json5文件buildOption/externalNativeOptions字段下，新增abiFilters字段并赋值为"armeabi-v7a"。
