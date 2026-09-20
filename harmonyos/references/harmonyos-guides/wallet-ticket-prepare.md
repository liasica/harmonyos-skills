---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/wallet-ticket-prepare
title: 开发准备
breadcrumb: 指南 > 应用服务 > Wallet Kit（钱包服务） > 活动/景点门票 > 开发准备
category: harmonyos-guides
scraped_at: 2026-09-21T06:18:51+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:95dc5d0ba5df691771f209275beec5fec0a0257ac5e040b6458174b157d0c7df
---

## 创建Wallet Kit服务

请先参考“[应用开发准备](application-dev-overview.md)”完成基本准备工作和指纹配置，再继续以下开发活动。

1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)，点击“开发与服务”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/ctIC9xS8RPm4hZc5Ksf6Ng/zh-cn_image_0000002762995031.png)
2. 选择对应项目。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/lvwi5H4YS9yCnPQDG66Jvw/zh-cn_image_0000002762835143.png)
3. 选择“钱包服务”，点击“申请服务”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/uBok8DSlQp2wpFzED0nW1Q/zh-cn_image_0000002762835145.png)
4. 点击“点击申请”，并选择新版本。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/_BDrz1eIT_qgAhjNoOMBNQ/zh-cn_image_0000002733275632.png)

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/XKFqLypbSjuzflbpfXDsfA/zh-cn_image_0000002762835155.png)
5. 配置Wallet Kit服务参数：服务类型选择票，服务子类型选择门票，服务项目按需选择，并指定服务号、开发者服务公钥及开发者云侧服务地址前缀后，点击“下一步”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/7onPl23OTXOiKGefxo9eSg/zh-cn_image_0000002733275642.png)

   | **参数** | **说明** |
   | --- | --- |
   | 服务名称 | Wallet Kit首页列表展示该开发者所有创建的服务时，服务名称用于区分不同的服务。建议命名为公司简称+Wallet Kit+应用场景，长度不超过64个字符。 |
   | 服务类型 | 固定选择“票”。 |
   | 服务子类型 | 固定选择“门票”。 |
   | 服务项目 | 选择接入的服务项目。 |
   | 默认卡名称 | 在钱包内显示的默认卡名称 ，长度不超过64个字符。 |
   | 服务号 | 开发者服务号，用于区分不同的项目和服务。建议格式为【hwpass.公司简称.项目名称.pass.服务项目】，须以hwpass开头 (自动填充，无需输入)，可为数字、字母，长度不超过32个字符。 |
   | 服务公钥 | 开发者将生成的公钥，后续该公钥将作为Wallet Kit服务器认证开发者身份的凭证。 |
   | 服务器地址前缀 | 开发者服务器地址，用于Wallet Kit服务器在开卡或删卡成功后回调开发者。如果不需要回调结果，可以不填该字段。 |
6. 配置NFC&二维码参数：可展码通行，但不涉及NFC，默认在用户华为账号登陆的所有设备可见，不支持动态二维码，推荐配置如下。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/rDb0hsmRRW2fdIBais2Msw/zh-cn_image_0000002762835183.png)
7. 配置添加预览信息：按要求上传卡面底图。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/QqhUArkuTByyieTj3CLZgQ/zh-cn_image_0000002733275670.png)
8. 配置卡详情页信息：按需配置卡面个性化信息，功能区，运营区以及官方App/元服务跳转。

   基本信息配置：可指定背景色、字体颜色、LOGO等，并输入样例信息查看实际活动/景点门票的效果。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/Q0RSts63Q3yc7fKumkaKaQ/zh-cn_image_0000002733435550.png)

   主要信息配置：支持自定义标签及内容，最多支持4个栏位。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/5ofSHfKiRDq9HMl3_xw6-A/zh-cn_image_0000002762835179.png)

   次要信息配置：支持自定义标签及内容，最多支持4个栏位。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/verawnJmTUunBjaK4ye4FA/zh-cn_image_0000002733275666.png)

   功能区配置：支持卡片信息和删除功能。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/9bKr_E4JSICaR9HZK14hDw/zh-cn_image_0000002762995069.png)

   | **参数** | **说明** |
   | --- | --- |
   | 卡片信息 | 用于展示卡面提供服务方（按需配置多语言）信息，按需勾选卡号和联系客服（客服电话方便用户联系）。在详情页点击卡面信息会跳转卡面信息展示。右边可以看到预览效果。 |
   | 删除 | 用于控制钱包内删卡。 |

   运营区配置：可以按需配置服务菜单（最多支持5个），按需配置是否提供使用记录查看链接以及华为服务号入口，右边可以查看配置的预览效果。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/04/v3/yxJ2UyG4T9OrnEq8UF0vHw/zh-cn_image_0000002762835181.png)

   | **参数** | **说明** |
   | --- | --- |
   | 服务菜单 | 用于控制详情页的运营区。如果需要配置，点添加按钮后需要配置菜单名称（多语言可选）以及跳转地址。 |
   | 是否提供使用记录查看链接 | 用于控制详情页的运营区是否展示使用记录。 |
   | 是否提供华为服务号入口 | 控制详情页的运营区的服务号是否展示，如果需要配置，则填写开通服务号的ID和名称。 |

   官方App/元服务跳转配置：按需配置官方App/元服务跳转，如果选择是，需要按需配置跳转链接，右边可以查看配置的预览效果。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/o1upxOGKSICElJJPFTMUUA/zh-cn_image_0000002733275668.png)
9. 提交前进行信息核对及预览，确认无误后，点击“提交”完成活动/景点门票Wallet Kit服务接入配置。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/UluNhnY8RTKvl_2sZRUNrQ/zh-cn_image_0000002762835159.png)
