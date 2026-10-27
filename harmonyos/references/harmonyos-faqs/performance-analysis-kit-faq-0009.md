---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/performance-analysis-kit-faq-0009
title: hdc工具常用命令与文件导出导入常见问题
breadcrumb: FAQ > 应用质量 > 技术质量 > 运维 > 常见问题 > hdc工具常用命令与文件导出导入常见问题
category: harmonyos-faqs
scraped_at: 2026-10-28T07:46:44+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:435d3be2d16e97f690f6d15a8a62e610acb89686f99245fce25421fc8a46ef43
---

**Q：hdc工具导出/导入文件等常用hdc命令有哪些？**

**A**：导出文件：hdc file recv 手机路径。

电脑路径导入文件：hdc file send 电脑路径。

查看已连接设备：hdc list targets。

手机常亮：hdc shell power-shell setmode 602。

查看OUC进程：ps -ef|grep com.huawei.hmos.ouccom.ohos.updateapp。

查看DUE进程：ps -ef|grep updater\_sa。
