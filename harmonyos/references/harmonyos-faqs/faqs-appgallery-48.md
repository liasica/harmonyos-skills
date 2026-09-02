---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-appgallery-48
title: 如何接入AGC应用性能监测服务（含崩溃服务）
breadcrumb: FAQ > 应用服务开发 > 应用市场服务（AppGallery Kit） > 如何接入AGC应用性能监测服务（含崩溃服务）
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:51+08:00
doc_updated_at: 2026-07-24
content_hash: sha256:9b246962945ccf1f45bee88a9e384d0dddd7fa209d2ceee26f440eca73588959
---

## 问题现象

性能管理服务是否实现崩溃日志堆栈信息上报收集功能？怎么在AGC平台上开通应用性能管理服务，方便应用崩溃时日志的查看和问题定位。

## 背景知识

崩溃服务已经合并至性能管理服务，该服务提供了与友盟/bugly等平台类似的崩溃日志上报收集功能。

应用性能管理服务（Application Performance Management Service，简称APMS）是AppGallery Connect（简称AGC）向开发者提供的一个现网质量监测解决方案。

应用性能管理服务能帮助您监测现网应用的崩溃（CPP CRASH、JS ERROR）、应用无响应（AppFreeze）等稳定性指标，以及应用的启动、页面加载、耗电等性能指标。它提供每个问题发生时的环境信息、堆栈信息等分析数据，并支持基于堆栈关键行进行准确的同类异常汇聚，让您轻松准确快速发现、识别、定位和解决问题。它还支持问题标记、指标告警等辅助能力，帮助您更高效的监测、处理质量问题。

## 解决方案

2025年4月9日前，创建且从未使用过APMS服务的存量应用，可通过更新【应用信息】的方式完成服务开通，刷新应用具体方法：登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html#/)进入“APP与元服务”，选择需要开启APMS服务的应用，在“应用信息”-“可本地化基础信息”中修改应用名称，点击右上角“保存”，再修改回原应用名。

2025年4月9日后，创建应用后，AGC将为应用自动开通APMS服务。创建应用可参考[AGC控制台配置](../AppGallery-connect-Guides/agc-cloudstorage-console-0000001275489978.md)。

接入APMS后，系统会自动收集到应用的性能数据，开发者可以根据堆栈信息进行问题的原因分析和修复，详情可以参考以下文档：

APMS指导文档可以参考：APMS[业务介绍](../app/agc-help-apms-introduction-0000002236333914.md)。

APMS崩溃相关可以参考：[异常管理](../app/agc-help-apms-crash-0000002577579282.md)。

## 常见FAQ

Q：如何能根据用户进行查找呢，比如怎么自定义userId或者tag，包括怎么区分测试版本和正式版本。

A：当前不能自定义userId或者tag的，测试版本和正式版本可以通过应用版本号区分出来。

Q：AGC崩溃服务无法采集数据。

A：检查应用在端侧安装是否连接网络，需要连接网络产生崩溃才会上传。

Q：崩溃服务和性能管理服务是否收费。

A：当前免费使用，主要功能是异常问题的监测，统计，日志和堆栈获取；性能问题的监测，统计。

Q：在华为应用上架后台，新开通了崩溃分析服务，提示需要更新文件agconnect-services.json，这个文件如果发现变化，会对项目哪些配置产生影响？

A：在AGC开启质量崩溃服务之后，无需在项目里面集成任何代码。

Q：在APMS服务中符号表如何获取，是否可以通过接口上传符号表？

A：

1. 获取符号表：release模式编译后，符号表位置：{ProjectPath}/{ModuleName}/build/{product}/cache/default/default@CompileArkTS/esmodule/release/sourceMaps.map，具体参考：[ArkTS调试产物sourcemap](../harmonyos-guides/ide-exception-stack-parsing-principle.md#section666114451518)。
2. APMS服务中符号表上传暂未开通接口方式进行上传方式。

Q：崩溃服务开通后，崩溃数据未及时获取到。

A：崩溃服务首次开通，需要2-3小时生效，这期间产生的崩溃数据不上传。

Q：崩溃数据上传时效是怎么样的？

A：崩溃数据是分钟级的数据。

Q：AppGallery Connect平台上可以查询到多长时间内的崩溃数据？

A：目前只能查到最近一个月的崩溃数据。

Q：APMS报错信息是混淆的，能否还原至原始代码？

A：点击“还原堆栈”页签，可将混淆后的业务堆栈信息还原成用户可读信息。请确保已上传对应符号表文件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/zRwcIjXPTZSILpn3PmKWKQ/zh-cn_image_0000002675224017.png)

Q：在APMS中为什么最新型号手机信息没有，导致异常日志搜索不到。

A：APMS机型代号信息是由手机上报异常时一并上报的，开发者在APMS【设备型号】下拉菜单上没搜到所谓的最新机型，说明没有这个机型的手机出现异常并上报问题。（APMS只展示上报上来问题的机型，非全量展示所有机型）

Q：本地调试的Debug版本崩溃日志也会上传APMS吗？是否能够设置不上传？希望只统计在架版本的数据。

A：应用接入异常管理后，可通过设置调试版本和发布版本的不同版本号进行区分。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/_NZYY-B6R7q65n6vOJ-YOA/zh-cn_image_0000002645184080.png)

Q：为什么收集到的崩溃信息的行号与源代码不一致？

A：APMS支持堆栈解析，但是注意sourceMaps上传的是map后缀的文件，nameCache上传的是json文件，上传后缀为json的sourceMaps暂不支持解析崩溃堆栈。

Q：APMS后台的JS\_ERROR、CPP\_CRASH、OOM等数据的来源是什么？

A：数据来源主要包括客户端、服务端和网络等多个层面的监控数据。

1. 客户端数据主要来源于用户设备上的应用程序。
2. 服务端数据主要来源于后端服务器、数据库、缓存系统等基础设施（比如日志数据依赖于服务器生成的日志文件）。
3. 网络数据主要来源于网络传输过程中的各种指标，比如网络延迟等。

Q：开发本地打的包，走华为公测流程的包，会统计到APMS吗？

A：APMS采的是系统事件，只要是这个应用上架过，运行的都会统计到APMS。
