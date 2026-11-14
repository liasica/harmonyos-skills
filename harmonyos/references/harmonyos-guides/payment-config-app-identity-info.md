---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/payment-config-app-identity-info
title: 端侧应用配置
breadcrumb: 指南 > 应用服务 > Payment Kit（鸿蒙支付服务） > 开发准备 > 端侧应用配置
category: harmonyos-guides
scraped_at: 2026-11-14T08:48:26+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:685b4e029d9e509977a9479a085fd2b1f9ec75ad1af10290ab84b5c78453c285
---

可下载并参考[示例代码-客户端](https://gitcode.com/HarmonyOS_Samples/payment-kit-sample-code-clientdemo-arkts)，以此来快速的完成商户端侧应用开发环境的构建。

通过下载示例代码或商户自行创建端侧应用后，需完成以下配置：

* 配置bundleName
* 配置应用属性

## 配置bundleName

在HarmonyOS应用/元服务“AppScope/app.json5”下的**bundleName**配置需要与开发者在[HarmonyOS 开发者中心](https://developer.huawei.com/consumer/cn/hdc-console)中[创建应用](../doccenter-getting-started/agc-help-create-app-0000002247955506.md)时的包名保持一致。

配置内容示例如下：

```json
{
  "app": {
    "bundleName": "com.huawei.******.******.demo",
  }
}
```

## 配置应用属性

在HarmonyOS应用/元服务“entry/src/main/module.json5”文件中**module**的**metadata**节点下增加**client\_id**和**app\_id**属性配置。

配置内容示例如下：

```json
{
    "module": {
        "metadata": [
            {
                "name": "app_id",
                "value": "..."
            },
            {
                "name": "client_id",
                "value": "..."
            },
        ]
    }
}
```

* 其中**app\_id**的value值为应用的APP ID（在[HarmonyOS 开发者中心](https://developer.huawei.com/consumer/cn/hdc-console)平台点击“开发者管理”，选择“ID、证书和Profile > APP ID”，在APP ID列表页面点击应用名称，进入应用详情页面，获取“APP ID”的值），详见下图的**标号1**处。
* 其中**client\_id**的value值为应用的OAuth 2.0客户端ID（在[HarmonyOS 开发者中心](https://developer.huawei.com/consumer/cn/hdc-console)平台“开发者管理”，选择“ID、证书和Profile > APP ID”，在APP ID列表页面点击应用名称，进入应用详情页面，获取“OAuth 2.0客户端ID（凭据）：Client ID”的值），详见下图的**标号2**处。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/-LsK0BLLQGyRepGzGfFmKA/zh-cn_image_0000002788308226.png?HW-CC-KV=V1&HW-CC-Date=20261114T004826Z&HW-CC-Expire=31536000000&HW-CC-Sign=42B4E18E7E805392283FAF0CFD036A7FFF1E6B0A6DB0852404BA0718316AEB4F)
