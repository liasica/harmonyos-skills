---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/wallet-generalcard-prepare
title: 开发准备
breadcrumb: 指南 > 应用服务 > Wallet Kit（钱包服务） > 通用凭证 > 开发准备
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-09-24
content_hash: sha256:cf7e87f7a68d4e14991c3f3193a720442fedbdb28283f98e3b9bbe4af074d038
---

## 创建Wallet Kit服务

请先参考“[应用开发准备](application-dev-overview.md)”完成基本准备工作和指纹配置，再继续以下开发活动。

1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)，点击“开发与服务”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/0g1EvI5mQvehf9qsZ9zl_w/zh-cn_image_0000002786520542.png?HW-CC-KV=V1&HW-CC-Date=20261112T233237Z&HW-CC-Expire=31536000000&HW-CC-Sign=4543175B872C64B91B4A14A64AF7C25CB40EEF33DB1BAE7ED390ACF05E3E90F5)
2. 选择对应项目。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/BQ8ovaHjSJqrKgWEaoNFuw/zh-cn_image_0000002786360614.png?HW-CC-KV=V1&HW-CC-Date=20261112T233237Z&HW-CC-Expire=31536000000&HW-CC-Sign=365C020FEAE7D4BC7350875CEED238F28BF9D2A81A3CB12DAFA8660322F85EC4)
3. 选择“钱包服务”，点击“申请服务”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/n1PhfYL4TAW5AFLvE1Sh_w/zh-cn_image_0000002786360616.png?HW-CC-KV=V1&HW-CC-Date=20261112T233237Z&HW-CC-Expire=31536000000&HW-CC-Sign=9F6B99A2290BE5BFA1ACE1023D574D4CF9C725971D497E220072C62C03DB1DFE)
4. 点击“点击申请”，并选择新版本。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/0m15jKweRUqJJAHaz2I_1g/zh-cn_image_0000002815560037.png?HW-CC-KV=V1&HW-CC-Date=20261112T233237Z&HW-CC-Expire=31536000000&HW-CC-Sign=3FAFDE396B5B0C3B5D69676E0C3B4315EEBE37A4F85AF40D8E843777F26D5AC5)

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/H0JzHGRyQFCU7edt7jQEXQ/zh-cn_image_0000002786360626.png?HW-CC-KV=V1&HW-CC-Date=20261112T233237Z&HW-CC-Expire=31536000000&HW-CC-Sign=922F089F1D8CFF9FC4D1F73FF4EDFBE14AA70A8BCC39D9587C5C67C8FFCFDE34)
5. 配置Wallet Kit服务参数：服务类型选择票，服务子类型选择通用凭证，服务项目按需选择，并指定服务号、开发者服务公钥及开发者云侧服务地址前缀后，点击“下一步”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/Y4vQS-_ZSCyNxX897UVjWw/zh-cn_image_0000002815560047.png?HW-CC-KV=V1&HW-CC-Date=20261112T233237Z&HW-CC-Expire=31536000000&HW-CC-Sign=CB200AE78B14782F67CD268621DB48D90B807B704D1C7DB091159939DFB47043)

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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/jrpx5df7TDCoUtK0gB8oqA/zh-cn_image_0000002815560077.png?HW-CC-KV=V1&HW-CC-Date=20261112T233237Z&HW-CC-Expire=31536000000&HW-CC-Sign=BD24C684B905081111621C155023B66E47029480A1B81FAF8C763B42E29018A1)
7. 配置添加预览信息：按要求上传卡面底图。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/4sJZ0fq8Sq-jDZ6Y6j0XTg/zh-cn_image_0000002815400161.png?HW-CC-KV=V1&HW-CC-Date=20261112T233237Z&HW-CC-Expire=31536000000&HW-CC-Sign=3FE8BC43D69858EF3618E11A0F2C887184203B1785139F935CC62EE2D35593FC)
8. 配置卡详情页信息：按需配置卡面个性化信息，功能区，运营区以及官方App/元服务跳转。

   基本信息配置：可指定背景色、字体颜色、LOGO等，并输入样例信息查看实际通用凭证的效果。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/bDoLLZ_ITYm0ScUEEZdC4w/zh-cn_image_0000002786520586.png?HW-CC-KV=V1&HW-CC-Date=20261112T233237Z&HW-CC-Expire=31536000000&HW-CC-Sign=497AE780FC28A64BC7F79EDC9293CADECCA62AE27359C60F1D490746A05DF9DB)

   主要信息配置：支持自定义标签及内容，最多支持4个栏位。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/jqYPqs2SQWCq201X8bQU-Q/zh-cn_image_0000002786360650.png?HW-CC-KV=V1&HW-CC-Date=20261112T233237Z&HW-CC-Expire=31536000000&HW-CC-Sign=EFBB74479F406FC74E61C607BD5DF1B2775EE2BD4982D7CC9A2EEFBDE05015AC)

   次要信息配置：支持自定义标签及内容，最多支持4个栏位。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/rcCwXvjtRPW0ZSl1yBH9iA/zh-cn_image_0000002815560071.png?HW-CC-KV=V1&HW-CC-Date=20261112T233237Z&HW-CC-Expire=31536000000&HW-CC-Sign=5E603473A74D4801819F92F637A784BADB616C66646EAED978A92A22E089E05A)

   功能区配置：支持卡片信息和删除功能。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/2eJJcG7XSBCnV09oVg92Rg/zh-cn_image_0000002786520580.png?HW-CC-KV=V1&HW-CC-Date=20261112T233237Z&HW-CC-Expire=31536000000&HW-CC-Sign=BFDA834C961E413BDB920489974C00E7748DFDE2F52B40700FFB7E26A4D01724)

   | **参数** | **说明** |
   | --- | --- |
   | 卡片信息 | 用于展示卡面提供服务方（按需配置多语言）信息，按需勾选卡号和联系客服（客服电话方便用户联系）。在详情页点击卡面信息会跳转卡面信息展示。右边可以看到预览效果。 |
   | 删除 | 用于控制钱包内删卡。 |

   运营区配置：可以按需配置服务菜单（最多支持5个），按需配置是否提供使用记录查看链接以及华为服务号入口，右边可以查看配置的预览效果。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/XaY9LaLaQNKUKSl0O_gtyQ/zh-cn_image_0000002786360652.png?HW-CC-KV=V1&HW-CC-Date=20261112T233237Z&HW-CC-Expire=31536000000&HW-CC-Sign=E4FEF23BCDB8E7864F99A7FB295F5E60CBA117597515C47FED0DDCB845132CA3)

   | **参数** | **说明** |
   | --- | --- |
   | 服务菜单 | 用于控制详情页的运营区。如果需要配置，点添加按钮后需要配置菜单名称（多语言可选）以及跳转地址。 |
   | 是否提供使用记录查看链接 | 用于控制详情页的运营区是否展示使用记录。 |
   | 是否提供华为服务号入口 | 控制详情页的运营区的服务号是否展示，如果需要配置，则填写开通服务号的ID和名称。 |

   官方App/元服务跳转配置：按需配置官方App/元服务跳转，如果选择是，需要按需配置跳转链接，右边可以查看配置的预览效果。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/zrgJAq4AQaOJPVHlVSkohQ/zh-cn_image_0000002815560073.png?HW-CC-KV=V1&HW-CC-Date=20261112T233237Z&HW-CC-Expire=31536000000&HW-CC-Sign=F286B752BCBBA97184096A608709A1B277C00F44583FF6450F4B08EE4A9B2EA9)
9. 提交前进行信息核对及预览，确认无误后，点击“提交”完成通用凭证Wallet Kit服务接入配置。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/tX0BbhSgT3OxnK_MnPTuLQ/zh-cn_image_0000002786360630.png?HW-CC-KV=V1&HW-CC-Date=20261112T233237Z&HW-CC-Expire=31536000000&HW-CC-Sign=12022756832EA0962197B17FE0369DA8661E7BA8BB2461725C284877F7D3693E)
