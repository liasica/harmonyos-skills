---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-cloudfoundation-8
title: 云数据库服务器侧错误，报错代码1008231001
breadcrumb: FAQ > 应用服务开发 > 云开发服务（Cloud Foundation Kit） > 云数据库服务器侧错误，报错代码1008231001
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:52+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:93ab1f316b183d26d943664e527c628460322cd5b5f02dfb43d3e003eb280d73
---

## 问题现象

* 问题1:云数据库服务器侧报错：

  ```log
  Failed to sign in:code:1008231001,message:1006001:object type is not found.
  ```
* 问题2:云数据库使用真机调试时数据请求失败，错误代码：

  ```log
  code: 1008231001, message: 403:205525004:hmos auth app doesn't have permission.
  ```
* 问题3:云数据库使用异常，错误代码：

  ```log
  code:1008231001,message:1005000:the system status does not meet the operation execution conditions.
  ```

## 解决方案

* 问题1:对象类型不存在，在[AGC](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)上检查一下[操作步骤](../harmonyos-guides/cloudfoundation-database-add-object.md#操作步骤)对象类型列表中对象类型名字和代码中是否一致。
* 问题2:[云开发服务](../harmonyos-guides/cloud-foundation-kit-guide.md)所有Kit的认证鉴权仅支持手动签名的环境，需要将DevEco Studio自动签名改成[手动签名](../harmonyos-guides/ide-signing.md#section297715173233)保证云数据库正常访问。
* 问题3：该报错和加密字段有关，加密字段只允许sdk访问。若不需要使用加密字段需要删除表重新创建。
