---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/performance-analysis-kit-faq-0003
title: hilog日志落盘存储常见问题
breadcrumb: FAQ > 应用质量 > 技术质量 > 运维 > 常见问题 > hilog日志落盘存储常见问题
category: harmonyos-faqs
scraped_at: 2026-10-15T07:13:35+08:00
doc_updated_at: 2026-10-14
content_hash: sha256:630603bba4ac6138d5cc54983157e7f6add6587fac9ccde96a00c2c307b4f702
---

**Q：hilog日志如何落盘存储？**

**A**：运行命令：hilog -w start -f ckTest -l 1M -n 5 -m zlib -j 11。

文件保存在目录：/data/log/hilog/。

参数解释：

```text
-w 开启日志落盘任务,start表示开始，stop表示停止。 
-f 设置日志文件名 
-l 设置单个日志文件大小，单位可以是：B/K/M/G 
-n 设置最大日志文件编号，当文件计数超过此编号时，日志文件旋转。范围：[2,1000]
-m 设置日志文件压缩算法 
-j 任务ID，范围：[10,0xffffffffff) 
更多参数含义请使用hilog --help查看。
```
