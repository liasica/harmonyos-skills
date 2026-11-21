---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/wallet-travel-prepare
title: 开发准备
breadcrumb: 指南 > 应用服务 > Wallet Kit（钱包服务） > 出行凭证 > 开发准备
category: harmonyos-guides
scraped_at: 2026-11-21T09:12:42+08:00
doc_updated_at: 2026-09-24
content_hash: sha256:3e1412daec0424ce090545293db30f7d76ffa03759d1641a20d61ca3fb49d5a0
---

## 创建Wallet Kit服务

请先参考“[应用开发准备](application-dev-overview.md)”完成基本准备工作和指纹配置，再继续以下开发活动。

1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)，点击“开发与服务”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/8QyiwprWSVauG2ZgEyoeFg/zh-cn_image_0000002792878330.png?HW-CC-KV=V1&HW-CC-Date=20261121T011241Z&HW-CC-Expire=31536000000&HW-CC-Sign=BA3D606D80710ECED00B6DAAF69F744647674A9C7382255AEBE37D6CEAE5121D)
2. 选择对应项目。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/lmOnephRTZuCHc0YOvQehA/zh-cn_image_0000002821838237.png?HW-CC-KV=V1&HW-CC-Date=20261121T011241Z&HW-CC-Expire=31536000000&HW-CC-Sign=E891B4475CB32CC41DDDA953343725E74E6ED40A19500DE96685A210BB94F887)
3. 选择“钱包服务”，点击“申请服务”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/SYz6pQZKSeeJ4Vzy7-FU7Q/zh-cn_image_0000002821838239.png?HW-CC-KV=V1&HW-CC-Date=20261121T011241Z&HW-CC-Expire=31536000000&HW-CC-Sign=8CDD398E602F570F863CE1BD3EDF18F1556A654A720FD81AEE94ED12A6EA1B26)
4. 点击“点击申请”，并选择新版本。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/pFHGj4yMTiK9fVOe62V6JQ/zh-cn_image_0000002821758241.png?HW-CC-KV=V1&HW-CC-Date=20261121T011241Z&HW-CC-Expire=31536000000&HW-CC-Sign=7133735D222D69E4B998F2FA9402040C45CD1A00479353D907B026902574B5ED)

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/GmFZIuj7SzKVepjM7x70xw/zh-cn_image_0000002821838249.png?HW-CC-KV=V1&HW-CC-Date=20261121T011241Z&HW-CC-Expire=31536000000&HW-CC-Sign=D8B51267EACC8C5A825ECA7ECEB39B1EA73D7370F34C552D87512083E55D664B)
5. 配置Wallet Kit服务参数：服务类型选择票，服务子类型选择出行凭证，服务项目按需选择，并指定服务号、开发者服务公钥及开发者云侧服务地址前缀后，点击“下一步”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/jMRIiR5mSVuAuEzBn9CwEA/zh-cn_image_0000002821758251.png?HW-CC-KV=V1&HW-CC-Date=20261121T011241Z&HW-CC-Expire=31536000000&HW-CC-Sign=E5CB4E1B06C598BA034C0D5974DD9B6C9B91FB8935408347FCD15646CD9479D3)

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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ca/v3/4Whx08MoRAeenEFBP6GJeg/zh-cn_image_0000002821758273.png?HW-CC-KV=V1&HW-CC-Date=20261121T011241Z&HW-CC-Expire=31536000000&HW-CC-Sign=30E6CE734C23532687116CEA2EBA592840636419A0E8CEA8B86BC41CDB678DB6)
7. 配置添加预览信息：按要求上传卡面底图。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/qjvRgKU6TUiJygIPQEr2kA/zh-cn_image_0000002793038336.png?HW-CC-KV=V1&HW-CC-Date=20261121T011241Z&HW-CC-Expire=31536000000&HW-CC-Sign=C790A76D4DEB86004B4DD446BB363D40C3EF1225BF6A339B795AFBFE22599530)
8. 配置卡详情页信息：按需配置卡面个性化信息，功能区，运营区以及官方App/元服务跳转。

   基本信息配置：可指定背景色、字体颜色、LOGO等，并输入样例信息查看实际出行凭证的效果。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/VccaUIA7QkWORL4Y6LM9Yg/zh-cn_image_0000002792878366.png?HW-CC-KV=V1&HW-CC-Date=20261121T011241Z&HW-CC-Expire=31536000000&HW-CC-Sign=669AE23A6AA24F3E2F9AF0BFFB7D079465380081C9983350FACD06727589E18D)

   主要信息配置：支持自定义标签及内容，最多支持4个栏位。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/jhX9fOhDS_a66oPdpRv-Ag/zh-cn_image_0000002821838273.png?HW-CC-KV=V1&HW-CC-Date=20261121T011241Z&HW-CC-Expire=31536000000&HW-CC-Sign=91033DE55814499094D1DBCA8B037E6E8E8AE5B23D2C576B094E651E70210112)

   次要信息配置：支持自定义标签及内容，最多支持4个栏位。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/goTSCqAtSp2iR-HNEggE4Q/zh-cn_image_0000002821758275.png?HW-CC-KV=V1&HW-CC-Date=20261121T011241Z&HW-CC-Expire=31536000000&HW-CC-Sign=D0C324D25CC4F14A240862077FF773AFDD4E5732ADC64FC103BE4BE4F119C9FF)

   补充信息区配置：该区域不展示标签，仅展示内容。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/OkpPkAmRT3S0IbnKno_Gfg/zh-cn_image_0000002793038338.png?HW-CC-KV=V1&HW-CC-Date=20261121T011241Z&HW-CC-Expire=31536000000&HW-CC-Sign=A213487527F0983E22BD04E86373B2F000ACE52CF172A2981151E759A244938C)

   功能区配置：支持卡片信息和删除功能。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/H21629ubShOW2B6yv6SlnA/zh-cn_image_0000002792878368.png?HW-CC-KV=V1&HW-CC-Date=20261121T011241Z&HW-CC-Expire=31536000000&HW-CC-Sign=14564616656B7F46B4B3156F647FF6E6BDBE7F90D35249AF2A0EC66455039358)

   | **参数** | **说明** |
   | --- | --- |
   | 卡片信息 | 用于展示卡面提供服务方（按需配置多语言）信息，按需勾选卡号和联系客服（客服电话方便用户联系）。在详情页点击卡面信息会跳转卡面信息展示。右边可以看到预览效果。 |
   | 删除 | 用于控制钱包内删卡。 |

   运营区配置：可以按需配置服务菜单（最多支持5个），按需配置是否提供使用记录查看链接以及华为服务号入口，右边可以查看配置的预览效果。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/aMmIcgeuRMKfsELv93RTPw/zh-cn_image_0000002821838275.png?HW-CC-KV=V1&HW-CC-Date=20261121T011241Z&HW-CC-Expire=31536000000&HW-CC-Sign=944A513D747BA50B029018B4D000BC3EEB8A8181AA6627B214E576E4D44BEC14)

   | **参数** | **说明** |
   | --- | --- |
   | 服务菜单 | 用于控制详情页的运营区。如果需要配置，点添加按钮后需要配置菜单名称（多语言可选）以及跳转地址。 |
   | 是否提供使用记录查看链接 | 用于控制详情页的运营区是否展示使用记录。 |
   | 是否提供华为服务号入口 | 控制详情页的运营区的服务号是否展示，如果需要配置，则填写开通服务号的ID和名称。 |

   官方App/元服务跳转配置：按需配置官方App/元服务跳转，如果选择是，需要按需配置跳转链接，右边可以查看配置的预览效果。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/Tt3phHCBT5q0vOCzaY5nfg/zh-cn_image_0000002821758277.png?HW-CC-KV=V1&HW-CC-Date=20261121T011241Z&HW-CC-Expire=31536000000&HW-CC-Sign=DB47CC108E228BD46F8114F0F88D238641835AD60918D806691467F8EA64EEDF)
9. 提交前进行信息核对及预览，确认无误后，点击“提交”完成出行凭证Wallet Kit服务接入配置。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/JaMsa3K_SNeUSVemDytusw/zh-cn_image_0000002821838253.png?HW-CC-KV=V1&HW-CC-Date=20261121T011241Z&HW-CC-Expire=31536000000&HW-CC-Sign=33323F2A961A07BF79EFC8365B4FDCFA2C27E5BE9C4E2D62BB61F1FA92512A77)
