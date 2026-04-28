---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/agc-harmonyos-clouddev-createfunc
title: 创建并配置函数
breadcrumb: 指南 > 开发环境搭建 > 工程创建 > 模块管理 > 端云一体化开发 > 开发端云工程 > 开发云侧工程 > 开发云函数 > 创建并配置函数
category: harmonyos-guides
scraped_at: 2026-04-28T07:55:01+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:ee887f1a213f9c07f83b9ab485a362b889cd2d2820240df85e10fc0b93ee6f7f
---

您可直接在DevEco Studio创建函数、为函数配置调用的触发器等。

## 创建函数

1. 右击“cloudfunctions”目录，选择“New > Cloud Function”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/ybE6hSGZRxCnzFqJGdeChA/zh-cn_image_0000002383015060.png?HW-CC-KV=V1&HW-CC-Date=20260427T235500Z&HW-CC-Expire=86400&HW-CC-Sign=8A4B406CF27A8A96F231DB96B3AAB512F37B4C29F63C1B7FDB29B791E86CC9BF)
2. 在“Select the Cloud Function Type”栏选择“Cloud Function”，输入云函数名称（如“my-cloud-function”），点击“OK”。

   函数名称长度2-63个字符，仅支持小写英文字母、数字、中划线（-），首字符必须为小写字母，结尾不能为中划线（-）。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/JrmOaRbxQiu_jCJYmJmX3A/zh-cn_image_0000002214858969.png?HW-CC-KV=V1&HW-CC-Date=20260427T235500Z&HW-CC-Expire=86400&HW-CC-Sign=21630CDEA82A64EA8F6A7768D23179EC9C4873703309EC3537CF1EE6051E07BE)

   “cloudfunctions”目录下生成新建的“my-cloud-function”函数目录，目录下主要包含如下文件：

   * 函数配置文件“function-config.json”
   * 函数入口文件“myCloudFunction.ts”
   * 依赖配置文件“package.json”

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/qs7soCYzQ4qZ6O7E-lnoAg/zh-cn_image_0000002179338652.png?HW-CC-KV=V1&HW-CC-Date=20260427T235500Z&HW-CC-Expire=86400&HW-CC-Sign=7358F07FDB463B38B2285E7F9EE6B367FE7F76EECE3B23F8A8F073FC8C2559DF)

## 配置函数

函数创建完毕后，您可在配置文件“function-config.json”的“triggers”下配置触发器，通过触发器暴露的触发条件来实现函数调用。

说明

“functionType”表示函数类型，“0”表示云函数，“1”表示云对象。“functionType”的值为创建时自动生成，不可手动修改，否则将导致云函数部署失败。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/_2vjBy39STuV7Hn_VMQsWw/zh-cn_image_0000002296067548.png?HW-CC-KV=V1&HW-CC-Date=20260427T235500Z&HW-CC-Expire=86400&HW-CC-Sign=981832963A174B30371AEC00AC7511141C64A697EDD8826B06E2B6F828A6CCDC)

云函数当前仅支持HTTP触发器， “function-config.json”文件中已为您自动完成HTTP触发器配置。配置了HTTP触发器的函数被部署到云端后，您的应用即可通过Cloud Foundation Kit调用函数。关于如何使用HTTP触发器调用函数，请参见[调用函数](cloudfoundation-call-function.md)。

注意

如您需在函数部署完成后更新触发器，请先删除之前的触发器配置，再添加新的触发器配置，否则您的更新将不生效。

```
1. {
2. "type": "http",
3. "properties": {
4. "enableUrlDecode": true,
5. "authFlag": "true",
6. "authAlgor": "HDA-SYSTEM",
7. "authType": "apigw-client"
8. }
9. }
```

* type：触发器类型，配置为“http”。
* properties：触发器属性，属性参数如下表所示。

  | 参数 | 说明 |
  | --- | --- |
  | enableUrlDecode | 通过HTTP触发器触发函数时，对于contentType为“application/x-www-form-urlencoded”的触发请求，是否使用URLDecoder对请求body进行解码再转发到函数中。  + true：启用。 + false：不启用。 |
  | authFlag | 是否鉴权，默认为true。 |
  | authAlgor | 鉴权算法，默认为HDA-SYSTEM。 |
  | authType | HTTP触发器的认证类型。  + apigw-client：端侧网关认证，适用于来自APP客户端侧（即本地应用或者项目）的函数调用。 + cloudgw-client：云侧网关认证，适用于来自APP服务器侧（即云函数）的函数调用。 |
