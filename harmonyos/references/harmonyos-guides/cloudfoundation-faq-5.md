---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cloudfoundation-faq-5
title: 如何通过应用侧日志定位预加载问题
breadcrumb: 指南 > 应用服务 > Cloud Foundation Kit（云开发服务） > Cloud Foundation Kit常见问题 > 预加载 > 如何通过应用侧日志定位预加载问题
category: harmonyos-guides
scraped_at: 2026-11-21T09:12:22+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:133e4d27ca49588196bc79f9253bb1fd1b132fe3c8a00d2205edb3247305da3c
---

预加载的日志进程为“clouddevelopproxy”，日志过滤选择“No filters”。

下文列举几种场景下的日志提示信息：

* 场景一：系统服务在应用安装期间预加载数据成功

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/OhSWLxY2T6W0v0YsaR4gXw/zh-cn_image_0000002821757895.png?HW-CC-KV=V1&HW-CC-Date=20261121T011222Z&HW-CC-Expire=31536000000&HW-CC-Sign=B289A2BFF051FD4EEF75E084BAE640E2290D0F124376A3FE2867D6A02BA08AA8)

  预加载数据成功时日志会提示：http onSuccess code: 200，并且提示预加载的数据大小：get rsp data, len 47（单位为字节）。
* 场景二：应用调用getPrefetchResult接口获取预加载数据成功

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/6WWeHB_KQbq_wjROYH0APA/zh-cn_image_0000002793037958.png?HW-CC-KV=V1&HW-CC-Date=20261121T011222Z&HW-CC-Expire=31536000000&HW-CC-Sign=2810C941C43444ED22BD45AD1A2C48B2DC5F5518639F35AD86D68AB2482D6817)

  数据获取成功时，无Error级别日志，会提示OnGetPreloadCache: end status:0。
* 场景三：应用调用getPrefetchResult接口获取预加载数据失败

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/1Gq2dAVZTzaXG6tSVXrwHA/zh-cn_image_0000002792877988.png?HW-CC-KV=V1&HW-CC-Date=20261121T011222Z&HW-CC-Expire=31536000000&HW-CC-Sign=1311E2A6259F36A25950D6F5A105DEEFA778D09654B209BD5F4CB418B12A8747)

  **问题现象**

  数据获取失败时，存在Error级别日志，会提示GetPreloadData get cache fail。

  **解决措施**

  出现此问题，可按照如下步骤排查和解决：

  1. 检查系统服务在应用安装期间预加载数据的日志。如果打印日志与上文场景一提示的日志信息不一致，则继续执行后续步骤。
  2. 确认是否存在多次调用安装预加载接口问题。安装预加载接口不支持多次调用。
  3. 排除以上原因后，检查日志中是否出现“appid \*\*\*\* is not in white list, to skip”或者“XXX Read timed out”。如果出现，请参考[运行应用时提示“appid \*\*\*\* is not in white list, to skip”](cloudfoundation-faq-3.md)或者[运行应用时报“XXX Read timed out”异常](cloudfoundation-faq-4.md)解决。
