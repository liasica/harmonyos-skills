---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/wallet-carkey-prepare
title: 开发准备
breadcrumb: 指南 > 应用服务 > Wallet Kit（钱包服务） > 数字车钥匙 > 开发准备
category: harmonyos-guides
scraped_at: 2026-09-10T06:23:31+08:00
doc_updated_at: 2026-09-09
content_hash: sha256:99897d8ef906168079704acce85fb95ad40da02926f7773b98013d3446897f29
---

## 准备图片素材

| 项目 | 尺寸规范 | 示例 |
| --- | --- | --- |
| 卡面logo | 128×128px，背景要求透明，底图要求128px直径白色圆形，logo居于中心位置。 |  |
| 卡面背景 | 1312×820px，方形直角，请勿切圆角，图片的边框不要有白边。 | 见卡面logo的示例 |
| 卡面（logo+背景） | 将卡面logo和卡面背景按照示例进行组合。1312×820px，方形直角，请勿切圆角，图片的边框不要有白边；logo居于背景左上角，与背景左边和上边间距均为96px。 | 见卡面logo的示例 |
| 添加入口 | 尺寸要求256×256px，背景要求白色，方形直角，请勿切圆角，logo居于中心位置。 |  |
| 车主App logo | 特殊情况下（比如春节等节日、重大宣传目的等）车主App logo会附加宣传元素，请提供不附带宣传元素的原始的logo图片。 |  |

## 准备配置和联调信息

下载并填写[准备配置和联调信息checklist](https://gitcode.com/HarmonyOS_Samples/wallet-kit-for-harmony-os_demo)。

## 创建Wallet Kit服务

在创建Wallet Kit服务前，需要先创建企业项目与应用，参考[应用开发准备](application-dev-overview.md)完成基本准备工作和指纹配置。

如果已经在HarmonyOS 5.0之前版本接入过ICCE车钥匙，可以跳过当前部分，直接复用已有的Wallet Kit服务。

1. 登录[AGC](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html#/)，点击“开发与服务”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/srmyRbVtTp-MLdYcsLZqJw/zh-cn_image_0000002717772012.png)
2. 选择车主App所在的项目。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/t537v4v0QWmkM9YFs95PIg/zh-cn_image_0000002717612080.png)
3. 选择车主App对应的HarmonyOS应用，将会展示如下应用信息，其中Client ID和Client Secret会用于DK服务器向华为钱包服务器发起https请求时[获取AccessToken](../harmonyos-references/wallet-rest-api-public.md#获取accesstoken)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/hEQNJ8YDRSOZj8AeMQ1VnQ/zh-cn_image_0000002747292033.png)
4. 选择“开放能力管理”，找到“华为钱包”，勾选并保存。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/CStlrCtkQRSS5YgIwMQKJg/zh-cn_image_0000002747211949.png)
5. 在车主App应用界面左侧的功能菜单中选择“钱包服务”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/CFNxshJ0ShmtWgygGVHiRQ/zh-cn_image_0000002717772014.png)
6. 点击“申请服务”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/0xcCmpB7TSKEIM--YywZEg/zh-cn_image_0000002717612082.png)
7. 选择“产品接入华为钱包服务”，然后点击“点击申请”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/ruc9DqdyQIy9dWpDXGwVNg/zh-cn_image_0000002747292035.png)
8. 选择接入版本，点击“老版本”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/q4_-hNHmRQyLeGprO3CQfQ/zh-cn_image_0000002747211951.png)
9. 配置Wallet Kit服务参数。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/_A0e786PTU-5ICl2AiwhKw/zh-cn_image_0000002717772016.png)

   | **参数** | **说明** |
   | --- | --- |
   | 服务类型 | 固定选择“钥匙”。 |
   | 服务项目 | 固定选择“ICCE车钥匙”。 |
   | 服务名称 | 建议使用品牌+车钥匙+环境名称，例如：  XX车钥匙-生产环境  XX车钥匙-测试环境  该字段仅用于方便开发者区分自己配置的多个服务。 |
   | 服务号 | 该字段为ICCE车钥匙卡片的发卡机构标识，用于唯一标识发卡机构，钱包可根据此值进行发卡机构的管控。 |
   | 接入方式 | 固定选择“云端接入”。 |
   | 回调地址 | 参见[准备配置和联调信息](wallet-carkey-prepare.md#准备配置和联调信息)中的“spNfcOperCallBackUrl”。 |
   | 用户公钥 | 按照“公钥操作步骤指导说明”提供的第一种方式：“网页、短信、Email、App应用内方式生成安全密钥”，使用该方式生成的公钥，并妥善保存公钥和私钥。 |
10. 配置NFC参数后，点击“下一步”，最终完成创建。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/bOYQ4io0SWCM3fMiEA2-tw/zh-cn_image_0000002717612084.png)

| **参数** | **说明** |
| --- | --- |
| 是否支持跨设备移动同步 | 固定选择“是”。 |
| 是否开通NFC能力 | 固定选择“是”。 |
