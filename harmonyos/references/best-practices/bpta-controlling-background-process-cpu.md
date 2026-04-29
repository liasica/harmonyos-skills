---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-controlling-background-process-cpu
title: 控制后台进程CPU使用率
breadcrumb: 最佳实践 > 功耗 > 应用功耗优化 > 后台任务低功耗 > 后台硬件资源合理使用 > 控制后台进程CPU使用率
category: best-practices
scraped_at: 2026-04-29T14:13:53+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:824ff9bd65b76e022b44c4f95a57dc709aacd2f757811c695dfcc27163278a56
---

CPU使用率表示进程在CPU上的运行时间占总时间的百分比，计算公式为：CPU使用率 = 运行时间 / 总时间。单核CPU使用率的最大值为100%，多核CPU使用率的最大值为核数乘以100%。例如，8核CPU使用率的最大值为800%。

系统将进程的任务调度到多个CPU核上，进程在所有核上运行的时间总和与总时间的比值即为该进程的CPU使用率。例如，1秒内进程在所有核上运行的总时间为1.1秒，则该进程的CPU使用率为110%。

## 约束

后台进程在10分钟内的单核CPU使用率不得超过80%。

短时任务后台进程CPU使用率约束：后台进程任务期间单核CPU使用率不得高于80%。

## 调测验证

1. 连接设备，打开命令行窗口，输入hdc shell进入设备。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/C_CA-tEQRIO-kUMmKWrbEA/zh-cn_image_0000002229450601.png?HW-CC-KV=V1&HW-CC-Date=20260429T061352Z&HW-CC-Expire=86400&HW-CC-Sign=2C8B6E52D0B88C888AE7C310E3510F9251E156592659870CB1A0B54AF4DE5C6C "点击放大")
2. 输入ps -ef | grep bundleName，查询应用使用率的进程号。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/gb0mOdlcT4eVulLcpBq5Tw/zh-cn_image_0000002229336117.png?HW-CC-KV=V1&HW-CC-Date=20260429T061352Z&HW-CC-Expire=86400&HW-CC-Sign=599269AEE0E57C137F8002AE0364CEC1B6851AAA030D718A91457E2618930B54 "点击放大")
3. 输入：top -p xxx，查看对应进程的使用率。查询结果中，CPU列显示进程的实时使用率。其中，xxx是进程ID(PID)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/f_K9HvqRRR6wqWAJ7iyFCQ/zh-cn_image_0000002194010320.png?HW-CC-KV=V1&HW-CC-Date=20260429T061352Z&HW-CC-Expire=86400&HW-CC-Sign=DE643847C943094116F0D16A6B6EB3D8DC54C77A7BE894C232ED48DB1C5FDA42 "点击放大")
