---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cloudfoundation-faq-5
title: 如何通过应用侧日志定位预加载问题
breadcrumb: 指南 > 应用服务 > Cloud Foundation Kit（云开发服务） > Cloud Foundation Kit常见问题 > 预加载 > 如何通过应用侧日志定位预加载问题
category: harmonyos-guides
scraped_at: 2026-11-14T08:48:16+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:a6494835018822862bb3085814a362723c687a4c1ac441014f9efc521aa21601
---

预加载的日志进程为“clouddevelopproxy”，日志过滤选择“No filters”。

下文列举几种场景下的日志提示信息：

* 场景一：系统服务在应用安装期间预加载数据成功

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/scLNdG03R-6MolkGSm8znA/zh-cn_image_0000002788467948.png?HW-CC-KV=V1&HW-CC-Date=20261114T004633Z&HW-CC-Expire=31536000000&HW-CC-Sign=965A030537D73E9DE4C3005F7EC26C0ABF9CE2F2358BD6E00593488609B28E5C)

  预加载数据成功时日志会提示：http onSuccess code: 200，并且提示预加载的数据大小：get rsp data, len 47（单位为字节）。
* 场景二：应用调用getPrefetchResult接口获取预加载数据成功

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/WsqGFKH1QPCt_lzz-E4-vw/zh-cn_image_0000002817507437.png?HW-CC-KV=V1&HW-CC-Date=20261114T004633Z&HW-CC-Expire=31536000000&HW-CC-Sign=E8A59DEFC88F0F38BC771763A72F890A76F991C9C7CB3DD1978E5A77F7F540F1)

  数据获取成功时，无Error级别日志，会提示OnGetPreloadCache: end status:0。
* 场景三：应用调用getPrefetchResult接口获取预加载数据失败

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/mhtTxqiQQkCIPgF7bbQ2Ww/zh-cn_image_0000002788308006.png?HW-CC-KV=V1&HW-CC-Date=20261114T004633Z&HW-CC-Expire=31536000000&HW-CC-Sign=F32A74B1444230A672BF3F9CE13FDEEF38FC3B626D0DB3CC66CE3CA7DAEE9329)

  **问题现象**

  数据获取失败时，存在Error级别日志，会提示GetPreloadData get cache fail。

  **解决措施**

  出现此问题，可按照如下步骤排查和解决：

  1. 检查系统服务在应用安装期间预加载数据的日志。如果打印日志与上文场景一提示的日志信息不一致，则继续执行后续步骤。
  2. 确认是否存在多次调用安装预加载接口问题。安装预加载接口不支持多次调用。
  3. 排除以上原因后，检查日志中是否出现“appid \*\*\*\* is not in white list, to skip”或者“XXX Read timed out”。如果出现，请参考[运行应用时提示“appid \*\*\*\* is not in white list, to skip”](cloudfoundation-faq-3.md)或者[运行应用时报“XXX Read timed out”异常](cloudfoundation-faq-4.md)解决。
