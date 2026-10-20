---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/arkdata-kit-faq-0002
title: RdbStore多线程常见问题
breadcrumb: FAQ > 应用框架开发 > 本地数据和文件 > 本地数据库管理 > 常见问题 > RdbStore多线程常见问题
category: harmonyos-faqs
scraped_at: 2026-10-21T07:11:40+08:00
doc_updated_at: 2026-10-20
content_hash: sha256:cc96a069dd2d13b0aa3f31c0f725ea61627cc5b16285c6d817e4567379645712
---

**Q：RdbStore多线程安全有哪些注意事项？**

**A**：RdbStore多线程安全的注意事项如下：

1. RDB开库后支持4个读连接，多线程读取不受限。但写连接仅限1个，每次只允许一个线程修改数据库。当多线程尝试获取写连接时，写连接未释放，其他申请写连接的线程将进入等待状态，超时2秒将报错14800048，提示空闲连接数已用尽。
2. 多个线程同时操作同一对象时，如果一个线程获取了该对象的控制权，其他线程使用该对象时可能会出现问题。
3. 在多线程环境中，不要在任何线程中开启事务，因为这会带来风险。事务影响整个数据库，如果线程1中开启事务但在提交之前，线程2尝试插入并查询数据，可能查询不到未提交的数据。
