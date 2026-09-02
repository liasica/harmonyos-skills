---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cloudfoundation-storage-config
title: 设置云存储配置项
breadcrumb: 指南 > 应用服务 > Cloud Foundation Kit（云开发服务） > 云存储 > 设置云存储配置项
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:25+08:00
doc_updated_at: 2026-09-01
content_hash: sha256:6c39f15d1536f9304baffe4d1dca55e7bb2f969ed2642bda77cc6927e9cb1469
---

## 约束与限制

支持Phone、Tablet设备。并且从5.1.0(18)版本开始，新增支持Wearable设备；从5.1.1(19)版本开始，新增支持TV设备；从6.1.0(23)版本开始，新增支持PC/2in1设备。

## 操作步骤

1. 在“entry/src/main/module.json5”文件中添加网络权限。

   ```typescript
   "requestPermissions": [
     {
       "name": "ohos.permission.INTERNET"
     }
   ]
   ```
2. （可选）如果存在需要登录应用才能使用云存储的场景（如上传下载文件），您需要执行如下操作：

   1. [通过AuthProvider获取用户凭据](../harmonyos-references/cloudfoundation-cloudcommon.md#authprovider)。
   2. 调用[init()](../harmonyos-references/cloudfoundation-cloudcommon.md#init)方法进行初始化时，传入获取的凭据。
3. （可选）自定义初始化参数。

   如开发者需要自定义云存储接口使用的网络类型或任务模式等初始化参数，可参考如下配置：

   1. 导入相关模块。

      ```typescript
      import { cloudCommon } from '@kit.CloudFoundationKit';
      import { request } from '@kit.BasicServicesKit';
      ```
   2. 通过[StorageOptions.network](../harmonyos-references/cloudfoundation-cloudcommon.md#storageoptions)配置云存储接口使用的网络类型，不配置则使用默认值request.agent.Network.ANY；通过[StorageOptions.mode](../harmonyos-references/cloudfoundation-cloudcommon.md#storageoptions)配置云存储上传下载任务的工作模式，不配置则使用默认值request.agent.Mode.BACKGROUND。

      ```typescript
      cloudCommon.init({
        storageOptions: {
          network: request.agent.Network.WIFI,
          mode: request.agent.Mode.FOREGROUND
        }
      });
      ```
