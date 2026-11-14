---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-package-permission-management
title: 包权限管理
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 开发环境搭建 > 工程创建 > 模块管理 > ohpm-repo私仓搭建工具 > 页面功能介绍 > 包权限管理
category: harmonyos-guides
scraped_at: 2026-11-14T08:48:48+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:8614eba28f6f5699b0eddf15095d4015fd2eda2cc4a79ad254f4a2fb86c41b3a
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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/Mhd9j_RGTKeknaR01dIXBA/zh-cn_image_0000002808764917.png?HW-CC-KV=V1&HW-CC-Date=20261114T004701Z&HW-CC-Expire=31536000000&HW-CC-Sign=AC7868AC72BEC4A7A3118BD0CEA835DE6D9F70CC1F8E43ED26F326B40DDF0BCF "点击放大")

* 区域1：筛选，点击列表标题旁的漏斗图标，可以进行包数据的筛选，支持针对包名和仓库名进行模糊搜索。例如筛选出包名含有group3，仓库名为ohpma的包，数据筛选效果如下图所示：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/0inIPQSzQUWzKLuV0pAsrg/zh-cn_image_0000002808885029.png?HW-CC-KV=V1&HW-CC-Date=20261114T004701Z&HW-CC-Expire=31536000000&HW-CC-Sign=9F31F03205AD7F84ECF28657881108C7CEBC764A041559A08B09085D0FA76648 "点击放大")
* 区域2：查看包所有版本列表，点击版本数量中的值，能够查看当前包具有多少个版本。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/PMCGIOFJRG20uZe04yvOAw/zh-cn_image_0000002808885015.png?HW-CC-KV=V1&HW-CC-Date=20261114T004701Z&HW-CC-Expire=31536000000&HW-CC-Sign=AAE28421318FB9D4CA490A7E2E238E53A63FEFE0419C512263100C9CD6595429 "点击放大")
* 区域3：管理所有者，包的所有者具有包的下载、上传、下架和编辑包Tag权限，支持对包所有者进行新增和删除。

  当包仅剩唯一一个所有者用户时，禁止删除。当一个用户已经是包的维护者时，禁止被添加为包的所有者。禁止删除当前用户的所有者权限。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/byDOOz1mRYGAd8auQ0rrhw/zh-cn_image_0000002779565360.png?HW-CC-KV=V1&HW-CC-Date=20261114T004701Z&HW-CC-Expire=31536000000&HW-CC-Sign=ED31A034075308878758B90121E510FF8DFF06B2AFCBC09CBE5B3B83E0F49B7B "点击放大")
* 区域4：管理维护者，包的维护者具有包的下载，上传和编辑Tag权限，支持对包维护者进行新增和删除。当一个用户已经是包的所有者时，禁止被添加为包的维护者。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/zuX66zP3TZqccuZBChn0hQ/zh-cn_image_0000002779405376.png?HW-CC-KV=V1&HW-CC-Date=20261114T004701Z&HW-CC-Expire=31536000000&HW-CC-Sign=0B934D04E0F8294ECA07DB4347A36985040DC7E297E0674013E6BE439244A216 "点击放大")
* 区域5：转移所有者，支持当前用户将包的所有者转移给其他非包所有者或维护者。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/XP9pWGaxRcyt4esa8be1jg/zh-cn_image_0000002808885031.png?HW-CC-KV=V1&HW-CC-Date=20261114T004701Z&HW-CC-Expire=31536000000&HW-CC-Sign=AB76C31BF99A2D328D7A70F91B7C028D9806B58787EC5B71BD943A3990F3CBD5 "点击放大")

## 所维护的包

在所维护的包界面，支持完成如下操作：

1. 筛选。
2. 查看包所有版本列表。
3. 查看包的所有者用户列表。
4. 查看包的维护者用户列表。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/NusY0lrbT9mTDdAKRhfn2w/zh-cn_image_0000002779565342.png?HW-CC-KV=V1&HW-CC-Date=20261114T004701Z&HW-CC-Expire=31536000000&HW-CC-Sign=D10E803F6D8DEA742EDDF528451ECB6F41A6C7693760251ED16928E0804EDD2A "点击放大")

* 区域1：筛选，点击列表标题旁的漏斗图标，可以进行包数据的筛选，支持针对包名和仓库名进行模糊搜索。例如筛选出包名含有a1，仓库名为ohpm的包，数据筛选效果如下图所示：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/dqhXuztLRVG49un77jfwlw/zh-cn_image_0000002779565346.png?HW-CC-KV=V1&HW-CC-Date=20261114T004701Z&HW-CC-Expire=31536000000&HW-CC-Sign=1109C38110B81410B2E337E9B8227CAC136ADFC87A948CD943299C67908B4DC9 "点击放大")
* 区域2：查看包所有版本列表，点击版本数量中的值，能够查看当前包具有多少个版本。
* 区域3：查看包的所有者用户列表。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/xa78ICSfSgmTfz5mfVxrxw/zh-cn_image_0000002808764935.png?HW-CC-KV=V1&HW-CC-Date=20261114T004701Z&HW-CC-Expire=31536000000&HW-CC-Sign=7CEEAC6196577820F0750C7EF7C95CBFD0FCD8E072AF17DAC011C9E26F54DC57 "点击放大")
* 区域4：查看包的维护者用户列表。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/x9_ymNgfS7GN1s36zNXQzg/zh-cn_image_0000002779565334.png?HW-CC-KV=V1&HW-CC-Date=20261114T004701Z&HW-CC-Expire=31536000000&HW-CC-Sign=813C0F7EDCD2A2EE983E20D1D0F759CB1375C9793C80FC2D59D984DA55B03E50 "点击放大")
