---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/wallet-carkey-prepare
title: 开发准备
breadcrumb: 指南 > 应用服务 > Wallet Kit（钱包服务） > 数字车钥匙 > 开发准备
category: harmonyos-guides
scraped_at: 2026-11-21T09:12:40+08:00
doc_updated_at: 2026-09-09
content_hash: sha256:8d6986b618fb287ba35854da2014c995a65f60ed5948504a27b31aa94d04cc5a
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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/HW2EoHrOTDq_6_rvE_BqYQ/zh-cn_image_0000002792878330.png?HW-CC-KV=V1&HW-CC-Date=20261121T011240Z&HW-CC-Expire=31536000000&HW-CC-Sign=5B0EB805C3EA6F641B59FF47E32BB00CD2F392A569A88254DE3D47AC547B514C)
2. 选择车主App所在的项目。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/zDySqLk2RmmlNG4VG0gINQ/zh-cn_image_0000002821838237.png?HW-CC-KV=V1&HW-CC-Date=20261121T011240Z&HW-CC-Expire=31536000000&HW-CC-Sign=DD60077469FD133012CA0E9AA8FDF693ED1A23869C4B4C643B4A34EE5460999F)
3. 选择车主App对应的HarmonyOS应用，将会展示如下应用信息，其中Client ID和Client Secret会用于DK服务器向华为钱包服务器发起https请求时[获取AccessToken](../harmonyos-references/wallet-rest-api-public.md#获取accesstoken)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/7uTXinZHQzqqpv8FodQedQ/zh-cn_image_0000002821758239.png?HW-CC-KV=V1&HW-CC-Date=20261121T011240Z&HW-CC-Expire=31536000000&HW-CC-Sign=5BF6D0875FCD700218FF9E7464CBC5BEF4971D6EA94A66E21EDF8EF02472D1A2)
4. 选择“开放能力管理”，找到“华为钱包”，勾选并保存。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/JtFBYcscRpeg3LF1rhPtOg/zh-cn_image_0000002793038302.png?HW-CC-KV=V1&HW-CC-Date=20261121T011240Z&HW-CC-Expire=31536000000&HW-CC-Sign=6A5A98C994BC4B4177ED32D7D4648F73F48086FA0848A6129FDE701A9F8669D0)
5. 在车主App应用界面左侧的功能菜单中选择“钱包服务”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/Pn9JQOyAQoSt2v5QvekWuQ/zh-cn_image_0000002792878332.png?HW-CC-KV=V1&HW-CC-Date=20261121T011240Z&HW-CC-Expire=31536000000&HW-CC-Sign=F8A98274D5D1590E91036A18D6DBD040249B494348D045779E77A18DF5628D31)
6. 点击“申请服务”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/BJ5ElBAHSJK3PJ3AajVTDg/zh-cn_image_0000002821838239.png?HW-CC-KV=V1&HW-CC-Date=20261121T011240Z&HW-CC-Expire=31536000000&HW-CC-Sign=B5EE659588BEA707EA2808AE84382D1242A7AE6C0204DA32FBB174E18908B3B2)
7. 选择“产品接入华为钱包服务”，然后点击“点击申请”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0d/v3/C0Hg4d5cQX2HAQRiYajDJg/zh-cn_image_0000002821758241.png?HW-CC-KV=V1&HW-CC-Date=20261121T011240Z&HW-CC-Expire=31536000000&HW-CC-Sign=29ADBE705608CE3C838929841DF333D41E56B70E42DF8FFAB64A6D28B61E90F1)
8. 选择接入版本，点击“老版本”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/V6TGl7U-SgyKYxn-XhDeaQ/zh-cn_image_0000002793038304.png?HW-CC-KV=V1&HW-CC-Date=20261121T011240Z&HW-CC-Expire=31536000000&HW-CC-Sign=BD3B04C565A6D3B2F2DE69FC748A9B09F89A0EC40B1FC043CBC495C0162ED103)
9. 配置Wallet Kit服务参数。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/jQoGGl7sQmKHCmJEerzfNg/zh-cn_image_0000002792878334.png?HW-CC-KV=V1&HW-CC-Date=20261121T011240Z&HW-CC-Expire=31536000000&HW-CC-Sign=88794BD23B3DC8B44657DF71CF35F1B6A8C7C9CF917C365E93F7ECBAC443A59E)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/-BIqnFwWSCaFQoX6COpotQ/zh-cn_image_0000002821838241.png?HW-CC-KV=V1&HW-CC-Date=20261121T011240Z&HW-CC-Expire=31536000000&HW-CC-Sign=734628FFCDD00B2030BBD9F931801906F460ABF517EAEA56F86FD9A994B77D56)

| **参数** | **说明** |
| --- | --- |
| 是否支持跨设备移动同步 | 固定选择“是”。 |
| 是否开通NFC能力 | 固定选择“是”。 |
