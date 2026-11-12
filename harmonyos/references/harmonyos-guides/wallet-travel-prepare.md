---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/wallet-travel-prepare
title: 开发准备
breadcrumb: 指南 > 应用服务 > Wallet Kit（钱包服务） > 出行凭证 > 开发准备
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-09-24
content_hash: sha256:cf2c0c0c0dae53a081483d8487c28c9e5f9121e1decfa1f641b0f0fff1447aa2
---

## 创建Wallet Kit服务

请先参考“[应用开发准备](application-dev-overview.md)”完成基本准备工作和指纹配置，再继续以下开发活动。

1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)，点击“开发与服务”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/U9-NN1lkT9WqpY3an6Rk8Q/zh-cn_image_0000002786520542.png?HW-CC-KV=V1&HW-CC-Date=20261112T233237Z&HW-CC-Expire=31536000000&HW-CC-Sign=76EA8ED314896CBC8F84880B294E0D4CB9C856F4B2D8DEE3856250E873675A67)
2. 选择对应项目。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ca/v3/LEGdxFn8T1as1XUlT2E4_A/zh-cn_image_0000002786360614.png?HW-CC-KV=V1&HW-CC-Date=20261112T233237Z&HW-CC-Expire=31536000000&HW-CC-Sign=6421D7852B2DD6E82B4B0C604420EC74BEA4F98AF44C84B23B784539BF28FAF0)
3. 选择“钱包服务”，点击“申请服务”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/ptvLzUbOQS2q1WjCx7iJRA/zh-cn_image_0000002786360616.png?HW-CC-KV=V1&HW-CC-Date=20261112T233237Z&HW-CC-Expire=31536000000&HW-CC-Sign=6E9A3CC6BB26323536A36C3E750A076F3089B2C172554E7E8EC549EB08A4D9CE)
4. 点击“点击申请”，并选择新版本。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5/v3/badasyMtTHyQmqe3K4ooLA/zh-cn_image_0000002815560037.png?HW-CC-KV=V1&HW-CC-Date=20261112T233237Z&HW-CC-Expire=31536000000&HW-CC-Sign=61E3C0E674C9446AEB3E626F3BB9013B7FA2ED77B9762D501A949E4B94F59444)

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/NWxUgHpUT4aJxBDazONV_Q/zh-cn_image_0000002786360626.png?HW-CC-KV=V1&HW-CC-Date=20261112T233237Z&HW-CC-Expire=31536000000&HW-CC-Sign=2AC8E799894A61384A2BDA4DE6B11CEA7A1E1148252F52BBD37398398F3560F6)
5. 配置Wallet Kit服务参数：服务类型选择票，服务子类型选择出行凭证，服务项目按需选择，并指定服务号、开发者服务公钥及开发者云侧服务地址前缀后，点击“下一步”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/SmbNGeOkTj2EznaLWgEAFw/zh-cn_image_0000002815560047.png?HW-CC-KV=V1&HW-CC-Date=20261112T233237Z&HW-CC-Expire=31536000000&HW-CC-Sign=EAF28478C4A739AEA5936FF28D1E62FFA6BA5CE3A586C8DF2DB97800E5B149FC)

   | **参数** | **说明** |
   | --- | --- |
   | 服务名称 | Wallet Kit首页列表展示该开发者所有创建的服务时，服务名称用于区分不同的服务。建议命名为公司简称+Wallet Kit+应用场景，长度不超过64个字符。 |
   | 服务类型 | 固定选择“票”。 |
   | 服务子类型 | 固定选择“出行凭证”。 |
   | 服务项目 | 选择接入的服务项目。 |
   | 默认卡名称 | 在钱包内显示的默认卡名称 ，长度不超过64个字符。 |
   | 服务号 | 开发者服务号，用于区分不同的项目和服务。建议格式为【hwpass.公司简称.项目名称.pass.服务项目】，须以hwpass开头 (自动填充，无需输入)，可为数字、字母，长度不超过32个字符。 |
   | 服务公钥 | Wallet Kit服务器认证开发者身份的凭证。依据页面上的"公钥操作步骤指导说明"生成公钥并回填。 |
   | 服务器地址前缀 | 开发者服务器地址，用于Wallet Kit服务器在开卡或删卡成功后回调开发者。如果不需要回调结果，可以不填该字段。 |
6. 配置NFC&二维码参数：可展码通行，但不涉及NFC，默认在用户华为账号登陆的所有设备可见，不支持动态二维码，推荐配置如下。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/vCERiFBvTYGl6CHNnziI6g/zh-cn_image_0000002815560069.png?HW-CC-KV=V1&HW-CC-Date=20261112T233237Z&HW-CC-Expire=31536000000&HW-CC-Sign=2D916F03256F074F7BDF44A9D9D95D7AB3CEEDB07C504870F7A4BB8FF7CDC575)
7. 配置添加预览信息：按要求上传卡面底图。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/nT7n02kUTFOMiL4U63LvGQ/zh-cn_image_0000002815400153.png?HW-CC-KV=V1&HW-CC-Date=20261112T233237Z&HW-CC-Expire=31536000000&HW-CC-Sign=68824874A24CA15595CA22863C2211AA72ED62A33B5F3BFFEACBC261E9C0F162)
8. 配置卡详情页信息：按需配置卡面个性化信息，功能区，运营区以及官方App/元服务跳转。

   基本信息配置：可指定背景色、字体颜色、LOGO等，并输入样例信息查看实际出行凭证的效果。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9/v3/RkZDbRzEQ7mFWNXVavAhVQ/zh-cn_image_0000002786520578.png?HW-CC-KV=V1&HW-CC-Date=20261112T233237Z&HW-CC-Expire=31536000000&HW-CC-Sign=04396BC9E2806D30CDD581A0B7C255C641522ABD17368957F7461245AD654EDA)

   主要信息配置：支持自定义标签及内容，最多支持4个栏位。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/SJ8M7kpRR2SUC_1rSIt2CQ/zh-cn_image_0000002786360650.png?HW-CC-KV=V1&HW-CC-Date=20261112T233237Z&HW-CC-Expire=31536000000&HW-CC-Sign=FEB777D94A55E02EB4614C48CB637BB6FC572D32D7DC73969D93AC405B1E6772)

   次要信息配置：支持自定义标签及内容，最多支持4个栏位。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/P2os3sIWRYCgXE2Dhrtv8A/zh-cn_image_0000002815560071.png?HW-CC-KV=V1&HW-CC-Date=20261112T233237Z&HW-CC-Expire=31536000000&HW-CC-Sign=E38A13952979314588E1C046394D2E1A96D552D40EC5311F5E0997E72B02B418)

   补充信息区配置：该区域不展示标签，仅展示内容。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/mFosU_dGQPyz8g6GmDMGgA/zh-cn_image_0000002815400155.png?HW-CC-KV=V1&HW-CC-Date=20261112T233237Z&HW-CC-Expire=31536000000&HW-CC-Sign=84A7E1C4F18531D426959F2CC9C7510CF7B8AAA2538943F48FA34CC4DB735826)

   功能区配置：支持卡片信息和删除功能。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/tQ0j2X3sQf-j4gYv4S_88g/zh-cn_image_0000002786520580.png?HW-CC-KV=V1&HW-CC-Date=20261112T233237Z&HW-CC-Expire=31536000000&HW-CC-Sign=EFB102D3A344F3D17F988526FDC4EC98EBEA3602F1B829B2E38A90A5C373873E)

   | **参数** | **说明** |
   | --- | --- |
   | 卡片信息 | 用于展示卡面提供服务方（按需配置多语言）信息，按需勾选卡号和联系客服（客服电话方便用户联系）。在详情页点击卡面信息会跳转卡面信息展示。右边可以看到预览效果。 |
   | 删除 | 用于控制钱包内删卡。 |

   运营区配置：可以按需配置服务菜单（最多支持5个），按需配置是否提供使用记录查看链接以及华为服务号入口，右边可以查看配置的预览效果。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/X9C8alzLQPevMETr3DVA-g/zh-cn_image_0000002786360652.png?HW-CC-KV=V1&HW-CC-Date=20261112T233237Z&HW-CC-Expire=31536000000&HW-CC-Sign=F80816F517D3D18960901331F314B0A49A84714A46FF923228E95B32E21D270E)

   | **参数** | **说明** |
   | --- | --- |
   | 服务菜单 | 用于控制详情页的运营区。如果需要配置，点添加按钮后需要配置菜单名称（多语言可选）以及跳转地址。 |
   | 是否提供使用记录查看链接 | 用于控制详情页的运营区是否展示使用记录。 |
   | 是否提供华为服务号入口 | 控制详情页的运营区的服务号是否展示，如果需要配置，则填写开通服务号的ID和名称。 |

   官方App/元服务跳转配置：按需配置官方App/元服务跳转，如果选择是，需要按需配置跳转链接，右边可以查看配置的预览效果。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/_RB3xpdVQt2xcKfMD8Qrdw/zh-cn_image_0000002815560073.png?HW-CC-KV=V1&HW-CC-Date=20261112T233237Z&HW-CC-Expire=31536000000&HW-CC-Sign=8AD331AAF3CD04C241B6A5B48465D25147FDEFB1FAF707506EB1DCBA21B0F301)
9. 提交前进行信息核对及预览，确认无误后，点击“提交”完成出行凭证Wallet Kit服务接入配置。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/3sydhUQbT5-LrY1fPK6B6g/zh-cn_image_0000002786360630.png?HW-CC-KV=V1&HW-CC-Date=20261112T233237Z&HW-CC-Expire=31536000000&HW-CC-Sign=21C05D7400C236E61B82AEF1EAD9000CE36A9963CD8036CA7316DCAE18C57174)
