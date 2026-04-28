---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/use-picker
title: 使用系统Picker
category: harmonyos-guides
scraped_at: 2026-04-28T07:42:06+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:07a6fc2bf82136abda48064252c35d9527fc1925d7e293cf40cc4bd368906a52
---

应用拉起系统Picker组件（文件选择器、照片选择器、联系人选择器等），由用户在Picker上选择对应的文件、照片、联系人等资源，应用即可获取到Picker的返回结果。

系统Picker由系统独立进程实现。

说明

由于系统Picker已经获取了对应权限的预授权，开发者使用系统Picker时，无需再次申请权限也可临时受限访问对应的资源。例如，当应用需要读取用户图片时，可通过使用照片Picker，在用户选择所需要的图片资源后，直接返回该图片资源，而不需要授予应用读取图片文件的权限。

当前，系统Picker作为拉起系统资源的一种方式，整合至“拉起系统应用”中，开发者可从“[拉起系统应用](system-app-startup.md)”获取所有拉起系统资源的方式。
