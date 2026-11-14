---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/wallet-generalcard-prepare
title: 开发准备
breadcrumb: 指南 > 应用服务 > Wallet Kit（钱包服务） > 通用凭证 > 开发准备
category: harmonyos-guides
scraped_at: 2026-11-14T08:48:35+08:00
doc_updated_at: 2026-09-24
content_hash: sha256:437076f052c166e1582cbe21d64693b2333a9e96403ab4b5dffea961e73f8a7b
---

## 创建Wallet Kit服务

请先参考“[应用开发准备](application-dev-overview.md)”完成基本准备工作和指纹配置，再继续以下开发活动。

1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)，点击“开发与服务”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/TDa0pGyZR2-AfHroygoxsg/zh-cn_image_0000002788468290.png?HW-CC-KV=V1&HW-CC-Date=20261114T004650Z&HW-CC-Expire=31536000000&HW-CC-Sign=F188750A5E3C42A2230E9066551FE221986F524FD89765A318D2FB1A7723883D)
2. 选择对应项目。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/BNKQchMITtG94wW-g26hZw/zh-cn_image_0000002817507779.png?HW-CC-KV=V1&HW-CC-Date=20261114T004650Z&HW-CC-Expire=31536000000&HW-CC-Sign=F412421622FE067004605B786C512F9406ECA49C961F21E96703AC0956028639)
3. 选择“钱包服务”，点击“申请服务”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/AmuXxF5aScuIQlOpZ40v1g/zh-cn_image_0000002817507781.png?HW-CC-KV=V1&HW-CC-Date=20261114T004650Z&HW-CC-Expire=31536000000&HW-CC-Sign=EEAD2C55E226193D948207832CCD751C171CF6D57AA93A19240423C8858872F5)
4. 点击“点击申请”，并选择新版本。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/E9aRgd_9TLmA9pVkQPvMLQ/zh-cn_image_0000002788308350.png?HW-CC-KV=V1&HW-CC-Date=20261114T004650Z&HW-CC-Expire=31536000000&HW-CC-Sign=A8E84BD769BEFEAD40B0D6641F9C1BF3CF9595E119E14929FFBE4111B9352E12)

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/oSv8PlZGTiuYIOR9EjZWLA/zh-cn_image_0000002817507791.png?HW-CC-KV=V1&HW-CC-Date=20261114T004650Z&HW-CC-Expire=31536000000&HW-CC-Sign=E24FE6EF8EBAA1688A5D7C222DDD1CD39FA351BE950F24E14A9DB7F449349BBB)
5. 配置Wallet Kit服务参数：服务类型选择票，服务子类型选择通用凭证，服务项目按需选择，并指定服务号、开发者服务公钥及开发者云侧服务地址前缀后，点击“下一步”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/ChOUnvNwR2O0BRDKaiKeiA/zh-cn_image_0000002788308360.png?HW-CC-KV=V1&HW-CC-Date=20261114T004650Z&HW-CC-Expire=31536000000&HW-CC-Sign=80EEBC7B9C4EB7D82EF2B77AE74F8A34FCA735F0E83DAA9D81E076219941A2C9)

   | **参数** | **说明** |
   | --- | --- |
   | 服务名称 | Wallet Kit首页列表展示该开发者所有创建的服务时，服务名称用于区分不同的服务。建议命名为公司简称+Wallet Kit+应用场景，长度不超过64个字符。 |
   | 服务类型 | 固定选择“票”。 |
   | 服务子类型 | 固定选择“通用凭证”。 |
   | 服务项目 | 选择接入的服务项目。 |
   | 默认卡名称 | 在钱包内显示的默认卡名称，长度不超过64个字符。 |
   | 服务号 | 开发者服务号，用于区分不同的项目和服务。建议格式为【hwpass.公司简称.项目名称.pass.服务项目】，须以hwpass开头 (自动填充，无需输入)，可为数字、字母，长度不超过32个字符。 |
   | 服务公钥 | Wallet Kit服务器认证开发者身份的凭证。依据页面上的"公钥操作步骤指导说明"生成公钥并回填。 |
   | 服务器地址前缀 | 开发者服务器地址，用于Wallet Kit服务器在开卡或删卡成功后回调开发者。如果不需要回调结果，可以不填该字段。 |
6. 配置NFC&二维码参数：按需选择卡片激活设备限制，可展码通行，但不涉及NFC，默认在用户华为账号登陆的所有设备可见，不支持动态二维码，推荐配置如下。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/7eDdqnWES8qtYfJy4dc2tQ/zh-cn_image_0000002788308390.png?HW-CC-KV=V1&HW-CC-Date=20261114T004650Z&HW-CC-Expire=31536000000&HW-CC-Sign=64B1E9F9B1F79FBD5A8D95E8E886509E3C4246E116225B13335E7205BA5D4ECF)
7. 配置添加预览信息：按要求上传卡面底图。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/lvM7pVkxS8eQ69RtV3OCFQ/zh-cn_image_0000002817427753.png?HW-CC-KV=V1&HW-CC-Date=20261114T004650Z&HW-CC-Expire=31536000000&HW-CC-Sign=C918007FD6E9BE1DDAD0AFE3225CFBD196EAAA8539BCB4290C4CBCD92A38EB79)
8. 配置卡详情页信息：按需配置卡面个性化信息，功能区，运营区以及官方App/元服务跳转。

   基本信息配置：可指定背景色、字体颜色、LOGO等，并输入样例信息查看实际通用凭证的效果。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/aBJszbTzT2eJFEONKnVC2g/zh-cn_image_0000002788468334.png?HW-CC-KV=V1&HW-CC-Date=20261114T004650Z&HW-CC-Expire=31536000000&HW-CC-Sign=EB39E5A1E4226CBE2572ABF2A1E72A67CAA44278B5D27211B36030C5B1C1949C)

   主要信息配置：支持自定义标签及内容，最多支持4个栏位。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/h9TsKpFjQnKjiXJI7pXaSQ/zh-cn_image_0000002817507815.png?HW-CC-KV=V1&HW-CC-Date=20261114T004650Z&HW-CC-Expire=31536000000&HW-CC-Sign=C02BC3696F09366264767A0D43D6E44AADA84E45AFB6B72700063EF7E0111346)

   次要信息配置：支持自定义标签及内容，最多支持4个栏位。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0a/v3/02C22IjbT7O4Bw492X6dmA/zh-cn_image_0000002788308384.png?HW-CC-KV=V1&HW-CC-Date=20261114T004650Z&HW-CC-Expire=31536000000&HW-CC-Sign=FAEA1228D5B211D4A1CE8EEA8079F67D5C8120CC452946988DA83ADAACE79343)

   功能区配置：支持卡片信息和删除功能。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/9v4ipHU4Tdychf9YeinH9w/zh-cn_image_0000002788468328.png?HW-CC-KV=V1&HW-CC-Date=20261114T004650Z&HW-CC-Expire=31536000000&HW-CC-Sign=85EED07A7265E8F0107A60679E29EBC7A1B6FDEEF120F8DD0A1FBF5212608089)

   | **参数** | **说明** |
   | --- | --- |
   | 卡片信息 | 用于展示卡面提供服务方（按需配置多语言）信息，按需勾选卡号和联系客服（客服电话方便用户联系）。在详情页点击卡面信息会跳转卡面信息展示。右边可以看到预览效果。 |
   | 删除 | 用于控制钱包内删卡。 |

   运营区配置：可以按需配置服务菜单（最多支持5个），按需配置是否提供使用记录查看链接以及华为服务号入口，右边可以查看配置的预览效果。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/4P5myQdlSUii_wpvB_DJjg/zh-cn_image_0000002817507817.png?HW-CC-KV=V1&HW-CC-Date=20261114T004650Z&HW-CC-Expire=31536000000&HW-CC-Sign=9E03A457B2D5851E775F853FCB15C2402FDFC99019B1D2B69152D489D795BC11)

   | **参数** | **说明** |
   | --- | --- |
   | 服务菜单 | 用于控制详情页的运营区。如果需要配置，点添加按钮后需要配置菜单名称（多语言可选）以及跳转地址。 |
   | 是否提供使用记录查看链接 | 用于控制详情页的运营区是否展示使用记录。 |
   | 是否提供华为服务号入口 | 控制详情页的运营区的服务号是否展示，如果需要配置，则填写开通服务号的ID和名称。 |

   官方App/元服务跳转配置：按需配置官方App/元服务跳转，如果选择是，需要按需配置跳转链接，右边可以查看配置的预览效果。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/11HuR7uxRtW0MWXtPFwSvA/zh-cn_image_0000002788308386.png?HW-CC-KV=V1&HW-CC-Date=20261114T004650Z&HW-CC-Expire=31536000000&HW-CC-Sign=23EF0DAC8CF1D20660FD16221AA1A62D558014F0CFD16DF6F6E7AB6910B8300E)
9. 提交前进行信息核对及预览，确认无误后，点击“提交”完成通用凭证Wallet Kit服务接入配置。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/iQWcpNG6QTmj4U0GbfdY-w/zh-cn_image_0000002817507795.png?HW-CC-KV=V1&HW-CC-Date=20261114T004650Z&HW-CC-Expire=31536000000&HW-CC-Sign=7185C163894BFB7864B5E50937F62617817C3C0FFC37B8C4306F7CDF27365D1B)
