---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-local-database-management-27
title: setSessionId加入组网和on启动监听前后设置的区别
breadcrumb: FAQ > 应用框架开发 > 本地数据和文件 > 本地数据库管理 > setSessionId加入组网和on启动监听前后设置的区别
category: harmonyos-faqs
scraped_at: 2026-04-28T08:27:17+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:cdaa47976a491aecafd64d8f9a7315dbec74f7ad10be5f5dfdb868472957c961
---

开发者应先启动监听再设置setSessionId加入组网，如果顺序相反，在setSessionId和启动监听之间的时间段内发生的数据变化将无法获取。具体影响需根据业务逻辑和代码确定。
