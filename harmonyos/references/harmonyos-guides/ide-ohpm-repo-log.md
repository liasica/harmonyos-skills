---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-repo-log
title: 日志
breadcrumb: 指南 > 开发环境搭建 > 工程创建 > 模块管理 > ohpm-repo私仓搭建工具 > 日志
category: harmonyos-guides
scraped_at: 2026-04-29T13:44:37+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:1300981ed8a99fa70120761ed21d708cfec0b5ae2100aefcef6bb138dbd75300
---

与任何web应用程序相同，ohpm-repo有一个内置的日志记录器，其定义了四种日志类型。

## 访问日志 - access.log

访问日志中主要包含操作时间、服务器IP、操作源、操作结果以及请求接口或者请求静态资源，其文件保存个数最多为180个。

## 操作日志 - operate.log

操作日志中主要包含操作时间、日志级别、操作人id（userId）、终端IP（ip）、操作资源（resource）、操作方法名（event）以及操作结果（result），其文件保存个数最多为180个。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/04/v3/pTLiwWtlSR2drnEmUMw_1g/zh-cn_image_0000002561751223.png?HW-CC-KV=V1&HW-CC-Date=20260429T054436Z&HW-CC-Expire=86400&HW-CC-Sign=07B084A6BE17A57A42A99110825E65749E847D2C8BBC84C4AE33348A08F1C6A1 "点击放大")

说明

**操作方法名(event)**： 当在ohpm-repo管理界面执行一系列操作时，会在operate.log文件生成一条条操作数据，操作方法名即表示当前操作涉及到的方法名字，例如login即表示登录操作，analyzePackage即表示上传包时对包的解析操作。

**表1** 常用操作方法说明

| 序号 | Event描述 | 说明 |
| --- | --- | --- |
| 1 | generateAccessToken / deleteAccessToken | 生成 / 删除AccessToken |
| 2 | login / logout | 登入 / 登出 |
| 3 | publish / unPublish/batchUnPublish | 上架资源包/ 下架资源包/批量下架资源包 |
| 4 | addGroup / deleteGroup | 添加/删除组织 |
| 5 | updateGroup | 更新组织 |
| 6 | addMember/deleteMember | 添加 / 删除组织成员 |
| 7 | addAdminMember/deleteAdminMember | 添加/删除组织管理员 |
| 8 | addPublicKey / delPublicKeyById | 添加 / 删除发布公钥 |
| 9 | addRepo/updateRepo/deleteRepo | 新增仓库/更新仓库/删除仓库 |
| 10 | analyzePackage | 解析上传的包文件 |
| 11 | uploadPackage | 上传包文件 |
| 12 | getPackageSizeLimit | 获取包的大小限制 |
| 13 | addUplink / deleteUplink | 添加 / 删除uplink |
| 14 | updateUplink | 更新uplink |
| 15 | updateUplinkProxy | 更新Uplink代理 |
| 16 | addUser / delUserByUserId | 添加/删除用户 |
| 17 | changePassWord | 改变用户账户密码 |
| 18 | resetPassWord | 重置用户账户密码 |
| 19 | changeRole | 修改用户角色(管理员和非管理员) |
| 20 | register | 注册账户 |
| 21 | resetKey | 重置系统密钥 |
| 22 | addPackagePermissionOwner/deletePackagePermissionOwner/transferPackagePermissionOwner | 新增/删除/转移包所有者 |
| 23 | addPackagePermissionMaintainer/deletePackagePermissionMaintainer | 新增/删除包维护者 |
| 24 | addPackagePermissionVisitor/deletePackagePermissionVisitor | 新增/删除包白名单用户 |
| 25 | editPackageReadPolicy | 编辑包可见性 |

## 运行日志 - run.log

运行日志中主要包含操作时间、日志级别以及日志信息，其文件保存个数最多为30个。运行日志定义了日志级别：all，trace，debug，info，warn，error，fatal，mark和off。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/Auc88Vh3SWS1aldLwbGefg/zh-cn_image_0000002530751280.png?HW-CC-KV=V1&HW-CC-Date=20260429T054436Z&HW-CC-Expire=86400&HW-CC-Sign=0D30FCF8CBF22D4949ED112835BD6CC891F9BA270B5B8A5FD7CD64D64D104AB7 "点击放大")

## 运行错误日志 - repoError.log

当ohpm-repo在运行过程中，所有run.log中生成的error日志都会打印到repoError.log中，是error日志的集合，日志打印级别与run.log日志保持一致。

## 下载错误日志

当从仓库中下载某个包失败时，仓库会生成一条错误日志记录在数据库中的downloadfailure 表中，当为ohpm-repo配置了sftp存储服务时，从任意一个sftp服务中下载失败时，都会生成一条错误日志并保存。每条日志都有handled标识，handled为0时表示已处理，handled为1时表示未处理。

## 日志存储路径

日志存储的默认路径为./logs，相对路径基准为ohpm-repo部署根目录[deploy\_root](ide-ohpm-repo-configuration.md#zh-cn_topic_0000001745376470_关于-deploy_root)。

## 日志打印级别

在配置文件中可以设置访问、操作、运行日志的打印级别，日志将会只打印不低于设置级别的日志，日志级别由低到高为：all，trace，debug，info，warn，error，fatal，mark和off。

```
1. loglevel_run: info
2. loglevel_operate: info
3. loglevel_access: info
```
