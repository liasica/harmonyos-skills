---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-device-file-explorer
title: 访问设备文件
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 应用调试 > 访问设备文件
category: harmonyos-guides
scraped_at: 2026-11-14T08:49:17+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:9a6849763381b2bb045bcf4faf1e751b67aad4aa90ba24387a7fbfcef7c9dc3e
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

1. 在编辑器右侧点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/zbVyrcR8Tc6hQpwwsbJLCA/zh-cn_image_0000002781311316.png?HW-CC-KV=V1&HW-CC-Date=20261114T004916Z&HW-CC-Expire=31536000000&HW-CC-Sign=6D67EE11B791298DD0EE585DE15DE7EE4DD5487A3B7773C92E153EE906428DF3 "点击放大")图标打开设备文件浏览器。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/CQDmOZjGTH6MaMwCydDP8w/zh-cn_image_0000002810750909.png?HW-CC-KV=V1&HW-CC-Date=20261114T004916Z&HW-CC-Expire=31536000000&HW-CC-Sign=871F700A1FCFB0FDD447A89DE8E00D24C7EDCDE83624289155C720A33A4FD18B)
2. 从下拉列表中选择设备（设备需已连接）。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/bGMlfovfRoad9K5U1c8k_A/zh-cn_image_0000002810630801.png?HW-CC-KV=V1&HW-CC-Date=20261114T004916Z&HW-CC-Expire=31536000000&HW-CC-Sign=A9278F8AAA537F7FCFE13DBCC1C8783A7DC4EE27CB5CB18601AB52A193B0889E)
3. 选择设备后，显示文件/文件夹列表，可进行以下操作：
   1. 右键单击目录或文件，进行新建/删除操作。
   2. 右键单击**下载**将选定的文件或目录下载到本地，右键单击**上传**将本地文件上传到设备指定目录。
   3. 在搜索框中输入关键字，可以对目录和文件进行搜索。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/R7scb-XsT2GknmTX9BTSsg/zh-cn_image_0000002810630803.png?HW-CC-KV=V1&HW-CC-Date=20261114T004916Z&HW-CC-Expire=31536000000&HW-CC-Sign=49D390F57D59A34029048E3E912D8F6D75D9D3EA2EEDBD3128FAFC1D9C220C1B)
   4. 双击某个文件可在DevEco Studio中将其打开。打开文件会默认下载文件到临时目录，关闭文件后，临时文件将被删除。
   5. 如果通过命令行方式上传文件到设备后，需要右键对应文件夹，选择**刷新**后（或点击顶部![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/FL18tk3CQvSrPgMlVkBGaQ/zh-cn_image_0000002810750911.png?HW-CC-KV=V1&HW-CC-Date=20261114T004916Z&HW-CC-Expire=31536000000&HW-CC-Sign=4A76FAFEC4D998DB2959FF8F582DA019CBD4368CED48652C6942D3A70D9EC169 "点击放大")刷新按钮）才可以在**设备文件浏览器**窗口中显示该文件。

## 普通文件视图

普通文件视图将按照设备的真实物理路径显示当前设备上的文件结构。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/qM2UKevURYKq4Q9EVDOxRQ/zh-cn_image_0000002781471252.png?HW-CC-KV=V1&HW-CC-Date=20261114T004916Z&HW-CC-Expire=31536000000&HW-CC-Sign=2748C89781F05FDAC837CABBA2645545DBF615EEFBEB0C091A4AFC5FCD88871B)

### 公共目录

用户的桌面、文档、下载等公共目录位于/storage/media/100/local/files/Docs路径下，支持删除、上传、下载操作。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/OmtYx5TnTyW5oHNP_D0yBQ/zh-cn_image_0000002781311318.png?HW-CC-KV=V1&HW-CC-Date=20261114T004916Z&HW-CC-Expire=31536000000&HW-CC-Sign=8918EF65DBFF52A572984916783076651D54D756CF93F7DAC6BBD60DA405DA6A)

## 应用沙箱视图

连接真机设备，将调试应用推送到设备上并运行。点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6/v3/1dkpPDuPSrKayhUq0l06Zw/zh-cn_image_0000002781471250.png?HW-CC-KV=V1&HW-CC-Date=20261114T004916Z&HW-CC-Expire=31536000000&HW-CC-Sign=71C9FD87572097825C7107E7ECDEA60F622A7FDDE10EFD08F6A6BA4385A38716)显示调试签名应用列表。

应用沙箱视图将按照应用的沙箱文件路径显示应用的沙箱文件结构，支持文件的新建、删除、上传、下载等操作。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/WBVzMpkQQUapOZEb-280gw/zh-cn_image_0000002781311314.png?HW-CC-KV=V1&HW-CC-Date=20261114T004916Z&HW-CC-Expire=31536000000&HW-CC-Sign=06A3598CA1F8A3358DF60F0EE8B6E25BC66A56A46B77286557A78C2A38EE0CDE)
