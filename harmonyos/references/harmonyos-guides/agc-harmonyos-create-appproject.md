---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/agc-harmonyos-create-appproject
title: 创建HarmonyOS应用工程
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 开发环境搭建 > 工程创建 > 模块管理 > 端云一体化开发 > 开发端云工程 > 创建端云一体化开发工程 > 创建HarmonyOS应用工程
category: harmonyos-guides
scraped_at: 2026-11-28T10:34:29+08:00
doc_updated_at: 2026-11-13
content_hash: sha256:c76104bea12983cbbbdf38648cc71a910b539340c740cad15a6468505080cbd8
---

## 新建工程

### 前提条件

* 您已完成[开发准备工作](agc-harmonyos-clouddev-prerequisite.md)。
* 您已使用[已实名认证](agc-harmonyos-clouddev-account.md)、且注册地为中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）的华为开发者账号登录DevEco Studio。
* 请确保您的华为开发者账号无欠款，账户欠费将导致云存储服务开通失败。

### 选择模板

1. 选择以下任一种方式，打开工程创建向导界面。
   * 如果当前未打开任何工程，可以在DevEco Studio的欢迎页点击“Create Project”开始创建一个新工程。
   * 如果已经打开了工程，可以在菜单栏选择“File > New > Create Project”来创建一个新工程。
2. 在“Application”页签，选择合适的云开发模板，然后点击“Next”。

   **说明** 

   当前仅支持通用云开发模板（[CloudDev]Empty Ability）。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/uZikYeJSSciICyNC4eeWpQ/zh-cn_image_0000002462973802.png?HW-CC-KV=V1&HW-CC-Date=20261128T023428Z&HW-CC-Expire=31536000000&HW-CC-Sign=0E9F139A50A89743496E1374BD1B02029CF96F2F69630E00DA6297182C719EE0)

### 配置工程信息

1. 在工程配置界面，配置工程的基本信息。

   其中，Device type和Enable CloudDev参数不可更改，其他参数请参考[创建一个新的工程](ide-create-new-project.md#section181328285169)内对应的指导进行配置。

   | 参数 | 说明 |
   | --- | --- |
   | Device type | 该工程模板支持的设备类型，目前仅支持手机设备。 |
   | Enable CloudDev | 是否启用云开发。云开发模板默认启用且无法更改。 |

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/cYi_A1l_QwKKw69WyU381g/zh-cn_image_0000002547465643.png?HW-CC-KV=V1&HW-CC-Date=20261128T023428Z&HW-CC-Expire=31536000000&HW-CC-Sign=6964518AA9BC304E2F611BC64D31487B7625E2A50268CAA09A098BBC673EBBC1)

2. 点击“Next”，开始关联云开发资源。

### 关联云开发资源

为工程关联云开发所需的资源，即将您账号团队在HarmonyOS 开发者中心创建的同包名应用关联到当前工程。具体操作如下：

1. （可选）如您尚未登录DevEco Studio，点击“Sign In”，在弹出的账号登录页面，使用[已实名认证](agc-harmonyos-clouddev-account.md)的华为开发者账号完成登录。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/VIhRI-PZSxGLMRglJOCqjA/zh-cn_image_0000002214858793.png?HW-CC-KV=V1&HW-CC-Date=20261128T023428Z&HW-CC-Expire=31536000000&HW-CC-Sign=57298156F5E3C33636546C04468E95129582CC83951F0AF94EED405C7611FE3E)

   登录成功后，界面将展示账号昵称。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/-vzkd7mhQV-Q-FwPnyrlXw/zh-cn_image_0000002179338404.png?HW-CC-KV=V1&HW-CC-Date=20261128T023428Z&HW-CC-Expire=31536000000&HW-CC-Sign=1357B1D7CE5540DB359894CBC6D333A308F5D2EC470EFE961A7400445648412B)
2. 点击“Team”下拉框，选择开发团队。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/i4odWUZLSvqTZFtqdMtELA/zh-cn_image_0000002500639597.png?HW-CC-KV=V1&HW-CC-Date=20261128T023428Z&HW-CC-Expire=31536000000&HW-CC-Sign=B017D592F03056E20B17CBED84D9729E96F7C5AD7A5B421825B72BB2BEE3DADE)
3. 关联应用。

   选中团队后，系统根据工程Bundle name在该团队中自动查询HarmonyOS 开发者中心的同包名应用。

   * 如查询到应用，选中该应用，点击“Finish”即可。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/ULezecRLTv20CzLH4fDTTw/zh-cn_image_0000002214704349.png?HW-CC-KV=V1&HW-CC-Date=20261128T023428Z&HW-CC-Expire=31536000000&HW-CC-Sign=5A0097F452D20E7E648584F3CBEA1251532538FED8662BE29376AAD19A0BDA38)
   * 如查询到的应用尚未关联任何项目（即为游离应用），则无法选中。请先[将游离应用添加到项目下](agc-harmonyos-create-appproject.md#section152521927193013)。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/VI0jg-VTTdyb9j6dLFM3Uw/zh-cn_image_0000002179498144.png?HW-CC-KV=V1&HW-CC-Date=20261128T023428Z&HW-CC-Expire=31536000000&HW-CC-Sign=E67611A099B5C3403B7F88C57B0EA1BD15F92AE38A5130E08EAD314E9626DEE7)
   * 如果查询到的应用所属项目尚未启用数据处理位置，请点击界面提示内的“AppGallery Connect”[设置数据处理位置](../app/agc-help-datalocation-0000001160439813.md)。设置完成后返回DevEco Studio界面，点击Bundle name后的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/dHFA0dLBT1ClVzevQx6n7g/zh-cn_image_0000002495893905.png?HW-CC-KV=V1&HW-CC-Date=20261128T023428Z&HW-CC-Expire=31536000000&HW-CC-Sign=DED58CCD155515D727E1AB724C1D6FB51603ED6513C95210E3D612C22AFC2D28)刷新当前APP ID列表，即可看到设置的数据处理位置。

     **注意** 

     + 由于云开发目前仅支持中国境内（香港特别行政区、澳门特别行政区、中国台湾除外），请确保项目启用的数据处理位置包含“中国”。
     + 无论项目启用的默认数据处理位置为哪个站点，后续开发的云服务资源都将部署在“中国”站点。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/08/v3/jg-Dq59RSHWPqs4j732_IQ/zh-cn_image_0000002495893753.png?HW-CC-KV=V1&HW-CC-Date=20261128T023428Z&HW-CC-Expire=31536000000&HW-CC-Sign=5F2A695D385028B20BA1438B65AA90007648B86895027804345FFE724F781D90)
   * 如查询到应用但出现如下提示，表明查询到的应用类型为元服务，与当前工程类型不一致。请修改以确保当前工程与HarmonyOS 开发者中心同包名应用均为HarmonyOS应用类型。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/3NXKNszHTri89rNIgnDW8Q/zh-cn_image_0000002462815550.png?HW-CC-KV=V1&HW-CC-Date=20261128T023428Z&HW-CC-Expire=31536000000&HW-CC-Sign=42226B5E4A7DD567B056B581FEA1CD33B423817724991C0CE4EB86E607154EA0)
   * 如在当前团队中未查询到同包名应用，请先确认填写的包名是否有误。
     + 如包名有误，点击界面提示中的“go back”返回工程信息配置界面进行修改。
     + 如包名无误，则表明当前团队尚未在HarmonyOS 开发者中心创建与当前工程包名相同的应用。您可点击界面提示中的“AppGallery Connect”，[前往HarmonyOS 开发者中心进行补充创建](agc-harmonyos-create-appproject.md#section397317130308)。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/-Ow0jB-LRlSAgi05i8It1A/zh-cn_image_0000002214858765.png?HW-CC-KV=V1&HW-CC-Date=20261128T023428Z&HW-CC-Expire=31536000000&HW-CC-Sign=CBEF7EAB939490FA2F67BA878F7409FF3334C20675486401A682F2FA1E3A3322)

     完成以上操作后，DevEco Studio即可获取到同包名应用信息。选中应用后，点击“Finish”。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3/v3/eWrcHxsITdGLJMS9j_mvIg/zh-cn_image_0000002214858801.png?HW-CC-KV=V1&HW-CC-Date=20261128T023428Z&HW-CC-Expire=31536000000&HW-CC-Sign=5C41946DC9DC53895E7CA0C7D53B53357E445B2C694120A1E5F35FAA6C41724B)
4. 如您所属的团队尚未签署云开发相关协议，点击协议链接仔细阅读协议内容后，勾选同意协议，点击“Finish”。

   **说明** 

   只有账号持有者和法务角色才有权限签署协议。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/bX_Xh0pkS-uhm79xB2C-2w/zh-cn_image_0000002179498108.png?HW-CC-KV=V1&HW-CC-Date=20261128T023428Z&HW-CC-Expire=31536000000&HW-CC-Sign=9AFC051348199A70DACEBE86BCCFEC4B0574305715EB63532F18A5B049B67E78)
5. 进入主开发界面，DevEco Studio执行工程同步操作，端侧工程会自动执行“ohpm install”，云侧工程会自动执行“npm install”，以分别下载端侧和云侧依赖。

   **说明** 

   若云侧执行“npm install”失败，请排查是否尚未[配置NPM代理](ide-environment-config.md#section197296441787)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/a0y2bsBvTDWJYZXsX0u6VQ/zh-cn_image_0000002179498148.png?HW-CC-KV=V1&HW-CC-Date=20261128T023428Z&HW-CC-Expire=31536000000&HW-CC-Sign=35A74F3F9345CCEF688DABDE628AE6FABA3F9C3D00F797835B1AA7804EB1C59F)
6. 在主开发界面，可查看刚刚新建的工程。关于工程的详细目录结构介绍，请参见[端云一体化开发工程目录结构](agc-harmonyos-create-appproject.md#section20250910164411)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/rfL4tTfrQ_WBD0t6uP8FOQ/zh-cn_image_0000002214704397.png?HW-CC-KV=V1&HW-CC-Date=20261128T023428Z&HW-CC-Expire=31536000000&HW-CC-Sign=BD910DFE54C388E11AE89A737B33D1D9EC916E88E0CEDD49B2A0AB98FC86F9C0)

## 工程初始化配置

当您成功创建工程并关联云开发资源后，DevEco Studio会为您的工程自动执行一些初始化配置。

### 自动开通云开发服务

DevEco Studio为工程关联的项目自动开通云函数、云数据库、云存储等云开发服务，您可在“Notifications”窗口查看服务开通状态。

**说明** 

* 如服务开通失败，您可通过[CloudDev云开发管理面板](agc-harmonyos-clouddev-console.md)快捷进入HarmonyOS 开发者中心进行手动开通。
* 如云存储服务自动开通与手动开通均失败，可能是账户欠费导致。请您[检查账户是否余额不足](../app/agc-help-set-balance-notify-0000002247531780.md)，[补齐欠款](../AppGallery-connect-Guides/agc-account-recharge-0000001126625360.md)后再前往HarmonyOS 开发者中心进行手动开通。

## 端云一体化开发工程目录结构

端云一体化开发工程主要包含端开发工程（Application）与云开发工程（CloudProgram）。

### 端开发工程（Application）

端开发工程主要用于开发应用端侧的业务代码，使用通用云开发模板创建的端开发工程目录结构如下图所示。

“Application/cloud\_objects”模块用于存放云对象的端侧调用接口类，“src/main/ets/pages”目录下包含了云存储、云数据库和云函数页面，其他目录文件介绍请参见[工程目录结构](ide-project-structure.md)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/tAvkbED_SsihU_bTqOcvMA/zh-cn_image_0000002214858825.png?HW-CC-KV=V1&HW-CC-Date=20261128T023428Z&HW-CC-Expire=31536000000&HW-CC-Sign=C5916FCC7FC87BC7C4B628AEDB78752AD3AC948E7D09EFC65E1A5A2CC7F831BE)

### 云开发工程（CloudProgram）

在云开发工程中，您可为您的应用开发云端代码，包括云函数和云数据库服务代码。使用通用云开发模板创建的云开发工程目录结构如下图所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/00dm5yDZTVedsIKYb0MC7A/zh-cn_image_0000002279845320.png?HW-CC-KV=V1&HW-CC-Date=20261128T023428Z&HW-CC-Expire=31536000000&HW-CC-Sign=C9AE6EA2C0D6407162A54A4B94854FD905682055716243162F72CA46AF350264)

* clouddb：云数据库目录，包含数据条目目录（dataentry）、对象类型目录（objecttype）以及云数据库配置文件 （db-config.json）。
  + dataentry：用于存放数据条目文件。

    该目录下一般会根据您选择的云开发模板预置数据条目示例文件。在通用云开发模板工程中，该目录下会预置名为“d\_Post.json”的数据条目示例文件，内含两条示例数据。您可按需使用、修改或删除。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/m0AbXsliQBConTw7TRr1jw/zh-cn_image_0000002314788585.png?HW-CC-KV=V1&HW-CC-Date=20261128T023428Z&HW-CC-Expire=31536000000&HW-CC-Sign=A91420DFFFF31470D998EEA7A3D5DD23BB6F9644FB543665586A186190778035)
  + objecttype：用于存放对象类型文件。

    该目录下一般会根据您选择的云开发模板预置对象类型示例文件。在通用云开发模板工程中，该目录下会预置名为“Post.json”的对象类型示例文件，内含对象类型“Post”的权限、索引、字段名称和字段值等。您可按需使用、修改或删除。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/oSCzr85fQBeD6vz4AF4n-w/zh-cn_image_0000002179498164.png?HW-CC-KV=V1&HW-CC-Date=20261128T023428Z&HW-CC-Expire=31536000000&HW-CC-Sign=2B4FABB5CA09EAA015E2039C6B47219EC3CA55C0420B9B48A2F0FA62B2A39D4F)
  + db-config.json：配置文件，主要包含云数据库工程的配置信息，如默认存储区名称、默认数据处理位置。
* cloudfunctions：云函数目录，包含各个云函数/云对象子目录。每个子目录下包含了云函数/云对象的配置文件、入口文件、依赖文件等。

  该目录下一般会根据您选择的云开发模板预置示例函数。通用云开发模板工程下预置了一个用于生成UUID的示例云对象“id-generator”，您可按需使用、修改或删除。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/2v0YxGeSSfWB1_T76VfrfA/zh-cn_image_0000002179498100.png?HW-CC-KV=V1&HW-CC-Date=20261128T023428Z&HW-CC-Expire=31536000000&HW-CC-Sign=A10B273E585C593D5F28DA4523EAB42FE0D3F8DFD28A8B800877B19023FCF179)
* node\_modules：工程同步时执行“npm install”生成，包含“typescript”和“@types/node”公共依赖。
* cloud-config.json：云开发工程配置文件，包含应用名称与ID、项目名称与ID、启用的数据处理位置、支持的设备类型等。
* package.json：定义了“typescript”和“@types/node”公共依赖。
* package-lock.json：工程同步时执行“npm install”生成，记录当前状态下实际安装的各个npm package的具体来源和版本号。

## （可选）HarmonyOS 开发者中心应用管理

### 从DevEco Studio补充创建同包名应用

如创建工程时，发现尚未在HarmonyOS 开发者中心创建与工程包名相同的应用，可进行补充创建。

1. 点击界面提示内的“AppGallery Connect”，浏览器打开HarmonyOS 开发者中心页面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/7MioG4GzRym0oKU4VON6Iw/zh-cn_image_0000002214858733.png?HW-CC-KV=V1&HW-CC-Date=20261128T023428Z&HW-CC-Expire=31536000000&HW-CC-Sign=D43299202352A76F81ACFAC6983D0B88D5FD00AACFBABC42A42BBCC2C23048F9)
2. 在“应用开发基础信息”页面，填写待创建的应用信息，完成后点击“下一步”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/jQY4LvMtRXO7IG_f5OcMNA/zh-cn_image_0000002312627449.png?HW-CC-KV=V1&HW-CC-Date=20261128T023428Z&HW-CC-Expire=31536000000&HW-CC-Sign=893107D1E626BAD41A02D0CBDBFD8FF64CD556433EDCEECE68446816D606B8D0)

   | 参数 | 说明 |
   | --- | --- |
   | 应用类型 | 创建的HarmonyOS应用形态，默认与您本地工程类型保持一致，不可更改。 |
   | 应用名称 | 应用在华为应用市场详情页展示的名称。 |
   | 应用包名 | 从DevEco Studio中带入自动填充，且不可更改。 |
   | 应用分类 | 请选择普通应用或游戏类应用。  说明：  应用分类设置后不支持修改，请谨慎选择。 |
3. 进入“所属项目信息”页面，为应用选择所属的项目后点击“下一步”。
   * 如需将应用添加到已有项目，点击下拉框进行选择。
   * 如需将应用添加到新项目，直接在框中填写新项目名称。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/gwFb_BLhTviO_9VRpQMSAQ/zh-cn_image_0000002312628981.png?HW-CC-KV=V1&HW-CC-Date=20261128T023428Z&HW-CC-Expire=31536000000&HW-CC-Sign=4A9F9E80FA62B410B016D13E4DC4793367D23CD26E6B51B8E844B06270B721B3)
4. 进入“云开发数据处理位置”页面，设置或管理项目的数据处理位置。
   * 如项目尚未设置数据处理位置：
     1. 点击“启用”。

        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/zd-2seLvSoq6VtxgtX8nuw/zh-cn_image_0000002312516673.png?HW-CC-KV=V1&HW-CC-Date=20261128T023428Z&HW-CC-Expire=31536000000&HW-CC-Sign=C72C9ACB23A0E58155B93F459897C17343E23A279472D501995CFCD7D3973652)
     2. 仔细阅读提示框的文字说明后，在“启用”栏为您的项目勾选一个或多个数据处理位置，并在“设为默认”栏将其中一个设置为默认数据处理位置。

        **注意** 

        启用的数据处理位置必须包含中国站点。

        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/qtBZKp8NRryBa1kUIHNZ4Q/zh-cn_image_0000002214858805.png?HW-CC-KV=V1&HW-CC-Date=20261128T023428Z&HW-CC-Expire=31536000000&HW-CC-Sign=915EB124958E6B0E4F1100984C6EA16885815F92DEFE9AF329C37884A5FC23A0)
   * 如项目已设置过数据处理位置，可点击“管理”启用新的数据处理位置、取消已启用的数据处理位置，或修改默认数据处理位置。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/13oJsNZdRcqvDnwdhxUlcg/zh-cn_image_0000002312630869.png?HW-CC-KV=V1&HW-CC-Date=20261128T023428Z&HW-CC-Expire=31536000000&HW-CC-Sign=C2EF1671401157E33B179217F654DEDF45063B5746720184C864BDF09C6F9C15)
5. 点击“确认”，应用创建完成。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/pr_5rMPgRXCUnJg48ibXgw/zh-cn_image_0000002214858821.png?HW-CC-KV=V1&HW-CC-Date=20261128T023428Z&HW-CC-Expire=31536000000&HW-CC-Sign=33BE76EB354DC58D7E502B90CDC91D13CA896D3717CDDB21755AC436D507D068)
6. 返回DevEco Studio，可看到界面已获取并展示了刚刚创建的应用信息。若不展示，可点击Bundle name后的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/8WLjQxzuRgirjiyKWGGYHw/zh-cn_image_0000002500745449.png?HW-CC-KV=V1&HW-CC-Date=20261128T023428Z&HW-CC-Expire=31536000000&HW-CC-Sign=231AAA62E653B892DFFCBA3A746E69F01AABBD46D5F61A2009783D4AECDB393F)刷新。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/Uv_8shPvTTmGHN0ADABSRQ/zh-cn_image_0000002179338492.png?HW-CC-KV=V1&HW-CC-Date=20261128T023428Z&HW-CC-Expire=31536000000&HW-CC-Sign=7F7726D44314E1050C111D21BEE50B5B177656A55ABD6C37EC59A5174EA2D55B)

### 将游离应用添加到项目下

游离应用指未关联任何项目的应用。创建工程时，如需要关联的应用为游离应用，则您需要将该应用添加到您的项目下。

**注意** 

应用与项目的关联关系一旦创建则无法再修改，请谨慎操作。

1. 点击“Not associated yet”，或点击界面下方提示内的“AppGallery Connect”，可打开HarmonyOS 开发者中心“开发与服务”页面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/goMCNP-iS1qwbX4uxj6FGA/zh-cn_image_0000002214704437.png?HW-CC-KV=V1&HW-CC-Date=20261128T023428Z&HW-CC-Expire=31536000000&HW-CC-Sign=6AABC5C301FD1C1A424833F8E4F88EEB5F7E1329817A877C66F68716FEAC2B9A)
2. 点击选择希望为应用关联的项目，或者点击“添加项目”新建一个项目。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/gpeueR1sSK2NsfD5Wj8XoA/zh-cn_image_0000002496495517.png?HW-CC-KV=V1&HW-CC-Date=20261128T023428Z&HW-CC-Expire=31536000000&HW-CC-Sign=6C0F1081D4586E1A823761926847540E8632E94033DB70CD01375CFD00D6B2A1)
3. 如选择了新建一个项目，设置项目名称，点击“确认”。

   如选择了已有项目，则忽略此步骤。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/Y19nzAMyQGy7OpPXJNoo2g/zh-cn_image_0000002214704389.png?HW-CC-KV=V1&HW-CC-Date=20261128T023428Z&HW-CC-Expire=31536000000&HW-CC-Sign=DFF97F17002250F8F6A2962760296C01B79BC45F5F9A49C08AD311718E1BBB34)
4. 设置或管理项目的数据处理位置。
   * 如项目尚未设置数据处理位置：
     1. 点击“启用”。

        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/S-FVae2lQIe9csLJBJqqeg/zh-cn_image_0000002214704417.png?HW-CC-KV=V1&HW-CC-Date=20261128T023428Z&HW-CC-Expire=31536000000&HW-CC-Sign=57BDCF9A55EACEF5A4FB50A8B363FFCA6763B01C28B384C39F97BCBEC7CCD021)
     2. 仔细阅读提示框的文字说明后，在“启用”栏为您的项目勾选一个或多个数据处理位置，并在“设为默认”栏将其中一个设置为默认数据处理位置。

        **注意** 

        启用的数据处理位置必须包含中国站点。

        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/2d377XcCQJGc9aKj-AYlbA/zh-cn_image_0000002179338436.png?HW-CC-KV=V1&HW-CC-Date=20261128T023428Z&HW-CC-Expire=31536000000&HW-CC-Sign=0E72ED1FFB4EC76D480C44C8FC856BE472D479569F934B2F1753E548F3D98105)
   * 如项目已设置过数据处理位置，可点击“管理”启用新的数据处理位置、取消已启用的数据处理位置，或修改默认数据处理位置。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/L9f93sy3TI-pDYBLl3C8-w/zh-cn_image_0000002179338464.png?HW-CC-KV=V1&HW-CC-Date=20261128T023428Z&HW-CC-Expire=31536000000&HW-CC-Sign=671849F53B9FDFB5616098F22C49208883331B3C9A95AC86B02775697C8C9A0D)
5. 点击“确认”，应用成功关联项目。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/kxzY-huCQsyMbZZm_vd2HA/zh-cn_image_0000002179498200.png?HW-CC-KV=V1&HW-CC-Date=20261128T023428Z&HW-CC-Expire=31536000000&HW-CC-Sign=8B02DEEAB7AF4CD16766156D20F41869BF0CF732635156B0DFA183811D517BAC)
6. 返回DevEco Studio，可看到应用已关联上了项目。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/6r1-D7DAQsWlxgpiEBhrlA/zh-cn_image_0000002214858777.png?HW-CC-KV=V1&HW-CC-Date=20261128T023428Z&HW-CC-Expire=31536000000&HW-CC-Sign=9C9BC992C524BE417EDB3DD79EF1FB5909F67712B58392EAE19BCC7455870E79)
