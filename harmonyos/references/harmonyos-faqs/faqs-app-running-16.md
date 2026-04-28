---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-running-16
title: 虚拟机打开时，一直报错“无法打开libQt5Network.5.dylib，因为Apple无法检查其是否包含恶意软件”
breadcrumb: FAQ > DevEco Studio > 应用运行 > 虚拟机打开时，一直报错“无法打开libQt5Network.5.dylib，因为Apple无法检查其是否包含恶意软件”
category: harmonyos-faqs
scraped_at: 2026-04-28T08:29:57+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:923c895b1888e5b86493dbf0659fe18c4492b946d78bd9d6e18e8a448a52a8dc
---

**问题描述**

按教程创建虚拟机后，虚拟机无法打开。虚拟机打开时，一直报错“无法打开libQt5Network.5.dylib，因为Apple无法检查其是否包含恶意软件”。已在设置/隐私中反复同意打开，但问题仍然存在。

**解决方案**

开发者应按照指导手册，使用DevEco Studio工具提供的unzip功能进行操作。安装DevEco Studio后，下载对应的模拟器镜像和平台压缩包，通过Tools -> Unzip，打开DevEco Studio的解压入口，依次选择模拟器镜像和平台压缩包的下载路径和解压路径，进行解压。解压完成后，启动模拟器即可避免上述问题。

临时解决方案：保持弹窗不关闭，依次点击“系统偏好设置” > “安全性与隐私” > “通用”，然后选择“仍要打开”。再次启动模拟器后，在弹窗中选择“打开”。
