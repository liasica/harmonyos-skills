---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/wallet-generalcard-prepare
title: 开发准备
breadcrumb: 指南 > 应用服务 > Wallet Kit（钱包服务） > 通用凭证 > 开发准备
category: harmonyos-guides
scraped_at: 2026-11-21T09:12:42+08:00
doc_updated_at: 2026-09-24
content_hash: sha256:70cf7b0b9259a8ae7dcc1025aa36e4533e8130e61f6a4d4ddeeebb41325f343c
---

## 创建Wallet Kit服务

请先参考“[应用开发准备](application-dev-overview.md)”完成基本准备工作和指纹配置，再继续以下开发活动。

1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)，点击“开发与服务”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/XSEZJ2EBS52T44Xdm3WK9w/zh-cn_image_0000002792878330.png?HW-CC-KV=V1&HW-CC-Date=20261121T011241Z&HW-CC-Expire=31536000000&HW-CC-Sign=0C305E272217E579E30A62287F6B72521B8C14DDDA71915A15DE8349951B3B1B)
2. 选择对应项目。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/7gjU1FyGSYe8raiuqo-Bvg/zh-cn_image_0000002821838237.png?HW-CC-KV=V1&HW-CC-Date=20261121T011241Z&HW-CC-Expire=31536000000&HW-CC-Sign=96DACABBBDDF301CC559D9140A3EF6B4B10E2707F5E3A49B2147DF645557F661)
3. 选择“钱包服务”，点击“申请服务”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/yJUS-363SWO3MujR9MCrlA/zh-cn_image_0000002821838239.png?HW-CC-KV=V1&HW-CC-Date=20261121T011241Z&HW-CC-Expire=31536000000&HW-CC-Sign=D0F29E922F91FD50B54DEEC5CA9BC59E1A06BFBADCAFD117DE7C5328FACE0FB1)
4. 点击“点击申请”，并选择新版本。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/veyrBePyS3mIrJG9ECgrQA/zh-cn_image_0000002821758241.png?HW-CC-KV=V1&HW-CC-Date=20261121T011241Z&HW-CC-Expire=31536000000&HW-CC-Sign=06AF86BD6291AFD12C9639B6C59AE5CCCD1B08382440B05002FE192EF50ECFF6)

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/TxmmgG19QfeNOIT19dOqnQ/zh-cn_image_0000002821838249.png?HW-CC-KV=V1&HW-CC-Date=20261121T011241Z&HW-CC-Expire=31536000000&HW-CC-Sign=5DADBB2E89E54185B56E78374A286F0B4E9051573983C9460F3DF52719E26094)
5. 配置Wallet Kit服务参数：服务类型选择票，服务子类型选择通用凭证，服务项目按需选择，并指定服务号、开发者服务公钥及开发者云侧服务地址前缀后，点击“下一步”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/4t8zm7Z6RaCEYSpf1uBgGQ/zh-cn_image_0000002821758251.png?HW-CC-KV=V1&HW-CC-Date=20261121T011241Z&HW-CC-Expire=31536000000&HW-CC-Sign=2ED3178BA7F09275AFC17AB33BD2653C0D09744B898AA867810F7F9A624B6693)

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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/7tZPd7YwSCG7AIB1DeSsgw/zh-cn_image_0000002821758281.png?HW-CC-KV=V1&HW-CC-Date=20261121T011241Z&HW-CC-Expire=31536000000&HW-CC-Sign=C6BB63029F049774CCAD85AE40B9302D50BA6BC1BCE2B4AECBDFBFF805588DD9)
7. 配置添加预览信息：按要求上传卡面底图。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/9qbKiBzVQoiJXYwgSjFeUA/zh-cn_image_0000002793038344.png?HW-CC-KV=V1&HW-CC-Date=20261121T011241Z&HW-CC-Expire=31536000000&HW-CC-Sign=2FB12708DACB5C902A8D238402A0783D8FF0661522A121517C936003D864F9DA)
8. 配置卡详情页信息：按需配置卡面个性化信息，功能区，运营区以及官方App/元服务跳转。

   基本信息配置：可指定背景色、字体颜色、LOGO等，并输入样例信息查看实际通用凭证的效果。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/P9JJS9iuT8CTwRPM6BRzJg/zh-cn_image_0000002792878374.png?HW-CC-KV=V1&HW-CC-Date=20261121T011241Z&HW-CC-Expire=31536000000&HW-CC-Sign=7628F08E1F952593BB6D8D33398B95738C1697D01867560D3135CEDA71CC2536)

   主要信息配置：支持自定义标签及内容，最多支持4个栏位。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/VSce2GW7TFigouBdtPju6w/zh-cn_image_0000002821838273.png?HW-CC-KV=V1&HW-CC-Date=20261121T011241Z&HW-CC-Expire=31536000000&HW-CC-Sign=3B3EAC4AB50DD9AE0623EE8F2E35CF0F2C95906CB86A0E4DA976FAB7AA208F97)

   次要信息配置：支持自定义标签及内容，最多支持4个栏位。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/FJBFkXVWQxiQPKSLtM9PlQ/zh-cn_image_0000002821758275.png?HW-CC-KV=V1&HW-CC-Date=20261121T011241Z&HW-CC-Expire=31536000000&HW-CC-Sign=2254F54B75D746073B991BBC7A5714D20E106F083E1B1E7125ED42175956816F)

   功能区配置：支持卡片信息和删除功能。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/QfmudLq6R1CoDQbg9dui9g/zh-cn_image_0000002792878368.png?HW-CC-KV=V1&HW-CC-Date=20261121T011241Z&HW-CC-Expire=31536000000&HW-CC-Sign=DC8DEA0CC5467B8D49C67E460EF499339CEEA1D3BA54D36F14DB7B4BFAF32457)

   | **参数** | **说明** |
   | --- | --- |
   | 卡片信息 | 用于展示卡面提供服务方（按需配置多语言）信息，按需勾选卡号和联系客服（客服电话方便用户联系）。在详情页点击卡面信息会跳转卡面信息展示。右边可以看到预览效果。 |
   | 删除 | 用于控制钱包内删卡。 |

   运营区配置：可以按需配置服务菜单（最多支持5个），按需配置是否提供使用记录查看链接以及华为服务号入口，右边可以查看配置的预览效果。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/NKnUcVSkTWmwfk7nBoMIww/zh-cn_image_0000002821838275.png?HW-CC-KV=V1&HW-CC-Date=20261121T011241Z&HW-CC-Expire=31536000000&HW-CC-Sign=8FD0F4DC218C206AAAC10765125903E960045C1DDEBB107D08F56EC3F3CA69F5)

   | **参数** | **说明** |
   | --- | --- |
   | 服务菜单 | 用于控制详情页的运营区。如果需要配置，点添加按钮后需要配置菜单名称（多语言可选）以及跳转地址。 |
   | 是否提供使用记录查看链接 | 用于控制详情页的运营区是否展示使用记录。 |
   | 是否提供华为服务号入口 | 控制详情页的运营区的服务号是否展示，如果需要配置，则填写开通服务号的ID和名称。 |

   官方App/元服务跳转配置：按需配置官方App/元服务跳转，如果选择是，需要按需配置跳转链接，右边可以查看配置的预览效果。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/HJ2vooM-Q6-xBH71p4-oJQ/zh-cn_image_0000002821758277.png?HW-CC-KV=V1&HW-CC-Date=20261121T011241Z&HW-CC-Expire=31536000000&HW-CC-Sign=3A2505C2E4AB64093C9277A6757E9C3F1BF93F438488615B5C40FC5D31BB4567)
9. 提交前进行信息核对及预览，确认无误后，点击“提交”完成通用凭证Wallet Kit服务接入配置。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/9SSpFzJpTWi-LzrItfQHrQ/zh-cn_image_0000002821838253.png?HW-CC-KV=V1&HW-CC-Date=20261121T011241Z&HW-CC-Expire=31536000000&HW-CC-Sign=C1ED37A135E656487EDD9F7BD5A13FC6773D84FB656D1E77B786D4C12CF8CD2B)
