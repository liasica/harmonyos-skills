---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/deviceconfig-structure
title: deviceConfig内部结构
breadcrumb: 指南 > 基础入门 > 开发基础知识 > 应用配置文件（FA模型） > deviceConfig内部结构
category: harmonyos-guides
scraped_at: 2026-04-28T07:37:30+08:00
doc_updated_at: 2026-04-10
content_hash: sha256:467a2820da14a886ad8164838688fefcbe0484b44ff9fa13e11e39e7eace8239
---

deviceConfig 包含设备上的应用配置信息，支持 default、tv、car、wearable 等属性。

## deviceConfig对象内部结构

**表1** **deviceConfig对象内部结构说明**

| 属性名称 | 含义 | 数据类型 | 是否可缺省 |
| --- | --- | --- | --- |
| default | 配置为default类型的应用，虽然可以正常编译构建，但是不支持发布上架。建议使用phone替代。 | 对象 | 可缺省，缺省值为空。 |
| tablet | 标识平板特有的应用配置信息。 | 对象 | 可缺省，缺省值为空。 |
| tv | 标识智慧屏特有的应用配置信息。 | 对象 | 可缺省，缺省值为空。 |
| car | 标识车机特有的应用配置信息。 | 对象 | 可缺省，缺省值为空。 |
| wearable | 标识智能穿戴特有的应用配置信息。 | 对象 | 可缺省，缺省值为空。 |
| 2in1 | 标识PC设备，主要交互方式以多窗口、多任务及键盘鼠标操作为主，充分发挥设备的生产力属性。 | 对象 | 可缺省，缺省值为空。 |
| phone | 标识手机特有的应用配置信息。 | 对象 | 可缺省，缺省值为空。 |
| liteWearable | 标识运动手表特有的应用配置信息。 | 对象 | 可缺省，缺省值为空。 |

上表中各设备对象的内部结构说明参见[deviceConfig设备对象内部结构](deviceconfig-structure.md#deviceconfig设备对象内部结构)。

## deviceConfig设备对象内部结构

**表2** **deviceConfig设备对象内部结构说明**

| 属性名称 | 含义 | 数据类型 | 是否可缺省 |
| --- | --- | --- | --- |
| process | 标识应用或Ability的进程名。如果在deviceConfig标签下配置了process标签，则应用的所有Ability运行在此进程中。如果在abilities标签下为某个Ability配置了process标签，则该Ability运行在此进程中。该标签最大长度为31。 | 字符串 | 可缺省，缺省值为空。 |
| keepAlive | 标识应用是否始终保持运行状态，仅支持系统应用配置，三方应用配置不生效。  - true：应用始终保持为运行状态。系统启动时，该应用会被系统驱动起来。应用进程退出后，系统也会重新启动应用进程。  - false：应用不会始终保持为运行状态。系统启动时，该应用不会被系统驱动起来。应用进程退出后，系统不会重新启动应用进程。 | 布尔类型 | 可缺省，缺省值为false。 |
| supportBackup | 标识应用是否支持备份和恢复。  - true：该应用支持执行备份或恢复操作。  - false：该应用不支持执行备份或恢复操作。 | 布尔类型 | 可缺省，缺省值为false。 |
| compressNativeLibs | 该字段在打包HAP时标识libs库是否以压缩方式存储。  - true：libs库以压缩方式存储。  - false：libs库以不压缩方式存储。  在应用安装时，该字段用于标识libs库是否需要解压出来（API16及之后版本支持，之前的版本均默认解压libs库）。  - true：解压。  - false：不解压。 | 布尔类型 | 该标签可缺省。打包HAP时缺省值为false，安装应用时未配置则默认为true。 |
| network | 标识网络安全性配置。该标签允许应用通过配置文件的安全声明自定义其网络安全，无需修改应用代码。 | 对象 | 可缺省，缺省值为空。 |

## network对象内部结构

**表3** **network对象内部结构说明**

| 属性名称 | 含义 | 数据类型 | 是否可缺省 |
| --- | --- | --- | --- |
| cleartextTraffic | 标识是否允许应用使用明文网络流量（例如，明文HTTP）。  - true：允许应用使用明文流量的请求。  - false：拒绝应用使用明文流量的请求。 | 布尔类型 | 可缺省，缺省值为false。 |
| securityConfig | 标识应用的网络安全配置信息。 | 对象 | 可缺省，缺省为空。 |

## securityConfig对象内部结构

**表4** **securityConfig对象内部结构说明**

| 属性名称 | 含义 | 数据类型 | 是否可缺省 |
| --- | --- | --- | --- |
| domainSettings | 标识自定义域名范围的安全配置，支持多层嵌套。一个domainSettings对象中可嵌套更小域名范围的domainSettings对象。 | 对象类型 | 可缺省，缺省为空。 |

## domainSettings对象内部结构

**表5** **domainSettings对象内部结构说明**

| 属性名称 | 含义 | 数据类型 | 是否可缺省 |
| --- | --- | --- | --- |
| cleartextPermitted | 标识自定义域名范围内是否允许明文流量传输。cleartextTraffic和securityConfig同时存在时，以cleartextPermitted的值为准。  - true：允许明文流量传输。  - false：拒绝明文流量传输。 | 布尔类型 | 可缺省，缺省值为false。 |
| domains | 标识域名配置信息，包含两个参数：subdomains和name。  - subdomains：表示是否包含子域名。取值为"true"时，表示该规则将与相应域名及所有子域名（包括子域名的子域名）匹配；取值为"false"时，规则仅适用于精确匹配项。  - name：表示域名名称，为字符串类型。 | 对象数组 | 可缺省，缺省值为空。 |

以下是deviceConfig的示例：

```
1. "deviceConfig": {
2. "default": {
3. "process": "com.example.test.example",
4. "supportBackup": false,
5. "network": {
6. "cleartextTraffic": true,
7. "securityConfig": {
8. "domainSettings": {
9. "cleartextPermitted": true,
10. "domains": [
11. {
12. "subdomains": true,
13. "name": "example.ohos.com"
14. }
15. ]
16. }
17. }
18. }
19. }
20. }
```
