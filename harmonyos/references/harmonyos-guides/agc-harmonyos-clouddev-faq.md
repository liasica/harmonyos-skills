---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/agc-harmonyos-clouddev-faq
title: FAQ
breadcrumb: 指南 > 开发环境搭建 > 工程创建 > 模块管理 > 端云一体化开发 > FAQ
category: harmonyos-guides
scraped_at: 2026-04-28T07:55:10+08:00
doc_updated_at: 2026-04-22
content_hash: sha256:73f41366bbe1b2fef329320845d70a2b5e68edc71d592d5e2de13c2538cf93a8
---

## 使用DevEco Studio打开端云一体化项目文件夹，左侧的项目列表不显示云侧工程

**问题现象**

开发者使用DevEco Studio打开端云一体化项目文件夹，左侧的项目列表不显示云侧工程“CloudProgram”。

**解决措施**

端云一体化工程根目录下只允许有“Application”与“CloudProgram”文件夹，不能有其他文件。否则，DevEco Studio会把该工程当成纯端侧工程，不显示云侧工程“CloudProgram”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/Wcyt6T1OTyeuVN68Qqqf9A/zh-cn_image_0000002313987669.png?HW-CC-KV=V1&HW-CC-Date=20260427T235508Z&HW-CC-Expire=86400&HW-CC-Sign=368AA93972B27AAD799E752F25B95493B3F36C22C74406BF077E33F8F59AF793)

## 部署云数据库时，提示“clouddb deploy failed. Reason is the number of CloudDBZone exceeds the limit.”

**问题现象**

部署云数据库失败，提示“clouddb deploy failed. Reason is the number of CloudDBZone exceeds the limit.”

**解决措施**

出现此错误，表示AGC云端的存储区数量超过最大限制。

部署到AGC云端的存储区数量不得超过4个，否则会导致部署失败。如AGC云端当前已存在4个存储区，请将数据部署到已有的存储区，或者删除已有存储区后再部署新的存储区。

**需要注意的是，删除存储区，该存储区内的数据也将一并删除，且不可恢复。**

## 部署云数据库时，提示“clouddb deploy failed. Reason is existing fields cannot be modified.”

**问题现象**

部署云数据库失败，提示“clouddb deploy failed. Reason is existing fields cannot be modified.”

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/_XF95Zd7SvypxoirazIn_A/zh-cn_image_0000002179338656.png?HW-CC-KV=V1&HW-CC-Date=20260427T235508Z&HW-CC-Expire=86400&HW-CC-Sign=4702A5923F05788F72066D6AA27B4CF5147EA23AE99EC71CC006F59D5AF4D67D)

**解决措施**

出现此错误，可能是您在本地对象类型内做了与云端不兼容的修改。

对象类型中的fieldType等字段信息，部署到AGC云端后，请勿在本地再做修改。例如，fieldType设置为String，对象类型部署成功后，又在本地修改fieldType为Integer，再次部署将失败，提示“clouddb deploy failed. Reason is existing fields cannot be modified.”错误。如需更改fieldType等字段信息，请先删除云端部署的对象类型。

**需要注意的是，删除云端对象类型，对象类型内添加的数据也将一并删除，且不可恢复。**

## 体验端云一体化模板APP功能时，云存储上传图片失败，Hilog中打印“on response {"version":"HTTP/1.1","statusCode":403,"reason":"Forbidden","headers":{}}”

**问题现象**

体验端云一体化模板APP功能时，云存储上传图片失败，Hilog中打印“on response {"version":"HTTP/1.1","statusCode":403,"reason":"Forbidden","headers":{}}”。

**解决措施**

出现此错误，原因是访问权限不足，可采用以下任一方法解决：

* [将云存储的安全策略配置为始终可读写](agc-harmonyos-clouddev-emptyability.md#li1693311281068)
* 参考[AuthProvider](../harmonyos-references/cloudfoundation-cloudcommon.md#authprovider)获取用户凭据

## 体验端云一体化模板APP功能时，云数据库界面不展示数据，Hilog中打印“schemaJson\_ is empty”

**问题现象**

体验端云一体化模板APP功能时，云数据库界面不展示数据，Hilog中打印“schemaJson\_ is empty”。

**解决措施**

请检查resources/rawfile目录下是否存在schema文件。schema文件是云数据库功能依赖的必要文件，部署云数据库成功时会自动产生。如schema文件不存在，请重新部署云数据库，或[从AGC控制台导出](../AppGallery-connect-Guides/agc-clouddb-agcconsole-objecttypes-0000001127675459.md#section1558018208151)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/h-LMf01SQSiMhzCuolSTwQ/zh-cn_image_0000002179338664.png?HW-CC-KV=V1&HW-CC-Date=20260427T235508Z&HW-CC-Expire=86400&HW-CC-Sign=AF09A001E6F7045C3E8DD39ED3EE737ADA5927506C3502DA4422B03731A69B42)

## 云数据库无法新建数据条目，Hilog中打印“2001015:permission denied”

**问题现象**

云数据库无法新建数据条目，Hilog中打印“2001015:permission denied”。

**解决措施**

出现此错误，是因为APP操作者的角色权限不足，请检查[操作的对象类型的权限配置](agc-harmonyos-clouddev-objecttype.md#li01856582915)。

## 云函数调用失败，error message包含“404:160404:Trigger not exist”

**问题现象**

云函数调用失败，error message包含“404:160404:Trigger not exist”。

**解决措施**

出现此错误，是因为云函数未部署。error message中的404是服务端返回的HTTP状态码，表示找不到对应的函数。

## 云函数调用失败，error message包含“hmos auth app doesn't have permission”

**问题现象**

云函数调用失败，error message包含“hmos auth app doesn't have permission”。

**解决措施**

出现此错误，是因为选择的签名方式有误。推荐您使用[关联注册应用进行签名](ide-signing.md#section20943184413328)方式，或者使用[手动签名](ide-signing.md#section297715173233)。

## 云函数部署失败，提示“The function type cannot be changed”

**问题现象**

云函数部署失败，错误信息中提示“The function type cannot be changed”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/yN18Aum5RwqLuaU3uC752g/zh-cn_image_0000002214858977.png?HW-CC-KV=V1&HW-CC-Date=20260427T235508Z&HW-CC-Expire=86400&HW-CC-Sign=10030E317483ED64C4780EE805E87E9D4DB71FD28D7E0951D7A8AAAFF42EB092)

**解决措施**

出现此错误，是因为云函数分为传统云函数类型和云对象类型。一种类型的云函数在部署到AGC云端后，不允许再变更成另一种类型。您可以前往AGC控制台的云函数服务页面，手动删除之前已部署的同名云函数/云对象，然后重新在DevEco Studio执行部署操作。

## 部署云工程失败，提示“Remote host terminated the handshake”

**问题现象**

部署云工程失败，错误信息中提示“Remote host terminated the handshake”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/TfVw2-EeSDCtxxVt8bu_oA/zh-cn_image_0000002279650126.png?HW-CC-KV=V1&HW-CC-Date=20260427T235508Z&HW-CC-Expire=86400&HW-CC-Sign=96F51E281ABF251DB871223747176DA92B1076D76A8CC97EBA7AD3EFA39AFABA)

**解决措施**

出现此错误，是因为网络连接SSL/TLS握手失败。建议检查[DevEco Studio Proxy代理配置](ide-environment-config.md#section10369436568)或本地网络防火墙/安全配置。

## 在云函数中调用云函数失败，提示“mismatched authType”

**问题现象**

在云函数中调用云函数失败，错误信息中提示“mismatched authType”。

**解决措施**

出现此错误，是因为被调用的云函数的HTTP触发器的认证类型须配置为云侧网关认证，即“authType”字段须配置为“cloudgw-client”。修改被调用云函数的“function-config.json”文件中的“authType”字段值，然后重新部署被调用的云函数即可。

## 端云一体化开发工程同步失败，失败步骤为npm install failed

**问题现象**

端云一体化开发工程同步失败，失败步骤是npm install failed。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/fm-1gLpEQsSlEMnSe7m9Wg/zh-cn_image_0000002279546734.png?HW-CC-KV=V1&HW-CC-Date=20260427T235508Z&HW-CC-Expire=86400&HW-CC-Sign=BCD716468D4962EA432C58120DCF3103E846EF1C8D0CBE4800321EB22B1AFFA1)

**解决措施**

出现此错误，是因为端云一体化开发的云侧工程是通过npm管理依赖，同步时需要通过npm去下载对应依赖。请参考[配置NPM代理](ide-environment-config.md#section197296441787)检查npm代理和网络情况。

## 使用云存储上传文件失败，提示“404:Product does not exist”

**问题现象**

使用云存储上传文件失败，HiLog提示“404:Product does not exist”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/UJFq1FLaTj-N9cOr0IA2vQ/zh-cn_image_0000002214704601.png?HW-CC-KV=V1&HW-CC-Date=20260427T235508Z&HW-CC-Expire=86400&HW-CC-Sign=06ED8B63A6BDAB8E46C6C43B1B390647FE5E64C957B6344667EE01EC92147B8E)

**解决措施**

云存储服务端返回的错误，出现此错误是因为云存储服务未开通。请在顶部菜单栏选择“Tools > CloudDev”，进入CloudDev云开发管理面板，点击“Cloud Storage”服务下的“Go to console”快捷进入AGC服务菜单进行手动开通。

## 使用云存储上传文件失败，app日志提示“"state":65”，upload进程日志提示“403 Forbidden”

**问题现象**

使用云存储上传文件失败，出现如下错误提示：

* app日志提示“"state":65”

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/Z4KTCmtCTeu7YqLSjbjSXw/zh-cn_image_0000002179498352.png?HW-CC-KV=V1&HW-CC-Date=20260427T235508Z&HW-CC-Expire=86400&HW-CC-Sign=DB0212CFFF16B5E757259EBC4E2D859302EA68DD7A35A520F1E009C5B91A183D)
* upload进程的日志提示“403 Forbidden”（通过设置“No filters”模式、过滤“C01C50”关键字查找）

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/pfYTIjgVQFaMYgjx6yrOQA/zh-cn_image_0000002214858989.png?HW-CC-KV=V1&HW-CC-Date=20260427T235508Z&HW-CC-Expire=86400&HW-CC-Sign=929798CE1FB6D586FD759F4F49BBC53D864F69066A46316AA4991CDD83CCF905)

**解决措施**

出现此问题，可按照如下步骤排查和解决：

* 请确认应用的签名方式正确。当前支持[关联注册应用进行自动签名](ide-signing.md#section20943184413328)和[手动签名](ide-signing.md#section297715173233)两种方式。
* [将云存储的安全策略配置为始终可读写](agc-harmonyos-clouddev-emptyability.md#li1693311281068)
* 参考[AuthProvider](../harmonyos-references/cloudfoundation-cloudcommon.md#authprovider)获取用户凭据
