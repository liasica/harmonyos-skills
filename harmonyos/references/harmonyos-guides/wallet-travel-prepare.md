---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/wallet-travel-prepare
title: 开发准备
breadcrumb: 指南 > 应用服务 > Wallet Kit（钱包服务） > 出行凭证 > 开发准备
category: harmonyos-guides
scraped_at: 2026-10-31T07:33:17+08:00
doc_updated_at: 2026-09-24
content_hash: sha256:427f055e972f8111140c43dd2f0b7c8f62eeb03e3ce7eb26154cce9f107aa054
---

## 创建Wallet Kit服务

请先参考“[应用开发准备](application-dev-overview.md)”完成基本准备工作和指纹配置，再继续以下开发活动。

1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)，点击“开发与服务”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/sR8OTRGGRsOryCntXac5pg/zh-cn_image_0000002806029907.png)
2. 选择对应项目。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/sX3tqdcJQqePi3qd6pw2sg/zh-cn_image_0000002806109797.png)
3. 选择“钱包服务”，点击“申请服务”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/2nxmAWWoSPqTvZi-t7fR5w/zh-cn_image_0000002806109799.png)
4. 点击“点击申请”，并选择新版本。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/qlmb3pd0RtOOP_pk0W1F0w/zh-cn_image_0000002776910180.png)

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/vjUQlEPpSXCeBr_uBw1Qxg/zh-cn_image_0000002806109809.png)
5. 配置Wallet Kit服务参数：服务类型选择票，服务子类型选择出行凭证，服务项目按需选择，并指定服务号、开发者服务公钥及开发者云侧服务地址前缀后，点击“下一步”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/BUXODP8-QNiJQbmVOEE1tg/zh-cn_image_0000002776910190.png)

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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/baxVxGQIT1WnNaOFuvGtOA/zh-cn_image_0000002776910212.png)
7. 配置添加预览信息：按要求上传卡面底图。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/-cRuUmFdSq-2T5Fs6Okjrg/zh-cn_image_0000002776750226.png)
8. 配置卡详情页信息：按需配置卡面个性化信息，功能区，运营区以及官方App/元服务跳转。

   基本信息配置：可指定背景色、字体颜色、LOGO等，并输入样例信息查看实际出行凭证的效果。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/X5q88AQjRAS9nWOUmAR_Xw/zh-cn_image_0000002806029943.png)

   主要信息配置：支持自定义标签及内容，最多支持4个栏位。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/sUnCFT8ZRZa8CGhYnzBfyw/zh-cn_image_0000002806109833.png)

   次要信息配置：支持自定义标签及内容，最多支持4个栏位。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/K6ghw6m-QZGRtrltERSewQ/zh-cn_image_0000002776910214.png)

   补充信息区配置：该区域不展示标签，仅展示内容。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8/v3/uCQLmWwcSAmM34nwfNNjzg/zh-cn_image_0000002776750228.png)

   功能区配置：支持卡片信息和删除功能。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/RAf-kO76QjmDuVOEgWOGYg/zh-cn_image_0000002806029945.png)

   | **参数** | **说明** |
   | --- | --- |
   | 卡片信息 | 用于展示卡面提供服务方（按需配置多语言）信息，按需勾选卡号和联系客服（客服电话方便用户联系）。在详情页点击卡面信息会跳转卡面信息展示。右边可以看到预览效果。 |
   | 删除 | 用于控制钱包内删卡。 |

   运营区配置：可以按需配置服务菜单（最多支持5个），按需配置是否提供使用记录查看链接以及华为服务号入口，右边可以查看配置的预览效果。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/BLG-VuwVTRmis8YbdyvCNQ/zh-cn_image_0000002806109835.png)

   | **参数** | **说明** |
   | --- | --- |
   | 服务菜单 | 用于控制详情页的运营区。如果需要配置，点添加按钮后需要配置菜单名称（多语言可选）以及跳转地址。 |
   | 是否提供使用记录查看链接 | 用于控制详情页的运营区是否展示使用记录。 |
   | 是否提供华为服务号入口 | 控制详情页的运营区的服务号是否展示，如果需要配置，则填写开通服务号的ID和名称。 |

   官方App/元服务跳转配置：按需配置官方App/元服务跳转，如果选择是，需要按需配置跳转链接，右边可以查看配置的预览效果。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/7K4EqOIDSLGBgBsBtvlGYQ/zh-cn_image_0000002776910216.png)
9. 提交前进行信息核对及预览，确认无误后，点击“提交”完成出行凭证Wallet Kit服务接入配置。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/mGTcP7hmQs6LQ3iPr_QSsA/zh-cn_image_0000002806109813.png)
