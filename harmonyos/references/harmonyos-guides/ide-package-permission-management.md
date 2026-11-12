---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-package-permission-management
title: 包权限管理
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 开发环境搭建 > 工程创建 > 模块管理 > ohpm-repo私仓搭建工具 > 页面功能介绍 > 包权限管理
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:59fe204c2eaa898ffc27cdc10ebab0aaeef0376ecbd83ecd5a231f20b3f8651e
---

ohpm-repo从5.3.0版本开始支持配置包级别的权限管理。系统支持对单个三方包配置精细的权限控制，包含包的所有者、包的维护者和包的查看者。

系统管理员在仓库管理页的[包的可见性配置](ide-ohpm-depot-management.md#li183931814142614)，能够把包设置为授权可读，并通过[白名单配置](ide-ohpm-depot-management.md#li174331117117)，添加包的查看者。当用户在执行下载、上传、下架和编辑Tag标签时，需要同时具有[仓库的对应权限](ide-ohpm-depot-management.md#section8501304122)和包的对应权限，缺一不可。

| 包权限角色 | 操作权限 | 适用场景 |
| --- | --- | --- |
| 所有者 | * 下载包 * 上传新包 * 下架现有包 * 编辑包标签（Tag） | 包的管理员，需要所有控制权限 |
| 维护者 | * 下载包 * 上传新包 * 编辑包标签（Tag） | 核心开发者，允许更新但不允许删除包（下架包） |
| 查看者 | * 下载包 | 仅需访问权限的成员或外部协作者 |

在包权限管理页，支持对所拥有的包执行如下操作：管理所有者、管理维护者、转移所有者；对所维护的包执行如下操作：查看所有者、查看维护者。

## 所拥有的包

在所拥有的包界面，支持完成如下操作：

1. 筛选。
2. 查看包所有版本列表。
3. 管理所有者。
4. 管理维护者。
5. 转移所有者。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/USuHfVSkQROTFmir4F2Ipg/zh-cn_image_0000002808764917.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=B04BAFBD0D3FC35764F24363BA689DDE37A8ABE79DDCDB52138DAF94BCDEE832 "点击放大")

* 区域1：筛选，点击列表标题旁的漏斗图标，可以进行包数据的筛选，支持针对包名和仓库名进行模糊搜索。例如筛选出包名含有group3，仓库名为ohpma的包，数据筛选效果如下图所示：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/M3B3mEHTTWSLVB1Xaubc1g/zh-cn_image_0000002808885029.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=424082E8C1D840029AB066E878C1369D9517571DF802281FB90F05C2491ABD73 "点击放大")
* 区域2：查看包所有版本列表，点击版本数量中的值，能够查看当前包具有多少个版本。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/6q2r6dKdQ6a3xcwedm_RBA/zh-cn_image_0000002808885015.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=5EF3CA164AEC91B26134277D0BE86D228635F83AD065D3CF7139A2E708017B15 "点击放大")
* 区域3：管理所有者，包的所有者具有包的下载、上传、下架和编辑包Tag权限，支持对包所有者进行新增和删除。

  当包仅剩唯一一个所有者用户时，禁止删除。当一个用户已经是包的维护者时，禁止被添加为包的所有者。禁止删除当前用户的所有者权限。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/XtEzFpoGTGmZCmKEgdw7jw/zh-cn_image_0000002779565360.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=5E72FEC51B87776AAF805B5A2024BBEFCD3ADCA67C5A19E7CC7994CCE139018D "点击放大")
* 区域4：管理维护者，包的维护者具有包的下载，上传和编辑Tag权限，支持对包维护者进行新增和删除。当一个用户已经是包的所有者时，禁止被添加为包的维护者。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/7awTLJhfQ_OmP-Kmh4PIFg/zh-cn_image_0000002779405376.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=832C762544F4EB447B93F71211C4E4161D638A20051B4B1C28DD367F202832AA "点击放大")
* 区域5：转移所有者，支持当前用户将包的所有者转移给其他非包所有者或维护者。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f/v3/PhQjW9ffRjauPoJRi8qwcw/zh-cn_image_0000002808885031.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=FC1738853D440B2DEE67195E67C885705DAF474B2710772BA969601E5D727EAD "点击放大")

## 所维护的包

在所维护的包界面，支持完成如下操作：

1. 筛选。
2. 查看包所有版本列表。
3. 查看包的所有者用户列表。
4. 查看包的维护者用户列表。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/vLFLC5rTQQCIkhhQHxEewg/zh-cn_image_0000002779565342.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=7A093EE71BC451C24A6A2A80639405115825150591035272E675D82FC7FC7950 "点击放大")

* 区域1：筛选，点击列表标题旁的漏斗图标，可以进行包数据的筛选，支持针对包名和仓库名进行模糊搜索。例如筛选出包名含有a1，仓库名为ohpm的包，数据筛选效果如下图所示：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/HDyf1yqkQ1mdrjeLpLm9EQ/zh-cn_image_0000002779565346.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=F1B89564FEAD77406D1FB5810DCB186CC8138EA1F2B22754A0B5A13466C44D54 "点击放大")
* 区域2：查看包所有版本列表，点击版本数量中的值，能够查看当前包具有多少个版本。
* 区域3：查看包的所有者用户列表。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/2FhoDudRQg-szKwJ1tsf5A/zh-cn_image_0000002808764935.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=A42DA2DB9DC8ABFCE04A875FF9CFDBB5CA1A105F6932518FF051DDF23A672320 "点击放大")
* 区域4：查看包的维护者用户列表。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/woWQ96VTQne9KyyHMZp07A/zh-cn_image_0000002779565334.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=07D87F14E614E2201B8EF91598ACE01981BA518E953A0DB9E68DC9F7B1C7B2B3 "点击放大")
