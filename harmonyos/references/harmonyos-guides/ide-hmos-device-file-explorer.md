---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-device-file-explorer
title: 访问设备文件
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 应用调试 > 访问设备文件
category: harmonyos-guides
scraped_at: 2026-10-09T08:15:33+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:eb55cf422c64c33b273c6690f7b958add69f6c317451ee860c9f2ec48fe4a066
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

1. 在编辑器右侧点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/e7b76P79QQenVOHFvulQYg/zh-cn_image_0000002749323980.png "点击放大")图标打开设备文件浏览器。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/7X-lCEQ-SpuqX-z1QMxEjw/zh-cn_image_0000002778923067.png)
2. 从下拉列表中选择设备（设备需已连接）。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/yyirP_rSQY-zjSgtK8-Esw/zh-cn_image_0000002749483852.png)
3. 选择设备后，显示文件/文件夹列表，可进行以下操作：
   1. 右键单击目录或文件，进行新建/删除操作。
   2. 右键单击**下载**将选定的文件或目录下载到本地，右键单击**上传**将本地文件上传到设备指定目录。
   3. 在搜索框中输入关键字，可以对目录和文件进行搜索。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/SA5BGJR-QOa5sN_6AevUig/zh-cn_image_0000002749323982.png)
   4. 双击某个文件可在DevEco Studio中将其打开。打开文件会默认下载文件到临时目录，关闭文件后，临时文件将被删除。
   5. 如果通过命令行方式上传文件到设备后，需要右键对应文件夹，选择**刷新**后（或点击顶部![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/AJL0GMNOTkyFlLSEa5msaQ/zh-cn_image_0000002778923069.png "点击放大")刷新按钮）才可以在**设备文件浏览器**窗口中显示该文件。

## 普通文件视图

普通文件视图将按照设备的真实物理路径显示当前设备上的文件结构。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/LSbcYCm7Q22ZC3hbyktbKw/zh-cn_image_0000002749483854.png)

### 公共目录

用户的桌面、文档、下载等公共目录位于/storage/media/100/local/files/Docs路径下，支持删除、上传、下载操作。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/vzSKBIYGQe24KV7d_jq3wg/zh-cn_image_0000002779082919.png)

## 应用沙箱视图

连接真机设备，将调试应用推送到设备上并运行。点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/z5rp-6H3RXyXDTktvTCuag/zh-cn_image_0000002779082915.png)显示调试签名应用列表。

应用沙箱视图将按照应用的沙箱文件路径显示应用的沙箱文件结构，支持文件的新建、删除、上传、下载等操作。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/6O3S1I5FRzO8LmK1TI1wIg/zh-cn_image_0000002749323978.png)
