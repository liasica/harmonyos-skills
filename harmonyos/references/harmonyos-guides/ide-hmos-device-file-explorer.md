---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-device-file-explorer
title: 访问设备文件
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 应用调试 > 访问设备文件
category: harmonyos-guides
scraped_at: 2026-10-11T07:23:21+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:12966f9a85003d967a91c63ab551d77890d9d605da226e853fc4d5ecd250c41a
---

开发者可以使用设备文件浏览器，在鸿蒙电脑DevEco Studio上进行文件新建、删除、上传、下载等操作，而无需使用命令行，提升开发效率，当前支持普通文件视图与应用沙箱视图两种模式。

## 使用场景

* 查看设备上的文件列表及基本信息。
* 在设备上搜索文件及文件夹。
* 在设备上新建、删除文件。
* 从本地上传文件到设备上，从设备上下载文件到本地。

## 使用约束

* 已连接设备。
* 不支持访问无权限目录，新建、删除、上传、下载文件受设备权限约束。
* 文件新建、删除、上传、下载操作时，每次只能选中一个目录或文件，不支持多选。
* 不支持文件拖拽。
* 不支持文件修改。如需对文件进行修改，需下载至本地，在本地修改后再上传至设备。
* 应用需为debug应用才可使用沙箱视图查看文件结构、对应用沙箱内的文件/文件夹进行新建、删除、上传或下载操作。

## 操作步骤

1. 在编辑器右侧点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/buqfqfJGTUiy96MERNW3pQ/zh-cn_image_0000002779728941.png "点击放大")图标打开设备文件浏览器。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/rkkrrVf2T66kV5Z_sNaACA/zh-cn_image_0000002750169768.png)
2. 从下拉列表中选择设备（设备需已连接）。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7/v3/sfA8C8hOTHyBTeQqal081Q/zh-cn_image_0000002750169770.png)
3. 选择设备后，显示文件/文件夹列表，可进行以下操作：
   1. 右键单击目录或文件，进行新建/删除操作。
   2. 右键单击**下载**将选定的文件或目录下载到本地，右键单击**上传**将本地文件上传到设备指定目录。
   3. 在搜索框中输入关键字，可以对目录和文件进行搜索。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/pujzFo-7S0W8iSDVxnai4w/zh-cn_image_0000002750009882.png)
   4. 双击某个文件可在DevEco Studio中将其打开。打开文件会默认下载文件到临时目录，关闭文件后，临时文件将被删除。
   5. 如果通过命令行方式上传文件到设备后，需要右键对应文件夹，选择**刷新**后（或点击顶部![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/PLFlloMVTyeiCgOdG1aflg/zh-cn_image_0000002750009880.png "点击放大")刷新按钮）才可以在**设备文件浏览器**窗口中显示该文件。

## 普通文件视图

普通文件视图将按照设备的真实物理路径显示当前设备上的文件结构。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/T3SPWv5BR5-ddBsxtvLkJQ/zh-cn_image_0000002779608797.png)

### 公共目录

用户的桌面、文档、下载等公共目录位于/storage/media/100/local/files/Docs路径下，支持删除、上传、下载操作。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/swAFqHqlQb6nAM69BYT-Cg/zh-cn_image_0000002750169778.png)

## 应用沙箱视图

连接真机设备，将调试应用推送到设备上并运行。点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/y046fmYiSuqLspsXq9mxag/zh-cn_image_0000002779728939.png)显示调试签名应用列表。

应用沙箱视图将按照应用的沙箱文件路径显示应用的沙箱文件结构，支持文件的新建、删除、上传、下载等操作。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/KBmka4QhTlamVLuyLqaBjg/zh-cn_image_0000002779728937.png)
