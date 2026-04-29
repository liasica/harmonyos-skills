---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/agc-pac
title: pac.json5隐私清单文件
breadcrumb: 指南 > 编写与调试应用 > 附录 > pac.json5隐私清单文件
category: harmonyos-guides
scraped_at: 2026-04-29T13:47:07+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:5c99f30c669abe840a6fa6e3fce68678a8590d67131be8f264187fee6477989c
---

## 概述

若您开发App，您在AppGallery Connect上架应用时需要提供应用的隐私标签，建议您在项目工程中创建pac.json5配置文件，在文件中声明处理的个人数据类型、使用目的等信息。编译构建时，如您集成的HSP/HAR中的pac.json5同步声明了隐私保护信息，信息将自动汇总至此文件并随软件打包，上架时AppGallery Connect可基于此文件内容自动生成隐私标签。

若您开发HSP或HAR，为了下游集成使用软件的开发者快速、准确地了解HSP或HAR处理个人数据的情况，建议您在项目工程中创建pac.json5配置文件，在文件中声明处理的个人数据类型、使用目的等信息。文件在编译构建时会合入软件包，隐私保护信息将随软件包同步传递给下游的开发者。

说明

支持版本：DevEco Studio 6.0.0 Beta2及以上版本。

## 创建pac.json5文件

* 开发App情况下，选中AppScope目录新建pac.json5文件。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/OCpnjSCQT--SFcpxy3iQpg/zh-cn_image_0000002530912976.png?HW-CC-KV=V1&HW-CC-Date=20260429T054706Z&HW-CC-Expire=86400&HW-CC-Sign=F7287781D74DB3D93D8924EBCA39370A0794EBD36FD3024940C6D2C720A71861)

* 开发HSP或HAR情况下，选中HSP或HAR模块目录新建pac.json5文件。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/fJ_Llc3mTWmkWiVp4PhcYQ/zh-cn_image_0000002530752982.png?HW-CC-KV=V1&HW-CC-Date=20260429T054706Z&HW-CC-Expire=86400&HW-CC-Sign=91BFC5C49A67CDA3E99A9B6119343B1285D26A1C06A11DB9BA6C354B1DAB8DDB)

## 配置文件结构

pac.json5隐私清单文件整体的结构如下。

```
1. dataProcess
2. └── dataType
3. └── dataLabels
4. └── label
5. └── purposes
6. └── userLinked
7. └── tracking
8. specialAPIs
9. └── apiType
10. └── reasons
```

## 配置文件字段说明

pac.json5隐私清单配置文件包括以下字段。

**表1** pac.json5隐私清单文件字段说明

| 字段名称 | 可选/必选 | 类型 | 含义 |
| --- | --- | --- | --- |
| [dataProcess](agc-pac.md#section82051543115414) | 可选 | 数组 | 声明应用收集的个人数据。 |
| [specialAPIs](agc-pac.md#section26881432131216) | 可选 | 数组 | 声明应用调用的可用于生成设备指纹的API信息。 |

说明

dataProcess和specialAPIs不能同时为空。

## dataProcess

dataProcess是声明应用收集的个人数据，包括数据类型、数据项和使用目的。

**表2** dataProcess

| 字段名称 | 可选/必选 | 类型 | 含义 |
| --- | --- | --- | --- |
| [dataType](agc-pac.md#table176277269236) | 必选 | 字符串 | 应用收集个人数据的类型。 |
| [dataLabels](agc-pac.md#section13345163017127) | 必选 | 数组 | 应用收集的个人数据项和目的。 |

**表3** dataType

| 数据类型 | 含义 |
| --- | --- |
| Identifiers | 标识符 |
| Financial information | 财务信息 |
| Basic information | 基本资料 |
| Transaction information | 交易信息 |
| Contact information | 联系人信息 |
| Special category data | 敏感信息 |
| Device information | 设备信息 |
| Location information | 位置信息 |
| App information | 应用信息 |
| User content | 用户内容 |
| Fitness and health information | 运动健康信息 |
| Other personal data | 其他个人数据 |

### dataLabels

dataLabels是声明应用收集的个人数据项和目的。

**表4** dataLabels

| 字段名称 | 可选/必选 | 类型 | 含义 |
| --- | --- | --- | --- |
| [label](agc-pac.md#table202051420105216) | 必选 | 字符串 | 应用收集的个人数据项。 |
| [purposes](agc-pac.md#table1292433153213) | 必选 | 数组 | 应用收集个人数据的目的。 |
| userLinked | 可选 | 布尔 | 应用收集的个人数据是否用于用户关联。 |
| tracking | 可选 | 布尔 | 应用收集的个人数据是否用于用户追踪。 |

**表5** label

| 个人数据项 | 含义 | 数据类型 |
| --- | --- | --- |
| ICCID | ICCID | Identifiers |
| IMEI | IMEI |
| IMSI | IMSI |
| MAC | MAC |
| MEID | MEID |
| OAID | OAID |
| SN | SN |
| Chip ID | Chip ID |
| ODID | ODID |
| SSID | SSID |
| BSSID | BSSID |
| Other device identifiers | 其他设备标识符 |
| ID card | 身份证 |
| Other identity information | 其他身份信息 |
| User identifiers | 用户标识符 |
| Bank account information | 银行账户信息 | Financial information |
| Other financial account information | 其他金融账户信息 |
| Asset information | 资产信息 |
| Other financial information | 其他账务信息 |
| Name | 姓名 | Basic information |
| Gender | 性别 |
| Age | 年龄 |
| Date of birth | 出生日期 |
| Account information | 账号信息 |
| Education information | 教育信息 |
| Work information | 工作信息 |
| Home information | 家庭信息 |
| Address | 地址 |
| Phone number | 电话号码 |
| Email address | 电子邮件地址 |
| Calendar and schedule | 日历 |
| Other personal information | 其他个人资料 |
| Order information | 订单信息 | Transaction information |
| Transaction records | 交易记录 |
| Package delivery information | 快递信息 |
| Other transaction information | 其他交易信息 |
| Contact list | 联系人列表 | Contact information |
| Social media accounts | 社交帐号 |
| Other contact information | 其他联系人信息 |
| Facial recognition features | 面部识别特征 | Special category data |
| Voiceprint information | 声纹 |
| Other biometric features | 其他生物特征 |
| Other special category data | 其他敏感信息 |
| Magnetometer | 磁力计信息 | Device information |
| Light sensor | 光照传感器 |
| Acceleration sensor | 加速器数据 |
| Screen orientation sensor | 屏幕方向传感器 |
| Barometer | 气压计 |
| Gyroscope | 陀螺仪数据 |
| Rotation vector sensor | 旋转矢量传感器信息 |
| Gravity sensor | 重力传感器信息 |
| OS information | 操作系统信息 |
| Other hardware and software parameters/System settings | 其他软硬件参数/系统设置 |
| Device status | 设备状态 |
| IP address | IP地址 |
| Wi-Fi parameters | WiFi参数 |
| Wi-Fi status | WiFi状态 |
| Network type | 网络类型 |
| Carrier | 运营商 |
| Other device information | 其他设备信息 |
| Network location | 网络位置 | Location information |
| Other approximate location information | 其他大致位置信息 |
| GPS location | GPS位置 |
| Other precise location information | 其他精确位置信息 |
| Browsing history | 浏览记录 | App information |
| Favorites | 收藏记录 |
| Basic app information | 应用基本信息 |
| App settings | 应用设置信息 |
| App running status | 应用运行状态 |
| App run logs | 应用运行日志 |
| App usage information | 其他使用应用的信息 |
| SMS messages | 短信 | User content |
| Call logs | 通话记录 |
| Other communication content | 其他通讯内容 |
| Image or video | 图片或视频 |
| Audio recording | 录音 |
| Audio | 音频 |
| Text information | 文字信息 |
| Search keywords | 搜索词 |
| Social interactions | 社交互动 |
| Game statistics | 游戏数据 |
| Customer service records | 客户支持 |
| Pasteboard | 剪切板 |
| Software installation list | 软件安装列表 |
| Other user content | 其他用户内容 |
| Heart rate | 心率 | Fitness and health information |
| Blood pressure | 血压 |
| Other health information | 其他健康信息 |
| Fitness information | 运动信息 |
| Other personal data | 其他个人数据 | Other personal data |

**表6** purposes

| 个人数据收集的目的 | 目的详细描述 |
| --- | --- |
| App functionality | 应用提供基本功能、安全防护功能、确保应用正常运营以及客户支持。 |
| Product personalization | 按照不同用户差异化呈现应用内容。 |
| Analytics | 评估用户行为，了解现有产品功能的效果、进行服务改进。 |
| Advertising and marketing | 用于在应用中显示广告或营销信息的数据。 |
| Disclosure to third parties | 将数据共享至第三方运营主体，目的包括但不限于：共享至物流公司用于物品邮件、共享至第三方用于广告投放效果评估、共享至第三方进行数据展示、评测/评估、研究、合作双方对账、由第三方提供运营、运维服务、论坛、社交等服务中公开披露。 |
| Cross-border transfer | 数据跨境传输。 |
| Others | 用于未列出的其他用途。 |

## specialAPIs

specialAPIs是声明应用调用的可用于生成设备指纹的API信息，包含API类型和调用原因。

**表7** specialAPIs

| 字段名称 | 可选/必选 | 类型 | 含义 |
| --- | --- | --- | --- |
| [apiType](agc-pac.md#table53349541435) | 必选 | 字符串 | API类型 |
| [reasons](agc-pac.md#table178321910193719) | 必选 | 数组 | API调用原因 |

**表8** apiType

| API类型 | API介绍 | API列表 |
| --- | --- | --- |
| File timestamp APIs | 用于获取文件的创建、修改或访问时间戳，有助于管理文件和数据同步。 | ctime  mtime  fs.getxattr  fs.getxattrSync  fs.stat  file.get  fs.lstat  cloudStorage.bucket().getMetadata |
| System boot time APIs | 提供系统启动时间信息，常用于计算系统运行时长或在系统重启后保持应用状态。 | systemDateTime.getUptime |
| Disk space APIs | 用于检测磁盘空间，有助于管理存储资源，例如在空间不足时提醒用户或优化数据存储。 | statvfs.getFreeSize  statvfs.getTotalSize |
| Active keyboard APIs | 用于检测当前激活的键盘，常用于提供上下文相关的输入体验或支持多语言输入。 | inputDevice.getKeyboardType |
| User preferences APIs | 用于存储和检索用户首选项，如应用配置或最近使用的项目，有助于提高用户体验和应用的个性化。 | preferences.getPreferences  sendablePreferences.getPreferences |

**表9** reasons

| API调用原因 | 目的详细描述 | API类型 |
| --- | --- | --- |
| Display to user on-device | 用于向用户显示文件的时间戳，如文件的创建、修改和访问时间。 | File timestamp APIs |
| Access file metadata in-app | 用于访问应用容器内或云存储（Cloud Foundation Kit）中文件的时间戳、大小或其他元数据。 |
| Files provided to app by user | 用于访问用户授权文件或目录的时间戳、大小或其他元数据。 |
| 3rd-party SDK wrapper on-device | 用于应用调用第三方SDK提供的文件时间戳封装函数。 |
| Measure time on-device | 用于计算应用内事件之间经过的时间，或通过时间计算实现定时器。 | System boot time APIs |
| Calculate timestamp for in-app event | 用于计算应用内事件的绝对时间戳。 |
| User-initiated bug report | 用于在用户主动提交的诊断报告中记录系统启动时间。 |
| Display to user on-device | 用于向用户显示磁盘空间信息。 | Disk space APIs |
| Write or delete file on-device | 用于写文件前检查磁盘空间是否充足，或检查到磁盘空间不足时触发垃圾文件清理。 |
| User-initiated bug report | 用于在用户主动提交的诊断报告中记录磁盘空间信息。 |
| Health research app | 用于检测是否有足够的磁盘空间存储应用收集的健康数据。 |
| Custom keyboard app on-device | 用于自定义键盘类应用检查当前设备激活的键盘。 | Active keyboard APIs |
| Customized UI on-device | 用于根据激活键盘状态向用户呈现正确的定制化UI界面。 |
| Access preferences data in-app | 用于访问仅限本应用读写的用户首选项配置信息。 | User preferences APIs |
| 3rd-party SDK wrapper on-device | 用于应用调用第三方SDK提供的用户首选项（Preference API）封装函数。 |

## pac.json5文件示例

```
1. {
2. "dataProcess": [
3. {
4. "dataType": "Identifiers",
5. "dataLabels": [
6. {
7. "label": "MAC",
8. "purposes": ["App functionality"],
9. "userLinked": true,
10. "tracking": true
11. }
12. ]
13. }
14. ],
15. "specialAPIs": [
16. {
17. "apiType": "File timestamp APIs",
18. "reasons": ["Display to user on-device","Access file metadata in-app"]
19. }
20. ]
21. }
```
