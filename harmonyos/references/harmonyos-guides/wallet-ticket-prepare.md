---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/wallet-ticket-prepare
title: 开发准备
breadcrumb: 指南 > 应用服务 > Wallet Kit（钱包服务） > 活动/景点门票 > 开发准备
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-09-24
content_hash: sha256:a933f6cf23f837b8dbcc4bafe79e70325aee1c10c0ce8db3a4cb59e1e7e48b8b
---

## 创建Wallet Kit服务

请先参考“[应用开发准备](application-dev-overview.md)”完成基本准备工作和指纹配置，再继续以下开发活动。

1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)，点击“开发与服务”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/14fS0ZGDQPGpZkv8BkV0Ag/zh-cn_image_0000002786520542.png?HW-CC-KV=V1&HW-CC-Date=20261112T233237Z&HW-CC-Expire=31536000000&HW-CC-Sign=2B4DA150155E89B304C1924AEB79FD718BE4BEB3772A0E8F789FFC776A518FCF)
2. 选择对应项目。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/tsxa-aZyRcWtHsX5zUC0tA/zh-cn_image_0000002786360614.png?HW-CC-KV=V1&HW-CC-Date=20261112T233237Z&HW-CC-Expire=31536000000&HW-CC-Sign=843CF9BACE50963D5FFBE19DFD33AA75C2E6DAC3CF592D607EC7F948D4CE6F46)
3. 选择“钱包服务”，点击“申请服务”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7/v3/MsYTvtuCSDS5bvl6E-WKzg/zh-cn_image_0000002786360616.png?HW-CC-KV=V1&HW-CC-Date=20261112T233237Z&HW-CC-Expire=31536000000&HW-CC-Sign=3D5A275012B7DC44F824DC132E7AB755A27FB0F0768B46482F478045E7E57998)
4. 点击“点击申请”，并选择新版本。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/G9Zo3bYjRC6DpgYMXpceJg/zh-cn_image_0000002815560037.png?HW-CC-KV=V1&HW-CC-Date=20261112T233237Z&HW-CC-Expire=31536000000&HW-CC-Sign=20AAAA0F8B8E4C00484CDE66488A5B5C5A395CFBE567EB66D968513CF9CDA5EE)

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/4_X-fl4IRKmAW7hUpIpqxQ/zh-cn_image_0000002786360626.png?HW-CC-KV=V1&HW-CC-Date=20261112T233237Z&HW-CC-Expire=31536000000&HW-CC-Sign=E13A3E759CED76CAA5535B5DADD22A96FC99D6BDF44E92DB04BDE55C7EC88A05)
5. 配置Wallet Kit服务参数：服务类型选择票，服务子类型选择门票，服务项目按需选择，并指定服务号、开发者服务公钥及开发者云侧服务地址前缀后，点击“下一步”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/t5i0bAczTyGkDqumqyR1Zg/zh-cn_image_0000002815560047.png?HW-CC-KV=V1&HW-CC-Date=20261112T233237Z&HW-CC-Expire=31536000000&HW-CC-Sign=AE771BAA59D8F9E1A38C9CC8742100103DF046A24BB442E0D8FB368D437A5011)

   | **参数** | **说明** |
   | --- | --- |
   | 服务名称 | Wallet Kit首页列表展示该开发者所有创建的服务时，服务名称用于区分不同的服务。建议命名为公司简称+Wallet Kit+应用场景，长度不超过64个字符。 |
   | 服务类型 | 固定选择“票”。 |
   | 服务子类型 | 固定选择“门票”。 |
   | 服务项目 | 选择接入的服务项目。 |
   | 默认卡名称 | 在钱包内显示的默认卡名称 ，长度不超过64个字符。 |
   | 服务号 | 开发者服务号，用于区分不同的项目和服务。建议格式为【hwpass.公司简称.项目名称.pass.服务项目】，须以hwpass开头 (自动填充，无需输入)，可为数字、字母，长度不超过32个字符。 |
   | 服务公钥 | Wallet Kit服务器认证开发者身份的凭证。依据页面上的"公钥操作步骤指导说明"生成公钥并回填。 |
   | 服务器地址前缀 | 开发者服务器地址，用于Wallet Kit服务器在开卡或删卡成功后回调开发者。如果不需要回调结果，可以不填该字段。 |
6. 配置NFC&二维码参数：可展码通行，但不涉及NFC，默认在用户华为账号登陆的所有设备可见，不支持动态二维码，推荐配置如下。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/z7Jx7GkhTfqmQrA5tQ2URw/zh-cn_image_0000002786360654.png?HW-CC-KV=V1&HW-CC-Date=20261112T233237Z&HW-CC-Expire=31536000000&HW-CC-Sign=3936AB01A653EBEB021863577F96744E7B72CE43644BB23C9222F486D141A523)
7. 配置添加预览信息：按要求上传卡面底图。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/NYlmNAwhS3Ch6zvJ-8RlbA/zh-cn_image_0000002815560075.png?HW-CC-KV=V1&HW-CC-Date=20261112T233237Z&HW-CC-Expire=31536000000&HW-CC-Sign=B90CB1B50F196E061F7AAFA3995FFEA5CF14FAB5F966D52F85D9C3C2DD442A4D)
8. 配置卡详情页信息：按需配置卡面个性化信息，功能区，运营区以及官方App/元服务跳转。

   基本信息配置：可指定背景色、字体颜色、LOGO等，并输入样例信息查看实际活动/景点门票的效果。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0f/v3/ybnCarFzTmehNzFeE5zNpQ/zh-cn_image_0000002815400159.png?HW-CC-KV=V1&HW-CC-Date=20261112T233237Z&HW-CC-Expire=31536000000&HW-CC-Sign=D9ED26A7285C4349F40FB2F855688E114E3EE555308EB9C7D39821AF73408D9D)

   主要信息配置：支持自定义标签及内容，最多支持4个栏位。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/TaYLnqwVTo6h0cXbxQDh9w/zh-cn_image_0000002786360650.png?HW-CC-KV=V1&HW-CC-Date=20261112T233237Z&HW-CC-Expire=31536000000&HW-CC-Sign=147D2C603653499686879570001BDCFF816E0E86384049420616F0A3A5E80F79)

   次要信息配置：支持自定义标签及内容，最多支持4个栏位。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/dsXH-Hm1T9WByLnobKFx0w/zh-cn_image_0000002815560071.png?HW-CC-KV=V1&HW-CC-Date=20261112T233237Z&HW-CC-Expire=31536000000&HW-CC-Sign=EAC6C3C2E1D9AFDDC9906524AD7571AFA666F454918CB80F9DC09A28CBC54B7C)

   功能区配置：支持卡片信息和删除功能。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/NqrxsKdeS9CSXGoLdEkiuw/zh-cn_image_0000002786520580.png?HW-CC-KV=V1&HW-CC-Date=20261112T233237Z&HW-CC-Expire=31536000000&HW-CC-Sign=8CCDE20ABDAFB3010EF8D676F95CCD47B84DDAE3B9BF2C9DCC3113CDBA4CA694)

   | **参数** | **说明** |
   | --- | --- |
   | 卡片信息 | 用于展示卡面提供服务方（按需配置多语言）信息，按需勾选卡号和联系客服（客服电话方便用户联系）。在详情页点击卡面信息会跳转卡面信息展示。右边可以看到预览效果。 |
   | 删除 | 用于控制钱包内删卡。 |

   运营区配置：可以按需配置服务菜单（最多支持5个），按需配置是否提供使用记录查看链接以及华为服务号入口，右边可以查看配置的预览效果。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/ZCKtKxK3TMyA_w1EYlQ-IQ/zh-cn_image_0000002786360652.png?HW-CC-KV=V1&HW-CC-Date=20261112T233237Z&HW-CC-Expire=31536000000&HW-CC-Sign=4F71CE750271878B63D5BB29647A3B7CB12B1497FBBD159D8AEE41396EED869E)

   | **参数** | **说明** |
   | --- | --- |
   | 服务菜单 | 用于控制详情页的运营区。如果需要配置，点添加按钮后需要配置菜单名称（多语言可选）以及跳转地址。 |
   | 是否提供使用记录查看链接 | 用于控制详情页的运营区是否展示使用记录。 |
   | 是否提供华为服务号入口 | 控制详情页的运营区的服务号是否展示，如果需要配置，则填写开通服务号的ID和名称。 |

   官方App/元服务跳转配置：按需配置官方App/元服务跳转，如果选择是，需要按需配置跳转链接，右边可以查看配置的预览效果。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/kSGZeoqnT_Swa3xD4CCm5A/zh-cn_image_0000002815560073.png?HW-CC-KV=V1&HW-CC-Date=20261112T233237Z&HW-CC-Expire=31536000000&HW-CC-Sign=99DB639E86543D4C10773B2A5EAD19A60340EF917C89871952EDF67AB4804C8B)
9. 提交前进行信息核对及预览，确认无误后，点击“提交”完成活动/景点门票Wallet Kit服务接入配置。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/grH7gBMDTGiDRvLwlMJxJQ/zh-cn_image_0000002786360630.png?HW-CC-KV=V1&HW-CC-Date=20261112T233237Z&HW-CC-Expire=31536000000&HW-CC-Sign=0ECBD663FCF2E002069CE9C5965E44BE9F104B4BBB8C3F93F7FAC15C734CA855)
