---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/agc-harmonyos-clouddev-faq
title: FAQ
breadcrumb: 指南 > 开发环境搭建 > 工程创建 > 模块管理 > 端云一体化开发 > FAQ
category: harmonyos-guides
scraped_at: 2026-04-29T13:45:05+08:00
doc_updated_at: 2026-04-22
content_hash: sha256:363af2b3c489a5218225e332a0416b7a46578dacdf7753d60be5d62fd89896da
---

## 使用DevEco Studio打开端云一体化项目文件夹，左侧的项目列表不显示云侧工程

**问题现象**

开发者使用DevEco Studio打开端云一体化项目文件夹，左侧的项目列表不显示云侧工程“CloudProgram”。

**解决措施**

端云一体化工程根目录下只允许有“Application”与“CloudProgram”文件夹，不能有其他文件。否则，DevEco Studio会把该工程当成纯端侧工程，不显示云侧工程“CloudProgram”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/P4-qhvCRQbuGLTMgs-nldQ/zh-cn_image_0000002313987669.png?HW-CC-KV=V1&HW-CC-Date=20260429T054505Z&HW-CC-Expire=86400&HW-CC-Sign=4AE44F458D639B5E0688932777A91B7C65F1277776C4002A8F92F97DF3D5E56D)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5/v3/POhFsOn_QN2dOGwpisvhHg/zh-cn_image_0000002179338656.png?HW-CC-KV=V1&HW-CC-Date=20260429T054505Z&HW-CC-Expire=86400&HW-CC-Sign=7CA657F9EEF21874D7690DA78BD27037D1C8A1502F2CBF67E79DCE6152FFB032)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/Gy1gsRPbSTO5tuwW0X_FzQ/zh-cn_image_0000002179338664.png?HW-CC-KV=V1&HW-CC-Date=20260429T054505Z&HW-CC-Expire=86400&HW-CC-Sign=7009B0A0190DAD7769E801A3457CC9AAFC9585B3E4C1203CE3D33D42EA0C1AEB)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/RM6YnZQpScGSwfxjlwX78A/zh-cn_image_0000002214858977.png?HW-CC-KV=V1&HW-CC-Date=20260429T054505Z&HW-CC-Expire=86400&HW-CC-Sign=0B1F7A66367382CE11AD91679018882C0AB1DD3057F8C238E6DC654E314FB19C)

**解决措施**

出现此错误，是因为云函数分为传统云函数类型和云对象类型。一种类型的云函数在部署到AGC云端后，不允许再变更成另一种类型。您可以前往AGC控制台的云函数服务页面，手动删除之前已部署的同名云函数/云对象，然后重新在DevEco Studio执行部署操作。

## 部署云工程失败，提示“Remote host terminated the handshake”

**问题现象**

部署云工程失败，错误信息中提示“Remote host terminated the handshake”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/vsc1-a_xRgOC3-eBUKxMgw/zh-cn_image_0000002279650126.png?HW-CC-KV=V1&HW-CC-Date=20260429T054505Z&HW-CC-Expire=86400&HW-CC-Sign=92B9CF8E51958F19AA3E5A36B21F81275ADA74A77C7A6794595E7CFD45B21D95)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/k8Q2DHzaRGOLoiEX_9_DzA/zh-cn_image_0000002279546734.png?HW-CC-KV=V1&HW-CC-Date=20260429T054505Z&HW-CC-Expire=86400&HW-CC-Sign=8BB1E66FDF3425E874562399F2BA3D700C8BF428233456769B56E0EFE2FF1DC2)

**解决措施**

出现此错误，是因为端云一体化开发的云侧工程是通过npm管理依赖，同步时需要通过npm去下载对应依赖。请参考[配置NPM代理](ide-environment-config.md#section197296441787)检查npm代理和网络情况。

## 使用云存储上传文件失败，提示“404:Product does not exist”

**问题现象**

使用云存储上传文件失败，HiLog提示“404:Product does not exist”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/y8b3KPjSQ--DWMqmwVWBKw/zh-cn_image_0000002214704601.png?HW-CC-KV=V1&HW-CC-Date=20260429T054505Z&HW-CC-Expire=86400&HW-CC-Sign=0A35C5ADE1C62B071F4D9AEA4CEB9B3E817E3289B5B06084D917D9FF5BEACC4B)

**解决措施**

云存储服务端返回的错误，出现此错误是因为云存储服务未开通。请在顶部菜单栏选择“Tools > CloudDev”，进入CloudDev云开发管理面板，点击“Cloud Storage”服务下的“Go to console”快捷进入AGC服务菜单进行手动开通。

## 使用云存储上传文件失败，app日志提示“"state":65”，upload进程日志提示“403 Forbidden”

**问题现象**

使用云存储上传文件失败，出现如下错误提示：

* app日志提示“"state":65”

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/012zgRPPSyeJFZx_cYuvzA/zh-cn_image_0000002179498352.png?HW-CC-KV=V1&HW-CC-Date=20260429T054505Z&HW-CC-Expire=86400&HW-CC-Sign=93A2452F2825769159A6CCC3096BD55D0D3014189A98383836B595141F722BCF)
* upload进程的日志提示“403 Forbidden”（通过设置“No filters”模式、过滤“C01C50”关键字查找）

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/qqYFL4O-Sm6gcFA-62EwcQ/zh-cn_image_0000002214858989.png?HW-CC-KV=V1&HW-CC-Date=20260429T054505Z&HW-CC-Expire=86400&HW-CC-Sign=9A40AA4C56BEEBEBEC4DD65F53BAB89C8F0EC023C2C6F2662D657FBDCE176BDA)

**解决措施**

出现此问题，可按照如下步骤排查和解决：

* 请确认应用的签名方式正确。当前支持[关联注册应用进行自动签名](ide-signing.md#section20943184413328)和[手动签名](ide-signing.md#section297715173233)两种方式。
* [将云存储的安全策略配置为始终可读写](agc-harmonyos-clouddev-emptyability.md#li1693311281068)
* 参考[AuthProvider](../harmonyos-references/cloudfoundation-cloudcommon.md#authprovider)获取用户凭据
