---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/wallet-ticket-prepare
title: 开发准备
breadcrumb: 指南 > 应用服务 > Wallet Kit（钱包服务） > 活动/景点门票 > 开发准备
category: harmonyos-guides
scraped_at: 2026-11-14T08:48:35+08:00
doc_updated_at: 2026-09-24
content_hash: sha256:f71a64215557770159a4cae7b7c87046c41e3af42b3d1448db169a04b5814424
---

## 创建Wallet Kit服务

请先参考“[应用开发准备](application-dev-overview.md)”完成基本准备工作和指纹配置，再继续以下开发活动。

1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)，点击“开发与服务”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/oPfDFablQOCdkxvzACFWEA/zh-cn_image_0000002788468290.png?HW-CC-KV=V1&HW-CC-Date=20261114T004650Z&HW-CC-Expire=31536000000&HW-CC-Sign=F8F15F5CF2D61F592924082E0B843CEB6A0698E11608D5AF7D3B9A4E04E5E612)
2. 选择对应项目。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/HVjFKQJOS-WBMl0ycdzVEg/zh-cn_image_0000002817507779.png?HW-CC-KV=V1&HW-CC-Date=20261114T004650Z&HW-CC-Expire=31536000000&HW-CC-Sign=78B5A498E04E510342BF5241972B49614A1F2FE99AEA66B10CB6CA937800AA1F)
3. 选择“钱包服务”，点击“申请服务”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/hjySfz95T-ONaOoeZSpH7A/zh-cn_image_0000002817507781.png?HW-CC-KV=V1&HW-CC-Date=20261114T004650Z&HW-CC-Expire=31536000000&HW-CC-Sign=0665EE9712110CFA7413401789365A1F45EFFBD579465EE7EC0BCBE5DEDA6910)
4. 点击“点击申请”，并选择新版本。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/6K9bD6ZnStKloIx4Cd0S4Q/zh-cn_image_0000002788308350.png?HW-CC-KV=V1&HW-CC-Date=20261114T004650Z&HW-CC-Expire=31536000000&HW-CC-Sign=B942DB1B5663F00BA6B145D9A49FFF71DB44BDCCF9937998D7747C191CA1AE57)

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/BpR3GsGkS_uL7pnebbcnDQ/zh-cn_image_0000002817507791.png?HW-CC-KV=V1&HW-CC-Date=20261114T004650Z&HW-CC-Expire=31536000000&HW-CC-Sign=3A87E013616675A8188316EDC4F10349E5824ACA61E7D2E650CFF92EB1A757CF)
5. 配置Wallet Kit服务参数：服务类型选择票，服务子类型选择门票，服务项目按需选择，并指定服务号、开发者服务公钥及开发者云侧服务地址前缀后，点击“下一步”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/9bi9nLpDTAmoQ9FwBGoN0w/zh-cn_image_0000002788308360.png?HW-CC-KV=V1&HW-CC-Date=20261114T004650Z&HW-CC-Expire=31536000000&HW-CC-Sign=DEF6B802EAEC89917C38C4528442C443A5A122C440F4B7EDDA9EF809A3CB97BD)

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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/yxDaeQsdR0CJ9b3O6Hh19w/zh-cn_image_0000002817507819.png?HW-CC-KV=V1&HW-CC-Date=20261114T004650Z&HW-CC-Expire=31536000000&HW-CC-Sign=FF413D5A9CB8F9A966A97375F48C03A18B60C3D771E719078E0CE565B0C9AFBF)
7. 配置添加预览信息：按要求上传卡面底图。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/9_wnvNpVQ9uhi4iNo73E-Q/zh-cn_image_0000002788308388.png?HW-CC-KV=V1&HW-CC-Date=20261114T004650Z&HW-CC-Expire=31536000000&HW-CC-Sign=2BB7139B0549A56CC99C84EC15DEB8CAA13776DC6F41646EE846AAB1D63E409C)
8. 配置卡详情页信息：按需配置卡面个性化信息，功能区，运营区以及官方App/元服务跳转。

   基本信息配置：可指定背景色、字体颜色、LOGO等，并输入样例信息查看实际活动/景点门票的效果。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/Tunydt1_TQCNoMRHOBOACA/zh-cn_image_0000002817427751.png?HW-CC-KV=V1&HW-CC-Date=20261114T004650Z&HW-CC-Expire=31536000000&HW-CC-Sign=3B54798442AE7F966E260738DBFF5AFD5C3304FEE4931180985A19070A021D69)

   主要信息配置：支持自定义标签及内容，最多支持4个栏位。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/xZEeKRa4SxeGgSWP4nEVKA/zh-cn_image_0000002817507815.png?HW-CC-KV=V1&HW-CC-Date=20261114T004650Z&HW-CC-Expire=31536000000&HW-CC-Sign=20C265322225FB30E863349C661C2B78FED15C4B281D385A0BD856D929EFDA36)

   次要信息配置：支持自定义标签及内容，最多支持4个栏位。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/9DeOlDXWS4-923xHL6NjKQ/zh-cn_image_0000002788308384.png?HW-CC-KV=V1&HW-CC-Date=20261114T004650Z&HW-CC-Expire=31536000000&HW-CC-Sign=FF97BE4ED90F43D344308EAC88CC157816EAB40062BFB01FC0CD9065CA8C6D81)

   功能区配置：支持卡片信息和删除功能。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/j9ILKtQ2TvOv8ewNK5XTXQ/zh-cn_image_0000002788468328.png?HW-CC-KV=V1&HW-CC-Date=20261114T004650Z&HW-CC-Expire=31536000000&HW-CC-Sign=5678DD00C83E82CEF8A5B7DB11A65488BBA6E4FA22899E776C25EE7715BB61CD)

   | **参数** | **说明** |
   | --- | --- |
   | 卡片信息 | 用于展示卡面提供服务方（按需配置多语言）信息，按需勾选卡号和联系客服（客服电话方便用户联系）。在详情页点击卡面信息会跳转卡面信息展示。右边可以看到预览效果。 |
   | 删除 | 用于控制钱包内删卡。 |

   运营区配置：可以按需配置服务菜单（最多支持5个），按需配置是否提供使用记录查看链接以及华为服务号入口，右边可以查看配置的预览效果。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/8GHS5t2YROCNqiGKJns_4Q/zh-cn_image_0000002817507817.png?HW-CC-KV=V1&HW-CC-Date=20261114T004650Z&HW-CC-Expire=31536000000&HW-CC-Sign=67467F670085543C607488AA1C9843EBB15FFFFF71C605AB91408DBAC6D29E0E)

   | **参数** | **说明** |
   | --- | --- |
   | 服务菜单 | 用于控制详情页的运营区。如果需要配置，点添加按钮后需要配置菜单名称（多语言可选）以及跳转地址。 |
   | 是否提供使用记录查看链接 | 用于控制详情页的运营区是否展示使用记录。 |
   | 是否提供华为服务号入口 | 控制详情页的运营区的服务号是否展示，如果需要配置，则填写开通服务号的ID和名称。 |

   官方App/元服务跳转配置：按需配置官方App/元服务跳转，如果选择是，需要按需配置跳转链接，右边可以查看配置的预览效果。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d/v3/DFh68guZS4-43QBvRFKj5Q/zh-cn_image_0000002788308386.png?HW-CC-KV=V1&HW-CC-Date=20261114T004650Z&HW-CC-Expire=31536000000&HW-CC-Sign=58EFA0628E5EF548AAB2F2BCF1CA470ACC6216569C6A889F827115D88C495D1E)
9. 提交前进行信息核对及预览，确认无误后，点击“提交”完成活动/景点门票Wallet Kit服务接入配置。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/T1CVvlJNSJipQ2vrz2v17g/zh-cn_image_0000002817507795.png?HW-CC-KV=V1&HW-CC-Date=20261114T004650Z&HW-CC-Expire=31536000000&HW-CC-Sign=14FFEA1C644992698AF52BE371A8A9A83735451EF0E79145E2A10A03D28A20DA)
