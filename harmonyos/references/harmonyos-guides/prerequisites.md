---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/prerequisites
title: 开发准备
breadcrumb: 指南 > 系统 > 安全 > User Authentication Kit（用户认证服务） > 开发准备
category: harmonyos-guides
scraped_at: 2026-11-12T09:51:41+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:365a9129dc23754337b8bd87659f29a852117824c7be303d8a61c91b73b8f700
---

应用在开发用户身份认证功能时，需要先了解以下流程，并根据实际需求参考对应指导开发。

* [查询设备支持的用户身份认证能力](obtain-supported-authentication-capabilities.md)。
* [发起身份认证请求，获取身份认证结果](start-authentication.md)。
* 校验和使用认证结果：请参考[通用密钥库二次认证密钥访问控制](huks-identity-authentication-overview.md)。
* （可选）[认证过程中取消认证](cancel-authentication.md)。
* （可选）[切换自定义认证](apply-custom-authentication.md)。

## 申请权限

在开发具备用户身份认证的应用前，需要先申请权限ohos.permission.ACCESS\_BIOMETRIC，应用才能使用生物特征识别能力（如人脸、指纹）进行身份认证。

该权限授权方式为system\_grant（系统授权），开发者只需要在module.json5配置文件的requestPermissions标签中声明权限，即可获取系统授权。具体声明指导请参考[申请应用权限-声明权限](declare-permissions.md)。

如需查询和订阅用户识别结果，需申请ohos.permission.ACCESS\_USER\_PASSIVE\_RECOGNITION，授权方式同为system\_grant。
