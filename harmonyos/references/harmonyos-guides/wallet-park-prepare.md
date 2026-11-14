---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/wallet-park-prepare
title: 开发准备
breadcrumb: 指南 > 应用服务 > Wallet Kit（钱包服务） > 园区卡 > 开发准备
category: harmonyos-guides
scraped_at: 2026-11-14T08:48:34+08:00
doc_updated_at: 2026-09-24
content_hash: sha256:f07008fce78d5b9a1629eeb6ec73da77ff3796fb54548158eca97d9b9af81959
---

## 创建Wallet Kit服务

请先参考“[应用开发准备](application-dev-overview.md)”完成基本准备工作和指纹配置，再继续以下开发活动。

1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)，点击“开发与服务”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/qHQLC67KSbiVXey6jrqhSw/zh-cn_image_0000002788468290.png?HW-CC-KV=V1&HW-CC-Date=20261114T004833Z&HW-CC-Expire=31536000000&HW-CC-Sign=DB38528C01676DB48B88ED93087C1A761241CFE8077366F1840E2C34750445FF)
2. 选择对应项目。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/g5TBQ2aOSY2KuoCvEUsu2A/zh-cn_image_0000002817507779.png?HW-CC-KV=V1&HW-CC-Date=20261114T004833Z&HW-CC-Expire=31536000000&HW-CC-Sign=ACB889752D9A70A42CC3AEAC05624A95947D51574192218DB6599825B3454B53)
3. 选择“钱包服务”，点击“申请服务”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/s-YR20VySBe9QRMXTGQ0jA/zh-cn_image_0000002817507781.png?HW-CC-KV=V1&HW-CC-Date=20261114T004833Z&HW-CC-Expire=31536000000&HW-CC-Sign=C2599686E7D1635531D345AF0888AEAFBFE2ED5E14D47F4DAA6E0CFC511D355A)
4. 点击“点击申请”，并选择新版本。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/qCzl6-A0RVKITShrEJimUQ/zh-cn_image_0000002788308350.png?HW-CC-KV=V1&HW-CC-Date=20261114T004833Z&HW-CC-Expire=31536000000&HW-CC-Sign=7A6AEDC41F5BE07EEFEDF199A1F640BE68C2844161924426CBAA2A760B6AE135)

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/XXbf5DoYSyGzDigtNTeEkw/zh-cn_image_0000002817507791.png?HW-CC-KV=V1&HW-CC-Date=20261114T004833Z&HW-CC-Expire=31536000000&HW-CC-Sign=D51C1A01FCA67B3C99FB5F20B7C3A25830DE891E364BD597BA626976F4FDC481)
5. 配置Wallet Kit服务参数：服务类型选择钥匙，服务子类型选择园区卡，服务项目按需选择，并指定服务号、开发者服务公钥及开发者云侧服务地址前缀后，点击“下一步”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/efPRyiQiQDe21nRTtF_dbw/zh-cn_image_0000002788308360.png?HW-CC-KV=V1&HW-CC-Date=20261114T004833Z&HW-CC-Expire=31536000000&HW-CC-Sign=F1FF3328C922B0AF018B42FE6E0F6288ACB1B0B67813DD9334894766E2718972)

   | **参数** | **说明** |
   | --- | --- |
   | 服务名称 | Wallet Kit首页列表展示该开发者所有创建的服务时，服务名称用于区分不同的服务。建议命名为公司简称+Wallet Kit+应用场景，长度不超过64个字符。 |
   | 服务类型 | 固定选择“钥匙”。 |
   | 服务子类型 | 固定选择“园区卡”。 |
   | 服务项目 | 选择接入的服务项目。 |
   | 默认卡名称 | 在钱包内显示的默认卡名称 ，长度不超过64个字符。 |
   | 服务号 | 开发者服务号，用于区分不同的项目和服务。建议格式为【hwpass.公司简称.项目名称.pass.服务项目】，须以hwpass开头 (自动填充，无需输入)，可为数字、字母，长度不超过32个字符。 |
   | 服务公钥 | Wallet Kit服务器认证开发者身份的凭证。依据页面上的"公钥操作步骤指导说明"生成公钥并回填。 |
   | 服务器地址前缀 | 开发者服务器地址，用于Wallet Kit服务器在开卡或删卡成功后回调开发者。如果不需要回调结果，可以不填该字段。 |
6. 配置NFC&二维码参数：按需选择卡片激活设备限制，默认选择开通NFC能力，开通NFC能力，同时需要配置应用ID和文件参数，按需选择二维码配置。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/zxrhgOZLTGy7XYdYGGAP2Q/zh-cn_image_0000002817427723.png?HW-CC-KV=V1&HW-CC-Date=20261114T004833Z&HW-CC-Expire=31536000000&HW-CC-Sign=970E5622460CC11E13AF9B6F19671DCE88979A146BBCD187B305464EEE15654E)

   | **参数** | **说明** |
   | --- | --- |
   | 卡片激活设备限制 | 用于控制设备激活限制。  单设备专属：激活后仅限当前设备使用，更换需解绑。  多设备共享：统一账号下支持多台设备同时激活。 |
   | 是否开通NFC能力 | 园区卡默认选择开通NFC能力。开通NFC能力，同时需要配置应用ID和文件参数。 |
   | 应用ID | 通过“获取AID”按钮创建新应用ID，内容格式为16进制数（字符为 0-F），最大长度为32（推荐32位）。 |
   | 外部认证密钥 | 用于离线读写卡时外部认证校验。内容格式为16进制数（字符为 0-F），最大长度为32（推荐32位）。 |
   | 文件参数定义 | 密钥信息，用于对指定文件区域读写权限的控制。内容格式为16进制数（字符为 0-F），最大长度为32（推荐32位）。 |
   | 是否需展示二维码 | 用于控制是否展示二维码。如果配置展示二维码需要配置二维码配置。 |
   | 二维码类型 | 用于控制二维码类型，如果是动态码需要提供相应API接口以便钱包实时请码，参考[生成展示二维码](wallet-park-scene-qr.md)章节实现。 |
   | 是否可反馈交易结果 | 用于控制扫码后是否支持跳转到成功页面，只有动态二维码才支持，静态二维码默认配置否。如果配置是，需要提供相应API接口以便钱包实时请求扫码结果。 |
   | 刷卡页是否默认展码 | 用于控制刷卡页是否默认展码。 |
7. 添加预览信息配置：按要求上传卡面底图。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/06/v3/jVsXoqlNTTGAl1ddkIX2-g/zh-cn_image_0000002788468304.png?HW-CC-KV=V1&HW-CC-Date=20261114T004833Z&HW-CC-Expire=31536000000&HW-CC-Sign=683A04A8FDC4EEA6362330B38559B65B1186AA3C2DF3E9F36EAFC11EDB1A2A89)
8. 详情页信息配置：按需配置卡面个性化信息，功能区，运营区以及官方App/元服务跳转。

   个性化信息配置：按需配置是否展示前缀，文字颜色，文字位置以及字段位置。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/BxNAusclSBiLVczPsApjcQ/zh-cn_image_0000002817507793.png?HW-CC-KV=V1&HW-CC-Date=20261114T004833Z&HW-CC-Expire=31536000000&HW-CC-Sign=2983C042808BE41F9D374057BBBB7F3B5F0CF3A2983D73F21335D06221F507C7)

   | **参数** | **说明** |
   | --- | --- |
   | 是否展示前缀 | 是否需要展示个性化字段的前缀（如：“号码：8888”），如需展示，可以自定义前缀名称，勾选字段后可预览效果。 |
   | 文字颜色 | 个性化字体颜色，可以用左边的选色版选色也可以自己编辑要求6位十六进制色值，以#开头，建议用默认值#ffffff。 |
   | 文字位置 | 用于控制个性化信息在卡面展示的位置，有靠近底部和居中两种位置选择。 |
   | 字段位置 | 按需勾选需要的字段，按需配置前缀值（如果勾选展示前缀），文字大小（建议默认值14），填写示例值，右边可以看到预览效果。 |

   功能区配置：按需配置充值和卡片信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/-D9AZ-fdSE6t_XCXfX8R-Q/zh-cn_image_0000002788308362.png?HW-CC-KV=V1&HW-CC-Date=20261114T004833Z&HW-CC-Expire=31536000000&HW-CC-Sign=BF03DBAFB8853D5561F0CEFE72AB6BBA1F2600BAB1F1B3D5C667AC4478B547F3)

   | **参数** | **说明** |
   | --- | --- |
   | 充值 | 用于控制详情页功能区的充值功能，如果需要充值功能，需要按需配置充值跳转链接，在卡详情功能区点击充值可以跳转配置的充值页面。 |
   | 卡片信息 | 用于展示卡面提供服务方（按需配置多语言）信息，按需勾选卡号和联系客服（客服电话方便用户联系）。在详情页点击卡面信息会跳转卡面信息展示。右边可以看到预览效果。 |

   运营区配置：可以按需配置服务菜单（最多支持5个），按需配置是否提供使用记录查看链接以及华为服务号入口，右边可以查看配置的预览效果。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/re1GhKLpQAWubeMVmLmGOA/zh-cn_image_0000002817427725.png?HW-CC-KV=V1&HW-CC-Date=20261114T004833Z&HW-CC-Expire=31536000000&HW-CC-Sign=D5770AFF050A3D4851714ECF1DD087C23A1F96D2603451AFED52F830D7155464)

   | **参数** | **说明** |
   | --- | --- |
   | 服务菜单 | 用于控制详情页的运营区。如果需要配置，点添加按钮后需要配置菜单名称（多语言可选）以及跳转地址。 |
   | 是否提供使用记录查看链接 | 用于控制详情页的运营区是否展示使用记录。 |
   | 是否提供华为服务号入口 | 控制详情页的运营区的服务号是否展示，如果需要配置，则填写开通服务号的ID和名称。 |

   官方App/元服务跳转配置：按需配置官方App/元服务跳转，如果选择是，需要按需配置跳转链接，右边可以查看配置的预览效果。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/zbu6S6sPRdWg_LS0lGNhlA/zh-cn_image_0000002788468306.png?HW-CC-KV=V1&HW-CC-Date=20261114T004833Z&HW-CC-Expire=31536000000&HW-CC-Sign=386406E750A9F320554B81E7021F77C8AFEF5CB31FBF145BB0EDDA5DB132450F)
9. 提交前进行信息核对及预览，确认无误后，点击“提交”完成园区卡Wallet Kit服务接入配置。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/Zie4Z6TyTyypsFnNr1GCTA/zh-cn_image_0000002817507795.png?HW-CC-KV=V1&HW-CC-Date=20261114T004833Z&HW-CC-Expire=31536000000&HW-CC-Sign=B9370DE8F17AA8535130A6E9343E54D4C80BD433EC70C90E64DD791297D52A69)
