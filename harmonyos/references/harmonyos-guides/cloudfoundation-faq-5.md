---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cloudfoundation-faq-5
title: 如何通过应用侧日志定位预加载问题
breadcrumb: 指南 > 应用服务 > Cloud Foundation Kit（云开发服务） > Cloud Foundation Kit常见问题 > 预加载 > 如何通过应用侧日志定位预加载问题
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:387f7f2565a58faf777f5d2798e1fdcefa5a6ccbc589557d0b2be808a115b1fe
---

预加载的日志进程为“clouddevelopproxy”，日志过滤选择“No filters”。

下文列举几种场景下的日志提示信息：

* 场景一：系统服务在应用安装期间预加载数据成功

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0e/v3/WlVlhTbSQ6iX5tNHmvmCWQ/zh-cn_image_0000002815559693.png?HW-CC-KV=V1&HW-CC-Date=20261112T233229Z&HW-CC-Expire=31536000000&HW-CC-Sign=26E63082DE3F461F7DA8C568A5D59F2F8F1C0ECB7543DD5E7E65D23C10B95B4E)

  预加载数据成功时日志会提示：http onSuccess code: 200，并且提示预加载的数据大小：get rsp data, len 47（单位为字节）。
* 场景二：应用调用getPrefetchResult接口获取预加载数据成功

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/OvkjA3C-QPm3QFZso-clAQ/zh-cn_image_0000002815399777.png?HW-CC-KV=V1&HW-CC-Date=20261112T233229Z&HW-CC-Expire=31536000000&HW-CC-Sign=D1774B1449322468A10D0A2774308A28211778ADA4D31E204C586EE8D54316D1)

  数据获取成功时，无Error级别日志，会提示OnGetPreloadCache: end status:0。
* 场景三：应用调用getPrefetchResult接口获取预加载数据失败

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/gSm_BIQZTjqmpr4fwuscsg/zh-cn_image_0000002786520202.png?HW-CC-KV=V1&HW-CC-Date=20261112T233229Z&HW-CC-Expire=31536000000&HW-CC-Sign=2FDE747A9FB89F5EDF3FC541666270441C9A096CB0D840F4973B44D36A6453F5)

  **问题现象**

  数据获取失败时，存在Error级别日志，会提示GetPreloadData get cache fail。

  **解决措施**

  出现此问题，可按照如下步骤排查和解决：

  1. 检查系统服务在应用安装期间预加载数据的日志。如果打印日志与上文场景一提示的日志信息不一致，则继续执行后续步骤。
  2. 确认是否存在多次调用安装预加载接口问题。安装预加载接口不支持多次调用。
  3. 排除以上原因后，检查日志中是否出现“appid \*\*\*\* is not in white list, to skip”或者“XXX Read timed out”。如果出现，请参考[运行应用时提示“appid \*\*\*\* is not in white list, to skip”](cloudfoundation-faq-3.md)或者[运行应用时报“XXX Read timed out”异常](cloudfoundation-faq-4.md)解决。
