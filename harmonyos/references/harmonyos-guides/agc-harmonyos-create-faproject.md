---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/agc-harmonyos-create-faproject
title: 创建元服务工程
breadcrumb: 指南 > 开发环境搭建 > 工程创建 > 模块管理 > 端云一体化开发 > 开发端云工程 > 创建端云一体化开发工程 > 创建元服务工程
category: harmonyos-guides
scraped_at: 2026-04-28T07:55:00+08:00
doc_updated_at: 2026-01-30
content_hash: sha256:5dc279db4faa8a5f78420ee72a2a7feb3f6a0ebb284e9d72f52fdf46b87b6b17
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
2. 点击“Atomic Service”页签，选择合适的云开发模板，然后点击“Next”。

   说明

   当前仅支持通用云开发模板（[CloudDev]Empty Ability）。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/EGJy5H8BR_6_UeHbKvfTfw/zh-cn_image_0000002495751689.png?HW-CC-KV=V1&HW-CC-Date=20260427T235458Z&HW-CC-Expire=86400&HW-CC-Sign=C898A64789193A797FF6C884873C4609FE1A1D96B1DE6579A63022BA41B93437)

### 关联云开发资源

为工程关联云开发所需的资源，即将您账号团队在AGC创建的元服务关联到待创建工程。具体操作如下：

1. （可选）如您尚未登录DevEco Studio，点击“Sign In”，在弹出的账号登录页面，使用[已实名认证](agc-harmonyos-clouddev-account.md)的华为开发者账号完成登录。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/P1Jjtfs3T4KU5CeEZE8D9w/zh-cn_image_0000002214858877.png?HW-CC-KV=V1&HW-CC-Date=20260427T235458Z&HW-CC-Expire=86400&HW-CC-Sign=AFA802884319EE6BB18C006C31AEB3E2EF53B86C2FE8305F7F393C1B7E9E5916)

   登录成功后，界面将展示账号昵称。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/99/v3/zOL2opKaQRCihT_D24Zcsw/zh-cn_image_0000002179498232.png?HW-CC-KV=V1&HW-CC-Date=20260427T235458Z&HW-CC-Expire=86400&HW-CC-Sign=7AE582F46154C5024D6367989B4CD0FB5E7F6EA50BE2B9B5B88D718ADCA6AC4E)
2. 选择已登录账号下的APP ID，以关联AGC上的元服务。
   * 从APP ID下拉列表中选中所需的APP ID后，界面会展示该元服务在AGC控制台的名称、所属项目、包名与数据处理位置。确认无误后，点击“Next”。

     说明

     元服务包名为自动生成，格式为固定前缀与appid的组合（com.atomicservice.[appid]）。不符合命名规范的包名无法在APP ID下拉列表中展示。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/v2Qnq5oVQtqPl7juA1VaDQ/zh-cn_image_0000002496005713.png?HW-CC-KV=V1&HW-CC-Date=20260427T235458Z&HW-CC-Expire=86400&HW-CC-Sign=337F44750A558E8C476AA7D02BEBB54E86C35D50E3DF67DEFA048A8B705B98E5)
   * 当出现以下场景时，您可点击“Register App ID”，[前往AGC控制台补充创建元服务](agc-harmonyos-create-faproject.md#section397317130308)。创建成功后返回DevEco Studio界面，即可看到新建的元服务信息。
     + APP ID框为空，即当前账号尚未在AGC控制台创建任何元服务。
     + 您需为待创建工程关联一个新的元服务。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/EqnWsWyoTAmLV8L0FwITrw/zh-cn_image_0000002214858837.png?HW-CC-KV=V1&HW-CC-Date=20260427T235458Z&HW-CC-Expire=86400&HW-CC-Sign=A10463A635256E2057BC21D6F4D29B5014F7592996DC2A3ACF6AFB6C6AE85486)
   * 如查询到的元服务尚未关联任何项目，则无法选中。请先[将游离元服务添加到AGC项目下](agc-harmonyos-create-faproject.md#section152521927193013)，再返回DevEco Studio界面操作。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/437BQA6lRcm-bEfdIO_vOg/zh-cn_image_0000002462648052.png?HW-CC-KV=V1&HW-CC-Date=20260427T235458Z&HW-CC-Expire=86400&HW-CC-Sign=73E4C8BE45A00323462C60C70EAC316110701D5A76B408793F03863C532EF33A)
   * 如果查询到的元服务所属项目尚未启用数据处理位置，请点击界面提示内的“AppGallery Connect”[设置数据处理位置](../app/agc-help-datalocation-0000001160439813.md)。设置完成后返回DevEco Studio界面，点击“Refresh”刷新当前APP ID列表，即可看到设置的数据处理位置。

     注意

     + 由于云开发目前仅支持中国境内（香港特别行政区、澳门特别行政区、中国台湾除外），请确保项目启用的数据处理位置包含“中国”。
     + 无论项目启用的默认数据处理位置为哪个站点，后续开发的云服务资源都将部署在“中国”站点。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/lU67pzHOQESn06YOpxq_eA/zh-cn_image_0000002462747966.png?HW-CC-KV=V1&HW-CC-Date=20260427T235458Z&HW-CC-Expire=86400&HW-CC-Sign=4D3DDDAA1BFBE9EEECEBE74B7149C02E8E6CE173CF7BE60929C5ED1E48047C5F)

### 配置工程信息

1. 进入工程配置界面，配置工程的基本信息。

   其中，Device type和Enable CloudDev参数不可更改，其他参数请参考[创建元服务工程](../atomic-guides/atomic-service-create-project.md)内对应的指导进行配置。

   | 参数 | 说明 |
   | --- | --- |
   | Device type | 该工程模板支持的设备类型，目前仅支持手机设备。 |
   | Enable CloudDev | 是否启用云开发。云开发模板默认启用且无法更改。 |

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/cTIiobKMRQmJ__GH3XK6-Q/zh-cn_image_0000002547471367.png?HW-CC-KV=V1&HW-CC-Date=20260427T235458Z&HW-CC-Expire=86400&HW-CC-Sign=646A1E34A7A88884C5E721A901F8297FFB0C35497AAB31466E005D15A6CDBCEC)

2. 点击“Finish”，进入主开发界面，DevEco Studio执行工程同步操作，端侧工程会自动执行“ohpm install”，云侧工程会自动执行“npm install”，以分别下载端侧和云侧依赖。

   说明

   若云侧执行“npm install”失败，请排查是否尚未[配置NPM代理](ide-environment-config.md#section197296441787)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/w1m_uxj_Sg-sOdJvKQoHlg/zh-cn_image_0000002214858865.png?HW-CC-KV=V1&HW-CC-Date=20260427T235458Z&HW-CC-Expire=86400&HW-CC-Sign=72B7F31197D05552A506E9C8FD276F99CD574DD9115E3D2AF24EDC9E9537F163)
3. 在主开发界面，可查看刚刚新建的工程。关于工程的详细目录结构介绍，请参见[端云一体化开发工程目录结构](agc-harmonyos-create-faproject.md#section20250910164411)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/gZdphO_3SAu47lxKvqgQzQ/zh-cn_image_0000002214704493.png?HW-CC-KV=V1&HW-CC-Date=20260427T235458Z&HW-CC-Expire=86400&HW-CC-Sign=7A37CB2143EF84A59F7393E449112CB654FA84E51B9E3EFB8FBA2F977513B22E)

## 工程初始化配置

当您成功创建工程并关联云开发资源后，DevEco Studio会为您的工程自动执行一些初始化配置。

### 自动开通云开发服务

DevEco Studio为工程关联的项目自动开通云函数、云数据库、云存储等云开发服务，您可在“Notifications”窗口查看服务开通状态。

说明

* 如服务开通失败，您可通过[CloudDev云开发管理面板](agc-harmonyos-clouddev-console.md)快捷进入AGC控制台进行手动开通。
* 如云存储服务自动开通与手动开通均失败，可能是账户欠费导致。请您[检查账户是否余额不足](../AppGallery-connect-Guides/agc-account-bill-0000001200817917.md#section813072912208)，[补齐欠款](../AppGallery-connect-Guides/agc-account-recharge-0000001126625360.md)后再前往AGC控制台进行手动开通。

## 端云一体化开发工程目录结构

端云一体化开发工程主要包含端开发工程（Application）与云开发工程（CloudProgram）。

### 端开发工程（Application）

端开发工程主要用于开发应用端侧的业务代码，使用通用云开发模板创建的端开发工程目录结构如下图所示。“Application/cloud\_objects”模块用于存放云对象的调用接口类，“src/main/ets/pages”目录下包含了云存储、云数据库和云函数页面，其他目录文件介绍请参见[工程目录结构](ide-project-structure.md)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/uJZJK6e-TbW2po6CB2nPEA/zh-cn_image_0000002179498204.png?HW-CC-KV=V1&HW-CC-Date=20260427T235458Z&HW-CC-Expire=86400&HW-CC-Sign=4D9ACFFD8B536F07B2AA9B8B674F255AC92353ABC3667F6AAD2640E37BC684BF)

### 云开发工程（CloudProgram）

在云开发工程中，您可为您的元服务开发云端代码，包括云函数和云数据库服务代码。使用通用云开发模板创建的云开发工程目录结构如下图所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/F5O857PMTGe2zB0-enxtAA/zh-cn_image_0000002279948894.png?HW-CC-KV=V1&HW-CC-Date=20260427T235458Z&HW-CC-Expire=86400&HW-CC-Sign=75455A3ECBFEBEB3F6A860BB2D876AF509C6435E9479DCE87B6BBD0B82DFC751)

* clouddb：云数据库目录，包含数据条目目录（dataentry）和对象类型目录（objecttype）。
  + dataentry：用于存放数据条目文件。

    该目录下一般会根据您选择的云开发模板预置数据条目示例文件。在通用云开发模板工程中，该目录下会预置名为“d\_Post.json”的数据条目示例文件，内含两条示例数据。您可按需使用、修改或删除。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/CJA0we_FQAau7Y3X6aEBbA/zh-cn_image_0000002314788585.png?HW-CC-KV=V1&HW-CC-Date=20260427T235458Z&HW-CC-Expire=86400&HW-CC-Sign=AA6EBED23405E9C021056711D2EACA51278B28762DFFF25687785ACA0F3ED7A3)
  + objecttype：用于存放对象类型文件。

    该目录下一般会根据您选择的云开发模板预置对象类型示例文件。在通用云开发模板工程中，该目录下会预置名为“Post.json”的对象类型示例文件，内含对象类型“Post”的权限、索引、字段名称和字段值等。您可按需使用、修改或删除。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/bhh1rHR2TQCENB9MIj4pPg/zh-cn_image_0000002179498164.png?HW-CC-KV=V1&HW-CC-Date=20260427T235458Z&HW-CC-Expire=86400&HW-CC-Sign=EE17BDAD3C38338DD7AEE80C7EA44168ED77515832BBFC7B41F5BA65934A3BFB)
  + db-config.json：模块配置文件，主要包含云数据库工程的配置信息，如默认存储区名称、默认数据处理位置。
* cloudfunctions：云函数目录，包含各个云函数/云对象子目录。每个子目录下包含了云函数/云对象的配置文件、入口文件、依赖文件等。

  该目录下一般会根据您选择的云开发模板预置示例函数。通用云开发模板工程下预置了一个用于生成UUID的示例云对象“id-generator”，您可按需使用、修改或删除。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/dPcu6MLTSuebXLDnsXffTQ/zh-cn_image_0000002179498100.png?HW-CC-KV=V1&HW-CC-Date=20260427T235458Z&HW-CC-Expire=86400&HW-CC-Sign=5B3FC1875316659D99A04D6CF3F230A1B04718274EE36335E97172F83796DDF5)
* node\_modules：工程同步时执行“npm install”生成，包含“typescript”和“@types/node”公共依赖。
* cloud-config.json：云开发工程配置文件，包含应用名称与ID、项目名称与ID、启用的数据处理位置、支持的设备类型等。
* package.json：定义了“typescript”和“@types/node”公共依赖。
* package-lock.json：工程同步时执行“npm install”生成，记录当前状态下实际安装的各个npm package的具体来源和版本号。

## （可选）AGC元服务管理

### 从DevEco Studio补充创建元服务

如创建元服务工程时，发现尚未在AGC控制台创建对应的元服务，可直接从DevEco Studio进行补充创建。

1. 点击“Register App ID”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/I45sAaHdSyCTBJtOKnF1bg/zh-cn_image_0000002214704425.png?HW-CC-KV=V1&HW-CC-Date=20260427T235458Z&HW-CC-Expire=86400&HW-CC-Sign=07B0F19B2D794CB10094137943FB0D5D4C740EB2AB6A5F8C4C337211DB79FBAC)
2. 在弹窗中填写待创建的元服务信息后，点击“OK”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/NrBHd2-SRmecfFA03E0pKA/zh-cn_image_0000002496008473.png?HW-CC-KV=V1&HW-CC-Date=20260427T235458Z&HW-CC-Expire=86400&HW-CC-Sign=A659C44863D506BDB5899C0AFB0C9FEB127E81FA5935C1F26857AD9A855DD1F8)

   | 参数 | 说明 |
   | --- | --- |
   | Project | 为当前元服务选择所属的项目。可以输入一个新项目名称，或在下拉框中选择已有项目。 |
   | App type | 应用形态。默认为“AtomicService”，不支持修改。 |
   | App name | 元服务在华为应用市场详情页展示的名称。 |
   | App category | 应用分类。元服务暂不支持游戏类别，请选择“App”。  说明  应用分类设置后不支持修改，请谨慎选择。 |
3. 返回DevEco Studio界面，可查看到刚刚创建的元服务的名称及APP ID、所属项目及项目ID、包名、数据处理位置。

   说明

   若元服务关联的是一个新建项目或者尚未启用数据处理位置的已有项目，则还会提示尚未启用数据处理位置，参考[上文](agc-harmonyos-create-faproject.md#li58931263712)处理即可。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/cZW9ZxZfT1aRplXD2G_3Kw/zh-cn_image_0000002463542130.png?HW-CC-KV=V1&HW-CC-Date=20260427T235458Z&HW-CC-Expire=86400&HW-CC-Sign=4E90C69360B1B78B4DCFEA7CEF8EC1F07980101A9CCCC5049DBE5B2577AB22F6)

### 将游离元服务添加到AGC项目下

游离元服务指未关联任何AGC项目的元服务。创建工程时，如需要关联的AGC元服务为游离状态，则您需要将该元服务添加到您的AGC项目下。

注意

元服务与项目的关联关系一旦创建则无法再修改，请谨慎操作。

1. 点击“Not associated yet”，或点击界面下方提示内的“AppGallery Connect”，可打开AGC控制台“开发与服务”页面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0b/v3/VN3becFAT86kdLze8muumw/zh-cn_image_0000002495887153.png?HW-CC-KV=V1&HW-CC-Date=20260427T235458Z&HW-CC-Expire=86400&HW-CC-Sign=C47CDDCBB3116F3DFC055575258397E64E64B6C32A17F51B15D1A24A7432B91F)
2. 点击选择希望为元服务关联的项目，或者点击“添加项目”新建一个项目。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/1y3is591Ty-Jta9yWbGuqw/zh-cn_image_0000002463616410.png?HW-CC-KV=V1&HW-CC-Date=20260427T235458Z&HW-CC-Expire=86400&HW-CC-Sign=3C79A43DE38008F6606A223056AC9BECBFEC9AB52FEE563A7F84D9F94178A96E)
3. 如选择了新建一个项目，设置项目名称，点击“确认”。

   如选择了已有项目，则忽略此步骤。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/1bvja17kSym1iaa9ecFitg/zh-cn_image_0000002179498244.png?HW-CC-KV=V1&HW-CC-Date=20260427T235458Z&HW-CC-Expire=86400&HW-CC-Sign=5C52F2BE561D972FD1C33B3319CCE2D5E95965909FF4C3DE01C89345DFD52A24)
4. 设置或管理项目的数据处理位置。
   * 如项目尚未设置数据处理位置：
     1. 点击“启用”。

        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/JWnglvzETM-3IQvmbs7DGA/zh-cn_image_0000002179338536.png?HW-CC-KV=V1&HW-CC-Date=20260427T235458Z&HW-CC-Expire=86400&HW-CC-Sign=9341AFCB2BB4DDB399F5D1885E52352F50DB74ABE13FBEDB5975C9E0C9C1C850)
     2. 仔细阅读提示框的文字说明后，在“启用”栏为您的项目勾选一个或多个数据处理位置，并在“设为默认”栏将其中一个设置为默认数据处理位置。

        注意

        启用的数据处理位置必须包含中国站点。

        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/8VrC1OnGTJiY4PRKtWn5tQ/zh-cn_image_0000002179498220.png?HW-CC-KV=V1&HW-CC-Date=20260427T235458Z&HW-CC-Expire=86400&HW-CC-Sign=B6C410ABB0983386D36EC7BB607A858AE1F25FA73EAECB9FE54AD441BE95BEA8)
   * 如项目已设置过数据处理位置，可点击“管理”启用新的数据处理位置、取消已启用的数据处理位置，或修改默认数据处理位置。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/YHCsnPisThmePXPPbjDNJA/zh-cn_image_0000002179338548.png?HW-CC-KV=V1&HW-CC-Date=20260427T235458Z&HW-CC-Expire=86400&HW-CC-Sign=8CCACC76D48E2A29B21F76C2BD40011889D209191AAEBCF78827950902335826)
5. 点击“确认”，元服务成功关联项目。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/LQ9pZ_zOSUmm-T9_bjvu_A/zh-cn_image_0000002214858853.png?HW-CC-KV=V1&HW-CC-Date=20260427T235458Z&HW-CC-Expire=86400&HW-CC-Sign=4A11138F004E7C9573FA2E54A111832DC7B08CCF618D8E395ABB54AFD6CEC55B)
6. 返回DevEco Studio，点击“Refresh”刷新，可看到元服务已关联上了项目。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/lN33ASCySXCCPqk-_2DRlw/zh-cn_image_0000002509136865.png?HW-CC-KV=V1&HW-CC-Date=20260427T235458Z&HW-CC-Expire=86400&HW-CC-Sign=25C283A7F7CC5FA0C4DDDACC4F7071EB03FDFF42C19F0E08AEC8AE98EB6388A9)
