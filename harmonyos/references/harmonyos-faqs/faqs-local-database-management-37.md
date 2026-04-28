---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-local-database-management-37
title: HarmonyOS应用数据存储仍采用沙箱机制，各个APP有自己数据可见范围，为什么不将各APP产生的数据统一存储（同一个目录或者DB下）
breadcrumb: FAQ > 应用框架开发 > 本地数据和文件 > 本地数据库管理 > HarmonyOS应用数据存储仍采用沙箱机制，各个APP有自己数据可见范围，为什么不将各APP产生的数据统一存储（同一个目录或者DB下）
category: harmonyos-faqs
scraped_at: 2026-04-28T08:27:19+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:a7b65a9382fc195720e7a0c4e8197a7045c727aca6cc10003f466159081dbbe9
---

* 安全性问题：所有应用的数据存储在同一个位置，若某应用数据被攻击者窃取，其他应用的数据也可能受到影响，增加安全风险。
* 隐私问题：应用数据统一存储可能使用户的个人隐私面临威胁，攻击者容易获取用户的所有数据。
* 性能问题：所有应用的数据存储在同一个位置，访问数据时可能产生竞争，导致性能下降。
