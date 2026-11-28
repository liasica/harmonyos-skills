---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-device-file-explorer
title: 访问设备文件
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 应用调试 > 访问设备文件
category: harmonyos-guides
scraped_at: 2026-11-28T10:34:55+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:875f493dfec54fc95cb0d4a3c2e976c364609130807c8a50f6bf802ea82f79bc
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

1. 在编辑器右侧点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/0ETgeQCJTVSjq71UEULcQA/zh-cn_image_0000002820681017.png?HW-CC-KV=V1&HW-CC-Date=20261128T023455Z&HW-CC-Expire=31536000000&HW-CC-Sign=9334B223F6FE11317D2136405A65CE2FB4B5CB767E92C1C389A79D2D9702F87F "点击放大")图标打开设备文件浏览器。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/LXDFK1NlSl6NwBONbnBXAQ/zh-cn_image_0000002820721025.png?HW-CC-KV=V1&HW-CC-Date=20261128T023455Z&HW-CC-Expire=31536000000&HW-CC-Sign=833C9EE7AE1A3B05FE7206E0D025AD36B86BCFF3FD618310071020068CBD2587)
2. 从下拉列表中选择设备（设备需已连接）。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/MHOF9tulRdqIM9PCkNNRmg/zh-cn_image_0000002820681019.png?HW-CC-KV=V1&HW-CC-Date=20261128T023455Z&HW-CC-Expire=31536000000&HW-CC-Sign=24F5DEC278AEADA6C63ACB3C25292EA995189E5BEA69EA71A6833E08A3128344)
3. 选择设备后，显示文件/文件夹列表，可进行以下操作：
   1. 右键单击目录或文件，进行新建/删除操作。
   2. 右键单击**下载**将选定的文件或目录下载到本地，右键单击**上传**将本地文件上传到设备指定目录。
   3. 在搜索框中输入关键字，可以对目录和文件进行搜索。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/Gl6OJubfTPq3Jxz_mAibGg/zh-cn_image_0000002792001060.png?HW-CC-KV=V1&HW-CC-Date=20261128T023455Z&HW-CC-Expire=31536000000&HW-CC-Sign=3471EFE93EFFDF44C71738AED6CF091EC928020CDE66EBAC8E574AE3ABC300C1)
   4. 双击某个文件可在DevEco Studio中将其打开。打开文件会默认下载文件到临时目录，关闭文件后，临时文件将被删除。
   5. 如果通过命令行方式上传文件到设备后，需要右键对应文件夹，选择**刷新**后（或点击顶部![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/mYLGASkYQcuyTzXm-FlJMg/zh-cn_image_0000002820721023.png?HW-CC-KV=V1&HW-CC-Date=20261128T023455Z&HW-CC-Expire=31536000000&HW-CC-Sign=7BC4591B13F1E52802CD825B2A011ADCB0F935801EFFED70DE510AC0B4837291 "点击放大")刷新按钮）才可以在**设备文件浏览器**窗口中显示该文件。

## 普通文件视图

普通文件视图将按照设备的真实物理路径显示当前设备上的文件结构。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/4t153HP5TIOKagruzP5Wmw/zh-cn_image_0000002791841082.png?HW-CC-KV=V1&HW-CC-Date=20261128T023455Z&HW-CC-Expire=31536000000&HW-CC-Sign=AC2B8492E458DC5A07855DA127A74BC340899ECDD9D2AFA0B5942D65118FB48D)

### 公共目录

用户的桌面、文档、下载等公共目录位于/storage/media/100/local/files/Docs路径下，支持删除、上传、下载操作。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/AOFW-KW7Q5SXhXw3X7vqqg/zh-cn_image_0000002792001056.png?HW-CC-KV=V1&HW-CC-Date=20261128T023455Z&HW-CC-Expire=31536000000&HW-CC-Sign=D34AD290C25AD4D4A26343452D00D4580A137B63AF679FEA71671AE6F9D70851)

## 应用沙箱视图

连接真机设备，将调试应用推送到设备上并运行。点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/exn2SKUNRParOpF0sd1zOQ/zh-cn_image_0000002791841086.png?HW-CC-KV=V1&HW-CC-Date=20261128T023455Z&HW-CC-Expire=31536000000&HW-CC-Sign=B1911079B9A7C51D8595234E99C748BD52EF68590400B893C83B397FBC113D4F)显示调试签名应用列表。

应用沙箱视图将按照应用的沙箱文件路径显示应用的沙箱文件结构，支持文件的新建、删除、上传、下载等操作。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/nOvwBwQGSLyioYDhvHjrpw/zh-cn_image_0000002791841084.png?HW-CC-KV=V1&HW-CC-Date=20261128T023455Z&HW-CC-Expire=31536000000&HW-CC-Sign=A13D412D81E15538D6826133F0542BEC6028A8CA39ACCE12CDF59ECAA7EA2F5B)
