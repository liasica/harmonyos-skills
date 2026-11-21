---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/wallet-ticket-prepare
title: 开发准备
breadcrumb: 指南 > 应用服务 > Wallet Kit（钱包服务） > 活动/景点门票 > 开发准备
category: harmonyos-guides
scraped_at: 2026-11-21T09:12:42+08:00
doc_updated_at: 2026-09-24
content_hash: sha256:6fd39a486da9c530156ad917b3996cb23115ddb629cd59b15891dd15811a6856
---

## 创建Wallet Kit服务

请先参考“[应用开发准备](application-dev-overview.md)”完成基本准备工作和指纹配置，再继续以下开发活动。

1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)，点击“开发与服务”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/a2AqfMMtS_KZu2kYbjiYCw/zh-cn_image_0000002792878330.png?HW-CC-KV=V1&HW-CC-Date=20261121T011114Z&HW-CC-Expire=31536000000&HW-CC-Sign=C0A9586321E3E120BEA9D59FFE1DAB396040004E7CCDB0533A65EA5F94048B5A)
2. 选择对应项目。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ca/v3/2TqXqImoTRunDx7yoRa-Lw/zh-cn_image_0000002821838237.png?HW-CC-KV=V1&HW-CC-Date=20261121T011114Z&HW-CC-Expire=31536000000&HW-CC-Sign=39B2317F148475F2151158A4EBAAA4CE5AAF590CD58C65DE59DA30E2370AAC58)
3. 选择“钱包服务”，点击“申请服务”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2/v3/qfi503qlQlialf0kVli6og/zh-cn_image_0000002821838239.png?HW-CC-KV=V1&HW-CC-Date=20261121T011114Z&HW-CC-Expire=31536000000&HW-CC-Sign=FA7D1461A32A6E3596273F19896C7BE400C356355A41A56DDD8FE77E8D4BEF64)
4. 点击“点击申请”，并选择新版本。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/HLUYGRYhSx2EHZ7T2_7JBA/zh-cn_image_0000002821758241.png?HW-CC-KV=V1&HW-CC-Date=20261121T011114Z&HW-CC-Expire=31536000000&HW-CC-Sign=2A446C3A600FCC7CE01CBC0ED2493A5475881F50D9B3C8BA25D06A17BD551594)

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/KR0yd4NVRE28hLknxF-seQ/zh-cn_image_0000002821838249.png?HW-CC-KV=V1&HW-CC-Date=20261121T011114Z&HW-CC-Expire=31536000000&HW-CC-Sign=6B1BF1B1C78211C386BBC033268035FCC2885EA767274513FBE9ECF146A9AE83)
5. 配置Wallet Kit服务参数：服务类型选择票，服务子类型选择门票，服务项目按需选择，并指定服务号、开发者服务公钥及开发者云侧服务地址前缀后，点击“下一步”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/UlI_lh2TTsu7bFPAO3gY5Q/zh-cn_image_0000002821758251.png?HW-CC-KV=V1&HW-CC-Date=20261121T011114Z&HW-CC-Expire=31536000000&HW-CC-Sign=1EAE2D2A88CC54A3CAE6216D11195E91A51F0A56E4B743681B94C6E599D3EEC5)

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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/gSjw0ZdQRDmHSkpIF0nkRQ/zh-cn_image_0000002821838277.png?HW-CC-KV=V1&HW-CC-Date=20261121T011114Z&HW-CC-Expire=31536000000&HW-CC-Sign=7FFE1CD767A963C679C2792EC76FB625159A9CA3AB6E79A03D61B92F2FBBA4DD)
7. 配置添加预览信息：按要求上传卡面底图。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/OxDWwn5BSGejQe4LUI4GIw/zh-cn_image_0000002821758279.png?HW-CC-KV=V1&HW-CC-Date=20261121T011114Z&HW-CC-Expire=31536000000&HW-CC-Sign=BFF5C2686C4C6958412271B41631F203EA822A190BD1E673B3307EB749795C4F)
8. 配置卡详情页信息：按需配置卡面个性化信息，功能区，运营区以及官方App/元服务跳转。

   基本信息配置：可指定背景色、字体颜色、LOGO等，并输入样例信息查看实际活动/景点门票的效果。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/tWDyo_t6RZWILslYbEeVkg/zh-cn_image_0000002793038342.png?HW-CC-KV=V1&HW-CC-Date=20261121T011114Z&HW-CC-Expire=31536000000&HW-CC-Sign=560B129CECA4856BABCA76BEDCD25A0995D37410B0DADCF188FCDB65D04A464E)

   主要信息配置：支持自定义标签及内容，最多支持4个栏位。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/yuUcEkLrRX-ExhVWq7AINQ/zh-cn_image_0000002821838273.png?HW-CC-KV=V1&HW-CC-Date=20261121T011114Z&HW-CC-Expire=31536000000&HW-CC-Sign=F96828225877C004525D3E951D3CA3FB55C9A1F61AC8374F4F52FBF22336EDE7)

   次要信息配置：支持自定义标签及内容，最多支持4个栏位。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/a0nvC7VRRnOGJuwwGFui6w/zh-cn_image_0000002821758275.png?HW-CC-KV=V1&HW-CC-Date=20261121T011114Z&HW-CC-Expire=31536000000&HW-CC-Sign=7093D5BD8C06FD9860D70442003B0DE979EECE5A8356A30F97FEE5ACF663D350)

   功能区配置：支持卡片信息和删除功能。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/QRMIovHYTx-rqBSLt5RVTA/zh-cn_image_0000002792878368.png?HW-CC-KV=V1&HW-CC-Date=20261121T011114Z&HW-CC-Expire=31536000000&HW-CC-Sign=B43F13BC251EF72DF870EBAFF7ADE72494D248309DBAC1429ACACA5D1B56999F)

   | **参数** | **说明** |
   | --- | --- |
   | 卡片信息 | 用于展示卡面提供服务方（按需配置多语言）信息，按需勾选卡号和联系客服（客服电话方便用户联系）。在详情页点击卡面信息会跳转卡面信息展示。右边可以看到预览效果。 |
   | 删除 | 用于控制钱包内删卡。 |

   运营区配置：可以按需配置服务菜单（最多支持5个），按需配置是否提供使用记录查看链接以及华为服务号入口，右边可以查看配置的预览效果。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/wvqXPmHGSze4hMMBYanWbQ/zh-cn_image_0000002821838275.png?HW-CC-KV=V1&HW-CC-Date=20261121T011114Z&HW-CC-Expire=31536000000&HW-CC-Sign=99A8357D740CB7DC169496FD8EFBB60BEA0AE3F24F02173830101CF0F3C59242)

   | **参数** | **说明** |
   | --- | --- |
   | 服务菜单 | 用于控制详情页的运营区。如果需要配置，点添加按钮后需要配置菜单名称（多语言可选）以及跳转地址。 |
   | 是否提供使用记录查看链接 | 用于控制详情页的运营区是否展示使用记录。 |
   | 是否提供华为服务号入口 | 控制详情页的运营区的服务号是否展示，如果需要配置，则填写开通服务号的ID和名称。 |

   官方App/元服务跳转配置：按需配置官方App/元服务跳转，如果选择是，需要按需配置跳转链接，右边可以查看配置的预览效果。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/5QBOUKxYRxSFQKhrNPfxTg/zh-cn_image_0000002821758277.png?HW-CC-KV=V1&HW-CC-Date=20261121T011114Z&HW-CC-Expire=31536000000&HW-CC-Sign=A711DC917128E15D3E576FA5087F1597F68E2708112F8C7465F31F60067DC33B)
9. 提交前进行信息核对及预览，确认无误后，点击“提交”完成活动/景点门票Wallet Kit服务接入配置。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/WbAtZ0UQRjmCRXkwiYMlOg/zh-cn_image_0000002821838253.png?HW-CC-KV=V1&HW-CC-Date=20261121T011114Z&HW-CC-Expire=31536000000&HW-CC-Sign=9094E833111E37FFE55B949B88627861A7CA5C2F5247B91E887551E5FE5DA96D)
