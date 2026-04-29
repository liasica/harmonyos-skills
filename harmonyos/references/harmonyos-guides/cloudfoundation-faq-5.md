---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cloudfoundation-faq-5
title: 如何通过应用侧日志定位预加载问题
breadcrumb: 指南 > 应用服务 > Cloud Foundation Kit（云开发服务） > Cloud Foundation Kit常见问题 > 预加载 > 如何通过应用侧日志定位预加载问题
category: harmonyos-guides
scraped_at: 2026-04-29T13:37:55+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:29aea51226b23c2d152714873c8947687e6161d6e9414ef89de6f2327cad4108
---

预加载的日志进程为“clouddevelopproxy”，日志过滤选择“No filters”。

下文列举几种场景下的日志提示信息：

* 场景一：系统服务在应用安装期间预加载数据成功

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/YddaTIh8SuGQSh0mzc240g/zh-cn_image_0000002558765380.png?HW-CC-KV=V1&HW-CC-Date=20260429T053754Z&HW-CC-Expire=86400&HW-CC-Sign=3A50B07DC8A614C7AAB4CD593E80CB8A46F6D6E8326D553C941BA769C3B17BF5)

  预加载数据成功时日志会提示：http onSuccess code: 200，并且提示预加载的数据大小：get rsp data, len 47（单位为字节）。
* 场景二：应用调用getPrefetchResult接口获取预加载数据成功

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/PhlmgU7jTjmEOg0dLK1gZw/zh-cn_image_0000002558605724.png?HW-CC-KV=V1&HW-CC-Date=20260429T053754Z&HW-CC-Expire=86400&HW-CC-Sign=44D37ACCB5FAEDDEDA9355A790DAB988DFA127AD0646CAFD963E1444E214CFAF)

  数据获取成功时，无Error级别日志，会提示OnGetPreloadCache: end status:0。
* 场景三：应用调用getPrefetchResult接口获取预加载数据失败

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/ChpZXErCRuKSIOKQ6FKY1A/zh-cn_image_0000002589325251.png?HW-CC-KV=V1&HW-CC-Date=20260429T053754Z&HW-CC-Expire=86400&HW-CC-Sign=0B94359B2417CC8F03E6BB807B32E1DBF7DBB42575D900C790E6D5D885F1F3AC)

  **问题现象**

  数据获取失败时，存在Error级别日志，会提示GetPreloadData get cache fail。

  **解决措施**

  出现此问题，可按照如下步骤排查和解决：

  1. 检查系统服务在应用安装期间预加载数据的日志。如果打印日志与上文场景一提示的日志信息不一致，则继续执行后续步骤。
  2. 确认是否存在多次调用安装预加载接口问题。安装预加载接口不支持多次调用。
  3. 排除以上原因后，检查日志中是否出现“appid \*\*\*\* is not in white list, to skip”或者“XXX Read timed out”。如果出现，请参考[运行应用时提示“appid \*\*\*\* is not in white list, to skip”](cloudfoundation-faq-3.md)或者[运行应用时报“XXX Read timed out”异常](cloudfoundation-faq-4.md)解决。
