---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-appgallery-80
title: In-house应用发布指导和常见问题分析
breadcrumb: FAQ > 应用服务开发 > 应用市场服务（AppGallery Kit） > In-house应用发布指导和常见问题分析
category: harmonyos-faqs
scraped_at: 2026-09-02T15:04:30+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:6e92514099b8818d1ad9f0b4e707a05708ff6242764fba167aab0f12349376a6
---

## 问题现象

一般来讲，HarmonyOS应用需要上架应用市场才可以进行安装。对于仅在企业内部分发的应用，如何实现不上架应用市场也能分发？

## 背景知识

[发布In-house应用](../app/agc-help-inhouse-0000002281532696.md)不属于标准的发布方案，仅允许部分特殊场景的开发者申请。

通过此方式分发，必须使用专用的组织内部发布证书和组织内部发布Profile来编译打包HarmonyOS应用，然后将应用包及应用描述文件上传到您的服务器或第三方云上，用户按指定方式直接下载安装即可。

**说明** 

使用In-house发布前，您需要分别完成账号和应用权限申请。我们将审核贵公司提交的申请信息，并确认非公开发布、定向应用发布、指定设备发布均无法满足您的需求。根据您提交的企业资质和申请理由，华为应用市场保留拒绝您申请的权利。

## 解决方案

1. 完成账号的注册和实名认证，获取分发资格。详细的操作步骤可参考[准备工作](../app/agc-help-inhouse-0000002281532696.md#section6267104872410)。

   **说明** 

   为避免权限冲突，需要重新申请In-house账号，不可与用于上架应用市场的普通开发者账号混用。

   In-house账号用于调试或发布In-house应用，不可用于调试或发布需上架华为应用市场的应用。
2. 申请[In-house发布证书](../app/agc-help-inhouse-cert-0000002248337770.md)和[In-house发布Profile](../app/agc-help-inhouse-profile-0000002283340021.md)。
3. [编译打包应用](../app/agc-help-inhouse-0000002281532696.md#section16967123194110)。

   **说明** 

   In-house应用仅支持编译HAP和应用内HSP包。
4. [构建Deeplink实现下载应用](../app/agc-help-inhouse-0000002281532696.md#section74503017418)。
   * 将编译得到的各个HAP/HSP包上传至您的服务器或第三方云上，获取HAP/HSP包下载URL，下载URL建议以“https”开头。
   * 基于应用信息生成应用描述文件。
   * 将生成的应用描述文件上传至您的服务器或第三方云上，并获取该文件的下载URL。
   * 将应用描述文件URL构建成Deeplink用于下载应用。

     **说明** 

     Deeplink仅支持页面点击行为触发拉起，不支持地址栏输入Deeplink拉起或HTML头文件自动拉起。

     仅支持华为浏览器拉起，且从华为浏览器拉起的所有行为，均需判断是否有用户点击行为，确认用户点击才允许拉起。

     Deeplink格式：store://enterprise/manifest?url=https://xxx.xxx/xxx.json5。
   * 服务器提供应用描述文件和安装包的https下载链接，并且下载链接中的域名不支持IP地址。
   * 应用描述文件和安装包的下载链接，均需要支持通过HEAD方式请求返回文件大小。
   * 自签证书需安装对应的CA证书，且有效期不超过13个月，超期请及时更换。
   * 服务器需支持分片下载能力。

5. 使用过程中可以参考[下载错误码](../app/agc-help-inhouse-0000002281532696.md#section13508931122415)和[安装错误码](../app/agc-help-inhouse-0000002281532696.md#section1569344319598)进行问题分析。

## 常见FAQ

Q：应用无法安装，提示：安装包解析失败，无法验证应用。请联系开发者获取更多帮助（错误码：99999），如何排查？

A：可以通过以下两点进行分析：

1. 检查描述文件的JSON格式是否有误，确保文件内容是JSON格式，无额外字符或者字段。
2. 检查packageHash值是否正确，确保使用certutil -hashfile PATH SHA256获取，其中PATH表示包路径。

Q：In-house应用，已配置icons链接，为什么下载的时候显示还是默认图标？

A：描述文件中的icons字段中两个图标字段"normal"和"large"链接需一致，且需要以https开头。

Q：In-house应用在编译构建HAP时能否将多个module打包到HAP包中？

A：如果这些module的构建产物是HAP或HSP包，则无法将它们打包进同一个HAP包中。需要单独编译成HAP或HSP包，然后分别配置下载链接、生成应用描述文件并上传至服务器。如果module是har模块，编译时会被应用直接打入包体中，不需要单独编译发布。

Q：在In-house的描述文件和[指定设备发布](../app/agc-help-internal-test-0000002270709477.md)描述文件有什么区别，其中的sign（描述文件签名）字段是否需要配置？

A：In-house的描述文件和指定设备发布的描述文件配置项基本一致。但指定设备发布必须要配置sign（描述文件签名）字段，不配置应用无法下载安装。In-house发布描述文件中sign字段是可选的，不配置不会影响应用下载安装。

Q：In-house应用安装报错：提示无法验证，需要联网验证才可运行。日志信息：{"rtnDesc":"TSMS ts verify failed.","rtnCode":636001}，是什么原因？

A：时间未同步导致。证书验证时，需要确保客户端本地时间和服务器时间同步，才可以验证安装。
