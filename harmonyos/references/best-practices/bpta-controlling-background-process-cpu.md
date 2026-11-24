---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-controlling-background-process-cpu
title: 控制后台进程CPU使用率
breadcrumb: 最佳实践 > 功耗 > 应用功耗优化 > 后台任务低功耗 > 后台硬件资源合理使用 > 控制后台进程CPU使用率
category: best-practices
scraped_at: 2026-11-24T12:47:54+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:87bb2eb10157b8197b7af07d1221cf019ffdfc12206c00a5c7961fd2e6d2ef65
---

CPU使用率表示进程在CPU上的运行时间占总时间的百分比，计算公式为：CPU使用率 = 运行时间 / 总时间。单核CPU使用率的最大值为100%，多核CPU使用率的最大值为核数乘以100%。例如，8核CPU使用率的最大值为800%。

系统将进程的任务调度到多个CPU核上，进程在所有核上运行的时间总和与总时间的比值即为该进程的CPU使用率。例如，1秒内进程在所有核上运行的总时间为1.1秒，则该进程的CPU使用率为110%。

## 约束

后台进程在10分钟内的单核CPU使用率不得超过80%。

短时任务后台进程CPU使用率约束：后台进程任务期间单核CPU使用率不得高于80%。

## 调测验证

1. 连接设备，打开命令行窗口，输入hdc shell进入设备。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/-1kPbRDeSKarz4XZlxRUbA/zh-cn_image_0000002229450601.png?HW-CC-KV=V1&HW-CC-Date=20261124T044754Z&HW-CC-Expire=31536000000&HW-CC-Sign=E4A63CF07C7A83BA779F41DCC5232E6F4AF29C7F8EB5439508009903562B7F63 "点击放大")
2. 输入ps -ef | grep bundleName，查询应用使用率的进程号。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/qtvyRSk3SBOOwx-5zXDP8g/zh-cn_image_0000002229336117.png?HW-CC-KV=V1&HW-CC-Date=20261124T044754Z&HW-CC-Expire=31536000000&HW-CC-Sign=75C93B40B910C4479DE5FF590A071A1B0D0BF2EC7A45BD7444E5613904B32BAA "点击放大")
3. 输入：top -p xxx，查看对应进程的使用率。查询结果中，CPU列显示进程的实时使用率。其中，xxx是进程ID(PID)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/EB6fh4V2R9ivKRz2FlYGmg/zh-cn_image_0000002194010320.png?HW-CC-KV=V1&HW-CC-Date=20261124T044754Z&HW-CC-Expire=31536000000&HW-CC-Sign=4BB865009855C8502F2BF535B3E22BE75CF8867C747381AB06EDC3AF4B07ACD3 "点击放大")
