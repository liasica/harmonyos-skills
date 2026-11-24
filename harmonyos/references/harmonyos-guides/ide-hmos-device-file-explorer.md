---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-device-file-explorer
title: 访问设备文件
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 应用调试 > 访问设备文件
category: harmonyos-guides
scraped_at: 2026-11-24T12:42:46+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:b00664717409044d6250842a9552ccf8f544c128a1015e56ebf2e1ef2932beab
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

1. 在编辑器右侧点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/C_aIwTDURyyxRYCisfMbQg/zh-cn_image_0000002820681017.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=DE101F8DDE4958ED0FA9615808E54BD299DA213686F25318DA9243DB7175FC79 "点击放大")图标打开设备文件浏览器。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/SrYI3x2mS4CeLvyUPl6iGg/zh-cn_image_0000002820721025.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=087AA498433E91BA0821F3A2A7C8D8C03EDCC24F283AB2DFFD785D47FE1ED66A)
2. 从下拉列表中选择设备（设备需已连接）。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/ttwhLwbbQpiazboCXOlalQ/zh-cn_image_0000002820681019.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=F203A1FCFDBBF4DA91CAB0091B9B86EAE6F5A2F28485564F405C5D60C9D88730)
3. 选择设备后，显示文件/文件夹列表，可进行以下操作：
   1. 右键单击目录或文件，进行新建/删除操作。
   2. 右键单击**下载**将选定的文件或目录下载到本地，右键单击**上传**将本地文件上传到设备指定目录。
   3. 在搜索框中输入关键字，可以对目录和文件进行搜索。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/5yqlABr7Tfm_9eFjLsXU8w/zh-cn_image_0000002792001060.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=2711EF1B277867BAB553FE0DF136DCC2802203F86EFB6EA242A35511BD02C518)
   4. 双击某个文件可在DevEco Studio中将其打开。打开文件会默认下载文件到临时目录，关闭文件后，临时文件将被删除。
   5. 如果通过命令行方式上传文件到设备后，需要右键对应文件夹，选择**刷新**后（或点击顶部![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/lHLrnTXYRlu9hvA8T5JDFg/zh-cn_image_0000002820721023.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=F6BCA54C2259EBDECD9E7382ED5D71060B58FB37CCF4A91A848A293E001F46BB "点击放大")刷新按钮）才可以在**设备文件浏览器**窗口中显示该文件。

## 普通文件视图

普通文件视图将按照设备的真实物理路径显示当前设备上的文件结构。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/7IqulbAnTq-qePfi7hhtVw/zh-cn_image_0000002791841082.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=4202F4D534A5A945586A564398377F5B0E923F462975737CC563F521C4654EE2)

### 公共目录

用户的桌面、文档、下载等公共目录位于/storage/media/100/local/files/Docs路径下，支持删除、上传、下载操作。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/tzMLdJePQQe0dJvLWtjJSQ/zh-cn_image_0000002792001056.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=29DC80379465A26DFA232B52BB8D934BFCBC6FD99ABDC7C9E01DCA2D72BB035F)

## 应用沙箱视图

连接真机设备，将调试应用推送到设备上并运行。点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/cLhOL6j-Sra5T5N-OdfaxQ/zh-cn_image_0000002791841086.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=D014C6A9A9E57D2AAE1A5EE9720E8715F4D7826BE3F9B2D8797AC07ACA912353)显示调试签名应用列表。

应用沙箱视图将按照应用的沙箱文件路径显示应用的沙箱文件结构，支持文件的新建、删除、上传、下载等操作。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/RhFNj6GnQvWWwfp75WEdNQ/zh-cn_image_0000002791841084.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=28002DE272BCDB53BBC2969CE218E1BD38F9D942807E95555DAE321958565331)
