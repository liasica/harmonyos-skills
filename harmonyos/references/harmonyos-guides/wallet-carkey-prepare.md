---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/wallet-carkey-prepare
title: 开发准备
breadcrumb: 指南 > 应用服务 > Wallet Kit（钱包服务） > 数字车钥匙 > 开发准备
category: harmonyos-guides
scraped_at: 2026-11-14T08:48:33+08:00
doc_updated_at: 2026-09-09
content_hash: sha256:221d6370d6e0015b04bd2e65b7477e8962dbe887e7dee26c145dcf4f6cc269c1
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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/PR68qzWuT0GcCCuh3g4aaA/zh-cn_image_0000002788468290.png?HW-CC-KV=V1&HW-CC-Date=20261114T004648Z&HW-CC-Expire=31536000000&HW-CC-Sign=B83A5EDFF64C6315F90CAF1A665B41FD6ECD99C901E0994A5D7E6EE42618D0AB)
2. 选择车主App所在的项目。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/kjAm2vBdSCqHlWe27M4VXQ/zh-cn_image_0000002817507779.png?HW-CC-KV=V1&HW-CC-Date=20261114T004648Z&HW-CC-Expire=31536000000&HW-CC-Sign=7CC1ACA1FAA2D15F2F9282FC6E0F075911C6E1C10EF52BC19ED4C6D062FD8909)
3. 选择车主App对应的HarmonyOS应用，将会展示如下应用信息，其中Client ID和Client Secret会用于DK服务器向华为钱包服务器发起https请求时[获取AccessToken](../harmonyos-references/wallet-rest-api-public.md#获取accesstoken)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/PBzQprzoS6Sr2vUAyHInFA/zh-cn_image_0000002788308348.png?HW-CC-KV=V1&HW-CC-Date=20261114T004648Z&HW-CC-Expire=31536000000&HW-CC-Sign=F6CEB5B67C0EEB611FDFFB465903D93B1061D1088FAE545AA43B91471BBF8DD0)
4. 选择“开放能力管理”，找到“华为钱包”，勾选并保存。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/Yn7zWvq5S_iJKG9MVMIP0g/zh-cn_image_0000002817427711.png?HW-CC-KV=V1&HW-CC-Date=20261114T004648Z&HW-CC-Expire=31536000000&HW-CC-Sign=A546EA9FD6153458CFB1A5C33D37F802962C1C3F5B3A78EBCD6972C31E8F9510)
5. 在车主App应用界面左侧的功能菜单中选择“钱包服务”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/L8ynocC2RHSGAEBMuJFIpQ/zh-cn_image_0000002788468292.png?HW-CC-KV=V1&HW-CC-Date=20261114T004648Z&HW-CC-Expire=31536000000&HW-CC-Sign=07CF84FFC72C8C5EE9329C6DC832839CE0969AD82069E031AE4BD440696F61C5)
6. 点击“申请服务”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/17tgF9HwRSG6uDFuFbKLYQ/zh-cn_image_0000002817507781.png?HW-CC-KV=V1&HW-CC-Date=20261114T004648Z&HW-CC-Expire=31536000000&HW-CC-Sign=EAF2AEE35071E236627718D8DD3CDB1124FF7752813FAB13FBC9D1599A3B9B69)
7. 选择“产品接入华为钱包服务”，然后点击“点击申请”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/qEVWde3wTKSkU67Q9bu3Rw/zh-cn_image_0000002788308350.png?HW-CC-KV=V1&HW-CC-Date=20261114T004648Z&HW-CC-Expire=31536000000&HW-CC-Sign=2D0C0D6CDCBA2A5ACB2D279D52706A262150F898AD91C7D33E6563E8EBEBFCAF)
8. 选择接入版本，点击“老版本”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/iMw6blZxR9WbN5MBg0R9Ow/zh-cn_image_0000002817427713.png?HW-CC-KV=V1&HW-CC-Date=20261114T004648Z&HW-CC-Expire=31536000000&HW-CC-Sign=6984C94F03080BA5E07D3B84F76235C5273B90B9A6EE80503474FF78A32B2ACE)
9. 配置Wallet Kit服务参数。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/C2EMQkG2TFmwax3fx4_Q7w/zh-cn_image_0000002788468294.png?HW-CC-KV=V1&HW-CC-Date=20261114T004648Z&HW-CC-Expire=31536000000&HW-CC-Sign=4BBB302CE0C98D9347DCCBB34A5ED686309611E662A44D624ED9DE00027DAFD9)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/_e_lWALyTNKDwPZN0RLr9g/zh-cn_image_0000002817507783.png?HW-CC-KV=V1&HW-CC-Date=20261114T004648Z&HW-CC-Expire=31536000000&HW-CC-Sign=95CD31E2336E9FE72E86297A851F40060C9BFD988ED1E774324F8350DBF69ECA)

| **参数** | **说明** |
| --- | --- |
| 是否支持跨设备移动同步 | 固定选择“是”。 |
| 是否开通NFC能力 | 固定选择“是”。 |
