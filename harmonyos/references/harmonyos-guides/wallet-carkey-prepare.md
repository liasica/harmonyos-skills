---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/wallet-carkey-prepare
title: 开发准备
breadcrumb: 指南 > 应用服务 > Wallet Kit（钱包服务） > 数字车钥匙 > 开发准备
category: harmonyos-guides
scraped_at: 2026-11-19T09:49:14+08:00
doc_updated_at: 2026-09-09
content_hash: sha256:2e0c24412063316fc31292141dbb3bd2f9cd11a4612f5180275cdb96bcc03316
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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/RAn18-4sSJOgK3xVkJbXLw/zh-cn_image_0000002791566676.png?HW-CC-KV=V1&HW-CC-Date=20261119T014819Z&HW-CC-Expire=31536000000&HW-CC-Sign=1BE1C7176D4EBA69D82EC4CEFB70259C7FD3AB5D4BA98E4FF49EF6F3DD3EF03E)
2. 选择车主App所在的项目。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/Bmc_3esXTy-WbYlayOBHYw/zh-cn_image_0000002820526629.png?HW-CC-KV=V1&HW-CC-Date=20261119T014819Z&HW-CC-Expire=31536000000&HW-CC-Sign=13CB0B9F31F1B1ECA2F5A509705FBB678ACE7F98662ACC012873EAB000609513)
3. 选择车主App对应的HarmonyOS应用，将会展示如下应用信息，其中Client ID和Client Secret会用于DK服务器向华为钱包服务器发起https请求时[获取AccessToken](../harmonyos-references/wallet-rest-api-public.md#获取accesstoken)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/4KeaYYahRfWyTdAfoW7Y3A/zh-cn_image_0000002820406629.png?HW-CC-KV=V1&HW-CC-Date=20261119T014819Z&HW-CC-Expire=31536000000&HW-CC-Sign=4F1DC34C717B032AF943084DE8451E8ADE5086BB9BB985DE9287278786BB62E1)
4. 选择“开放能力管理”，找到“华为钱包”，勾选并保存。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/u4X0OV0YT8-TgCJDL5Y4aQ/zh-cn_image_0000002791726650.png?HW-CC-KV=V1&HW-CC-Date=20261119T014819Z&HW-CC-Expire=31536000000&HW-CC-Sign=A62762938218A3277451F37A79AEF2BC052D00ED21AADCB17D7FACA61145ADF7)
5. 在车主App应用界面左侧的功能菜单中选择“钱包服务”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/9hkQiAYITNaV1AOaFAmotA/zh-cn_image_0000002791566678.png?HW-CC-KV=V1&HW-CC-Date=20261119T014819Z&HW-CC-Expire=31536000000&HW-CC-Sign=269017B238B4219D831514A1A3E4B9023CF5FE12850213C353284CAE988DEA8B)
6. 点击“申请服务”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/6YQEVQRjQyaGSgmyiLhJRw/zh-cn_image_0000002820526631.png?HW-CC-KV=V1&HW-CC-Date=20261119T014819Z&HW-CC-Expire=31536000000&HW-CC-Sign=9758D6703A9E9F968E7FD19339365F8FDA59F2B2F3D3C72C6059FCC8CE8FFE9C)
7. 选择“产品接入华为钱包服务”，然后点击“点击申请”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/07/v3/hlh9VUc6SZOyFHlXte8Feg/zh-cn_image_0000002820406631.png?HW-CC-KV=V1&HW-CC-Date=20261119T014819Z&HW-CC-Expire=31536000000&HW-CC-Sign=0CB82FEC3BC38C64578133EF0B8B1BD848E788676528E71062F870E3C973F7DD)
8. 选择接入版本，点击“老版本”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/_Evry0CbSYyBd_pLow8IGg/zh-cn_image_0000002791726652.png?HW-CC-KV=V1&HW-CC-Date=20261119T014819Z&HW-CC-Expire=31536000000&HW-CC-Sign=F4CF105879C002A896F685AFF59C2943E23B73D1103B4F87B33649A73F45A860)
9. 配置Wallet Kit服务参数。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5/v3/zjOpXzFmTWuQLVQyAzJ1wQ/zh-cn_image_0000002791566680.png?HW-CC-KV=V1&HW-CC-Date=20261119T014819Z&HW-CC-Expire=31536000000&HW-CC-Sign=6888C7F5A92E89BEBAD8D451D783704CF63A2571C47CC213CC47DF85C623456C)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/GuU5tUc-T_ebdjfOzaXWqQ/zh-cn_image_0000002820526633.png?HW-CC-KV=V1&HW-CC-Date=20261119T014819Z&HW-CC-Expire=31536000000&HW-CC-Sign=EEF0F6526C190A2DFA08FF091A959A5B6866BCAA8EEC097FB9B63B1BB01FDB7C)

| **参数** | **说明** |
| --- | --- |
| 是否支持跨设备移动同步 | 固定选择“是”。 |
| 是否开通NFC能力 | 固定选择“是”。 |
