---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-performance-analysis-kit-31
title: hdc工具导出/导入文件等常用hdc命令有哪些
breadcrumb: FAQ > 应用质量 > 技术质量 > 运维 > hdc工具导出/导入文件等常用hdc命令有哪些
category: harmonyos-faqs
scraped_at: 2026-04-28T08:23:17+08:00
doc_updated_at: 2026-03-17
content_hash: sha256:d4d6a7062d00689fa2b1a903ae0cf5380fffc0b81e29af4b4cfe6d93fd3c129f
---

导出文件：hdc file recv 手机路径

电脑路径导入文件：hdc file send 电脑路径

查看已连接设备：hdc list targets

手机常亮：hdc shell power-shell setmode 602

查看OUC进程：ps -ef|grep com.huawei.hmos.ouccom.ohos.updateapp

查看DUE进程：ps -ef|grep updater\_sa
