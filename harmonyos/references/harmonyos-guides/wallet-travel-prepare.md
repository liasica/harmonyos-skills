---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/wallet-travel-prepare
title: 开发准备
breadcrumb: 指南 > 应用服务 > Wallet Kit（钱包服务） > 出行凭证 > 开发准备
category: harmonyos-guides
scraped_at: 2026-11-14T08:48:34+08:00
doc_updated_at: 2026-09-24
content_hash: sha256:ffe8611ea4807ef59ef36a9a55563a79c4fd52acc909732352274c190e17712f
---

## 创建Wallet Kit服务

请先参考“[应用开发准备](application-dev-overview.md)”完成基本准备工作和指纹配置，再继续以下开发活动。

1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)，点击“开发与服务”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/sDMIRLgwTTuUlotTqwaj-g/zh-cn_image_0000002788468290.png?HW-CC-KV=V1&HW-CC-Date=20261114T004834Z&HW-CC-Expire=31536000000&HW-CC-Sign=32EFFCB11DF06373E9E631E242207077AD129CCC830A4B1DBE5F3BE36F13700A)
2. 选择对应项目。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/z8f_Aty0QPuGISjtZ176eg/zh-cn_image_0000002817507779.png?HW-CC-KV=V1&HW-CC-Date=20261114T004834Z&HW-CC-Expire=31536000000&HW-CC-Sign=A92C669DCC20D61542A22849FF030CFC1638BBBAC947A017078A8AD9B3E5349E)
3. 选择“钱包服务”，点击“申请服务”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/OfthLG-2QVeOnGFVWIP4sg/zh-cn_image_0000002817507781.png?HW-CC-KV=V1&HW-CC-Date=20261114T004834Z&HW-CC-Expire=31536000000&HW-CC-Sign=89EC88A7E565721501406B61FC65EFE91A7630B4E307114F3BEE115A3DD0FF55)
4. 点击“点击申请”，并选择新版本。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/TR6x0e2bS7SWZkLV5p3ZpA/zh-cn_image_0000002788308350.png?HW-CC-KV=V1&HW-CC-Date=20261114T004834Z&HW-CC-Expire=31536000000&HW-CC-Sign=F41B8CEEB7327A0E96DF973D386A0396604BE93FF58422D9C4BBFCEAB7E65A27)

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ca/v3/_Eo63EBvRFWaDpJKpaeX9A/zh-cn_image_0000002817507791.png?HW-CC-KV=V1&HW-CC-Date=20261114T004834Z&HW-CC-Expire=31536000000&HW-CC-Sign=C45FBF8DF8698D2532D1B488455F7697B6F94ED0EE38439AE9D4B31A5C9CFF79)
5. 配置Wallet Kit服务参数：服务类型选择票，服务子类型选择出行凭证，服务项目按需选择，并指定服务号、开发者服务公钥及开发者云侧服务地址前缀后，点击“下一步”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/uJsH9xyUQ3-Jy9ukZvkM7g/zh-cn_image_0000002788308360.png?HW-CC-KV=V1&HW-CC-Date=20261114T004834Z&HW-CC-Expire=31536000000&HW-CC-Sign=5139B640CEF8E5FD21E8781D45DD1F7A1422314F33FB0F44A9EFDEB8DE1E74B6)

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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/ddM_4aZoSFCUD1zjuqy5VA/zh-cn_image_0000002788308382.png?HW-CC-KV=V1&HW-CC-Date=20261114T004834Z&HW-CC-Expire=31536000000&HW-CC-Sign=27F9EB87AF63A1982F881569DAB660661F8F24EFB9D51B13B9A1F3CBC8BAC176)
7. 配置添加预览信息：按要求上传卡面底图。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/G4PcqkH5RRS5Of_-CuVxtw/zh-cn_image_0000002817427745.png?HW-CC-KV=V1&HW-CC-Date=20261114T004834Z&HW-CC-Expire=31536000000&HW-CC-Sign=56E83E8C9C3DBE5DB7A7C45F349FE7620C1F9C9D8A7E1F3D32DC88B90FDCF7B5)
8. 配置卡详情页信息：按需配置卡面个性化信息，功能区，运营区以及官方App/元服务跳转。

   基本信息配置：可指定背景色、字体颜色、LOGO等，并输入样例信息查看实际出行凭证的效果。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/vnbCMcZURh2JJVFFPbFCYA/zh-cn_image_0000002788468326.png?HW-CC-KV=V1&HW-CC-Date=20261114T004834Z&HW-CC-Expire=31536000000&HW-CC-Sign=0F13B5446D425D839A5965EF6DB43E7CB5EC8C10DED332EAF9ED09E03035396E)

   主要信息配置：支持自定义标签及内容，最多支持4个栏位。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5/v3/7xoTA0yxRASJWAMKuXOOgg/zh-cn_image_0000002817507815.png?HW-CC-KV=V1&HW-CC-Date=20261114T004834Z&HW-CC-Expire=31536000000&HW-CC-Sign=F522AD0248020888BFCBCCDBAE0C8029E50C472726434417BA0A966389A64EA4)

   次要信息配置：支持自定义标签及内容，最多支持4个栏位。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/oJJKnbhvS_GXqFa7DhSkiQ/zh-cn_image_0000002788308384.png?HW-CC-KV=V1&HW-CC-Date=20261114T004834Z&HW-CC-Expire=31536000000&HW-CC-Sign=BDBB2F00F526D31C6E1A83F8B4997879509421A7AED683AEF64D07B50E9EE6E5)

   补充信息区配置：该区域不展示标签，仅展示内容。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/8LqZhgJkQaaqeTA4bD8Kxg/zh-cn_image_0000002817427747.png?HW-CC-KV=V1&HW-CC-Date=20261114T004834Z&HW-CC-Expire=31536000000&HW-CC-Sign=A73E72A2D701DF149394010FA11FEB5F2B02E7765A4AAA342D2CFE8274293A80)

   功能区配置：支持卡片信息和删除功能。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/o8oeObzPRHqhkdO9ykAmFQ/zh-cn_image_0000002788468328.png?HW-CC-KV=V1&HW-CC-Date=20261114T004834Z&HW-CC-Expire=31536000000&HW-CC-Sign=F1D4860F445F6686EEA063AC5FB227106F74A2113DE62C466E50C76CA1BCB7D8)

   | **参数** | **说明** |
   | --- | --- |
   | 卡片信息 | 用于展示卡面提供服务方（按需配置多语言）信息，按需勾选卡号和联系客服（客服电话方便用户联系）。在详情页点击卡面信息会跳转卡面信息展示。右边可以看到预览效果。 |
   | 删除 | 用于控制钱包内删卡。 |

   运营区配置：可以按需配置服务菜单（最多支持5个），按需配置是否提供使用记录查看链接以及华为服务号入口，右边可以查看配置的预览效果。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/2DTnd1gXT1W0xOiKO-TYeA/zh-cn_image_0000002817507817.png?HW-CC-KV=V1&HW-CC-Date=20261114T004834Z&HW-CC-Expire=31536000000&HW-CC-Sign=99652088CAF0FA70562CC25FE8783FA1D4E7DE0F66109867658042DFF9FD7576)

   | **参数** | **说明** |
   | --- | --- |
   | 服务菜单 | 用于控制详情页的运营区。如果需要配置，点添加按钮后需要配置菜单名称（多语言可选）以及跳转地址。 |
   | 是否提供使用记录查看链接 | 用于控制详情页的运营区是否展示使用记录。 |
   | 是否提供华为服务号入口 | 控制详情页的运营区的服务号是否展示，如果需要配置，则填写开通服务号的ID和名称。 |

   官方App/元服务跳转配置：按需配置官方App/元服务跳转，如果选择是，需要按需配置跳转链接，右边可以查看配置的预览效果。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/IhFrmXGVSOSsHse89DRmig/zh-cn_image_0000002788308386.png?HW-CC-KV=V1&HW-CC-Date=20261114T004834Z&HW-CC-Expire=31536000000&HW-CC-Sign=DCC0196304DC5DD97C4FB52F7D151A513E6BD123B7F142BA697BF47B2837B7B5)
9. 提交前进行信息核对及预览，确认无误后，点击“提交”完成出行凭证Wallet Kit服务接入配置。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/nBhU-L61RACHmhqYajlrzQ/zh-cn_image_0000002817507795.png?HW-CC-KV=V1&HW-CC-Date=20261114T004834Z&HW-CC-Expire=31536000000&HW-CC-Sign=3F2142359C444CC379331C28D3077667E85A5DAF4440CE77D0F6FD8937E58E59)
