---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-depot-management
title: 仓库管理
breadcrumb: 指南 > 开发环境搭建 > 工程创建 > 模块管理 > ohpm-repo私仓搭建工具 > 页面功能介绍 > 仓库管理
category: harmonyos-guides
scraped_at: 2026-04-29T13:44:46+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:4b353d02cc1795736a2a1cefb0e994efc52283eab953205ac0a61ae2671a4de0
---

仓库管理主要负责管理仓库信息，包括仓库中所有包权限管理，包的上传与下架和uplinks管理。

## 管理仓库

ohpm-repo从5.3.0开始支持多仓配置，并且支持对每个仓库进行权限编辑。

仓库权限分为读权限和写权限。当用户在执行下载包、上传包、下架现有包和编辑包标签时，需要同时具有仓库的对应权限和[包的对应权限](ide-package-permission-management.md)，缺一不可。

| 仓库权限类型 | 前提条件 | 可执行操作 | 典型场景 |
| --- | --- | --- | --- |
| 可读 | 1. 公开可读  2. 授权可读，用户位于授权可读白名单中 | * 下载包 | 开发者获取依赖包 |
| 可写 | 1. 公开可写  2. 授权可写，用户位于授权可写白名单中 | * 下载包 * 上传包 * 下架现有包 * 编辑包标签（Tag） | 维护者更新仓库内容 |

管理仓库页面展示当前所拥有的仓库信息，包含如下四个功能：

1. 管理ohpm仓库三方包。
2. 编辑仓库。
3. 删除仓库。
4. 新增仓库。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a/v3/3SgoFFmpTFi51JFLXKvcoQ/zh-cn_image_0000002530751504.png?HW-CC-KV=V1&HW-CC-Date=20260429T054444Z&HW-CC-Expire=86400&HW-CC-Sign=EA635556655E17AD7BCA0496D1B31D663E6BB7F1B4FFA28BF16A6163281CD9E4 "点击放大")

### 管理三方包

管理三方包页面包含权限管理和上下架两部分。

### **权限管理**

ohpm-repo从5.3.0版本开始支持配置包级别的访问权限。系统管理员能够对仓库中所有的包进行权限管理，支持配置包的可见性、白名单和管理所有者。支持通过包名模糊检索到需要管理权限的包。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/G8_iRGNuRnuiHhVmdZZjXw/zh-cn_image_0000002561751477.png?HW-CC-KV=V1&HW-CC-Date=20260429T054444Z&HW-CC-Expire=86400&HW-CC-Sign=ABEA2042A38311495256BAFD0693FF1299B6F4392776EFD3983A14C6F4B78E94 "点击放大")

* 区域1：可见性配置，能够配置一个包的可见性，默认为公开可读。当配置为授权可读时，支持在区域2中添加可读白名单。当包设置为公开可读时，所有用户对包具有下载和查看权限；当包设置为授权可读时，仅添加在可读白名单中的用户具有包的下载权限。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/MYrldF8SStysQrOCfD6YzA/zh-cn_image_0000002561831429.png?HW-CC-KV=V1&HW-CC-Date=20260429T054444Z&HW-CC-Expire=86400&HW-CC-Sign=24F2C64B960D181599839D29225E0EADE444292BAAC99741598F0D07AEE4934A "点击放大")

* 区域2：白名单配置，在白名单中的用户将具有包的下载和查看权限，包的所有者和维护者会自动添加到包的白名单中。点击“新增用户”或“删除”按钮，可以在白名单配置中添加或者删除查看者用户，所有者和维护者用户禁止被删除。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/zVrxE3VjQ6O6OYtY5xIpjw/zh-cn_image_0000002561831417.png?HW-CC-KV=V1&HW-CC-Date=20260429T054444Z&HW-CC-Expire=86400&HW-CC-Sign=B545D95297BA2FE140DB87C4D61FB622587C6D5BE5C24A9B2F84774BBA8DF20E "点击放大")

* 区域3：管理所有者，包的所有者具有包的下载，上传，下架和编辑包tag权限。支持对包所有者进行新增和删除，当包仅剩唯一一个所有者用户时，禁止被删除。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/QIs0c07rSpuYxGz1NbtAfw/zh-cn_image_0000002561751453.png?HW-CC-KV=V1&HW-CC-Date=20260429T054444Z&HW-CC-Expire=86400&HW-CC-Sign=05B273330148C7987ADC6F431AF432E28E169C505FB5368400CE277C6DC90D94 "点击放大")

### **上下架**

点击“管理ohpm仓库三方包”按钮，进入仓库管理详情面板，展示所有已上传至ohpm-repo的三方包信息。上下架包含上传三方包、单个包下架、批量包下架和搜索三方包四个功能。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/b6wZDwczS9K1DK7Ior4uag/zh-cn_image_0000002530751540.png?HW-CC-KV=V1&HW-CC-Date=20260429T054444Z&HW-CC-Expire=86400&HW-CC-Sign=2CBDBF334991FFC4117DE393A7F08A73BBA9E303DF3DA152C42826FE0F292277 "点击放大")

* 区域1：上传三方包，点击“上传三方包”按钮，能够上传指定的包文件或选择本地三方包文件，将其上传至仓库中，页面效果如下图所示：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/ln0JEjQWQ6uQPA2XIwpubg/zh-cn_image_0000002530911500.png?HW-CC-KV=V1&HW-CC-Date=20260429T054444Z&HW-CC-Expire=86400&HW-CC-Sign=ECE0BAAD2A49C6A95B06DBF660E6A98D51D9D0F6F0D3EA07584CA04E37EE3FA1 "点击放大")
* 区域2：下架，点击指定包右边的“下架”按钮，进行单个包下架操作，输入下架原因即可完成包的下架，页面效果如下图所示：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/zi0tIgrjSQ68YF0JOLxgVQ/zh-cn_image_0000002530911512.png?HW-CC-KV=V1&HW-CC-Date=20260429T054444Z&HW-CC-Expire=86400&HW-CC-Sign=A56A707214E1AA79A0396A788B64141F119128CCAA7664B5903ECBC55FDF67A2 "点击放大")
* 区域3：批量下架，勾选包左边的待选框，点击“批量下架”按钮，能够批量下架已勾选的包，可以通过改变页面底部每页包含的数据值，批量下架更多的包。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/9aXvVA9hSiaB67w2JXvxTg/zh-cn_image_0000002530751518.png?HW-CC-KV=V1&HW-CC-Date=20260429T054444Z&HW-CC-Expire=86400&HW-CC-Sign=A5A335E0D856E0202455FBCEAAC5F63368DD6AEC7B2482C38B88560A5B023949 "点击放大")
* 区域4：筛选，点击列表标题旁的漏斗图标，可以进行包数据的筛选。支持通过Name、Version、Publisher、Author和PublishTime字段筛选包数据。例如筛选出Name带有数字3，版本号大于等于2.0.0，发布人为accessToken1的包，数据筛选效果如下图所示：

  - Name：支持对包名进行模糊搜索。

  - Version：支持输入最小版本号和最大版本号，进行版本号区间搜索。

  - Publisher：支持对包发布者名称进行模糊搜索。

  - Author：支持对包作者名称进行模糊搜索。

  - PublishTime：支持对包发布时间进行区间搜索。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/UKmU0vbbTsSuBA-enwd7yg/zh-cn_image_0000002530911534.png?HW-CC-KV=V1&HW-CC-Date=20260429T054444Z&HW-CC-Expire=86400&HW-CC-Sign=E8CFB35D450B12E953E7B47F58BA10D750B0D44F02301AB8385E049A72DF0AC1 "点击放大")

### 编辑仓库

点击指定仓库的“编辑”图标按钮，进入仓库信息编辑界面，可以修改仓库的Name 、Uplink、可读策略、授权可读白名单、可写策略，授权可写白名单、发布策略和描述信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/HdUbeNP5TZyFw-QcvmyGEA/zh-cn_image_0000002561831461.png?HW-CC-KV=V1&HW-CC-Date=20260429T054444Z&HW-CC-Expire=86400&HW-CC-Sign=D19623CE027E4E1F4D497CF93CFAFC7FD748BD3527223E856A34F0EF21C4CBFB "点击放大")

* Name：仓库的名称。当仓库发过包或者已添加授权可读白名单或可写白名单时，禁止修改仓库名。
* Uplink：配置代理仓库地址。其中Uplink为下拉框选择，选项为仓库管理页面的[uplinks](ide-ohpm-depot-management.md#zh-cn_topic_0000001792256181_uplinks)面板配置的Uplink仓库。
* 可读策略： 分为公开可读和授权可读。当一个仓库被设置为授权可读时，将出现授权可读名单配置项，系统管理员默认具有仓库读和写权限。当仓库设置为公开可读时，所有用户对仓库具有读权限，能够访问仓库中包的信息和下载包；当设置为授权可读时，仅授权可读白名单中用户拥有仓库的读权限。当仓库可读策略设置为授权可读时，可写策略默认选择授权可写，不可修改。
* 授权可读名单：当可读策略选择授权可读时，将出现授权可读名单配置项，能够逐个添加仓库可读用户。授权可读白名单最多添加200个。支持搜索用户名逐个添加，也支持使用英文逗号分隔用户名批量添加。
* 可写策略：分为公开可写和授权可写。当一个仓库被设置为授权可写时，将出现授权可写名单配置项，仅在可写名单中的用户具有仓库的写权限，具有写权限默认具有读权限，系统管理员默认具有仓库读写权限。当仓库设置为公开可写时，所有用户对仓库具有写权限，能够对仓库中的包进行下载，上传，下架和编辑tag操作；当设置为授权可写时，仅授权可写白名单中用户拥有仓库的写权限。
* 授权可写名单：当可写策略选择授权可写时，将出现授权可写名单配置项，能够逐个添加仓库可写用户。授权可写白名单最多添加200个。支持搜索用户名逐个添加，也支持使用英文逗号分隔用户名批量添加。
* 发布策略：分为禁止同版本覆盖和支持同版本覆盖两种模式。在禁止同版本覆盖模式下，若尝试向仓库重复发布同一版本的包，系统会报错提示“该三方库已存在此版本”，确保版本唯一性。在支持同版本覆盖模式下，允许重复发布同版本包，新包将直接覆盖旧包，适用于需要持续更新的场景。用户可通过配置灵活选择适合的发布策略。**覆盖操作不可逆，请谨慎选择**。

### 删除仓库

点击“删除”图标按钮将删除当前选中的仓库。当仓库下存在上架包时禁止删除仓库，当仅剩最后一个仓库时禁止被删除。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/VL4s88j7QNCn8ufXqdaPgw/zh-cn_image_0000002561831451.png?HW-CC-KV=V1&HW-CC-Date=20260429T054444Z&HW-CC-Expire=86400&HW-CC-Sign=5C60D2182B91693898D8C95CBED0D602FBA7DAC3D493786C212438F58A5582A6 "点击放大")

### 新增仓库

点击“+”图标按钮将新增一个仓库，可以对仓库的Name、Uplink、可读策略、可写策略、发布策略和描述信息进行编辑。可读策略默认为公开可读，可写策略默认为公开可写，发布策略默认为禁止同版本覆盖。最多支持创建20个仓库。![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/pOn8-3bWQ9emoqRlYvg2gg/zh-cn_image_0000002561831439.png?HW-CC-KV=V1&HW-CC-Date=20260429T054444Z&HW-CC-Expire=86400&HW-CC-Sign=CE55F3417DC4FDDC762E65612865CD2AD6E5FCF9A4B0077A4A2E355C400BBE0A "点击放大")

## uplinks

uplinks功能可以让当前仓库获取配置的uplink仓库的所有包，若从某个已配置uplink的仓库下载当前仓库中不存在的三方包时，则会通过uplink仓库下载该包，如果访问uplink仓库需要代理，请配置好所需代理信息，uplink页面如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/cgBsqRAeQtOT-8_N9utk8w/zh-cn_image_0000002530911490.png?HW-CC-KV=V1&HW-CC-Date=20260429T054444Z&HW-CC-Expire=86400&HW-CC-Sign=CA4FC953FFDBE21F2075C4277E8C181C6507E02A3E5360FBEBDA942BAACFDE32 "点击放大")

1. 点击新增按钮，可以创建新的uplink仓库。一旦完成新增uplink仓库的设置，必须前往仓库管理 > 管理仓库 > 编辑页面进行应用，这样该功能才会生效，且ohpm-repo只允许同时配置一个uplink仓库。uplink仓库地址不建议配置为其他ohpm-repo的地址，避免出现仓库A配置uplink为仓库B，仓库B配置uplink为仓库A，导致循环查找问题。页面效果如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/FoBZWDpBSMmVNNwT00vCRg/zh-cn_image_0000002561751441.png?HW-CC-KV=V1&HW-CC-Date=20260429T054444Z&HW-CC-Expire=86400&HW-CC-Sign=0AF16A44C6170477B23EB47EAB40F4C762035025E9C347008B7FB001AD2238AD "点击放大")
2. 点击编辑，可以修改已配置的uplink仓库信息，页面效果如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/nGtcO5AYTrK2nb5o2x6hsw/zh-cn_image_0000002530751530.png?HW-CC-KV=V1&HW-CC-Date=20260429T054444Z&HW-CC-Expire=86400&HW-CC-Sign=38F5D3207B7B1FA5F835BCD71FA79C7E1522B7F740A761D86383C5A5D463D985 "点击放大")
3. 点击删除，可以删除配置的uplink仓库，页面效果如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/a-B2DsV7RduXoPuMA1psqg/zh-cn_image_0000002530911526.png?HW-CC-KV=V1&HW-CC-Date=20260429T054444Z&HW-CC-Expire=86400&HW-CC-Sign=063DD93051FDCBC7BD0EA468DF73896E15C127E77B5368735E4EED05D55864F2 "点击放大")
4. 由于搭建的ohpm-repo私仓可能需要通过代理来访问已配置的uplink仓库，因此ohpm-repo提供了代理功能。点击配置代理，可以添加代理信息，页面效果如下图所示：

   说明

   HttpProxy、HttpsProxy和uplinks仓库地址有关，与搭建的代理服务器协议无关。若uplinks仓库地址是http协议，则选择HttpProxy配置代理；若uplinks仓库地址是https协议，则选择HttpsProxy配置代理。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/snNLMZDqTdGcOYWa6_APWQ/zh-cn_image_0000002561751465.png?HW-CC-KV=V1&HW-CC-Date=20260429T054444Z&HW-CC-Expire=86400&HW-CC-Sign=83910C599E10CEAC0BA6748FBAA79AD50BCBD0A601C614E8DAEFC04BA6A7A8C5 "点击放大")
